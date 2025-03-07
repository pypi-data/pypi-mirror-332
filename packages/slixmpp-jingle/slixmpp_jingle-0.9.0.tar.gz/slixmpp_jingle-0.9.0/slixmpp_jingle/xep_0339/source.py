# Copyright (C) 2024 Elmar Meyer
# This file is part of slixmpp-jingle.
# See the file LICENSE for copying permission.

import logging


from slixmpp import Iq
from slixmpp.plugins import BasePlugin
from slixmpp.xmlstream import register_stanza_plugin
from slixmpp_jingle.xep_0166 import Jingle, Content
from slixmpp_jingle.xep_0167 import Description
from slixmpp_jingle.xep_0339.stanza import SourceGroup, Source, Parameter

import re

log = logging.getLogger(__name__)


class XEP_0339(BasePlugin):

    name = 'xep_0339'
    description = 'XEP-0339: Jingle'
    dependencies = set(['xep_0166','xep_0167'])
#    stanza = stanza

    def plugin_init(self):
        register_stanza_plugin(Iq,Jingle)
        register_stanza_plugin(Jingle,Content,True)
        register_stanza_plugin(Content,Description)
        register_stanza_plugin(Description,SourceGroup)
        register_stanza_plugin(Description,Source,True)
        register_stanza_plugin(SourceGroup,Source,True)
        register_stanza_plugin(Source,Parameter,True)

    def make_ssrcgroup(self, sdp):
        m = re.search(r'^a=ssrc-group:FID ([^\r]+)\r$',sdp,re.M)
        if m:
            ssrcgroup = SourceGroup()
            ssrcgroup['semantics'] = 'FID'
            ssrcs =m.group(1).split(' ')
            sources = []
            for ssrc_id in ssrcs:
                source = Source()
                source['ssrc'] = ssrc_id
                ssrcgroup.append(source)
                sources.append(self.make_source(sdp, ssrc_id))
#                ssrcgroup.append(self.make_source(sdp, ssrc_id))
            return (ssrcgroup, sources)
        return None

    def make_source(self, sdp, id = None):
        if id is None:
            m = re.search(r'^a=ssrc:(\S+)',sdp,re.M)
            if m is None:
               return None 
            id = m.group(1)
        iter = re.finditer(r'^a=ssrc:'+id+' ([^\r]+)\r$',sdp,re.M)
        if iter:
            source = Source()
            source['ssrc'] = id
            for p in iter:
                parameter = Parameter()
                s = p.group(1).split(':')
                if len(s)>1:
                    parameter['name'] = s[0]
                    parameter['value'] = s[1]
                else:
                    parameter['name'] = s[0]
                source.append(parameter)
            return source
        return None
