# Copyright (C) 2024 Elmar Meyer
# This file is part of slixmpp-jingle.
# See the file LICENSE for copying permission.

from typing import Iterable, List, Tuple, Optional
from slixmpp.xmlstream import ElementBase, ET

import re

class Transport(ElementBase):
    name = 'transport'
    namespace = 'urn:xmpp:jingle:transports:raw-udp:1'
    plugin_attrib = 'raw-transport'
    interfaces = {}

    def getSDP(self):
        return self['candidate'].getSDP()

class Candidate(ElementBase):
    name = 'candidate'
    namespace = 'urn:xmpp:jingle:transports:raw-udp:1'
    plugin_attrib = 'candidate'
    interfaces = {'component','generation','id','ip','port','type'}
    plugin_multi_attrib = 'candidates'

    def getSDP(self):
        return '\r\nc=IN IP4 '+self['ip']
