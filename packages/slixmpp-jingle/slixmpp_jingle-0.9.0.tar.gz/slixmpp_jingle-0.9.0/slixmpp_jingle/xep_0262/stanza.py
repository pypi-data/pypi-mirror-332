# Copyright (C) 2024 Elmar Meyer
# This file is part of slixmpp-jingle.
# See the file LICENSE for copying permission.

from typing import Iterable, List, Tuple, Optional
from slixmpp.xmlstream import ElementBase, ET

class Zrtp(ElementBase):
    name = 'zrtp-hash'
    namespace = 'urn:xmpp:jingle:apps:rtp:zrtp:1'
    plugin_attrib = 'zrtp'
    interfaces = {'version'}
    sub_interfaces = {}

    def getSDP(self):
        if self['version']:
            return "\r\na=zrtp-hash:%s %s" % (self['version'],self.xml.text)
        return None
