package main

func findRepeatedDnaSequences(s string) (ans []string) {
	N := 10
	m := make(map[string]int)
	for i := 0; i < len(s)-N; i++ {
		subS := s[i : i+10]
		m[subS] += 1
		if m[subS] == 2 {
			ans = append(ans, subS)
		}
	}
	return ans
}

func findRepeatedDnaSequences2(s string) (ans []string) {
	N := 10
	if len(s) < N+1 {
		return ans
	}
	bin := map[byte]int{'A': 0, 'C': 1, 'G': 2, 'T': 3}
	m := make(map[int]int)
	key := 0
	for i := 0; i < N-1; i++ {
		key = (key << 2) | bin[s[i]]
	}
	for i := N - 1; i < len(s); i++ {
		key = ((key << 2) | bin[s[i]]) & (1<<(2*N) - 1)
		m[key] += 1
		if m[key] == 2 {
			ans = append(ans, s[i-N+1:i+1])
		}
	}
	return ans
}

// func main() {

// }
