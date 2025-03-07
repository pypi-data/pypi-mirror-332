# Copyright (C) 2024 Elmar Meyer
# This file is part of slixmpp-jingle.
# See the file LICENSE for copying permission.

import logging

from typing import Iterable, Tuple, Optional

from slixmpp import JID, Iq
from slixmpp.plugins import BasePlugin
from slixmpp.xmlstream import register_stanza_plugin
from slixmpp.xmlstream.handler import Callback
from slixmpp.xmlstream.matcher import StanzaPath
from slixmpp_jingle.xep_0166 import Jingle, Content
from slixmpp_jingle.xep_0167 import Description, Encryption
from slixmpp_jingle.xep_0262 import stanza, Zrtp

log = logging.getLogger(__name__)


class XEP_0262(BasePlugin):

    name = 'xep_0262'
    description = 'XEP-0262: ZRTP in RTP Session'
    dependencies = set(['xep_0166','xep_0176'])
    stanza = stanza

    def plugin_init(self):
        register_stanza_plugin(Iq,Jingle)
        register_stanza_plugin(Jingle,Content)
        register_stanza_plugin(Content,Description)
        register_stanza_plugin(Description,Encryption)
        register_stanza_plugin(Encryption,Zrtp)

        self.xmpp.register_handler(
            Callback('Jingle Content Transport Fingerprint',
                StanzaPath('iq/jingle/content/description/encryption/zrtp'),
                self._handle_jingle_content_description_encryption_zrtp))

#    def session_bind(self, jid):
#        pass

#    def plugin_end(self):
#        pass


#######################################################################

    def _handle_jingle_content_description_encryption_zrtp(self, message):
        self.xmpp.event('jingle_content_description__encryption_zrtp', message['jingle']['content']['description']['encryption']['zrtp'])
