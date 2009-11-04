"""Definition of the GroupSpace content type
"""

from zope.interface import implements, directlyProvides

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from collective.groupspace.content import CONTENT_MESSAGE_FACTORY as _
from collective.groupspace.content.interfaces import IGroupSpace
from collective.groupspace.content.config import PROJECTNAME

from collective.groupspace.roles.interfaces import ILocalGroupSpacePASRoles
from collective.groupspace.workflow.interfaces import ILocalGroupSpaceWorkflow

GroupSpaceSchema = folder.ATFolderSchema.copy() 
GroupSpaceSchema['title'].storage = atapi.AnnotationStorage()
GroupSpaceSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(
    GroupSpaceSchema,
    folderish=True,
    moveDiscussion=False
)

class GroupSpace(folder.ATFolder):
    """GroupSpace container implementing the IGroupSpace interface.

       It implements the ILocalGroupSpacePASRoles so that local PAS roles
       can be assigned dynamically in the roles view.

       In addition, the ILocalGroupSpaceWorkflow is supported, so that when
       a GroupSpace is created, a special local workflow policy is added that
       enforces the use of a default workflow.
    """
    implements(IGroupSpace,
               ILocalGroupSpacePASRoles,
               ILocalGroupSpaceWorkflow)

    meta_type = "GroupSpace"
    schema = GroupSpaceSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')
    
    # The following attributes need to be initialized in order to support the
    # ILocalGroupSpacePASRoles interface
    user_roles = None
    group_roles = None

atapi.registerType(GroupSpace, PROJECTNAME)
