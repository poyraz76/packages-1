
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
    autotools.rawConfigure ("--prefix=%(ROOT)s --bindir=%(ROOT)s/bin --libdir=%(ROOT)s/lib --libexecdir=%(ROOT)s/lib --includedir=%(ROOT)s/usr/include --datadir=%(ROOT)s/usr/share --mandir=%(ROOT)s/usr/share/man" % { 'ROOT': get.installDIR()} )
						
def build():
	autotools.make ()
	
def install():
	autotools.make ("DESTDIR=%s install install-lib install-dev" % get.installDIR())
	pisitools.dosym ("/lib/libacl.so.1", "/usr/lib/libacl.so.1")
	# Install some documention

	pisitools.dodoc ("README", "VERSION", "doc/TODO", "doc/CHANGES", "doc/COPYING", "doc/COPYING.LGPL", "doc/INSTALL")
