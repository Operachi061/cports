pkgname = "hare-xml"
pkgver = "0.25.2.0"
pkgrel = 0
build_style = "makefile"
make_install_args = ["PREFIX=/usr"]  # XXX prefix
hostmakedepends = [
    f"binutils-{self.profile().arch}",
    "hare",
]
makedepends = ["hare"]
pkgdesc = "XML support for Hare"
license = "EUPL-1.2"
url = "https://git.sr.ht/~sircmpwn/hare-xml"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "76c2d6321524b8065cc78874e9677600949dc4bff11bb75c9e07c4180093cfbb"
tools = {"AS": f"{self.profile().triplet}-as"}
