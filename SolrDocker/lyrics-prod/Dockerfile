FROM solr:latest

# Create the data directory for your core
RUN mkdir -p /var/solr/data/mycore

# Copy Solr configuration
COPY conf/ /var/solr/data/mycore/conf/

# Copy data
COPY data/lyrics.csv /var/solr/data/mycore/

# Copy the script that starts Solr, creates the core, and loads the data
COPY start_solr.sh /opt/docker-solr/

# Run the script when the container starts
CMD ["/bin/bash", "/opt/docker-solr/start_solr.sh"]