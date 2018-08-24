#!/usr/bin/python2
# -*- coding: utf-8 -*-

import pickle
import redis
import os
import socket
import freeswitch as fs


def hangup_hook(session, what, args=''):
    uuid = session.getVariable("uuid")
    fs.consoleLog("info", "%s hangup_hook what=(%s)\n" % (uuid, what))
    fs.consoleLog("info", "%s hangup_hook args=(%s)\n" % (uuid, args))

    return


def input_dtmf(session, what, obj, args=''):
    uuid = session.getVariable("uuid")
    #order_data = pickle.loads(session.setVariable("__order_data__"))
    fs.consoleLog('info', '%s input_dtmf pressed «%s» %s\n' % (uuid, what, obj.digit))
    if what == "dtmf":
        #pressed_dtmf = int(obj.digit)
        session.setVariable("__pressed_dtmf__", obj.digit)
    return "pause"


def handler(session, args=''):
    uuid = session.getVariable("uuid")
    fs.consoleLog('info', '%s handler start...\n' % uuid)
    session.answer()
    try:
        #fs.consoleLog('info', '%s handler read order_data...\n' % uuid)
        order_data = pickle.load(open('/tmp/%s' % uuid, 'rb')) # Получить данные отзвона
        #session.setVariable("__order_data__", pickle.dumps(order_data))
        fs.consoleLog('info', '%s handler order_data %s\n' % (uuid, order_data))
        if order_data['event'] == 'ORDER_NO_CARS':
            p = order_data['message'][0]
            digits = session.playAndGetDigits(1, 4, 3, 5000, "", p.encode('UTF-8'), "", "\\d+")
            #if digits: break
            fs.consoleLog('info', '%s handler ORDER_NO_CARS\n' % uuid)
            # TODO: Новая запись на no_cars
            # "В данный момент нет подходящих машин, но, если вы готовы продлить
            # ожидание вашего заказа, нажмите 1, иначе 6"
            #pressed_dtmf = session.getVariable("__pressed_dtmf__")
            event = 'ORDERS:SET_NO_CARS_ABORTED'
            try:
                digits = int(digits)
                fs.consoleLog('info', '%s handler pressed_dtmf=%s, sending...\n' % (uuid, digits))
                if digits == 1:
                    #order_data.update(uuid=uuid)
                    event = 'ORDER_SET_CREATED'
                    """
                    if send_event('ORDER_SET_CREATED', order_data, uuid):
                        fs.consoleLog("info", "handler Pressed DTMF sended\n")
                    else:
                        fs.consoleLog("error", "handler send_event exception\n")
                    """
                    #session.execute("playback", "thank-you-for-calling.wav") # Воспроизвести
                else:
                    fs.consoleLog('info', '%s handler nothing pressed\n' % uuid)
            except Exception as e:
                fs.consoleLog('error', '%s handler exception1 %s\n' % (uuid, e))

            if event:
                ROUTER = order_data['ROUTER']
                del order_data['ROUTER']
                data = pickle.dumps([event, order_data], protocol=2)
                fs.consoleLog("info", "%s handler send_event (%s %s)\n" % (uuid, event, order_data))
                so_buffer = 1024
                # TODO: Плюхнуть в redis
                try:
                    so = socket.socket()
                    fs.consoleLog("info", "%s handler send_event socket=%s\n" % (uuid, so))
                    so.connect(ROUTER)
                    fs.consoleLog("info", "%s handler send_event connected socket=%s\n" % (uuid, so))
                    while data:
                        so.send(data[:so_buffer])
                        data = data[so_buffer:]
                    so.close()
                    result = True
                    fs.consoleLog("info", "%s handler send_event Pressed DTMF order_id %s sended\n" % (uuid, order_data['order_id']))
                except Exception as e:
                    result = False
                    fs.consoleLog("error", "%s handler send_event Pressed DTMF order_id %s send exception %s\n" % (uuid, order_data['order_id'], e))


    except Exception as e:
        fs.consoleLog('error', '%s handler exception2 %s \n' % (uuid, e))
        try:
            for p in order_data['message']:
                #fs.consoleLog("info", "%s %s playback %s\n" % (uuid, order_data['phone'], p.encode('UTF-8')))
                session.execute("playback", p.encode('UTF-8')) # Воспроизвести
                #https://www.freeswitch.org/confluence/display/FREESWITCH/mod_dptools%3A+play+and+get+digits
        except Exception as e:
            fs.consoleLog('error', '%s handler exception2-1 %s \n' % (uuid, e))


    try:
        os.remove('/tmp/%s' % uuid)
        fs.consoleLog('info', '%s handler remove /tmp/%s\n' % (uuid, uuid))
    except Exception as e:
        fs.consoleLog('error', '%s handler exception3 %s\n' % (uuid, e))
