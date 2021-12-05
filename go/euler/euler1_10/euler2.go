package euler1_10

func Euler2Solve() int {
	total := 0
	a, b := 0, 1
	for b < 4_000_000 {
		a, b = b, a+b
		if b%2 == 0 {
			total += b
		}
	}
	return total
}
