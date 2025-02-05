# Local development environment

- Install Docker
- Run the following command to start the system:
```
docker-compose up --build
```
Now, your services will be running in Docker containers:

- FastAPI API → http://localhost:8000
- GraphQL Playground → http://localhost:8000/graphql
- PostgreSQL DB → Port 5432
- MinIO Console → http://localhost:9001 (Login: minioadmin / minioadmin)