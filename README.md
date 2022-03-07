# Ip v4 Retrieval Process

___

## Launch docker environment

```shell
docker-compose -p ip-retrieval-process --env-file .env up -d
```

## Update requirement on windows

```shell
docker run --rm -v /YOUR/LOCAL/PROJECT:/project azlyth/docker-pipreqs > requirements.txt
```

[Github ](https://github.com/azlyth/docker-pipreqs)