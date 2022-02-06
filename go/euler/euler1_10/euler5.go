package euler1_10

import "euler/mymath"

func Euler5Solve() int {
	return mymath.Lcm(mymath.CreateRange(1, 21)...)
}
