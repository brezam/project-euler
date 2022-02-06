package euler11_20

var ones = []string{
	"",
	"one",
	"two",
	"three",
	"four",
	"five",
	"six",
	"seven",
	"eight",
	"nine",
	"ten",
	"eleven",
	"twelve",
	"thirteen",
	"fourteen",
	"fifteen",
	"sixteen",
	"seventeen",
	"eighteen",
	"nineteen",
}

var tens = []string{
	"",
	"",
	"twenty",
	"thirty",
	"forty",
	"fifty",
	"sixty",
	"seventy",
	"eighty",
	"ninety",
}

func numberLength(n int) int {
	if n < 20 {
		return len(ones[n])
	}
	if n < 100 {
		return len(tens[n/10]) + len(ones[n%10])
	}
	hundreds := (n / 100) % 10
	thousands := n / 1000
	left := n % 100

	result := 0
	if n > 999 {
		result += numberLength(thousands) + len("thousand")
	}
	if hundreds > 0 {
		result += numberLength(hundreds) + len("hundred")
	}
	if left > 0 {
		result += len("and") + numberLength(left)
	}
	return result
}

func Euler17Solve() int {
	total := 0
	for i := 1; i < 1001; i++ {
		total += numberLength(i)
	}
	return total
}
