package main

import (
	"sort"
	"strconv"
	"strings"
)

func alertNames(keyName []string, keyTime []string) (ans []string) {
	m := map[string][]int{}
	for i, key := range keyName {
		times := strings.Split(keyTime[i], ":")
		hour, _ := strconv.Atoi(times[0])
		minute, _ := strconv.Atoi(times[1])
		m[key] = append(m[key], hour*60+minute)
	}
	for k, vs := range m {
		if len(vs) > 2 {
			sort.Ints(vs)
			for i := 0; i < len(vs)-2; i++ {
				if vs[i+2]-vs[i] <= 60 {
					ans = append(ans, k)
					break
				}
			}
		}
	}
	sort.Strings(ans)
	return
}
