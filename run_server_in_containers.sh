docker run -p 8001:8080 -v ./data/:/app/data link-shortner-dev &
docker run -p 8002:8080 -v ./data/:/app/data link-shortner-dev &
docker run -p 8003:8080 -v ./data/:/app/data link-shortner-dev &

wait
