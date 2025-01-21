#!/bin/sh
echo "Welcome to PDF-to-Text Converter!"
echo "The web UI is running at http://localhost:8080"
echo "Please open the link in your browser."
echo "To exit the server and the container, press: CTRL+C"

# Start the server automatically when the container runs
exec gunicorn -w 4 -b 0.0.0.0:8080 server:app