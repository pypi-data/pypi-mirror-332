# Copyright (C) 2024 Elmar Meyer
# This file is part of slixmpp-jingle.
# See the file LICENSE for copying permission.

from slixmpp.xmlstream import ElementBase

class Jingle(ElementBase):
    name = 'jingle'
    namespace = 'urn:xmpp:jingle:1'
    plugin_attrib = 'jingle'
    interfaces = {'action','initiator','sid'}

    def getReason(self):
        return self['reason'].getMessage()

    def getAction(self):
        return self['action']

    def getSid(self):
        return self['sid']

    def getSDP(self):
        ret = ''
        if self['action']=='transport-info':
            for content in self['contents']:
                ret += content['ice-transport'].getSDP() or ''
            return ret
        else:
            version = '0' # wird bei jeden neuen Version hochgezaehlt
            ret  = "v=%s" % (version) # Version des SDP-Protokoll.
            ret += "\r\no=%s %s %s IN IP4 127.0.0.1" % (self['initiator'] or '-', self['sid'], version)
            ret += "\r\ns=-" # +self['name']
            ret += "\r\nt=0 0"
# Group muss den rtcp-mux entsprechen!
#        if self.get_plugin(name='group',check=True):
#            ret += self['group'].getSDP()
        tmp = ''
        bundle = ''
        for content in self['contents']:
            tmp += content.getSDP()
            if content['description'].get_plugin(name='rtcp-mux',check=True):
                bundle += ' ' + content['name']
                tmp += "\r\na=mid:" + content['name']
        if bundle!='':
            ret += '\r\na=group:BUNDLE'+ bundle
        ret += tmp
        return ret+"\r\n"

class Content(ElementBase):
    name = 'content'
    namespace = 'urn:xmpp:jingle:1'
    plugin_attrib = 'content'
    interfaces = {'creator','name','senders'}
    plugin_multi_attrib = 'contents'

    def getSourceSSRC(self):
        ssrc = []
        for source in self['description']['sources']:
            ssrc.append(int(source['ssrc']))
        return ssrc

    def getSDP(self):
        if self.get_plugin(name='raw-transport',check=True):
            ret = self['description'].getSDP(self['raw-transport']['candidate']['port'],self['raw-transport'].getSDP()) or ''
        else:
            ret  = self['description'].getSDP() or ''
            ret += self['ice-transport'].getSDP() or ''
        if self.get_plugin(name='senders',check=True):
            switcher = {'initiator':'recvonly', 'responder':'sendonly', 'both':'sendrecv'}
            ret += "\r\na=%s" % switcher[self['senders']]
        else:
            ret += "\r\na=sendrecv"
        return ret

class Reason(ElementBase):
    name = 'reason'
    namespace = 'urn:xmpp:jingle:1'
    plugin_attrib = 'reason'
    interfaces = {}
    
    def getMessage(self):
        return self['text'].xml.text


class Alternative_Session(ElementBase):
    name = 'alternative-session'
    namespace = 'urn:xmpp:jingle:1'
    plugin_attrib = 'alternative-session'
    interfaces = {}

class Busy(ElementBase):
    name = 'busy'
    namespace = 'urn:xmpp:jingle:1'
    plugin_attrib = 'busy'
    interfaces = {}

class Cancel(ElementBase):
    name = 'cancel'
    namespace = 'urn:xmpp:jingle:1'
    plugin_attrib = 'cancel'
    interfaces = {}

class Connectivity_Error(ElementBase):
    name = 'connectivity-error'
    namespace = 'urn:xmpp:jingle:1'
    plugin_attrib = 'connectivity-error'
    interfaces = {}

class Decline(ElementBase):
    name = 'decline'
    namespace = 'urn:xmpp:jingle:1'
    plugin_attrib = 'decline'
    interfaces = {}

class Expired(ElementBase):
    name = 'expired'
    namespace = 'urn:xmpp:jingle:1'
    plugin_attrib = 'expired'
    interfaces = {}

class Failed_Application(ElementBase):
    name = 'failed-application'
    namespace = 'urn:xmpp:jingle:1'
    plugin_attrib = 'failed-application'
    interfaces = {}

class Failed_Transport(ElementBase):
    name = 'failed-transport'
    namespace = 'urn:xmpp:jingle:1'
    plugin_attrib = 'failed-transport'
    interfaces = {}

class General_Error(ElementBase):
    name = 'general-error'
    namespace = 'urn:xmpp:jingle:1'
    plugin_attrib = 'general-error'
    interfaces = {}

class Gone(ElementBase):
    name = 'gone'
    namespace = 'urn:xmpp:jingle:1'
    plugin_attrib = 'gone'
    interfaces = {}

class Incompatible_Parameters(ElementBase):
    name = 'incompatible-parameters'
    namespace = 'urn:xmpp:jingle:1'
    plugin_attrib = 'incompatible-parameters'
    interfaces = {}

class Media_Error(ElementBase):
    name = 'media-error'
    namespace = 'urn:xmpp:jingle:1'
    plugin_attrib = 'media-error'
    interfaces = {}

class Security_Error(ElementBase):
    name = 'security-error'
    namespace = 'urn:xmpp:jingle:1'
    plugin_attrib = 'security-error'
    interfaces = {}

class Success(ElementBase):
    name = 'success'
    namespace = 'urn:xmpp:jingle:1'
    plugin_attrib = 'success'
    interfaces = {}

class Timeout(ElementBase):
    name = 'timeout'
    namespace = 'urn:xmpp:jingle:1'
    plugin_attrib = 'timeout'
    interfaces = {}

class Unsupported_Applications(ElementBase):
    name = 'unsupported-applications'
    namespace = 'urn:xmpp:jingle:1'
    plugin_attrib = 'unsupported-applications'
    interfaces = {}

class Unsupported_Transports(ElementBase):
    name = 'unsupported-transports'
    namespace = 'urn:xmpp:jingle:1'
    plugin_attrib = 'unsupported-transports'
    interfaces = {}


class Thread(ElementBase):
    name = 'thread'
    namespace = 'urn:xmpp:jingle:1'
    plugin_attrib = 'thread'
    interfaces = {}

class Text(ElementBase):
    name = 'text'
    namespace = 'urn:xmpp:jingle:1'
    plugin_attrib = 'text'
    interfaces = {}
