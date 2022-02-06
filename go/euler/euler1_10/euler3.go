package euler1_10

import (
	"euler/mymath"
	"euler/prime"
)

func Euler3Solve() int {
	if answer, err := mymath.Max(prime.PrimeFactors(600851475143)...); err != nil {
		return answer
	}
	return -1
}
