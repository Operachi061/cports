pkgname = "hare-json"
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
url = "https://git.sr.ht/~sircmpwn/hare-json"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "5488c5c2a205450667ae4278c6874c8d83177b0f6c12bb9e48d47713b6616782"
tools = {"AS": f"{self.profile().triplet}-as"}
