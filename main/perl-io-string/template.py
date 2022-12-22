pkgname = "perl-io-string"
pkgver = "1.08"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = ["gmake", "perl"]
makedepends = ["perl"]
depends = ["perl"]
pkgdesc = "Emulate file interface for in-core strings"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/release/IO-String"
source = f"$(CPAN_SITE)/IO/IO-String-{pkgver}.tar.gz"
sha256 = "2a3f4ad8442d9070780e58ef43722d19d1ee21a803bf7c8206877a10482de5a0"

# FIXME visibility
hardening = ["!vis"]
