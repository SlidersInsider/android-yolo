## Info

This repo created for training model to detecting objects such as banknotes, coins and cards

## How to use

Use next instruction for start training model. Before start you should download repo.

### Build Docker image

```
docker build -t detect-train .
```

### Train model

```
docker run --rm -it -v .\python\dataset:/detect_app/datasets/dataset -v .\python\results:/detect_app/results detect-train python3 train.py
```

### Validate model

```
docker run --rm -it -v .\python\dataset:/detect_app/datasets/dataset -v .\python\results:/detect_app/results detect-train python3 val.py
```