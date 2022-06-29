package main

import (
	"fmt"
	"os"
	"runtime/trace"
	"time"
)

// go run go_tool_trace.go
// go tool trace trace.out
// open http://127.0.0.1:35488
func main() {
	f, err := os.Create("trace.out")
	if err != nil {
		panic(err)
	}
	defer f.Close()

	err = trace.Start(f)
	if err != nil {
		panic(err)
	}
	defer trace.Stop()

	for i := 0; i < 5; i++ {
		time.Sleep(time.Second)
		fmt.Println("hello")
	}
}
