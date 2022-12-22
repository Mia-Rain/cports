pkgname = "xsetroot"
pkgver = "1.1.3"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = [
    "xbitmaps", "libxmu-devel", "libxrender-devel",
    "libxfixes-devel", "libxcursor-devel"
]
pkgdesc = "X root window parameter setting utility"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/{pkgname}-{pkgver}.tar.gz"
sha256 = "80dbb0d02807e89294a042298b8a62f9aa0c3a94d89244ccbc35e4cf80fcaaba"

def post_install(self):
    self.install_license("COPYING")

# FIXME visibility
hardening = ["!vis"]
