package imath

import (
	"math"
)

// Returns a slice from `start` up to but not including `end` with step of 1
func CreateRange(start, end int) []int {
	answer := make([]int, end-start)
	i := 0
	for n := start; n < end; n++ {
		answer[i] = n
		i++
	}
	return answer
}

// Returns a slice from `start` up to but not including `end` with step of `step`
func CreateRangeStep(start, end, step int) []int {
	answer := make([]int, int(math.Ceil(float64(end-start)/float64(step))))
	i := 0
	for n := start; n < end; n += step {
		answer[i] = n
		i++
	}
	return answer
}
