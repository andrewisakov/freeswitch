# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
from sys import version_info

if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module(
                '_ESL', [dirname(__file__)])
        except ImportError:
            import _ESL
            return _ESL
        if fp is not None:
            try:
                _mod = imp.load_module('_ESL', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _ESL = swig_import_helper()
    del swig_import_helper
else:
    import _ESL
del version_info


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError(name)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


class ESLevent:
    __swig_setmethods__ = {}

    def __setattr__(self, name, value): return _swig_setattr(
        self, ESLevent, name, value)
    __swig_getmethods__ = {}

    def __getattr__(self, name): return _swig_getattr(self, ESLevent, name)
    __repr__ = _swig_repr
    __swig_setmethods__["event"] = _ESL.ESLevent_event_set
    __swig_getmethods__["event"] = _ESL.ESLevent_event_get
    __swig_setmethods__[
        "serialized_string"] = _ESL.ESLevent_serialized_string_set
    __swig_getmethods__[
        "serialized_string"] = _ESL.ESLevent_serialized_string_get
    __swig_setmethods__["mine"] = _ESL.ESLevent_mine_set
    __swig_getmethods__["mine"] = _ESL.ESLevent_mine_get

    def __init__(self, *args):
        this = _ESL.new_ESLevent(*args)
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _ESL.delete_ESLevent

    def __del__(self): return None

    def serialize(self, format=None): return _ESL.ESLevent_serialize(
        self, format)

    def setPriority(self, *args): return _ESL.ESLevent_setPriority(self, *args)

    def getHeader(self, *args): return _ESL.ESLevent_getHeader(self, *args)

    def getBody(self): return _ESL.ESLevent_getBody(self)

    def getType(self): return _ESL.ESLevent_getType(self)

    def addBody(self, *args): return _ESL.ESLevent_addBody(self, *args)

    def addHeader(self, *args): return _ESL.ESLevent_addHeader(self, *args)

    def pushHeader(self, *args): return _ESL.ESLevent_pushHeader(self, *args)

    def unshiftHeader(
        self, *args): return _ESL.ESLevent_unshiftHeader(self, *args)

    def delHeader(self, *args): return _ESL.ESLevent_delHeader(self, *args)

    def firstHeader(self): return _ESL.ESLevent_firstHeader(self)

    def nextHeader(self): return _ESL.ESLevent_nextHeader(self)


ESLevent_swigregister = _ESL.ESLevent_swigregister
ESLevent_swigregister(ESLevent)


class ESLconnection:
    __swig_setmethods__ = {}

    def __setattr__(self, name, value): return _swig_setattr(
        self, ESLconnection, name, value)
    __swig_getmethods__ = {}

    def __getattr__(self, name): return _swig_getattr(
        self, ESLconnection, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _ESL.new_ESLconnection(*args)
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _ESL.delete_ESLconnection

    def __del__(self): return None

    def socketDescriptor(
        self): return _ESL.ESLconnection_socketDescriptor(self)

    def connected(self): return _ESL.ESLconnection_connected(self)

    def getInfo(self): return _ESL.ESLconnection_getInfo(self)

    def send(self, *args): return _ESL.ESLconnection_send(self, *args)

    def sendRecv(self, *args): return _ESL.ESLconnection_sendRecv(self, *args)

    def api(self, *args): return _ESL.ESLconnection_api(self, *args)

    def bgapi(self, *args): return _ESL.ESLconnection_bgapi(self, *args)

    def sendEvent(
        self, *args): return _ESL.ESLconnection_sendEvent(self, *args)

    def sendMSG(self, *args): return _ESL.ESLconnection_sendMSG(self, *args)

    def recvEvent(self): return _ESL.ESLconnection_recvEvent(self)

    def recvEventTimed(
        self, *args): return _ESL.ESLconnection_recvEventTimed(self, *args)

    def filter(self, *args): return _ESL.ESLconnection_filter(self, *args)

    def events(self, *args): return _ESL.ESLconnection_events(self, *args)

    def execute(self, *args): return _ESL.ESLconnection_execute(self, *args)

    def executeAsync(
        self, *args): return _ESL.ESLconnection_executeAsync(self, *args)

    def setAsyncExecute(
        self, *args): return _ESL.ESLconnection_setAsyncExecute(self, *args)

    def setEventLock(
        self, *args): return _ESL.ESLconnection_setEventLock(self, *args)

    def disconnect(self): return _ESL.ESLconnection_disconnect(self)


ESLconnection_swigregister = _ESL.ESLconnection_swigregister
ESLconnection_swigregister(ESLconnection)


def eslSetLogLevel(*args):
  return _ESL.eslSetLogLevel(*args)


eslSetLogLevel = _ESL.eslSetLogLevel
# This file is compatible with both classic and new-style classes.
