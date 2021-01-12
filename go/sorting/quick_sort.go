package main

import (
	"math/rand"
	"fmt"
)

func QuickSort(arr []int) []int {
	if len(arr) <= 1 {
		return arr
	}
	pivot := arr[rand.Intn(len(arr))]

	low := make([]int, 0, len(arr))
	high := make([]int, 0, len(arr))
	mid := make([]int, 0, len(arr))

	for _, item := range arr {
		switch {
			case item < pivot:
				low = append(low, item)	
			case item == pivot:
				mid = append(mid, item)
			case item > pivot:
				high = append(high, item)
		}
	}

	low = QuickSort(low)
	high = QuickSort(high)

	low = append(low, mid...)
	low = append(low, high...)
	
	return low
}

func main() {
	primes := [7]int{11, 17, 5, 7, 2, 13, 3}
	var p []int = primes[:]
	fmt.Println(QuickSort(p))
}