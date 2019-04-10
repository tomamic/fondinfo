sudo snap install go

sudo apt install libsdl2*-dev
go get -u github.com/gen2brain/dlgs
go get -u github.com/veandco/go-sdl2/{sdl,img,mix,ttf}
ln -s ~/fondinfo/go/g2dsdl ~/go/src/g2dsdl
go build g2dsdl
