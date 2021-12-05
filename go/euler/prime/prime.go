package prime

import (
	"math"
)

// Returns all primes below `n` using Sieve of Eratosthenes
func SievePrime(n uint) []uint {
	primes := make([]bool, n)
	answer := []uint{}
	primes[0] = true
	primes[1] = true
	maxNumberToCheck := uint(math.Sqrt(float64(n)))
	for i := uint(2); i <= maxNumberToCheck; i++ {
		if !primes[i] {
			for j := i * i; j < n; j += i {
				primes[j] = true
			}
		}
	}
	for i, b := range primes {
		if !b {
			answer = append(answer, uint(i))
		}
	}
	return answer
}

// Primality check using 6k+-1 rule
func IsPrime(n uint) bool {
	if n < 4 {
		return n > 1
	}
	if n%2 == 0 || n%3 == 0 {
		return false
	}
	maxNumberToCheck := uint(math.Sqrt(float64(n)))
	for i := uint(5); i <= maxNumberToCheck; i += 6 {
		if n%i == 0 || n%(i+2) == 0 {
			return false
		}
	}
	return true
}
