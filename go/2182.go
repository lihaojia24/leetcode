package main

func repeatLimitedString(s string, repeatLimit int) string {
	m := make([]int, 26)
	for i := range s {
		// fmt.Printf("s[i]: %v\n", s[i]-'a')
		m[s[i]-'a']++
	}
	// fmt.Printf("m: %v\n", m)
	res := make([]byte, len(s))
	io := 25
	ir := 0
	for io > -1 {
		// fmt.Printf("io: %v\n", io)
		// fmt.Printf("m[io]: %v\n", m[io])
		if m[io] <= 0 {
			io--
			continue
		}
		if m[io] <= repeatLimit {
			for i := 0; i < m[io]; i++ {
				res[ir] = byte('a' + io)
				ir++
			}
			io--
		} else {
			for i := 0; i < repeatLimit; i++ {
				res[ir] = byte('a' + io)
				ir++
			}
			m[io] -= repeatLimit
			t := io - 1
			for t > -1 {
				if m[t] > 0 {
					break
				}
				t--
			}
			if t == -1 {
				break
			} else {
				res[ir] = byte('a' + t)
				m[t]--
				ir++
			}
		}
	}
	return string(res[:ir])
}

// func main() {
// 	fmt.Printf("repeatLimitedString(\"cczazcc\", 3): %v\n", repeatLimitedString("cczazcc", 3))
// }
