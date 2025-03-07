# Copyright (C) 2024 Elmar Meyer
# This file is part of slixmpp-jingle.
# See the file LICENSE for copying permission.

from typing import Iterable, List, Tuple, Optional
from slixmpp.xmlstream import ElementBase, ET

class Group(ElementBase):
    name = 'group'
    namespace = 'urn:xmpp:jingle:apps:grouping:0'
    plugin_attrib = 'group'
    interfaces = {'semantics'}

    def getSDP(self):
        ret = "\r\na=group:"+self['semantics']
        for content in self['contents']:
            ret += " "+content['name']
        return ret

class Content(ElementBase):
    name = 'content'
    namespace = 'urn:xmpp:jingle:apps:grouping:0'
    plugin_attrib = 'content'
    interfaces = {'name'}
    plugin_multi_attrib = 'contents'

