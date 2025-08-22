pkgname = "ghc"
pkgver = "9.10.2"
pkgrel = 0
archs = ["aarch64", "x86_64"]
build_style = "configure"
configure_args = ["--prefix=/usr"]
hostmakedepends = [
    "automake",
    "libffi8",
    "numactl-libs",
    "perl"
]
depends = ["libffi8", "numactl-libs", "perl"]
pkgdesc = "Glorious Glasgow Haskell Compiler"
license = "BSD-3-Clause"
url = "http://www.haskell.org/ghc"
source = f"https://downloads.haskell.org/ghc/{pkgver}/ghc-{pkgver}-{self.profile().arch}-alpine3_12-linux-static.tar.xz"
sha256 = "4af3e763578496cae898e96ad35cb7fc2ed1d7d1f40e3e9b9dc0455f0d3bf776"
# no check target
options = ["!check"]

def build(self):
    pass

def post_install(self):
    for slib in self.find(self.destdir, "*.a"):
        print(slib)

    self.install_license(f"share/doc/x86_64-linux-ghc-{pkgver}/ghc-{pkgver}/LICENSE")


@subpackage("ghc-static")
def _(self):
    # /home/bartlomiej/repositories/tool/cports/bldroot/destdir/ghc-9.10.2/ghc/usr/lib/ghc-9.10.2/lib/x86_64-linux-ghc-9.10.2/rts-1.0.2/libCffi_debug_p.a
    return [f"usr/lib/ghc-{pkgver}/lib/*-linux-ghc-{pkgver}"]
