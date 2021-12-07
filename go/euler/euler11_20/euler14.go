package euler11_20

func collatz(n int) int {
	steps := 0
	for n > 1 {
		if n%2 == 0 {
			n /= 2
		} else {
			n = 3*n + 1
		}
		steps++
	}
	return steps
}

func Euler14Solve() int {
	bestN := 0
	bestChain := 0
	for n := 0; n < 1_000_000; n++ {
		chainLength := collatz(n)
		if chainLength > bestChain {
			bestN = n
			bestChain = chainLength
		}
	}
	return bestN
}
