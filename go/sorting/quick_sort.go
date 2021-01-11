package main

import (
	"math/rand"
	"fmt"
)

func QuickSort(arr []int) []int {
	if len(arr) <= 1 {
		return arr
	}
	median := arr[rand.Intn(len(arr))]

	lowPart := make([]int, 0, len(arr))
	highPart := make([]int, 0, len(arr))
	middlePart := make([]int, 0, len(arr))

	for _, item := range arr {
		switch {
		case item < median:
			lowPart = append(lowPart, item)	
		case item == median:
			middlePart = append(middlePart, item)
		case item > median:
			highPart = append(highPart, item)
		}
	}

	lowPart = QuickSort(lowPart)
	highPart = QuickSort(highPart)

	lowPart = append(lowPart, middlePart...)
	lowPart = append(lowPart, highPart...)
	
	return lowPart
}

func main() {
	primes := [7]int{11, 17, 5, 7, 2, 13, 3}
	var p []int = primes[:]
	fmt.Println(QuickSort(p))
}