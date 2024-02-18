package main

type Node struct {
	Val      int
	Children []*Node
}

func levelOrder(root *Node) (res [][]int) {
	if root == nil {
		return
	}
	st := []*Node{root}
	res_perlevel := []int{}
	for len(st) > 0 {
		res_perlevel = []int{}
		n := len(st)
		for i := 0; i < n; i++ {
			res_perlevel = append(res_perlevel, st[i].Val)
			for _, node := range st[i].Children {
				st = append(st, node)
			}
		}
		res = append(res, res_perlevel)
		st = st[n:]
	}
	return
}
