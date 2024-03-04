package main

type MyQueue struct {
	s1, s2 []int
}

func Constructor232() (q MyQueue) {
	return
}

func (q *MyQueue) Push(x int) {
	for len(q.s1) > 0 {
		q.s2 = append(q.s2, q.s1[len(q.s1)-1])
		q.s1 = q.s1[:len(q.s1)-1]
	}
	q.s2 = append(q.s2, x)
	for len(q.s2) > 0 {
		q.s1 = append(q.s1, q.s2[len(q.s2)-1])
		q.s2 = q.s2[:len(q.s2)-1]
	}
}

func (q *MyQueue) Pop() int {
	v := q.s1[len(q.s1)-1]
	q.s1 = q.s1[:len(q.s1)-1]
	return v
}

func (q *MyQueue) Peek() int {
	return q.s1[len(q.s1)-1]
}

func (q *MyQueue) Empty() bool {
	return len(q.s1) < 1
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Peek();
 * param_4 := obj.Empty();
 */
