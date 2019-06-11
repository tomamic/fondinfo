package main

import . "g2d"

type Animal interface {
    Say()
}

type Dog struct {
    name string
}

type Cat struct {
    name string
}

type Pig struct {
    name string
}

func NewDog(name string) *Dog {
    return &Dog{name}
}

func NewCat(name string) *Cat {
    return &Cat{name}
}

func NewPig(name string) *Pig {
    return &Pig{name}
}

func (d *Dog) Say() {
    Println("I'm " + d.name + " Dog. I say: WOOF!")
}

func (c *Cat) Say() {
    Println("I'm " + c.name + " Cat. I say: MEOW!")
}

func (p *Pig) Say() {
    Println("I'm " + p.name + " Pig. I say: OINK!")
}

func main() {
    d := NewDog("Danny")
    c := NewCat("Candy")
    p1 := NewPig("Peppa")
    p2 := NewPig("George")
    animals := []Animal{d, c, p1, p2}

    for _, a := range animals {
        a.Say()
    }
}
