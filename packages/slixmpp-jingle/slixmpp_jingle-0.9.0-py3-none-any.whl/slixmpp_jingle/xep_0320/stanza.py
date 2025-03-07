# Copyright (C) 2024 Elmar Meyer
# This file is part of slixmpp-jingle.
# See the file LICENSE for copying permission.

from typing import Iterable, List, Tuple, Optional
from slixmpp.xmlstream import ElementBase, ET

class Fingerprint(ElementBase):
    name = 'fingerprint'
    namespace = 'urn:xmpp:jingle:apps:dtls:0'
    plugin_attrib = 'fingerprint'
    interfaces = {'hash','setup'}
    sub_interfaces = {}

    def getFingerprint(self):
        return self.xml.text

    def getSDP(self):
        ret = '\r\na=fingerprint:'+self['hash']+' '+ self.xml.text
        ret += '\r\na=setup:'+self['setup']
        return ret
