package main

type ThroneInheritance struct {
	king  string
	edges map[string][]string
	dead  map[string]struct{}
}

func Constructor(kingName string) ThroneInheritance {
	return ThroneInheritance{kingName, map[string][]string{}, map[string]struct{}{}}
}

func (t *ThroneInheritance) Birth(parentName string, childName string) {
	t.edges[parentName] = append(t.edges[parentName], childName)
}

func (t *ThroneInheritance) Death(name string) {
	t.dead[name] = struct{}{}
}

func (t *ThroneInheritance) GetInheritanceOrder() []string {
	ans := []string{}
	var preOrder func(name string)
	preOrder = func(name string) {
		if _, ok := t.dead[name]; !ok {
			ans = append(ans, name)
		}
		for _, child := range t.edges[name] {
			preOrder(child)
		}
	}
	preOrder(t.king)
	return ans
}

/**
 * Your ThroneInheritance object will be instantiated and called as such:
 * obj := Constructor(kingName);
 * obj.Birth(parentName,childName);
 * obj.Death(name);
 * param_3 := obj.GetInheritanceOrder();
 */
