package euler1_10

import "euler/prime"

func Euler7Solve() uint {
	count := 0
	i := uint(0)
	for count < 10_001 {
		i++
		if prime.IsPrime(i) {
			count += 1
		}
	}
	return i
}
