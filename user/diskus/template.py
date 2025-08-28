pkgname = "diskus"
pkgver = "0.8.0"
pkgrel = 0
build_style = "cargo"
makedepends = [
    "cargo",
    "cargo-auditable"
]
pkgdesc = "Minimal, fast alternative to 'du -sh'"
license = "MIT"
url = "https://github.com/sharkdp/diskus"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "9733570d64a1eafcf96fe233fd978ec3855c77705005037ad253c49a188fdf51"
