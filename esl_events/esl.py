#!/usr/bin/python2
import json
import threading
import datetime
import redis
import ESL
import settings


class ESLcon(threading.Thread):
    def __init__(self, esl_server, esl_passwd):
        threading.Thread.__init__(self)
        self._esl_server = esl_server
        self._esl_passwd = esl_passwd
        self._time_shift = datetime.timedelta(0)
        self._active = True

    def set_time_shift(self, _esl_con):
        fs_time = _esl_con.api('strftime')
        fs_time = datetime.datetime.strptime(fs_time.serialize().split('\n')[-1:][0], '%Y-%m-%d %H:%M:%S')
        fs_time -= datetime.datetime.now()
        self._time_shift = fs_time

    def run(self):
        _redcon = redis.Redis(host='localhost', port=6379)
        _esl_con = ESL.ESLconnection(self._esl_server[0], self._esl_server[1], self._esl_passwd)
        if _esl_con.connected:
            self.set_time_shift(_esl_con)
            _esl_con.events('json', 'all')
            while self._active and _esl_con.connected:
                ev = _esl_con.recvEvent()
                if ev:
                    ev = json.loads(ev.serialize('json'))
                    channel = 'ESL_EVENT:'+ev.get(u'Event-Name')
                    _redcon.publish(channel, json.dumps(ev))
