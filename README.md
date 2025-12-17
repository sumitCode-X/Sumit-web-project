Project: Sumit Web Portfolio

Quick start

1) Run locally with Python (development)

```powershell
# from project root
# serve on all interfaces (useful on VPS)
python -m http.server 8000 --bind 0.0.0.0
# or use the helper script
python serve.py --port 8000 --host 0.0.0.0 --no-open
```

2) Build and run with Docker

```bash
# build image (run from project root)
docker build -t sumit-portfolio:latest .

# run container mapping host port 8000 to container port 80
docker run -d -p 8000:80 --name sumit-site sumit-portfolio:latest

# open http://<VPS_IP>:8000
```

Files added

- `requirements.txt` — currently no Python dependencies required.
- `Dockerfile` — serves static files using nginx.
- `serve.py` — helper script to quickly run a Python server and detect IPs.

VPS notes

- Open the port in your firewall/security group (e.g., `sudo ufw allow 8000/tcp`).
- For production use put an nginx or Caddy reverse proxy in front with TLS (Certbot).

If you want, I can:
- Add a docker-compose.yml
- Add an nginx config with SPA fallback and gzip
- Add HTTPS support using a simple self-signed cert (for testing)
