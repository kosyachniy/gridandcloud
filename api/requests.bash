# Регистрация / авторизация

curl -X POST -H "Content-Type: application/json" -d '{"method": "account.auth", "params": {"login": "log", "password": "pas"}}' http://127.0.0.1:5500/

# Выход

curl -X POST -H "Content-Type: application/json" -d '{"method": "account.exit", "token": "pIoSQQL5YOGvGEvAaiiFuv1zff7mNvWQ"}' http://127.0.0.1:5500/

# Тест
curl -d "file=test.png" http://127.0.0.1:5500/upload
curl -X POST -F "file=@/test.png" http://127.0.0.1:5500/upload