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
from slixmpp_jingle.xep_0176 import Transport
from slixmpp_jingle.xep_0320 import stanza, Fingerprint

import re

log = logging.getLogger(__name__)

class XEP_0320(BasePlugin):

    name = 'xep_0320'
    description = 'XEP-0320: DTLS-SRTP fingerprint'
    dependencies = set(['xep_0166','xep_0176'])
    stanza = stanza

    def plugin_init(self):
        register_stanza_plugin(Iq,Jingle)
        register_stanza_plugin(Jingle,Content)
        register_stanza_plugin(Content,Transport)
        register_stanza_plugin(Transport,Fingerprint)

        self.xmpp.register_handler(
            Callback('Jingle Content Transport Fingerprint',
                StanzaPath('iq/jingle/content/transport/fingerprint'),
                self._handle_jingle_content_transport_fingerprint))

#    def session_bind(self, jid):
#        pass

#    def plugin_end(self):
#        pass


#######################################################################

    def _handle_jingle_content_transport_fingerprint(self, message):
        self.xmpp.event('jingle_content_transport_fingerprint', message['jingle']['content']['transport']['fingerprint'])

# a=fingerprint:hash-func fingerprint
# a=setup:role
    def make_fingerprint(self,sdp):
        m = re.search(r'^a=fingerprint:(\S+) +([^\r]+)\r$',sdp,re.M)
        if m:
            fingerprint = Fingerprint()
            fingerprint['hash'] = m.group(1)
            fingerprint.xml.text = m.group(2)
            m = re.search(r'^a=setup:([^\r]+)\r$',sdp,re.M)
            if m:
                fingerprint['setup'] = m.group(1)
            return fingerprint
        return None
