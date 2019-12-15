curl -d "file=test.png" http://127.0.0.1:5500/upload

curl -X POST -F "file=@/test.png" http://127.0.0.1:5500/upload

curl -X POST -H "Content-Type: application/json" -d '{"method": "tasks.get"}' http://127.0.0.1:5500/