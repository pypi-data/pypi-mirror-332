# Copyright (C) 2024 Elmar Meyer
# This file is part of slixmpp-jingle.
# See the file LICENSE for copying permission.

from typing import Iterable, List, Tuple, Optional
from slixmpp.xmlstream import ElementBase, ET

import re

class Transport(ElementBase):
    name = 'transport'
    namespace = 'urn:xmpp:jingle:transports:ice-udp:1'
    plugin_attrib = 'ice-transport'
    interfaces = {'pwd','ufrag'}

    def getSDP(self):
        ret = ""
        if self['ufrag']:
            ret += "\r\na=ice-ufrag:%s" % self['ufrag']
        if self['pwd']:
            ret += "\r\na=ice-pwd:%s" % self['pwd']
        if self.get_plugin(name='fingerprint',check=True):
            ret += self['fingerprint'].getSDP() or ''
        for candidate in self['candidates']:
            ret += candidate.getSDP()
        return ret

class Candidate(ElementBase):
    name = 'candidate'
    namespace = 'urn:xmpp:jingle:transports:ice-udp:1'
    plugin_attrib = 'candidate'
    interfaces = {'component','foundation','generation','id','ip','port','priority','protocol','rel-addr','rel-port','network','type'}
    plugin_multi_attrib = 'candidates'

    def getSDP(self):
        if self['type']=='srflx':
            return "\r\na=candidate:%s %s %s %s %s %s typ %s raddr %s rport %s generation %s" % (self['foundation'],self['component'],self['protocol'],self['priority'],self['ip'],self['port'],self['type'],self['rel-addr'],self['rel-port'],self['generation'])
        else:
            return "\r\na=candidate:%s %s %s %s %s %s typ %s generation %s" % (self['foundation'],self['component'],self['protocol'],self['priority'],self['ip'],self['port'],self['type'],self['generation'])
#        return "\r\na=candidate:%s %s %s %s %s %s typ %s generation %s" % (self['id'],self['foundation'],self['protocol'],self['priority'],self['ip'],self['port'],self['type'],self['generation'])


class RemoteCandidate(ElementBase):
    name = 'remote-candidate'
    namespace = 'urn:xmpp:jingle:transports:ice-udp:1'
    plugin_attrib = 'remote_candidate'
    interfaces = {'component','ip','port'}
