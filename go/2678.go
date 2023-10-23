package main

import "strconv"

func countSeniors(details []string) (ans int) {
	for _, s := range details {
		age, _ := strconv.Atoi(s[11:13])
		if age > 60 {
			ans += 1
		}
	}
	return
}

func main() {

}
