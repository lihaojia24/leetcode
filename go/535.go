package main

import (
	"strconv"
	"strings"
)

const k1 = 1117
const k2 = 1e9 + 7

type Codec struct {
	key2url map[int]string
	url2key map[string]int
}

func Constructor535() Codec {
	return Codec{make(map[int]string), make(map[string]int)}
}

// Encodes a URL to a shortened URL.
func (this *Codec) encode(longUrl string) string {
	if key, ok := this.url2key[longUrl]; ok {
		return "http://tinyurl.com/" + strconv.Itoa(key)
	}
	key, base := 0, 1
	for _, v := range longUrl {
		key = (key + int(v)*base) % k2
		base = (k1 * base) % k2
	}
	for this.key2url[key] != "" {
		key = (key + 1) % k2
	}
	this.key2url[key] = longUrl
	this.url2key[longUrl] = key
	return "http://tinyurl.com/" + strconv.Itoa(key)
}

// Decodes a shortened URL to its original URL.
func (this *Codec) decode(shortUrl string) string {
	i := strings.LastIndexByte(shortUrl, '/')
	if key, err := strconv.Atoi(shortUrl[i+1:]); err == nil {
		return this.key2url[key]
	}
	return ""
}

/**
 * Your Codec object will be instantiated and called as such:
 * obj := Constructor();
 * url := obj.encode(longUrl);
 * ans := obj.decode(url);
 */

// func main() {

// }
