from zope import schema
from zope.interface import Interface

from zope.app.container.constraints import contains
from zope.app.container.constraints import containers

from collective.groupspace.content import CONTENT_MESSAGE_FACTORY as _

class IGroupSpace(Interface):
    """GroupSpace content type"""
    
    # -*- schema definition goes here -*-
