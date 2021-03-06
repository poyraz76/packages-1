
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
	autotools.configure("--disable-static\
						 --libexecdir=/usr/lib/openbox\
						 --prefix=/usr")

def build():
	autotools.make()
	
def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())
