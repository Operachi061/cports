pkgname = "hare-wayland"
pkgver = "0.25.2.0"
pkgrel = 0
build_style = "makefile"
make_install_args = ["PREFIX=/usr"]  # XXX prefix
hostmakedepends = [
    f"binutils-{self.profile().arch}",
    "hare",
    "hare-xml",
    "pkgconf",
    "wayland-devel",
]
makedepends = ["hare"]
pkgdesc = "Wayland client & server implementation for Hare"
license = "EUPL-1.2"
url = "https://git.sr.ht/~sircmpwn/hare-wayland"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "62bb33bdf1e21968e65ca4b44fad60abc7ed1801c2b747ca2b7a9c341537149e"
tools = {"AS": f"{self.profile().triplet}-as"}
