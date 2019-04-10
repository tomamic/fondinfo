```
sudo snap install go

go get -u github.com/gopherjs/gopherjs
ln -s ~/dev/fondinfo/go/g2d  ~/go/src/g2d
~/go/bin/gopherjs build g2d
cp ~/go/pkg/linux_js/g2d.a ~/dev/gopherjs/pkg/g2d.a.js
```
