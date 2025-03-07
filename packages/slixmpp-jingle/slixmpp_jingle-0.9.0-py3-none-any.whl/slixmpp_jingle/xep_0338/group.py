# Copyright (C) 2024 Elmar Meyer
# This file is part of slixmpp-jingle.
# See the file LICENSE for copying permission.

import logging

from typing import Iterable, Tuple, Optional

import re

from slixmpp import JID, Iq
from slixmpp.plugins import BasePlugin
from slixmpp.xmlstream import register_stanza_plugin
from slixmpp.xmlstream.handler import Callback
from slixmpp.xmlstream.matcher import StanzaPath
from slixmpp_jingle.xep_0166 import Jingle
from slixmpp_jingle.xep_0338 import stanza, Group, Content

log = logging.getLogger(__name__)


class XEP_0338(BasePlugin):

    name = 'xep_0338'
    description = 'XEP-0338: Grouping Framework'
    dependencies = set(['xep_0166'])
    stanza = stanza

    def plugin_init(self):
        register_stanza_plugin(Iq,Jingle)
        register_stanza_plugin(Jingle,Group)
        register_stanza_plugin(Group,Content,True)

        self.xmpp.register_handler(
            Callback('Jingle Group',
                StanzaPath('iq/jingle/group'),
                self._handle_jingle_group))

#    def session_bind(self, jid):
#        pass

#    def plugin_end(self):
#        pass


#######################################################################

    def _handle_jingle_group(self, message):
        self.xmpp.event('jingle_group', message['jingle']['group'])

    def make_group(self,sdp):
        m = re.search(r'^a=group:([^ ]+) +([^\r]+)\r$',sdp,re.M)
        if m:
            group = Group()
            group['semantics'] = m.group(1)
            medias = m.group(2).split(' ')
            for media in medias:
                content = Content()
                content['name'] = media
                group.append(content)
            return group
        return None
