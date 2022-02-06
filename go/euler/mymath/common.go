package mymath

import (
	"errors"
	"math"
)

type Number interface {
	int | int64 | float64
}

func Sign[T Number](value T) int {
	if value > 0 {
		return 1
	} else if value < 0 {
		return -1
	} else {
		return 0
	}
}

func Abs[T Number](a T) T {
	if a < 0 {
		return -a
	}
	return a
}

func min[T Number](a T, b T) T {
	if a < b {
		return a
	}
	return b
}

func max[T Number](a T, b T) T {
	if a > b {
		return a
	}
	return b
}

func Max[T Number](slice ...T) (T, error) {
	var total T
	if len(slice) > 0 {
		total = slice[0]
		for _, v := range slice[1:] {
			if v > total {
				total = v
			}
		}
		return total, nil
	}
	return total, errors.New("empty slice")
}

func Min[T Number](slice ...T) (T, error) {
	var total T
	if len(slice) > 0 {
		total = slice[0]
		for _, v := range slice[1:] {
			if v < total {
				total = v
			}
		}
		return total, nil
	}
	return total, errors.New("empty slice")
}

// Calculates the greatest common denominator of `a` and `b`
func gcd(a int, b int) int {
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
func Gcd(nums ...int) int {
	switch len(nums) {
	case 0:
		return 0
	case 1:
		return nums[0]
	default:
		acc := 0
		for _, v := range nums {
			acc = gcd(acc, v)
		}
		return acc
	}
}

// Calculates the least common multiple of `a` and `b`
func lcm(a, b int) int {
	if a == 0 || b == 0 {
		return 0
	}
	return Abs(a*b) / Gcd(a, b)
}

// Calculates the least common multiple of all elements of `nums`
func Lcm(nums ...int) int {
	switch len(nums) {
	case 0:
		return 1
	case 1:
		return nums[0]
	default:
		acc := 1
		for _, v := range nums {
			acc = lcm(acc, v)
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
