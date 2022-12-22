pkgname = "perl-net-smtp-ssl"
pkgver = "1.04"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = ["gmake", "perl"]
makedepends = ["perl", "perl-io-socket-ssl"]
depends = list(makedepends)
pkgdesc = "SSL support for Net::SMTP"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/release/Net-SMTP-SSL"
source = f"$(CPAN_SITE)/Net/Net-SMTP-SSL-{pkgver}.tar.gz"
sha256 = "7b29c45add19d3d5084b751f7ba89a8e40479a446ce21cfd9cc741e558332a00"

# FIXME visibility
hardening = ["!vis"]
