# Docker SDK for Python

[![Build Status](https://github.com/docker/docker-py/actions/workflows/ci.yml/badge.svg)](https://github.com/docker/docker-py/actions/workflows/ci.yml)

A Python library for the Docker Engine API. It lets you do anything the `docker` command does, but from within Python apps – run containers, manage containers, manage Swarms, etc.

## Installation

The latest stable version [is available on PyPI](https://pypi.python.org/pypi/docker/). Install with pip:

    pip install docker

> Older versions (< 6.0) required installing `docker[tls]` for SSL/TLS support.
> This is no longer necessary and is a no-op, but is supported for backwards compatibility.

## Usage

Connect to Docker using the default socket or the configuration in your environment:

```python
import docker
client = docker.from_env()
```

You can run containers:

```python
>>> client.containers.run("ubuntu:latest", "echo hello world")
'hello world\n'
```

You can run containers in the background:

```python
>>> client.containers.run("bfirsh/reticulate-splines", detach=True)
<Container '45e6d2de7c54'>
```

You can manage containers:

```python
>>> client.containers.list()
[<Container '45e6d2de7c54'>, <Container 'db18e4f20eaa'>, ...]

>>> container = client.containers.get('45e6d2de7c54')

>>> container.attrs['Config']['Image']
"bfirsh/reticulate-splines"

>>> container.logs()
"Reticulating spline 1...\n"

>>> container.stop()
```

You can stream logs:

```python
>>> for line in container.logs(stream=True):
...   print(line.strip())
Reticulating spline 2...
Reticulating spline 3...
...
```

You can manage images:

```python
>>> client.images.pull('nginx')
<Image 'nginx'>

>>> client.images.list()
[<Image 'ubuntu'>, <Image 'nginx'>, ...]
```

[Read the full documentation](https://docker-py.readthedocs.io) to see everything you can do.

Modified to bypass broken SSH logic in the codebase..
