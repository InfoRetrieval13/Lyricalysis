FROM solr:latest

# Install dos2unix
RUN apt-get update && apt-get install -y dos2unix

# Create the data directory for your core
RUN mkdir -p /var/solr/data/mycore

# Copy Solr configuration
COPY conf/ /var/solr/data/mycore/conf/

# Copy data
COPY data/lyrics.csv /var/solr/data/mycore/

# Copy the script that starts Solr, creates the core, and loads the data
COPY start_solr.sh /opt/docker-solr/

# Convert CRLF to LF in the script
RUN dos2unix /opt/docker-solr/start_solr.sh

# Run the script when the container starts
CMD ["/bin/bash", "/opt/docker-solr/start_solr.sh"]