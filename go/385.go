package main

import "unicode"

type NestedInteger struct {
}

func (n NestedInteger) IsInteger() bool

func (n NestedInteger) GetInteger() int

func (n *NestedInteger) SetInteger(value int)

func (n *NestedInteger) Add(elem NestedInteger)

func (n NestedInteger) GetList() []*NestedInteger

func deserialize(s string) *NestedInteger {
	index := 0
	var dfs func() *NestedInteger
	dfs = func() *NestedInteger {
		ni := &NestedInteger{}
		if s[index] == '[' {
			index++
			for s[index] != ']' {
				ni.Add(*dfs())
				if s[index] == ',' {
					index++
				}
			}
			index++
			return ni
		}

		negative := s[index] == '-'
		if negative {
			index++
		}
		num := 0
		for ; index < len(s) && unicode.IsDigit(rune(s[index])); index++ {
			num = num*10 + int(s[index]-'0')
		}
		if negative {
			num = -num
		}
		ni.SetInteger(num)
		return ni
	}
	return dfs()
}
