package euler11_20

import (
	"bufio"
	"euler/mymath"
	u "euler/util"
	"os"
	"strconv"
	"strings"
)

const pyramidNumbersFilePath = "euler11_20/euler18numbers.txt"

func loadNumbers() (result [][]int) {
	file := u.Unwrap(os.Open(pyramidNumbersFilePath))
	sc := bufio.NewScanner(file)
	for sc.Scan() {
		rowString := strings.Split(sc.Text(), " ")
		result = append(result, u.Map(rowString, func(str string) int {
			return u.Unwrap(strconv.Atoi(str))
		}))
	}
	return result
}

func bestSum(numbers [][]int, i, j int) int {
	if i >= len(numbers) || j >= len(numbers[i]) {
		return 0
	}
	return numbers[i][j] + u.Unwrap(mymath.Max(bestSum(numbers, i+1, j), bestSum(numbers, i+1, j+1)))
}

func Euler18Solve() int {
	return bestSum(loadNumbers(), 0, 0)
}
