from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get



def install():
    def do_chmod(path, mode):
        path = "%s/%s" % (get.installDIR(), path)
        shelltools.chmod (path, mode=mode)

    # Install everything
    pisitools.insinto("/", "root/*")

    for dire in ["/tmp", "/var/tmp", "/dev", "/proc", "/sys", "/var/lock", "/root", "/home"]:
		pisitools.dodir (dire)
		
    # Adjust permissions
    do_chmod("/tmp", 01777)
    do_chmod("/var/tmp", 01777)
    do_chmod("/var/lock", 0775)
    do_chmod("/usr/share/baselayout/shadow", 0600)
    do_chmod("/dev", 0755)
    do_chmod("/proc", 0555)
    do_chmod("/sys", 0755)
    do_chmod("/home", 0755)

    pisitools.dosym ("/proc/self/mounts", "/etc/mtab")

    # Write out a default .profile.. temporary
    shelltools.echo ("%s/etc/skel/.profile" % get.installDIR(), "source /etc/profile")
    shelltools.echo ("%s/etc/skel/.bashrc" % get.installDIR(), "source /etc/profile")

    # Bump this ourselves in baselayout next time
    pisitools.dosed ("%s/etc/issue" % get.installDIR(), "Alpha8", "Alpha 9")
    pisitools.dosed ("%s/usr/share/baselayout/issue" % get.installDIR(), "Alpha8", "Alpha 9")
