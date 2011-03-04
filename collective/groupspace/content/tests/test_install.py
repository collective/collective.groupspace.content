from Products.PloneTestCase import PloneTestCase
from base import TestCase
import Products.Five
import Products.GenericSetup
import Products.CMFPlone
from Products.Five import zcml
from Testing import ZopeTestCase

import collective.groupspace.content


zcml.load_config('meta.zcml' , Products.CMFPlone)
zcml.load_config('meta.zcml' , Products.Five)
zcml.load_config('meta.zcml' , Products.GenericSetup)
zcml.load_config('configure.zcml' , Products.Five)
zcml.load_config('configure.zcml', collective.groupspace.content)
PloneTestCase.setupPloneSite(extension_profiles=\
                             ['collective.groupspace.content:default'])
        

class TestInstallation(PloneTestCase.PloneTestCase):
    
    def _setup(self):
        PloneTestCase.PloneTestCase._setup(self)
                    
    def test_install(self):
        self.failUnless('collective.groupspace.content' in \
                        [x['id'] for x \
                         in self.portal\
                         .portal_quickinstaller.listInstalledProducts()])

def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestInstallation))
    return suite
