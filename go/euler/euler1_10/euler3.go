package euler1_10

import (
	"euler/imath"
	"euler/prime"
)

func Euler3Solve() int {
	if answer, err := imath.MaxSlice(prime.Factorize(600851475143)); err != nil {
		return answer
	}
	return -1
}
