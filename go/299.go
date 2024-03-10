package main

import "fmt"

func getHint(secret string, guess string) string {
	m_secret := make(map[byte]int, 0)
	m_guess := make(map[byte]int, 0)
	n_bull := 0
	n_cow := 0
	for i := range secret {
		ch_secret := secret[i]
		ch_guess := guess[i]
		if ch_secret == ch_guess {
			n_bull++
		} else {
			m_secret[ch_secret]++
			m_guess[ch_guess]++
		}
	}
	for k, n_secret := range m_secret {
		if n_guess, ok := m_guess[k]; ok {
			n_cow += min(n_secret, n_guess)
		}
	}
	return fmt.Sprintf("%dA%dB", n_bull, n_cow)
}
