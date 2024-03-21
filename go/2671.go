package main

type FrequencyTracker struct {
	cnt  map[int]int
	freq map[int]int
}

func Constructor() FrequencyTracker {
	return FrequencyTracker{cnt: map[int]int{}, freq: map[int]int{}}
}

func (f *FrequencyTracker) Add(number int) {
	f.freq[f.cnt[number]]--
	f.cnt[number]++
	f.freq[f.cnt[number]]++
}

func (f *FrequencyTracker) DeleteOne(number int) {
	if f.cnt[number] > 0 {
		f.freq[f.cnt[number]]--
		f.cnt[number]--
		f.freq[f.cnt[number]]++
	}
}

func (f *FrequencyTracker) HasFrequency(frequency int) bool {
	return f.freq[frequency] > 0
}

/**
 * Your FrequencyTracker object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Add(number);
 * obj.DeleteOne(number);
 * param_3 := obj.HasFrequency(frequency);
 */
