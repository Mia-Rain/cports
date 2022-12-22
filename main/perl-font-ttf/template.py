pkgname = "perl-font-ttf"
pkgver = "1.06"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = ["gmake", "perl-io-string"]
makedepends = ["perl-io-string"]
depends = ["perl-io-string"]
pkgdesc = "Perl module for TrueType Font hacking"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Artistic-2.0"
url = "https://metacpan.org/release/Font-TTF"
source = f"$(CPAN_SITE)/Font/Font-TTF-{pkgver}.tar.gz"
sha256 = "4b697d444259759ea02d2c442c9bffe5ffe14c9214084a01f743693a944cc293"

# FIXME visibility
hardening = ["!vis"]
