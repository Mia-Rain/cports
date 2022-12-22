pkgname = "bdfresize"
pkgver = "1.5"
pkgrel = 0
build_style = "gnu_configure"
pkgdesc = "Tool for resizing BDF format font"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "http://openlab.ring.gr.jp/efont/dist/tools/bdfresize"
source = f"{url}/{pkgname}-{pkgver}.tar.gz"
sha256 = "440cfc0620a0237e46352c14a0774caa3f3059759b0a20defefc94e8490897a6"

# FIXME visibility
hardening = ["!vis"]
