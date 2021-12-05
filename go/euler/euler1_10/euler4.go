package euler1_10

func isPalindrome(n int) bool {
	original_n := n
	reversed_n := 0
	for n > 0 {
		rem := n % 10
		reversed_n = reversed_n*10 + rem
		n /= 10
	}
	return reversed_n == original_n
}

func Euler4Solve() int {
	var maxSoFar int
	for a := 999; a > 99; a-- {
		for b := a; b > 99; b-- {
			number := a * b
			if isPalindrome(number) && number > maxSoFar {
				maxSoFar = number
			}
		}
	}
	return maxSoFar
}
