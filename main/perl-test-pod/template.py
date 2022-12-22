pkgname = "perl-test-pod"
pkgver = "1.52"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = ["gmake", "perl"]
makedepends = ["perl"]
depends = ["perl"]
pkgdesc = "Test::Pod - checks for POD errors in files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/release/Test-Pod"
source = f"$(CPAN_SITE)/Test/Test-Pod-{pkgver}.tar.gz"
sha256 = "60a8dbcc60168bf1daa5cc2350236df9343e9878f4ab9830970a5dde6fe8e5fc"

# FIXME visibility
hardening = ["!vis"]
