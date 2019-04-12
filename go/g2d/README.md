```
sudo snap install go
ln -s ~/dev/fondinfo/go/g2d ~/go/src/g2d
cd ~/go/src/g2d
```

- SDL2
```
sudo apt install libsdl2*-dev
go get -u github.com/gen2brain/dlgs
go get -u github.com/veandco/go-sdl2/{sdl,img,mix,ttf}
go install
```

- GopherJS
```
go get -u github.com/gopherjs/gopherjs
~/go/bin/gopherjs install
cp ~/go/pkg/linux_js/g2d.a ~/dev/gopherjs/pkg/g2d.a.js
```
