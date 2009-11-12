import unittest
from base import TestCase
from collective.groupspace.content import initialize

class TestInitialize(TestCase):
    def test_initialize(self):
        class Dummy:
            def registerClass(self, meta_type=None, constructors=None, icon=None, permission=None):
                self.meta_type = meta_type
                self.constructors = constructors
                self.icon = icon
                self.permission = permission
        obj = Dummy()
        initialize(obj)
        self.failUnless(obj.permission == "collective.groupspace.content: Add GroupSpace")
        self.failUnless(obj.icon == None)
        self.failUnless(obj.constructors[0].func_name == 'manage_addContentForm')
        self.failUnless(obj.constructors[1].func_name == 'manage_addContent')
        self.failUnless(obj.constructors[2].__name__ == 'contentinit')
        self.failUnless(obj.constructors[3].func_name == 'addGroupSpace')

def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestInitialize))
    return suite

if __name__ == '__main__':
    unittest.main()
