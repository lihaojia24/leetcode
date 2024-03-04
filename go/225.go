package main

type MyStack struct {
	q1, q2 []int
}

func Constructor225() (s MyStack) {
	return
}

func (s *MyStack) Push(x int) {
	s.q2 = append(s.q2, x)
	if len(s.q1) > 0 {
		s.q2 = append(s.q2, s.q1...)
		s.q1 = []int{}
	}
	s.q1, s.q2 = s.q2, s.q1
}

func (s *MyStack) Pop() int {
	v := s.q1[0]
	s.q1 = s.q1[1:]
	return v
}

func (s *MyStack) Top() int {
	return s.q1[0]
}

func (s *MyStack) Empty() bool {
	return len(s.q1) < 1
}

/**
 * Your MyStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.Empty();
 */
