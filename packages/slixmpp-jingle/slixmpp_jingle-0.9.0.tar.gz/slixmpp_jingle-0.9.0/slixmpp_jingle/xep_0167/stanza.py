# Copyright (C) 2024 Elmar Meyer
# This file is part of slixmpp-jingle.
# See the file LICENSE for copying permission.

from slixmpp.xmlstream import ElementBase

class Description(ElementBase):
    name = 'description'
    namespace = 'urn:xmpp:jingle:apps:rtp:1'
    plugin_attrib = 'description'
    interfaces = {'media','ssrc'}

    def getSDP(self,port = None, cline = None):
        ret = "\r\nm=%s %s " % (self['media'],port or '0')
        if port==None:
            ret += "UDP/"
        if self.parent().get_plugin(name='ice-transport',check=True):
            if self.parent()['ice-transport'].get_plugin(name='fingerprint',check=True):
                ret += "TLS/RTP/SAVPF"
            else:
                ret += "TLS/RTP/SAVPF"
        elif self.parent().get_plugin(name='raw-transport',check=True):
            if self.parent()['raw-transport'].get_plugin(name='fingerprint',check=True):
                ret += "TLS/RTP/SAVPF"
            else:
                ret += "RTP/AVP"
        for rtcpfb in self['rtcp-fbs']: # Ist das überflüssig?
            ret += rtcpfb.getSDP() or ''
        tmp = ''
        ptime_max = -1
        maxptime_max = -1
        if self['maxptime']:
            maxptime_max = max(maxptime_max,int(self['maxptime']))
        for payload in self['payload-types']:
            ret += ' '+payload['id']
            if payload['ptime']:
                ptime_max = max(ptime_max,int(payload['ptime']))
            if payload['maxptime']:
                maxptime_max = max(maxptime_max,int(payload['maxptime']))
            tmp += payload.getSDP()
        if cline:
            ret += cline
        ret += tmp
        if ptime_max>-1:
            ret += "\r\na=ptime:%s" % (ptime_max)
        if maxptime_max>-1:
            ret += "\r\na=maxptime:%s" % (maxptime_max)
        if self.get_plugin(name='hdrexts',check=True):
#            ret += "\r\na=sendrecv"
            for hdrext in self['hdrexts']:
                ret += hdrext.getSDP() or ''
        if self.get_plugin(name='extmap-allow-mixed',check=True):
            ret += "\r\na=extmap-allow-mixed"
        if self.get_plugin(name='ssrc-group',check=True):
            ret += self['ssrc-group'].getSDP() or ''
        for source in self['sources']:
            ret += source.getSDP()
        if self.get_plugin(name='encryption',check=True):
           ret += self['encryption'].getSDP() or ''
        return ret

class PayloadType(ElementBase):
    name = 'payload-type'
    namespace = 'urn:xmpp:jingle:apps:rtp:1'
    plugin_attrib = 'payload-type'
    interfaces = {'channels','clockrate','id','maxptime','name','ptime'}
    plugin_multi_attrib = 'payload-types'

    def getSDP(self):
        ret = "\r\na=rtpmap:%s " % self['id']
        # name optional in jingle if one of the standard payload ids required in sdp
        # standard payload ids: https://en.m.wikipedia.org/wiki/RTP_payload_formats
        if self['name']:
            ret += "%s" % (self['name'])
        if self['clockrate']:
            ret += "/%s" % (self['clockrate'])
        if self['channels']:
            ret += "/%s" % (self['channels'])
        # ptime, maxptime are not really usefull
        if self.get_plugin(name='parameters',check=True):
            ret += "\r\na=fmtp:%s " % (self['id'])
            tmp = ''
            for parameter in self['parameters']:
                tmp += ';'+parameter.getSDP()
            ret += tmp[1:]
        for rtcpfb in self['rtcp-fbs']: # Ist das überflüssig?
            ret += rtcpfb.getSDP(self['id']) or ''
        return ret

class RtcpMux(ElementBase):
    name = 'rtcp-mux'
    namespace = 'urn:xmpp:jingle:apps:rtp:1'
    plugin_attrib = 'rtcp-mux'
    interfaces = {}

    def getSDP(self):
       return '\r\na=rtcp-mux'

class Encryption(ElementBase):
    name = 'encryption'
    namespace = 'urn:xmpp:jingle:apps:rtp:1'
    plugin_attrib = 'encryption'
    interfaces = {'required'}

    def getSDP(self):
       if self.get_plugin(name='crypto',check=True):
           return self['crypto'].getSDP()
       return None

class Crypto(ElementBase):
    name = 'crypto'
    namespace = 'urn:xmpp:jingle:apps:rtp:1'
    plugin_attrib = 'crypto'
    interfaces = {'crypto-suite','key-params','session-params','tag'}

    def getSDP(self):
        return "\r\na=crypto:%s %s %s %s" % (self['tag'],self['crypto-suite'],self['key-params'],self['session-params'])

class Bandwidth(ElementBase):
    name = 'bandwidth'
    namespace = 'urn:xmpp:jingle:apps:rtp:1'
    plugin_attrib = 'bandwidth'
    interfaces = {'type'}

class Parameter(ElementBase):
    name = 'parameter'
    namespace = 'urn:xmpp:jingle:apps:rtp:1'
    plugin_attrib = 'parameter'
    interfaces = {'name','value'}
    plugin_multi_attrib = 'parameters'

    def getSDP(self):
        if self['name']:
            return "%s=%s" % (self['name'],self['value'])
        return "%s" % (self['value'])

#class RtcpFB(ElementBase):  --> xep_0293
#    name = 'rtcp-fb'
#    namespace = 'urn:xmpp:jingle:apps:rtp:rtcp-fb:0'
#    plugin_attrib = 'rtcp-fb'
#    interfaces = {'subtype','type'}
#
#    def getSDP(self):
#        return self['type']
