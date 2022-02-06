package euler11_20

import "euler/mymath"

func triangleNumberGenerator() func() int {
	total := 0
	i := 1
	return func() int {
		total += i
		i++
		return total
	}
}

func Euler12Solve() int {
	gen := triangleNumberGenerator()
	for {
		n := gen()
		numOfDivisors := len(mymath.AllFactors(n))
		if numOfDivisors > 500 {
			return n
		}
	}
}
