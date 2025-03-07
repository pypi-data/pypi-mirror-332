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
from slixmpp_jingle.xep_0167 import Description
from slixmpp_jingle.xep_0294 import stanza, HdrExt, Parameter, ExtMapAllowMixed

import re

log = logging.getLogger(__name__)


class XEP_0294(BasePlugin):

    name = 'xep_0294'
    description = 'XEP-0294: Jingle RTP Header Extensions Negotiation'
    dependencies = set(['xep_0166','xep_0167'])
    stanza = stanza

    def plugin_init(self):
        register_stanza_plugin(Iq,Jingle)
        register_stanza_plugin(Jingle,Content,True)
        register_stanza_plugin(Content,Description)
        register_stanza_plugin(Description,ExtMapAllowMixed)
        register_stanza_plugin(Description,HdrExt,True)
        register_stanza_plugin(HdrExt,Parameter,True)

    def make_extmapallowmixed(self, sdp):
        m = re.finditer('^a=extmap-allow-mixed\r$',sdp,re.M)
        if m:
            return ExtMapAllowMixed()
        return None

    def make_hdrexts(self, sdp):
        general = 'both'
        m = re.search('a=(sendrecv|send|recv)$',sdp,re.M)
        if m:
            if m.group(1)   == 'send':
                general = 'responder'
            elif m.group(1) == 'recv':
                general = 'initiator'
        iter = re.finditer('a=extmap:([^ /]+)(/[^ ]+)? +([^\r\n]+)\r$',sdp,re.M)
        if iter:
            hdrexts = []
            for m in iter:
                switcher = {'/recvonly':'initiator', '/sendonly':'responder'}
                hdrext = HdrExt()
                hdrext['id'] = m.group(1)
                if m.group(2):
                    hdrext['senders'] = switcher.get(m.group(2),general)
                elif general!='both':
                    hdrext['senders'] = general
                hdrext['uri'] = m.group(3)
                hdrexts.append(hdrext)
            return hdrexts
        return None
