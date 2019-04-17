package g2d

type Actor interface {
	Move()
	Collide(other Actor)
	Position() Rect
	Symbol() Rect
}

type Arena struct {
	w, h   int
	actors []Actor
}

func NewArena(size Size) *Arena {
	a := &Arena{size.W, size.H, []Actor{}}
	return a
}

func (a *Arena) Add(actor Actor) {
	if !a.Contains(actor) {
		a.actors = append(a.actors, actor)
	}
}

func (a *Arena) Remove(actor Actor) {
	for i, v := range a.actors {
		if v == actor {
			a.actors = append(a.actors[:i], a.actors[i+1:]...)
			return
		}
	}
}

func (a *Arena) Contains(actor Actor) bool {
	for _, v := range a.actors {
		if v == actor {
			return true
		}
	}
	return false
}

func (a *Arena) MoveAll() {
	actors := a.ReversedActors()
	for _, actor := range actors {
		actor.Move()
		for _, other := range actors {
			if actor != other && a.CheckCollision(actor, other) {
				actor.Collide(other)
				other.Collide(actor)
			}
		}
	}
}

func (a *Arena) CheckCollision(a1, a2 Actor) bool {
	r1 := a1.Position()
	r2 := a2.Position()
	return (r2.X < r1.X+r1.W && r1.X < r2.X+r2.W &&
		r2.Y < r1.Y+r1.H && r1.Y < r2.Y+r2.H &&
		a.Contains(a1) && a.Contains(a2))
}

func (a *Arena) Actors() []Actor {
	actors := make([]Actor, len(a.actors))
	for i, v := range a.actors {
		actors[i] = v
	}
	return actors
}

func (a *Arena) ReversedActors() []Actor {
	actors := make([]Actor, len(a.actors))
	for i, v := range a.actors {
		actors[len(a.actors)-i-1] = v
	}
	return actors
}

func (a *Arena) Size() Size {
	return Size{a.w, a.h}
}
