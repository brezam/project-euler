package util

// Creates a new slice populated with the results of calling mapFunction for each element of original slice
func Map[R, E any](slice []R, mapFunction func(R) E) []E {
	result := make([]E, 0, len(slice))
	for _, item := range slice {
		result = append(result, mapFunction(item))
	}
	return result
}

// Performs reduction on nums by successive calling `numbeSliceReducer`.
// Parameter `numberSliceReducer` must be a function that accepts two parameters, the accumulator and new value, respectively.
// Parameter `start` is the initial value for the accumulator.
func ReduceSlice[T int | int64 | float64](nums []T, numberSliceReducer func(T, T) T, start T) T {
	total := start
	for _, v := range nums {
		total = numberSliceReducer(total, v)
	}
	return total
}
