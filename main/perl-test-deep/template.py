pkgname = "perl-test-deep"
pkgver = "1.130"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = ["gmake", "perl"]
makedepends = ["perl"]
depends = ["perl"]
pkgdesc = "Extremely flexible deep comparison"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/release/Test-Deep"
source = f"$(CPAN_SITE)/Test/Test-Deep-{pkgver}.tar.gz"
sha256 = "4064f494f5f62587d0ae501ca439105821ee5846c687dc6503233f55300a7c56"

# FIXME visibility
hardening = ["!vis"]
