pkgname = "dinit-userservd"
pkgver = "0.1.0_git20220712"
_commit = "52ddb5049226a5917205b20561e30c82432ff8dc"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["linux-pam-devel"]
pkgdesc = "Dinit user instance manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/chimera-linux/dinit-userservd"
source = f"https://github.com/chimera-linux/{pkgname}/archive/{_commit}.tar.gz"
sha256 = "1d827738d801b8148b4f475ced7714e180d49b6b868ab2cacb657d25acc03623"
