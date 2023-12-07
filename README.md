# Air Quality Hackathon 2023 - Polish Smog Alert challenge

## Prerequisites

* Docker Desktop
* Google Air Quality API token - to pass in `API_TOKEN` variable

## Development

1. Build docker image

```sh
docker build --build-arg API_TOKEN=xxx -t psa-challenge .
```

2. Run docker image
```sh
docker run -p 5000:80 psa-challenge
```
