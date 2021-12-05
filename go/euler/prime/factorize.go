package prime

// returns prime factors of `number`
func Factorize(number int) []int {
	var factors []int
numberLoop:
	for number > 1 {
		for i := 2; i*i <= number; i++ {
			if number%i == 0 {
				factors = append(factors, i)
				number /= i
				continue numberLoop
			}
		}
		factors = append(factors, number)
	}
	return factors
}
