package main

import "strconv"

func getFolderNames(names []string) (ans []string) {
	m := map[string]int{}
	for _, name := range names {
		if m[name] == 0 {
			ans = append(ans, name)
		} else {
			for m[name+"("+strconv.Itoa(m[name])+")"] > 0 {
				m[name]++
			}
			ans = append(ans, name+"("+strconv.Itoa(m[name])+")")
			m[name+"("+strconv.Itoa(m[name])+")"]++
		}
		m[name]++
	}
	return ans
}

// func main() {
// 	getFolderNames([]string{"ss", "aa", "ss", "aa(2)"})
// }
