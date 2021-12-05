package euler1_10

import "euler/prime"

func Euler10Solve() int {
	total := uint(0)
	for _, v := range prime.SievePrime(uint(2_000_000)) {
		total += v
	}
	return int(total)
}
