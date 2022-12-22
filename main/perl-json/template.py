pkgname = "perl-json"
pkgver = "4.10"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = ["gmake", "perl"]
makedepends = ["perl"]
checkdepends = ["perl-test-pod"]
depends = ["perl"]
pkgdesc = "JSON encoder/decoder"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/release/JSON"
source = f"$(CPAN_SITE)/JSON/JSON-{pkgver}.tar.gz"
sha256 = "df8b5143d9a7de99c47b55f1a170bd1f69f711935c186a6dc0ab56dd05758e35"

# FIXME visibility
hardening = ["!vis"]
