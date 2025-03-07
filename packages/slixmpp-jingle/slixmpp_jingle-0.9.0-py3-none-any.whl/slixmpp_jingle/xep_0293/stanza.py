# Copyright (C) 2024 Elmar Meyer
# This file is part of slixmpp-jingle.
# See the file LICENSE for copying permission.

from typing import Iterable, List, Tuple, Optional
from slixmpp.xmlstream import ElementBase, ET

class RtcpFB(ElementBase):
    name = 'rtcp-fb'
    namespace = 'urn:xmpp:jingle:apps:rtp:rtcp-fb:0'
    plugin_attrib = 'rtcp-fb'
    interfaces = {'type','subtype'}
    plugin_multi_attrib = 'rtcp-fbs'

    def getSDP(self,id='*'):
        if self['type']:
            if self['subtype']:
                ret = "\r\na=rtcp-fb:%s %s %s" % (id,self['type'],self['subtype'])
            else:
                ret = "\r\na=rtcp-fb:%s %s" % (id,self['type'])
            tmp = ''
            for parameter in self['parameters']:
                tmp += ','+parameter.getSDP()
            if tmp[1:]:
                ret += ' '+tmp[1:]
            return ret
        return None

class Parameter(ElementBase):
    name = 'parameter'
    namespace = 'urn:xmpp:jingle:apps:rtp:rtcp-fb:0'
    plugin_attrib = 'parameter'
    interfaces = {'name','value'}
    plugin_multi_attrib = 'parameters'

    def getSDP(self):
        parameter = self['name']
        if self['value']:
            parameter += ":"+self['value']
        return parameter

class RtcpFBTrrInt(ElementBase):
    name = 'rtcp-fb-trr-int'
    namespace = 'urn:xmpp:jingle:apps:rtp:rtcp-fb:0'
    plugin_attrib = 'rtcp-fb-trr-int'
    interfaces = {'value'}

    def getSDP(self,id='*'):
        return "\r\na=rtcp-fb:%s trr-int %s" % (id,self['value'])
