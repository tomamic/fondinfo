cd g2d
go mod init g2d
go mod tidy
cd ..
go mod init fondinfo
go mod tidy
go mod edit -replace g2d=./g2d
go get g2d
