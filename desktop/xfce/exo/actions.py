#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import autotools, pisitools


def setup():
    autotools.configure()


def build():
    autotools.make()


def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING")

    pisitools.remove("/usr/share/icons/hicolor/icon-theme.cache")
