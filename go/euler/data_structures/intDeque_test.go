package data_structures

import (
	"fmt"
	"testing"
)

func compareSlices(slice1 []int, slice2 []int) bool {
	if len(slice1) != len(slice2) {
		return false
	}
	for i := 0; i < len(slice1); i++ {
		if slice1[i] != slice2[i] {
			return false
		}
	}
	return true
}

func TestIntDequeAppendsAndPops(t *testing.T) {
	deq := IntDequefromSlice([]int{1, 2, 3, 4})
	fmt.Println(deq.ToString())
	if !compareSlices([]int{1, 2, 3, 4}, deq.ToSlice()) {
		t.Errorf("FAIL: {%v} is not equal to {%v}", []int{1, 2, 3, 4}, deq.ToSlice())
	}
	if deq.GetLength() != 4 {
		t.Error("FAIL: deque length should be 4")
	}

	deq.AppendLeft(0)
	if !compareSlices([]int{0, 1, 2, 3, 4}, deq.ToSlice()) {
		t.Errorf("FAIL: {%v} is not equal to {%v}", []int{0, 1, 2, 3, 4}, deq.ToSlice())
	}
	if deq.GetLength() != 5 {
		t.Error("FAIL: deque length should be 5")
	}

	deq.AppendRight(5)
	if !compareSlices([]int{0, 1, 2, 3, 4, 5}, deq.ToSlice()) {
		t.Errorf("FAIL: {%v} is not equal to {%v}", []int{0, 1, 2, 3, 4, 5}, deq.ToSlice())
	}
	if deq.GetLength() != 6 {
		t.Error("FAIL: deque length should be 6")
	}

	deq.PopRight()
	if !compareSlices([]int{0, 1, 2, 3, 4}, deq.ToSlice()) {
		t.Errorf("FAIL: {%v} is not equal to {%v}", []int{0, 1, 2, 3, 4}, deq.ToSlice())
	}
	if deq.GetLength() != 5 {
		t.Error("FAIL: deque length should be 5")
	}
	if deq.tail.data != 4 || deq.tail.next != nil {
		t.Errorf("FAIL: deque tail is %v", deq.tail)
	}

	deq.PopLeft()
	if !compareSlices([]int{1, 2, 3, 4}, deq.ToSlice()) {
		t.Errorf("FAIL: {%v} is not equal to {%v}", []int{1, 2, 3, 4}, deq.ToSlice())
	}
	if deq.GetLength() != 4 {
		t.Error("FAIL: deque length should be 4")
	}
	if deq.head.data != 1 || deq.head.previous != nil {
		t.Errorf("FAIL: deque head is %v", deq.head)
	}
}

func TestIntDequeChainAndLength(t *testing.T) {
	deq := IntDequefromSlice([]int{-8, 5, 3, 5, -2, 7, 1, -10, 2, 1, 6, -1})
	current := deq.head
	i := 1
	for current.next != nil {
		i++
		if current.next.previous != current {
			t.Error("node .next .previous should be equal to itself but isn't")
		}
		current = current.next
	}
	if deq.GetLength() != i {
		t.Errorf("deque length should be %d but is %d", i, deq.GetLength())
	}
}

func TestIntDequeIterator(t *testing.T) {
	slice := []int{-8, 5, 3, 5, -2, 7, 1, -10, 2, 1, 6, -1}
	deq := IntDequefromSlice(slice)
	iter := deq.Iter()
	i := 0
	for {
		v, finished := iter()
		if finished {
			break
		}
		if (slice[i] != v) {
			t.Errorf("Iterator FAIL: %d should be %d", v, slice[i])
		}
		i++
	}
}

func SkipVerifyIntDequeImplementsInterface() {
	var _ IntDeque = &IntDequeImpl{} // Compile time error if &IntDequeImpl doesn't implement IntDeque
}
