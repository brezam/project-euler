package euler1_10

func Euler1Solve() int {
	total := 0
	for i := 0; i < 1_000; i++ {
		if i%3 == 0 || i%5 == 0 {
			total += i
		}
	}
	return total
}
