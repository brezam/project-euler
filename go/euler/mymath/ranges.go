package mymath

import (
	"math"
)

// Returns a slice from `start` up to but not including `end` with step of 1
func CreateRange[T int | uint](start, end T) []T {
	answer := make([]T, end-start)
	i := 0
	for n := T(start); n < end; n++ {
		answer[i] = n
		i++
	}
	return answer
}

// Returns a slice from `start` up to but not including `end` with step of `step`
func CreateRangeStep[T int | uint](start, end, step T) []T {
	answer := make([]T, int(math.Ceil(float64(end-start)/float64(step))))
	i := 0
	for n := T(start); n < end; n += step {
		answer[i] = n
		i++
	}
	return answer
}
