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
from slixmpp_jingle.xep_0167 import Description, PayloadType
from slixmpp_jingle.xep_0293 import stanza, RtcpFB, Parameter, RtcpFBTrrInt

import re

log = logging.getLogger(__name__)


class XEP_0293(BasePlugin):

    name = 'xep_0293'
    description = 'XEP-0293: Jingle'
    dependencies = set(['xep_0166','xep_0167'])
    stanza = stanza

    def plugin_init(self):
        register_stanza_plugin(Iq,Jingle)
        register_stanza_plugin(Jingle,Content,True)
        register_stanza_plugin(Content,Description)
        register_stanza_plugin(Description,RtcpFB,True)
        register_stanza_plugin(Description,PayloadType,True)
        register_stanza_plugin(PayloadType,RtcpFB,True)
        register_stanza_plugin(RtcpFB,Parameter,True)
        register_stanza_plugin(PayloadType,RtcpFBTrrInt,True)

    def make_rtcpfb(self,sdp,id='*'):
        ret = []
        iter = re.finditer(r'^a=rtcp-fb:'+id+r' +(\S+)(?: +(\S+))?\r$',sdp,re.M)
        for m in iter:
            rtcpfb = RtcpFB()
            rtcpfb['type'] = m.group(1)
            if m.group(2):
                rtcpfb['subtype'] = m.group(2)
                m = re.search(r'^a=rtcp-fb:'+id+r' +[\S]+(?: +\S+)? +([^:\r]+:[^,\r]+(?:,[^:\r]+:[^,\r])*)\r$',sdp,re.M)
                if m:
                    parameters = m.group(1).split(',')
                    for p in parameters:
                        parameter = Parameter()
                        param = p.split(':')
                        parameter['name'] = param[1]
                        if len(param)>1:
                            parameter['value'] = param[2]
                        rtcpfb.append(parameter)
            ret.append(rtcpfb)
        return ret

