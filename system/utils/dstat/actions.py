#!/usr/bin/python

# Created for SolusOS

from pisi.actionsapi import autotools, get, pisitools

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())
	pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "README", "TODO")
