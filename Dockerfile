FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# This adds the execute permission to the file inside the container
RUN chmod +x /app/entrypoint.sh

EXPOSE 8080

# User-facing script, displays important infos for the user
ENTRYPOINT ["/app/entrypoint.sh"]

# CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "server:app"]