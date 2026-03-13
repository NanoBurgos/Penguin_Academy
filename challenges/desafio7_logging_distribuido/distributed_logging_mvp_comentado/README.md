
# Distributed Logging MVP

## 1. Instalación

```bash
pip install -r requirements.txt
```

## 2. Ejecutar servidor

```bash
cd server
uvicorn main:app --reload
```

Servidor disponible en:
http://127.0.0.1:8000

## 3. Ejecutar cliente simulador

En otra terminal:

```bash
cd clients
python simulate_service_a.py
```

## 4. Probar con curl

Enviar log manual:

```bash
curl -X POST http://127.0.0.1:8000/logs \
-H "Authorization: Token service-a-token" \
-H "Content-Type: application/json" \
-d '{"timestamp":"2026-01-01T10:00:00","service":"service-a","severity":"ERROR","message":"Test log"}'
```

Consultar logs:

```bash
curl http://127.0.0.1:8000/logs
```
