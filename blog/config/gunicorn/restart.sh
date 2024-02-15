#!/bin/bash

# restart Gunicorn
cd '/home/ubuntu/newproject/newproject'

# Get the existing Gunicorn process IDs
pgrep_result=$(pgrep gunicorn)


if [ -n "$pgrep_result" ]; then
    echo "Stopping existing Gunicorn processes..."
    sudo kill  $pgrep_result
    sleep 5  # Wait for processes to stop (adjust this as needed)
fi

if gunicorn -c config/gunicorn/dev.py; then
    echo "Server has been started successfully."
else
    echo "Failed to start the server. Please check the logs for more information."
fi