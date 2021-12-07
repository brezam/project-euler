package euler11_20

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
	"strconv"
)

func loadNums(filePath string) []*big.Int {
	file, err := os.Open(filePath)
	if err != nil {
		panic(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	var nums []*big.Int
	for scanner.Scan() {
		text := scanner.Text()
		n, ok := new(big.Int).SetString(text, 10)
		if !ok {
			panic(fmt.Sprintf("could not create big int for string %s", text))
		}
		nums = append(nums, n)
	}
	return nums
}

func SumBigInts(nums []*big.Int) *big.Int {
	total := big.NewInt(0)
	for _, n := range nums {
		total = total.Add(total, n)
	}
	return total
}

func Euler13Solve() int {
	total := SumBigInts(loadNums("euler11_20/euler13numbers.txt"))
	n, err := strconv.Atoi(total.String()[:10])
	if err != nil {
		panic(err)
	}
	return n
}
