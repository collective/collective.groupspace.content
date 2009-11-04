"""Definition of the GroupSpace content type
"""

from zope.interface import implements, directlyProvides

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from collective.groupspace.content import GROUPSPACE_MESSAGE_FACTORY as _
from collective.groupspace.content.interfaces import IGroupSpace
from collective.groupspace.content.config import PROJECTNAME

GroupSpaceSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

GroupSpaceSchema['title'].storage = atapi.AnnotationStorage()
GroupSpaceSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(
    GroupSpaceSchema,
    folderish=True,
    moveDiscussion=False
)

class GroupSpace(folder.ATFolder):
    """GroupSpace content type"""
    implements(IGroupSpace)

    meta_type = "GroupSpace"
    schema = GroupSpaceSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')
    
    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(GroupSpace, PROJECTNAME)
