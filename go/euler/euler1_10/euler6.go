package euler1_10

import "euler/mymath"

func sumOfSquares(nums []int) int {
	total := 0
	for _, v := range nums {
		total += v * v
	}
	return total
}

func squareOfSum(nums []int) int {
	total := 0
	for _, v := range nums {
		total += v
	}
	return total * total
}

func Euler6Solve() int {
	nums := mymath.CreateRange(1, 101)
	return squareOfSum(nums) - sumOfSquares(nums)
}
