package main

func isWinner(player1 []int, player2 []int) int {
	s1, s2 := 0, 0
	bonus1, bonus2 := 0, 0
	for i := range player1 {
		s1 += player1[i]
		s2 += player2[i]
		if bonus1 > 0 {
			s1 += player1[i]
			bonus1 -= 1
		}
		if bonus2 > 0 {
			s2 += player2[i]
			bonus2 -= 1
		}
		if player1[i] == 10 {
			bonus1 = 2
		}
		if player2[i] == 10 {
			bonus2 = 2
		}
	}
	if s1 > s2 {
		return 1
	} else if s1 < s2 {
		return 2
	}
	return 0
}
