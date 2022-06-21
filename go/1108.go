package main

func defangIPaddr(address string) (ans string) {
	// return strings.ReplaceAll(address, ".", "[.]")
	for _, v := range address {
		if v == '.' {
			ans += "[.]"
		} else {
			ans += string(v)
		}
	}
	return
}

func main() {

}
