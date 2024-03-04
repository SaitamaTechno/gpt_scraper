docker run -d -e API_KEY=saitama_key -p 6901:6901 -p 81:80 --name gpt1 gpt_scraper
docker build -t gpt_scraper .
