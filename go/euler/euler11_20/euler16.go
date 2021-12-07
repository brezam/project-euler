package euler11_20

import "math/big"

func Euler16Solve() int {
	n := big.NewInt(2)
	two := big.NewInt(2)
	for i := 2; i <= 1000; i++ {
		n = n.Mul(n, two)
	}
	stringN := n.String()
	total := 0
	for _, digitString := range stringN {
		digit := int(digitString - '0')
		total += digit
	}
	return total
}
