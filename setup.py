# -*- coding: utf-8 -*-
"""
collective.groupspace.content
"""
import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '1.0.2'

long_description = (
    read('README.txt')
    + '\n\n' +
    read('CHANGES.txt')
    )

tests_require=['zope.testing']

setup(name='collective.groupspace.content',
    version=version,
    description="Plone collective.groupspace content type for privately working in groups",
    long_description=long_description,
    classifiers=[
      "Development Status :: 5 - Production/Stable",
      "Environment :: Web Environment",
      "Framework :: Plone",
      "Framework :: Zope2",
      "Intended Audience :: Developers",
      "License :: OSI Approved :: GNU General Public License (GPL)",
      "Operating System :: OS Independent",
      "Programming Language :: Python",
      "Topic :: Internet :: WWW/HTTP :: Dynamic Content",        
      "Topic :: Office/Business :: Groupware",
      "Topic :: Software Development :: Libraries :: Python Modules",
      ],
    keywords='groupspace, roles, pas, borg.localrole, grufspaces',
    author='Maik Roeder',
    author_email='roeder@berg.net',
    url='http://plone.org/products/collective.groupspace.content',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective', 'collective.groupspace'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools',
                      # -*- Extra requirements: -*-
                      ],
    tests_require=tests_require,
    extras_require=dict(tests=tests_require),
    test_suite = 'collective.groupspace.tests.test_docs.test_suite',
    entry_points="""
    # -*- Entry points: -*-

    [distutils.setup_keywords]
    paster_plugins = setuptools.dist:assert_string_list

    [egg_info.writers]
    paster_plugins.txt = setuptools.command.egg_info:write_arg
    """,
    paster_plugins = ["ZopeSkel"],
    )
