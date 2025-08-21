pkgname = "hare-ev"
pkgver = "0.25.2.0"
pkgrel = 0
build_style = "makefile"
make_install_args = ["PREFIX=/usr"]  # XXX prefix
hostmakedepends = [
    f"binutils-{self.profile().arch}",
    "hare",
]
makedepends = ["hare"]
pkgdesc = "Event loop for Hare"
license = "EUPL-1.2"
url = "https://git.sr.ht/~sircmpwn/hare-ev"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "75a30928e7b7d8e7df1eb3c9713827f05d517052bf946eea2d905716db1116ca"
tools = {"AS": f"{self.profile().triplet}-as"}
