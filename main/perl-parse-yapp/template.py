pkgname = "perl-parse-yapp"
pkgver = "1.21"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = ["gmake", "perl"]
makedepends = ["perl"]
depends = ["perl"]
pkgdesc = "Yet Another Parser Parser for Perl"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/release/Parse-Yapp"
source = f"$(CPAN_SITE)/Parse/Parse-Yapp-{pkgver}.tar.gz"
sha256 = "3810e998308fba2e0f4f26043035032b027ce51ce5c8a52a8b8e340ca65f13e5"

# FIXME visibility
hardening = ["!vis"]
