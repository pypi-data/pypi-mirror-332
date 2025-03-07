# Copyright (C) 2024 Elmar Meyer
# This file is part of slixmpp-jingle.
# See the file LICENSE for copying permission.

from typing import Iterable, List, Tuple, Optional
from slixmpp.xmlstream import ElementBase, ET

class HdrExt(ElementBase):
    name = 'rtp-hdrext'
    namespace = 'urn:xmpp:jingle:apps:rtp:rtp-hdrext:0'
    plugin_attrib = 'hdrext'
    interfaces = {'id','uri','senders'}
    plugin_multi_attrib = 'hdrexts'

    def getSDP(self):
        switcher = {'initiator':'/recvonly', 'responder':'/sendonly'}
        ret = "\r\na=extmap:%s%s %s" % (self['id'],switcher.get(self['senders'],''),self['uri'])
        if self.get_plugin(name='parameters',check=True):
            tmp = ''
            for parameter in self['parameters']:
                tmp += ','+parameter.getSDP()
            ret += ' '+tmp[1:]
        return ret

class Parameter(ElementBase):
    name = 'parameter'
    namespace = 'urn:xmpp:jingle:apps:rtp:rtp-hdrext:0'
    plugin_attrib = 'parameter'
    interfaces = {'name','value'}
    plugin_multi_attrib = 'parameters'

    def getSDP(self):
        parameter = self['name']
        if self['value']:
            parameter += ":"+self['value']
        return parameter

class ExtMapAllowMixed(ElementBase):
    name = 'extmap-allow-mixed'
    namespace = 'urn:xmpp:jingle:apps:rtp:rtp-hdrext:0'
    plugin_attrib = 'extmap-allow-mixed'
    interfaces = {}

    def getSDP(self):
        return '\r\na=extmap-allow-mixed'
