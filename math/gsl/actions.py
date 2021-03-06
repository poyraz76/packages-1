
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
    autotools.configure("--disable-static")
						
def build():
    autotools.make()
	
def install():
    autotools.install()
    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "README", "THANKS")
