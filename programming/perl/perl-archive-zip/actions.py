#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import perlmodules, pisitools


def setup():
    perlmodules.configure()


def build():
    perlmodules.make()


def install():
    perlmodules.install()

    pisitools.dodoc("LICENSE")
