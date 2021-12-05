package data_structures

import (
	"fmt"
	"strings"
)

type intNode struct {
	previous *intNode
	next     *intNode
	data     int
}

type IntDeque interface {
	ToString() string
	ToSlice() []int
	AppendRight(n int)
	AppendLeft(n int)
	PopRight() int
	PopLeft() int
	GetLength() int
	Iter() func() (int, bool)
}

type IntDequeImpl struct {
	length uint
	head   *intNode
	tail   *intNode
}

func IntDequefromSlice(nums []int) *IntDequeImpl {
	deque := IntDequeImpl{length: 0, head: nil, tail: nil}
	if len(nums) == 0 {
		return &deque
	}
	deque.head = &intNode{data: nums[0]}
	deque.length++
	var current *intNode = deque.head
	for i := 1; i < len(nums); i++ {
		deque.length++
		newNode := &intNode{data: nums[i], previous: current}
		current.next = newNode
		current = newNode
	}
	deque.tail = current
	return &deque
}

func (deq *IntDequeImpl) ToString() string {
	var values strings.Builder
	current := deq.head
	fmt.Fprint(&values, "Deque<")
	for current != nil {
		if current != deq.head {
			fmt.Fprint(&values, ", ")
		}
		fmt.Fprintf(&values, "%d", current.data)
		current = current.next
	}
	fmt.Fprintf(&values, ">")
	return values.String()
}
func (deq *IntDequeImpl) ToSlice() []int {
	nums := make([]int, deq.length)
	if deq.length == 0 {
		return nums
	}
	current := deq.head
	for i := 0; i < int(deq.length); i++ {
		nums[i] = current.data
		current = current.next
	}
	return nums
}

func (deq *IntDequeImpl) AppendRight(n int) {
	newTail := intNode{previous: deq.tail, next: nil, data: n}
	deq.length++
	deq.tail.next = &newTail
	deq.tail = &newTail
}
func (deq *IntDequeImpl) AppendLeft(n int) {
	newHead := intNode{previous: nil, next: deq.head, data: n}
	deq.length++
	deq.head.previous = &newHead
	deq.head = &newHead
}
func (deq *IntDequeImpl) PopLeft() int {
	value := deq.head.data
	deq.head = deq.head.next
	deq.head.previous = nil
	deq.length--
	return value
}
func (deq *IntDequeImpl) PopRight() int {
	value := deq.tail.data
	deq.tail = deq.tail.previous
	deq.tail.next = nil
	deq.length--
	return value
}
func (deq *IntDequeImpl) GetLength() int {
	return int(deq.length)
}

// Returns an iterator function that iterates over each element of the deque from head to tail.
// It returns (value, finished) in each call. `value` refers to each element of the deque
// `finished` is true if iterator is already finished (in which case the accompanying `value` is only a zero value and not actual data)
func (deq *IntDequeImpl) Iter() func() (int, bool) {
	current := deq.head
	return func() (int, bool) {
		if current == nil {
			return 0, true
		}
		value := current.data
		current = current.next
		return value, false
	}
}
