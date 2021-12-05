package euler1_10

import "euler/imath"

func Euler5Solve() int {
	return imath.LcmSlice(imath.CreateRange(1, 21))
}
