# Copyright (C) 2024 Elmar Meyer
# This file is part of slixmpp-jingle.
# See the file LICENSE for copying permission.

from slixmpp.xmlstream import ElementBase

class SourceGroup(ElementBase):
    name = 'ssrc-group'
    namespace = 'urn:xmpp:jingle:apps:rtp:ssma:0'
    plugin_attrib = 'ssrc-group'
    interfaces = {'semantics'}

    def getSDP(self):
        ret = ''
        for source in self['sources']:
            ret += ' '+source['ssrc']
        if ret!='':
            ret = "\r\na=ssrc-group:FID" + ret
        return ret

class Source(ElementBase):
    name = 'source'
    namespace = 'urn:xmpp:jingle:apps:rtp:ssma:0'
    plugin_attrib = 'source'
    interfaces = {'ssrc'}
    plugin_multi_attrib = 'sources'

    def getSDP(self):
        ret = ''
        for parameter in self['parameters']:
            ret += "\r\na=ssrc:%s %s" % (self['ssrc'],parameter.getSDP())
        return ret

class Parameter(ElementBase):
    name = 'parameter'
    namespace = 'urn:xmpp:jingle:apps:rtp:ssma:0'
    plugin_attrib = 'parameter'
    plugin_multi_attrib = 'parameters'
    interfaces = {'name','value'}
    plugin_multi_attrib = 'parameters'

    def getSDP(self):
        parameter = self['name']
        if self['value']:
            parameter += ":"+self['value']
        return parameter
