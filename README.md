# Docker Watch

## About
Docker Watch is a containzerized Python script that allows you to easily set up and configure monitoring Docker events. This lets you get notified if (and, lets be honest, when) a container crashes, a service is removed, or anything that Docker emits events for.

### What is a Docker event?
Docker events are fired by Docker when something interesting happens in the lifecycle of a network, service, container, etc. You can read about Docker events and see a full list of supported events [here](https://docs.docker.com/engine/reference/commandline/events/).

## Usage

```bash
docker run --name docker-watch --restart on-failure[5] -d -v /var/run/docker.sock:/var/run/docker.sock -v config.yml:/app/config.yml docker-watch
```

## Development
1. Clone the repository.
2. Run `pip install -r requirements.txt`.
3. Run `python main.py`.

## Contributing
Be nice and write good code and I'll merge the PR eventually :)