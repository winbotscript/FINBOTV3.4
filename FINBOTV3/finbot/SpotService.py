from FinbotServer.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from FinbotServer.protocol.TProtocol import TProtocolException
from FinbotServer.TRecursive import fix_spec
import sys
import logging
from .ttypes import *
from FinbotServer.Thrift import TProcessor
from FinbotServer.transport import TTransport
all_structs = []

class Iface(object):
    def lookupByPhoneNumber(self, countryAreaCode, phoneNumber):
        """
        Parameters:
         - countryAreaCode
         - phoneNumber
        """
        pass

    def lookupNearby(self, location, category, query, countryAreaCode):
        """
        Parameters:
         - location
         - category
         - query
         - countryAreaCode
        """
        pass


class Client(Iface):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0

    def lookupByPhoneNumber(self, countryAreaCode, phoneNumber):
        """
        Parameters:
         - countryAreaCode
         - phoneNumber
        """
        self.send_lookupByPhoneNumber(countryAreaCode, phoneNumber)
        return self.recv_lookupByPhoneNumber()

    def send_lookupByPhoneNumber(self, countryAreaCode, phoneNumber):
        self._oprot.writeMessageBegin('lookupByPhoneNumber', TMessageType.CALL, self._seqid)
        args = lookupByPhoneNumber_args()
        args.countryAreaCode = countryAreaCode
        args.phoneNumber = phoneNumber
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_lookupByPhoneNumber(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = lookupByPhoneNumber_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "lookupByPhoneNumber failed: unknown result")

    def lookupNearby(self, location, category, query, countryAreaCode):
        """
        Parameters:
         - location
         - category
         - query
         - countryAreaCode
        """
        self.send_lookupNearby(location, category, query, countryAreaCode)
        return self.recv_lookupNearby()

    def send_lookupNearby(self, location, category, query, countryAreaCode):
        self._oprot.writeMessageBegin('lookupNearby', TMessageType.CALL, self._seqid)
        args = lookupNearby_args()
        args.location = location
        args.category = category
        args.query = query
        args.countryAreaCode = countryAreaCode
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_lookupNearby(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = lookupNearby_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "lookupNearby failed: unknown result")


class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["lookupByPhoneNumber"] = Processor.process_lookupByPhoneNumber
        self._processMap["lookupNearby"] = Processor.process_lookupNearby

    def process(self, iprot, oprot):
        (name, type, seqid) = iprot.readMessageBegin()
        if name not in self._processMap:
            iprot.skip(TType.STRUCT)
            iprot.readMessageEnd()
            x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
            oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
            x.write(oprot)
            oprot.writeMessageEnd()
            oprot.trans.flush()
            return
        else:
            self._processMap[name](self, seqid, iprot, oprot)
        return True

    def process_lookupByPhoneNumber(self, seqid, iprot, oprot):
        args = lookupByPhoneNumber_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = lookupByPhoneNumber_result()
        try:
            result.success = self._handler.lookupByPhoneNumber(args.countryAreaCode, args.phoneNumber)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("lookupByPhoneNumber", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_lookupNearby(self, seqid, iprot, oprot):
        args = lookupNearby_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = lookupNearby_result()
        try:
            result.success = self._handler.lookupNearby(args.location, args.category, args.query, args.countryAreaCode)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("lookupNearby", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

# HELPER FUNCTIONS AND STRUCTURES


class lookupByPhoneNumber_args(object):
    """
    Attributes:
     - countryAreaCode
     - phoneNumber
    """


    def __init__(self, countryAreaCode=None, phoneNumber=None,):
        self.countryAreaCode = countryAreaCode
        self.phoneNumber = phoneNumber

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.STRING:
                    self.countryAreaCode = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.phoneNumber = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('lookupByPhoneNumber_args')
        if self.countryAreaCode is not None:
            oprot.writeFieldBegin('countryAreaCode', TType.STRING, 2)
            oprot.writeString(self.countryAreaCode.encode('utf-8') if sys.version_info[0] == 2 else self.countryAreaCode)
            oprot.writeFieldEnd()
        if self.phoneNumber is not None:
            oprot.writeFieldBegin('phoneNumber', TType.STRING, 3)
            oprot.writeString(self.phoneNumber.encode('utf-8') if sys.version_info[0] == 2 else self.phoneNumber)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(lookupByPhoneNumber_args)
lookupByPhoneNumber_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'countryAreaCode', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'phoneNumber', 'UTF8', None, ),  # 3
)


class lookupByPhoneNumber_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = SpotPhoneNumberResponse()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('lookupByPhoneNumber_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(lookupByPhoneNumber_result)
lookupByPhoneNumber_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [SpotPhoneNumberResponse, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class lookupNearby_args(object):
    """
    Attributes:
     - location
     - category
     - query
     - countryAreaCode
    """


    def __init__(self, location=None, category=None, query=None, countryAreaCode=None,):
        self.location = location
        self.category = category
        self.query = query
        self.countryAreaCode = countryAreaCode

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.STRUCT:
                    self.location = Location()
                    self.location.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.category = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.query = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.countryAreaCode = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('lookupNearby_args')
        if self.location is not None:
            oprot.writeFieldBegin('location', TType.STRUCT, 2)
            self.location.write(oprot)
            oprot.writeFieldEnd()
        if self.category is not None:
            oprot.writeFieldBegin('category', TType.I32, 3)
            oprot.writeI32(self.category)
            oprot.writeFieldEnd()
        if self.query is not None:
            oprot.writeFieldBegin('query', TType.STRING, 4)
            oprot.writeString(self.query.encode('utf-8') if sys.version_info[0] == 2 else self.query)
            oprot.writeFieldEnd()
        if self.countryAreaCode is not None:
            oprot.writeFieldBegin('countryAreaCode', TType.STRING, 5)
            oprot.writeString(self.countryAreaCode.encode('utf-8') if sys.version_info[0] == 2 else self.countryAreaCode)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(lookupNearby_args)
lookupNearby_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRUCT, 'location', [Location, None], None, ),  # 2
    (3, TType.I32, 'category', None, None, ),  # 3
    (4, TType.STRING, 'query', 'UTF8', None, ),  # 4
    (5, TType.STRING, 'countryAreaCode', 'UTF8', None, ),  # 5
)


class lookupNearby_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = SpotNearbyResponse()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('lookupNearby_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(lookupNearby_result)
lookupNearby_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [SpotNearbyResponse, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)
fix_spec(all_structs)
del all_structs

