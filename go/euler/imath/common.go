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

// Calculates the product of all the elements in `nums`.
// When `nums` is empty, returns 1.
func ProdSlice(nums []int) int {
	total := 1
	for _, v := range nums {
		total *= v
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
