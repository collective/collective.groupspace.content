
import config
from Products.CMFCore import permissions as CMFCorePermissions
from AccessControl.SecurityInfo import ModuleSecurityInfo
from Products.CMFCore.permissions import setDefaultRoles

security = ModuleSecurityInfo(config.PROJECTNAME)
for p in config.ADD_PERMISSIONS:
    
    security.declarePublic(config.ADD_PERMISSIONS[p])
    MyPermission = config.ADD_PERMISSIONS[p]
    setDefaultRoles(MyPermission, ('Manager', 'Owner'))
