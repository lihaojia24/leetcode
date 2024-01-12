package main

import (
	"strings"
)

func numUniqueEmails(emails []string) int {
	ans := map[string]struct{}{}
	for _, email := range emails {
		field := strings.Split(email, "@")
		local_name, host_name := field[0], field[1]
		local_name = strings.Split(local_name, "+")[0]
		local_name = strings.ReplaceAll(local_name, ".", "")
		ans[local_name+"@"+host_name] = struct{}{}
	}
	return len(ans)
}
