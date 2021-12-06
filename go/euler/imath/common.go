package imath

import (
	"errors"
	"math"
)

func Abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func Min(a int, b int) int {
	if a < b {
		return a
	}
	return b
}

func Max(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func MaxSlice(slice []int) (int, error) {
	total := math.MinInt
	if len(slice) > 0 {
		for _, v := range slice {
			if v > total {
				total = v
			}
		}
		return total, nil
	}
	return total, errors.New("empty slice")
}

func MinSlice(slice []int) (int, error) {
	total := math.MinInt
	if len(slice) > 0 {
		for _, v := range slice {
			if v < total {
				total = v
			}
		}
		return total, nil
	}
	return total, errors.New("empty slice")
}

// Performs reduction on nums by successive calling `intSliceReducer`.
// Parameter `intSliceReducer` must be a function that accepts two parameters, the accumulator and new value, respectively.
// Parameter `start` is the initial value for the accumulator.
func ReduceSlice(nums []int, intSliceReducer func(int, int) int, start int) int {
	total := start
	for _, v := range nums {
		total = intSliceReducer(total, v)
	}
	return total
}

// Calculates the greatest common denominator of `a` and `b`
func Gcd(a int, b int) int {
	if a == 0 {
		return b
	}
	if b == 0 {
		return a
	}
	for a != b {
		if a > b {
			a -= b
		} else {
			b -= a
		}
	}
	return a
}

// Calculates the greatest common denominator of all elements in `nums`
func GcdSlice(nums []int) int {
	switch len(nums) {
	case 0:
		return 0
	case 1:
		return nums[0]
	default:
		acc := 0
		for _, v := range nums {
			acc = Gcd(acc, v)
		}
		return acc
	}
}

// Calculates the least common multiple of `a` and `b`
func Lcm(a, b int) int {
	if a == 0 || b == 0 {
		return 0
	}
	return Abs(a*b) / Gcd(a, b)
}

// Calculates the least common multiple of all elements of `nums`
func LcmSlice(nums []int) int {
	switch len(nums) {
	case 0:
		return 1
	case 1:
		return nums[0]
	default:
		acc := 1
		for _, v := range nums {
			acc = Lcm(acc, v)
		}
		return acc
	}
}

// Calculates all factors of `n`
func AllFactors(n int) []int {
	if n < 1 {
		return []int{}
	} else if n == 1 {
		return []int{1}
	}
	factors := []int{1}
	revFactors := []int{n}
	for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
		if n%i == 0 {
			factors = append(factors, i)
			other := n / i
			if other != i {
				revFactors = append(revFactors, n/i)
			}
		}
	}
	for i := len(revFactors) - 1; i >= 0; i-- {
		factors = append(factors, revFactors[i])
	}
	return factors
}
