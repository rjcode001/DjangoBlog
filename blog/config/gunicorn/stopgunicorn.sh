#!/bin/bash

# Stop Gunicorn
pgrep_result=$(pgrep gunicorn)


if [ -n "$pgrep_result" ]; then
    echo "Stopping existing Gunicorn processes..."
    sudo kill -TERM $pgrep_result
    sleep 5  # Wait for processes to stop (adjust this as needed)
fi
