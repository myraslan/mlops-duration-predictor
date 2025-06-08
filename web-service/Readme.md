## Deploying a model

```bash
docker build -t ride-duration-prediction-service:v1 .
```

```bash
docker run -it --rm -p 9696:9696  ride-duration-prediction-service:v1
```