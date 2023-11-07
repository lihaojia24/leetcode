package main

func findTheLongestBalancedSubstring(s string) (ans int) {
	cntZero := 0
	cntOne := 0
	countZeroFlag := true
	for _, ch := range s {
		if ch == '0' {
			if countZeroFlag {
				cntZero++
			} else {
				ans = max(ans, min(cntOne, cntZero)*2)
				cntOne = 0
				cntZero = 1
				countZeroFlag = true
			}
		}
		if ch == '1' {
			if countZeroFlag {
				countZeroFlag = false
			}
			cntOne++
		}
	}
	ans = max(ans, min(cntOne, cntZero)*2)
	return
}

func main() {

}
