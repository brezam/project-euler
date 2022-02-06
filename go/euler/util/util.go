package util

// Unwraps (value, error) into value and panics if error is not nil
func Unwrap[T any](value T, err error) T {
	if err != nil {
		panic(err)
	}
	return value
}
