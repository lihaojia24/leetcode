package main

type AuthenticationManager struct {
	tokens map[string]int
	ttl    int
}

func Constructor(timeToLive int) AuthenticationManager {
	return AuthenticationManager{map[string]int{}, timeToLive}
}

func (am *AuthenticationManager) Generate(tokenId string, currentTime int) {
	am.tokens[tokenId] = am.ttl + currentTime
}

func (am *AuthenticationManager) Renew(tokenId string, currentTime int) {
	if dt, ok := am.tokens[tokenId]; ok && dt > currentTime {
		am.tokens[tokenId] = currentTime + am.ttl
	}
}

func (am *AuthenticationManager) CountUnexpiredTokens(currentTime int) (ans int) {
	for _, dt := range am.tokens {
		if dt < currentTime {
			ans++
		}
	}
	return
}

/**
 * Your AuthenticationManager object will be instantiated and called as such:
 * obj := Constructor(timeToLive);
 * obj.Generate(tokenId,currentTime);
 * obj.Renew(tokenId,currentTime);
 * param_3 := obj.CountUnexpiredTokens(currentTime);
 */

func main() {

}
