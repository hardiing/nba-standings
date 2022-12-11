# NBA DATA PROJECT

A flask application that collects data from a couple different NBA API endpoints and inserts them
into a MySQL database. The HTML tables are built by querying the tables for the data most relevant to me.

## Technologies used: Python, Flask, Docker, MySQL, HTML/CSS

## HOW TO USE:
With Docker and Docker Compose installed and running:

```
docker-compose up --build
```

Once the containers are up and running, go to localhost:5000 to access the application.

ctrl-c to stop the containers when finished.

docker-compose down to shut down the containers.