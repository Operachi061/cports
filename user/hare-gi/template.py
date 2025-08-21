pkgname = "hare-gi"
pkgver = "0.1.0"
pkgrel = 0
build_style = "makefile"
make_install_args = ["PREFIX=/usr"]  # XXX prefix
hostmakedepends = [
    "at-spi2-core-devel",
    f"binutils-{self.profile().arch}",
    "gdk-pixbuf-devel",
    "gobject-introspection-devel",
    "gtk+3-devel",
    "gtk4-devel",
    "hare",
    "pkgconf",
    "wayland-devel"
]
makedepends = ["hare"]
pkgdesc = "Wayland client & server implementation for Hare"
license = "EUPL-1.2"
url = "https://git.sr.ht/~yerinalexey/hare-gi"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "3d70fde77c07be396d5e7cfc1344e72a3fb4b1ce8a58eeb938bd792c6a1a452e"
tools = {"AS": f"{self.profile().triplet}-as"}

def check(self):
    pass
