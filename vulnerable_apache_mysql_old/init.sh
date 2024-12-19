docker compose down
docker volume rm $(docker volume ls -q)
docker rmi -f $(docker images -q)
docker compose up -d