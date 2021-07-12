## Basic structs

- `type Point struct{ X, Y int }`
- `type Rect struct{ X, Y, W, H int }`
- `type Color struct{ R, G, B int }`

## Canvas functions

- `func InitCanvas(size Point)` : Initialize the drawing canvas
- `func MainLoop(tick ...func())` : Start the event loop, accepting an optional `tick` function, which will be called periodically
- `func ClearCanvas()` : Clear the canvas
- `func SetFrameRate(fps float64)` : Set the frame rate, which otherwise by default is 30 fps
- `func UpdateCanvas()` : Draw all pending graphics on the canvas, it is called automaticall after each `tick`
- `func CloseCanvas()` : Close the canvas and exit the main loop

## Drawing functions

- `func SetColor(c Color)` : Set the drawing color
- `func DrawLine(pt1, pt2 Point)` : Draw a line from `pt1` to `pt2`
- `func FillCircle(center Point, r int)` : Fill a circle, given `center` and `radius`
- `func FillRect(position, size Point)` : Fill a rectangle, given left-top `position` and `size`
- `func DrawText(txt string, position Point, size int)` : Draw a text, given left-top `position` and font px `size`
- `func DrawTextCentered(txt string, position Point, size int)` : Draw a centered text, given center `position` and font px `size`

## Images and sounds

- `func LoadImage(src string) string` : Load an image and return a name for it
- `func DrawImage(image string, p Point)` : Blit a whole image, given its name and the position
- `func DrawImageClip(image string, clip Rect, r Rect)` : Blit a portion of an image
- `func LoadAudio(src string) string` : Load a sound and return a name for it
- `func PlayAudio(audio string, loop bool)` : Play a sound, possibly in a loop, given its name
- `func PauseAudio(audio string)` : Stop playing a sound, given its name

## Input and output

- `func MousePosition() Point` : Get current mouse position
- `func KeyPressed(key string) bool` : Check if a key has been pressed after last `tick`
- `func KeyReleased(key string) bool` : Check if a key has been released after last `tick`
- `func Prompt(a ...interface{}) string` : Show a dialog for entering a line of text
- `func Confirm(a ...interface{}) bool` : Show a dialog for confirming a decision
- `func Alert(a ...interface{})` : Show a dialog with a message

## Utility functions

- `func Println(a ...interface{})` : Same as `fmt.Println`
- `func Printf(format string, a ...interface{})` : Same as `fmt.Printf`
- `func ToInt(text string, defval ...int) int` : Convert a text to an int, defaulting to 0 or `defval`
- `func ToFloat(text string, defval ...float64) float64` : Convert a text to a float, defaulting to 0 or `defval`
- `func RandInt(min, max int) int`: Generate a number in the closed range `[min, max]`

## Installing

- Go
```
sudo snap install --classic go
go get -u github.com/tomamic/fondinfo/go/g2d
```

- GopherJS : <http://www.ce.unipr.it/gopherjs>
```
go get -u github.com/gopherjs/gopherjs
cd ~/go/src/g2d
~/go/bin/gopherjs install
cp ~/go/pkg/linux_js/g2d.a ~/dev/gopherjs/pkg/g2d.a.js
```
