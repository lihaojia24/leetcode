package main

type unionSet struct {
	parents []int
}

func (this *unionSet) find(x int) int {
	if this.parents[x] != x {
		this.parents[x] = this.find(this.parents[x])
		return this.parents[x]
	} else {
		return x
	}
}

func (this *unionSet) union(x, y int) {
	xP := this.find(x)
	yP := this.find(y)
	if xP != yP {
		this.parents[xP] = yP
	}
}

func CreateUnionSet(n int) *unionSet {
	us := &unionSet{}
	us.parents = make([]int, n)
	for i := 0; i < len(us.parents); i++ {
		us.parents[i] = i
	}
	return us
}

func euler(n int) []int {
	notPrime := make([]bool, n)
	primes := []int{}
	for i := 2; i < n; i++ {
		if !notPrime[i] {
			primes = append(primes, i)
		}
		for j := 0; primes[j]*i < n; j++ {
			notPrime[primes[j]*i] = true
			if i%primes[j] == 0 {
				break
			}
		}
	}
	return primes
}

func maxl(nums []int) int {
	ans := nums[0]
	for i := 1; i < len(nums); i++ {
		if nums[i] > ans {
			ans = nums[i]
		}
	}
	return ans
}

func largestComponentSize(nums []int) int {
	n := maxl(nums)
	primes := euler(n + 1)
	us := CreateUnionSet(n + 1)
	for _, num := range nums {
		q := num
		for j := 0; j < len(primes) && primes[j]*primes[j] <= q; j++ {
			if q%primes[j] == 0 {
				us.union(num, primes[j])
				for q%primes[j] == 0 {
					q /= primes[j]
				}
			}
		}
		if q > 1 {
			us.union(num, q)
		}
	}
	ans := make([]int, n+1)
	for _, num := range nums {
		ans[us.find(num)]++
	}
	return maxl(ans)
}

// func main() {
// 	nums := []int{4, 6, 15, 35}
// 	fmt.Printf("largestComponentSize(nums): %v\n", largestComponentSize(nums))
// }
