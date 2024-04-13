#!/bin/bash

# Start the Solr server
solr start

# Wait a bit for the server to start
sleep 10

# Create the core
solr create_core -c mycore -d /var/solr/data/mycore/conf/

# Load the CSV data
solr post -c mycore /var/solr/data/mycore/lyrics.csv

# Keep the container running
tail -f /dev/null