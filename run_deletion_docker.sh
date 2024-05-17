  docker compose up delete_invalid_links
  #docker run -e LINKS_PATH=./data/links.json -v ./data/:/app/data/ link-shortner-devops -c "python delete_invalid_links.py"