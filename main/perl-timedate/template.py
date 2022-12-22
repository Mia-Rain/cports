pkgname = "perl-timedate"
pkgver = "2.33"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = ["gmake", "perl"]
makedepends = ["perl"]
depends = ["perl"]
pkgdesc = "Date formating subroutines"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/release/TimeDate"
source = f"$(CPAN_SITE)/Date/TimeDate-{pkgver}.tar.gz"
sha256 = "c0b69c4b039de6f501b0d9f13ec58c86b040c1f7e9b27ef249651c143d605eb2"

# FIXME visibility
hardening = ["!vis"]
