package main

import (
	"strconv"
	"strings"
)

func isIPv4(queryIP string) bool {
	fields := strings.Split(queryIP, ".")
	if len(fields) != 4 {
		return false
	}
	for _, num := range fields {
		if len(num) > 3 {
			return false
		}
		if len(num) > 1 && num[0] == '0' {
			return false
		}
		if i, err := strconv.Atoi(num); err != nil || i > 255 {
			return false
		}
	}
	return true
}

func isIPv6(queryIP string) bool {
	fields := strings.Split(queryIP, ":")
	if len(fields) != 8 {
		return false
	}
	for _, num := range fields {
		if len(num) > 4 {
			return false
		}
		if _, err := strconv.ParseUint(num, 16, 32); err != nil {
			return false
		}
	}
	return true
}

func validIPAddress(queryIP string) string {
	if isIPv6(queryIP) {
		return "IPv6"
	}
	if isIPv4(queryIP) {
		return "IPv4"
	}
	return "Neither"
}

// func main() {
// 	queryIP := "256.256.256.256"
// 	fmt.Printf("validIPAddress(queryIP): %v\n", validIPAddress(queryIP))
// }
