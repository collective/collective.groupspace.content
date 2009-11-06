Introduction
============

Implements a folderish content type that implements the ILocalGroupSpacePASRoles
interface, This interface allows managemment of dynamic roles for users and groups
in a context, and is implemented in collective.groupspace.roles.

This package is part of the collective.groupspace suite, whose components should
be installed as needed:

* collective.groupspace.workflow

* collective.groupspace.roles

* collective.groupspace.mail

collective.groupspace.content Installation
------------------------------------------

To install collective.groupspace.content into the global Python environment (or a workingenv),
using a traditional Zope 2 instance, you can do this:

* When you're reading this you have probably already run
  ``easy_install collective.groupspace.content``. Find out how to install setuptools
  (and EasyInstall) here:
  http://peak.telecommunity.com/DevCenter/EasyInstall

* Create a file called ``collective.groupspace.content-configure.zcml`` in the
  ``/path/to/instance/etc/package-includes`` directory.  The file
  should only contain this::

    <include package="collective.groupspace.content" />


Alternatively, if you are using zc.buildout and the plone.recipe.zope2instance
recipe to manage your project, you can do this:

* Add ``collective.groupspace.content`` to the list of eggs to install, e.g.:

    [buildout]
    ...
    eggs =
        ...
        collective.groupspace.content

* Tell the plone.recipe.zope2instance recipe to install a ZCML slug:

    [instance]
    recipe = plone.recipe.zope2instance
    ...
    zcml =
        collective.groupspace.content

* Re-run buildout, e.g. with:

    $ ./bin/buildout

You can skip the ZCML slug if you are going to explicitly include the package
from another package's configure.zcml file.

