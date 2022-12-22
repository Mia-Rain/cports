pkgname = "perl-io-stringy"
pkgver = "2.113"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = ["gmake", "perl"]
makedepends = ["perl"]
depends = ["perl"]
pkgdesc = "I/O on in-core objects like strings/arrays"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/release/IO-stringy"
source = f"https://github.com/genio/IO-Stringy/archive/v{pkgver}.tar.gz"
sha256 = "faf40bbd657835ebcc87e556b802fbecaecc13776a03a8137cf935846108d022"

# FIXME visibility
hardening = ["!vis"]
