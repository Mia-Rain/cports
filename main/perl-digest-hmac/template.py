pkgname = "perl-digest-hmac"
pkgver = "1.04"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = ["gmake", "perl"]
makedepends = ["perl"]
depends = ["perl"]
pkgdesc = "Perl interface to HMAC message-digest algorithms"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/release/Digest-HMAC"
source = f"$(CPAN_SITE)/Digest/Digest-HMAC-{pkgver}.tar.gz"
sha256 = "d6bc8156aa275c44d794b7c18f44cdac4a58140245c959e6b19b2c3838b08ed4"

# FIXME visibility
hardening = ["!vis"]
