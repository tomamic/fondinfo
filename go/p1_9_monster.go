package main

import . "g2d"

func main() {
	w, h := 5, 5

	playerX := 0
	playerY := 0
	monsterX := playerX
	monsterY := playerY
	for monsterX == playerX && monsterY == playerY {
		monsterX = RandInt(0, w-1)
		monsterY = RandInt(0, h-1)
	}
	goldX := playerX
	goldY := playerY
	for (goldX == playerX && goldY == playerY) || (goldX == monsterX && goldY == monsterY) {
		goldX = RandInt(0, w-1)
		goldY = RandInt(0, h-1)
	}

	//Println("Monster:", monsterX, monsterY)
	//Println("Gold:", goldX, goldY)
	//Println("Player:", playerX, playerY)

	for (playerX != monsterX || playerY != monsterY) && (playerX != goldX || playerY != goldY) {
		direction := Prompt(playerX, playerY, " WASD? ")
		if direction == "w" && playerY > 0 {
			playerY -= 1
		} else if direction == "a" && playerX > 0 {
			playerX -= 1
		} else if direction == "s" && playerY < h-1 {
			playerY += 1
		} else if direction == "d" && playerX < w-1 {
			playerX += 1
		}
	}
	if playerX == goldX && playerY == goldY {
		Println("Gold!")
	} else {
		Println("Monster!")
	}
}

