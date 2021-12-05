package euler1_10

func Euler9Solve() int {
	for c := 1000; c > 0; c-- {
		for b := 1000 - c - 1; b > (1000-c)/2; b-- {
			a := 1000 - c - b
			if a*a+b*b == c*c {
				return a * b * c
			}
		}
	}
	return -1
}
