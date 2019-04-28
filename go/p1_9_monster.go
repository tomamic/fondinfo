package main

import . "g2d"

func main() {
	w, h := 5, 5

	player := Point{0, 0}
	monster := player
	for monster == player {
		monster = Point{RandInt(0, w-1), RandInt(0, h-1)}
	}
	gold := player
	for (gold == player) || (gold == monster) {
		gold = Point{RandInt(0, w-1), RandInt(0, h-1)}
	}

	//Println("Monster: ", monster)
	//Println("Gold: ", gold)
	//Println("Player: ", player)

	for (player != monster) && (player != gold) {
		direction := Prompt(player, " wasd? ")
		if direction == "w" && player.Y > 0 {
			player.Y -= 1
		} else if direction == "a" && player.X > 0 {
			player.X -= 1
		} else if direction == "s" && player.Y < h-1 {
			player.Y += 1
		} else if direction == "d" && player.X < w-1 {
			player.X += 1
		}
	}
	if player == gold {
		Alert("Gold!")
	} else {
		Alert("Monster!")
	}
}
