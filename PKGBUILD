# Maintainer: losted <losted@losted.net>
# Contributer: Laurie Clark-Michalek <bluepeppers@archlinux.us> and graysky <graysky AT archlinux DOR us>

pkgname=archey
pkgver=0.4.63.g9d9caf5
pkgrel=1
pkgdesc="Python script to display system infomation alongside the Arch Linux logo."
arch=('any')
url="http://github.com/losted/archey-git"
license=('GPL')
depends=('python')
makedepends=('git' 'python-distribute' 'miniupnpc')
optdepends=(
'python-mpd-git: python libary for mpd interaction',
'python-logbook-git: for logging'
'imagemagick: for default screenshot command'
)
conflicts=('archey3')
provides=('archey')
source=('git://github.com/losted/archey-git')
md5sums=('SKIP')
pkgver() {
	cd ${pkgname}-git
	git describe --always | sed 's|-|.|g'
}

package() {
	cd "$srcdir/$pkgname-git"
	python setup.py install --root=${pkgdir}
	install -D -m644 COPYING ${pkgdir}/usr/share/licenses/archey/COPYING
}
