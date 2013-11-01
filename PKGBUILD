# Maintainer: Laurie Clark-Michalek <bluepeppers@archlinux.us>
# Contributer: graysky <graysky AT archlinux DOR us>

pkgname=archey3
pkgver=0.5
pkgrel=1
pkgdesc="Python script to display system infomation alongside the Arch Linux logo."
arch=('any')
url="http://bluepeppers.github.com/archey3"
license=('GPL')
depends=('python')
makedepends=('git' 'python-distribute')
optdepends=(
'python-mpd-git: python libary for mpd interaction',
'python-logbook-git: for logging'
'imagemagick: for default screenshot command'
)
conflicts=('archey')
provides=('archey')
source="git://github.com/bluepeppers/archey3.git"
md5sums=('SKIP')

pkgver() {
	cd ${pkgname}
	git describe --always | sed 's|-|.|g'
}

package() {
	cd "$srcdir/$pkgname"
	python setup.py install --root=${pkgdir}
	install -D -m644 COPYING ${pkgdir}/usr/share/licenses/archey/COPYING
}
