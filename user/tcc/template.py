pkgname = "tcc"
pkgver = "0.9.27.20250903"
_gitrev="bcfb872fd02aea39ef923a8b132b967e7786b743"
pkgrel = 0
archs = ["aarch64", "riscv64", "x86_64"]
build_style = "configure"
make_check_target = "test"
pkgdesc = "Tiny C Compiler"
license = "LGPL-2.1-or-later"
url = "http://repo.or.cz/tinycc.git"
source = f"{url}/snapshot/{_gitrev}.tar.gz"
sha256 = "e1120b194d20b9681494222b48e602bf0e69180aacefcde8c64bedd7d513b74e"
hardening = ["!int", "!scp", "!ssp", "!var-init", "!pie"]
options = ["!lto"]

def configure(self):
    self.do("./configure", "--config-musl", "--prefix=/usr")
