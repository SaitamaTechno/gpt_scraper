Run from Docker Hub: <a href="https://hub.docker.com/r/saitamatechno/gpt_scraper">https://hub.docker.com/r/saitamatechno/gpt_scraper</a><br>
docker run -d -p 6901:6901 -p 80:80 --name gpt1 saitamatechno/gpt_scraper:v1.0<br>

Run locally:<br>
docker build -t gpt_scraper .<br>
docker run -d -e API_KEY=saitama_key -p 6901:6901 -p 81:80 --name gpt1 gpt_scraper<br>
