docker run -d -p 6901:6901 -p 80:80 --name gpt1 saitamatechno/gpt_scraper:v1.0<br>
docker run -d -e API_KEY=saitama_key -p 6901:6901 -p 81:80 --name gpt1 gpt_scraper<br>
docker build -t gpt_scraper .
