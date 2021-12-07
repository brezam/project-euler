package euler11_20

import (
	"math/big"
)

func Euler15Solve() *big.Int {
	// Answer is 40 choose 20 = 40*39*38*...*22*21/(20*19*18*...*2*1)
	denominator := big.NewInt(1)
	for i := int64(2); i <= 20; i++ {
		denominator = denominator.Mul(denominator, big.NewInt(i))
	}
	numerator := big.NewInt(1)
	for i := int64(21); i <= 40; i++ {
		numerator = numerator.Mul(numerator, big.NewInt(i))
	}
	return numerator.Div(numerator, denominator)
}
