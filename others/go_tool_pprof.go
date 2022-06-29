// go run go_tool_pprof.go
// go tool pprof -http=:1248 http://127.0.0.1:6060/debug/pprof/goroutine
package main

import (
	"net/http"
	_ "net/http/pprof"
)

func main() {
	for i := 0; i < 100; i++ {
		go func() {
			select {}
		}()
	}

	go func() {
		http.ListenAndServe("localhost:6060", nil)
	}()

	select {}
}
