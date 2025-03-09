# 🤖 askhelmut

[![License](https://img.shields.io/github/license/helmut-hoffer-von-ankershoffen/askhelmut?logo=opensourceinitiative&logoColor=3DA639&labelColor=414042&color=A41831)
](https://github.com/helmut-hoffer-von-ankershoffen/askhelmut/blob/main/LICENSE)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/askhelmut.svg?logo=python&color=204361&labelColor=1E2933)](https://github.com/helmut-hoffer-von-ankershoffen/askhelmut/blob/main/noxfile.py)
[![CI](https://github.com/helmut-hoffer-von-ankershoffen/askhelmut/actions/workflows/test-and-report.yml/badge.svg)](https://github.com/helmut-hoffer-von-ankershoffen/askhelmut/actions/workflows/test-and-report.yml)
[![Read the Docs](https://img.shields.io/readthedocs/askhelmut)](https://askhelmut.readthedocs.io/en/latest/)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=helmut-hoffer-von-ankershoffen_askhelmut&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=helmut-hoffer-von-ankershoffen_askhelmut)
[![Security](https://sonarcloud.io/api/project_badges/measure?project=helmut-hoffer-von-ankershoffen_askhelmut&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=helmut-hoffer-von-ankershoffen_askhelmut)
[![Maintainability](https://sonarcloud.io/api/project_badges/measure?project=helmut-hoffer-von-ankershoffen_askhelmut&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=helmut-hoffer-von-ankershoffen_askhelmut)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=helmut-hoffer-von-ankershoffen_askhelmut&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=helmut-hoffer-von-ankershoffen_askhelmut)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=helmut-hoffer-von-ankershoffen_askhelmut&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=helmut-hoffer-von-ankershoffen_askhelmut)
[![Coverage](https://codecov.io/gh/helmut-hoffer-von-ankershoffen/askhelmut/graph/badge.svg?token=SX34YRP30E)](https://codecov.io/gh/helmut-hoffer-von-ankershoffen/askhelmut)
[![Ruff](https://img.shields.io/badge/style-Ruff-blue?color=D6FF65)](https://github.com/helmut-hoffer-von-ankershoffen/askhelmut/blob/main/noxfile.py)
[![MyPy](https://img.shields.io/badge/mypy-checked-blue)](https://github.com/helmut-hoffer-von-ankershoffen/askhelmut/blob/main/noxfile.py)
[![GitHub - Version](https://img.shields.io/github/v/release/helmut-hoffer-von-ankershoffen/askhelmut?label=GitHub&style=flat&labelColor=1C2C2E&color=blue&logo=GitHub&logoColor=white)](https://github.com/helmut-hoffer-von-ankershoffen/askhelmut/releases)
[![GitHub - Commits](https://img.shields.io/github/commit-activity/m/helmut-hoffer-von-ankershoffen/askhelmut/main?label=commits&style=flat&labelColor=1C2C2E&color=blue&logo=GitHub&logoColor=white)](https://github.com/helmut-hoffer-von-ankershoffen/askhelmut/commits/main/)
[![PyPI - Version](https://img.shields.io/pypi/v/askhelmut.svg?label=PyPI&logo=pypi&logoColor=%23FFD243&labelColor=%230073B7&color=FDFDFD)](https://pypi.python.org/pypi/askhelmut)
[![PyPI - Status](https://img.shields.io/pypi/status/askhelmut?logo=pypi&logoColor=%23FFD243&labelColor=%230073B7&color=FDFDFD)](https://pypi.python.org/pypi/askhelmut)
[![Docker - Version](https://img.shields.io/docker/v/helmuthva/askhelmut?sort=semver&label=Docker&logo=docker&logoColor=white&labelColor=1354D4&color=10151B)](https://hub.docker.com/r/helmuthva/askhelmut/tags)
[![Docker - Size](https://img.shields.io/docker/image-size/helmuthva/askhelmut?sort=semver&arch=arm64&label=image&logo=docker&logoColor=white&labelColor=1354D4&color=10151B)](https://hub.docker.com/r/helmuthva/askhelmut/)
[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-orange.json)](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template)
[![Open in Dev Containers](https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iI2ZmZiIgZD0iTTE3IDE2VjdsLTYgNU0yIDlWOGwxLTFoMWw0IDMgOC04aDFsNCAyIDEgMXYxNGwtMSAxLTQgMmgtMWwtOC04LTQgM0gzbC0xLTF2LTFsMy0zIi8+PC9zdmc+)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/helmut-hoffer-von-ankershoffen/askhelmut)
[![Open in GitHub Codespaces](https://img.shields.io/static/v1?label=GitHub%20Codespaces&message=Open&color=blue&logo=github)](https://github.com/codespaces/new/helmut-hoffer-von-ankershoffen/askhelmut)

<!---
[![ghcr.io - Version](https://ghcr-badge.egpl.dev/helmut-hoffer-von-ankershoffen/askhelmut/tags?color=%2344cc11&ignore=0.0%2C0%2Clatest&n=3&label=ghcr.io&trim=)](https://github.com/helmut-hoffer-von-ankershoffen/askhelmut/pkgs/container/askhelmut)
[![ghcr.io - Sze](https://ghcr-badge.egpl.dev/helmut-hoffer-von-ankershoffen/askhelmut/size?color=%2344cc11&tag=latest&label=size&trim=)](https://github.com/helmut-hoffer-von-ankershoffen/askhelmut/pkgs/container/askhelmut)
-->

> [!TIP]
> 📚 [Online documentation](https://askhelmut.readthedocs.io/en/latest/) - 📖 [PDF Manual](https://askhelmut.readthedocs.io/_/downloads/en/latest/pdf/)
---


Exploration.

Use Cases:
1) Fast and easy to use project setup
2) Consistent update of already scaffolded projects to benefit from new and improved features.
3) Dummy CLI application and service demonstrating example usage of the generated directory structure and build pipeline

## Scaffolding Instructions

Step 1: Install uv package manager and copier
```shell
if [[ "$OSTYPE" == "darwin"* ]]; then                 # Install dependencies for macOS X
  if ! command -v brew &> /dev/null; then             ## Install Homebrew if not present
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  fi
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then            # Install dependencies for Linux
  sudo apt-get update -y && sudo apt-get install curl -y # Install curl
fi
if ! command -v uvx &> /dev/null; then                # Install uv package manager if not present
  curl -LsSf https://astral.sh/uv/install.sh | sh
  source $HOME/.local/bin/env
fi
uv tool install copier                                # Install copier as global tool
```

Step 2: Now create an empty repo on GitHub and clone it to your local machine in a directory of your choice. Change to that directory.

Step 3: Scaffold the project
```shell
copier copy gh:helmut-hoffer-von-ankershoffen/oe-python-template .
```
Step 4: Setup the local environment

```shell
uv run nox -s setup_eev
```

Step 5: Perform inital commit and push
```shell
git add .
git commit -m "feat: Initial commit"
```

Visit your GitHub repository and check the Actions tab. The CI workflow should fail at the SonarQube step,
as this external service is not yet configured for our new repository.

Step 6: Follow the instructions in SERVICE_CONNECTIONS.md to setup the connections to external services
such as Cloudcov, SonarQube Cloud, Read The Docs, Docker.io, GHCR.io and Streamlit Community Cloud.

Step 7: Release the first versions
```shell
./bump
```
Notes:
* You can remove this section post having successfully scafolded your project.
* The following sections refer to the dummy application and service provided by this template.
  Use them as inspiration and adapt them to your own project.

## Overview

Adding askhelmut to your project as a dependency is easy.

```shell
uv add askhelmut             # add dependency to your project
```

If you don't have uv installed follow [these instructions](https://docs.astral.sh/uv/getting-started/installation/). If you still prefer pip over the modern and fast package manager [uv](https://github.com/astral-sh/uv), you can install the library like this:

```shell
pip install askhelmut        # add dependency to your project
```

Executing the command line interface (CLI) is just as easy:

```shell
uvx askhelmut
```

The CLI provides extensive help:

```shell
uvx askhelmut --help              # all CLI commands
uvx askhelmut command --help      # all options for command
```


## Highlights

* Exploration.
* Various Examples:
  - [Simple Python script]https://github.com/helmut-hoffer-von-ankershoffen/askhelmut/blob/main/examples/script.py)
  - [Streamlit web application](https://askhelmut.streamlit.app/) deployed on [Streamlit Community Cloud](https://streamlit.io/cloud)
  - [Jupyter](https://github.com/helmut-hoffer-von-ankershoffen/askhelmut/blob/main/examples/notebook.ipynb) and [Marimo](https://github.com/helmut-hoffer-von-ankershoffen/askhelmut/blob/main/examples/notebook.py) notebook
* [Complete reference documenation](https://askhelmut.readthedocs.io/en/latest/reference.html) on Read the Docs
* [Transparent test coverage](https://app.codecov.io/gh/helmut-hoffer-von-ankershoffen/askhelmut) including unit and E2E tests (reported on Codecov)
* Matrix tested with [multiple python versions](https://github.com/helmut-hoffer-von-ankershoffen/askhelmut/blob/main/noxfile.py) to ensure compatibility (powered by [Nox](https://nox.thea.codes/en/stable/))
* Compliant with modern linting and formatting standards (powered by [Ruff](https://github.com/astral-sh/ruff))
* Up-to-date dependencies (monitored by [Renovate](https://github.com/renovatebot/renovate))
* [A-grade code quality](https://sonarcloud.io/summary/new_code?id=helmut-hoffer-von-ankershoffen_askhelmut) in security, maintainability, and reliability with low technical debt and low codesmell (verified by SonarQube)
* 1-liner for installation and execution of command line interface (CLI) via [uv(x)](https://github.com/astral-sh/uv) or [Docker](https://hub.docker.com/r/helmuthva/askhelmut/tags)
* Setup for developing inside a [devcontainer](https://code.visualstudio.com/docs/devcontainers/containers) included (supports VSCode and GitHub Codespaces)


## Usage Examples

### Minimal Python Script:

```python
"""Example script demonstrating the usage of the service provided by askhelmut."""

from dotenv import load_dotenv
from rich.console import Console

from askhelmut import Service

console = Console()

load_dotenv()

message = Service.get_hello_world()
console.print(f"[blue]{message}[/blue]")
```

[Show script code](https://github.com/helmut-hoffer-von-ankershoffen/askhelmut/blob/main/examples/script.py) - [Read the reference documentation](https://askhelmut.readthedocs.io/en/latest/reference.html)

### Streamlit App

Serve the functionality provided by askhelmut in the web by easily integrating the service into a Streamlit application.

[Try it out!](https://askhelmut.streamlit.app) - [Show the code](https://github.com/helmut-hoffer-von-ankershoffen/askhelmut/blob/main/examples/streamlit.py)

... or serve the app locally
```shell
uv sync --all-extras                                # Install streamlit dependency part of the examples extra, see pyproject.toml
uv run streamlit run examples/streamlit.py          # Serve on localhost:8501, opens browser
```

## Notebooks

### Jupyter

[Show the Jupyter code](https://github.com/helmut-hoffer-von-ankershoffen/askhelmut/blob/main/examples/notebook.ipynb)

... or run within VSCode

```shell
uv sync --all-extras                                # Install ipykernel dependency part of the examples extra, see pyproject.toml
```
Install the [Jupyter extension for VSCode](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)

Click on `examples/notebook.ipynb` in VSCode and run it.

### Marimo

[Show the marimo code](https://github.com/helmut-hoffer-von-ankershoffen/askhelmut/blob/main/examples/notebook.py)

Execute the notebook as a WASM based web app

```shell
uv sync --all-extras                                # Install ipykernel dependency part of the examples extra, see pyproject.toml
uv run marimo run examples/notebook.py --watch      # Serve on localhost:2718, opens browser
```

or edit interactively in your browser

```shell
uv sync --all-extras                                # Install ipykernel dependency part of the examples extra, see pyproject.toml
uv run marimo edit examples/notebook.py --watch     # Edit on localhost:2718, opens browser
```

... or edit interactively within VSCode

Install the [Marimo extension for VSCode](https://marketplace.visualstudio.com/items?itemName=marimo-team.vscode-marimo)

Click on `examples/notebook.py` in VSCode and click on the caret next to the Run icon above the code (looks like a pencil) > "Start in marimo editor" (edit).

## Command Line Interface (CLI)

### Run with [uvx](https://docs.astral.sh/uv/guides/tools/)

Show available commands:

```shell
uvx askhelmut --help
```

Execute commands:

```shell
uvx askhelmut hello-world
uvx askhelmut hello-world --json
uvx askhelmut echo "Lorem Ipsum"
```

### Environment

The service loads environment variables including support for .env files.

```shell
cp .env.example .env              # copy example file
echo "THE_VAR=MY_VALUE" > .env    # overwrite with your values
```

Now run the usage examples again.

### Run with Docker

You can as well run the CLI within Docker.

```shell
docker run helmuthva/askhelmut --help
docker run helmuthva/askhelmut hello-world
docker run helmuthva/askhelmut hello-world --json
docker run helmuthva/askhelmut echo "Lorem"
```

Execute command:

```shell
docker run --env THE_VAR=MY_VALUE helmuthva/askhelmut echo "Lorem Ipsum"
```

Or use docker compose

The .env is passed through from the host to the Docker container.

```shell
docker compose up
docker compose run askhelmut --help
```

## Extra: Lorem Ipsum

Dolor sit amet, consectetur adipiscing elit. Donec a diam lectus. Sed sit amet ipsum mauris. Maecenas congue ligula ac quam.


## Further Reading

* Check out the [reference](https://askhelmut.readthedocs.io/en/latest/reference.html) with detailed documentation of public classes and functions.
* Our [release notes](https://askhelmut.readthedocs.io/en/latest/release-notes.html) provide a complete log of recent improvements and changes.
* In case you want to help us improve 🤖 askhelmut: The [contribution guidelines](https://askhelmut.readthedocs.io/en/latest/contributing.html) explain how to setup your development environment and create pull requests.

## Star History

<a href="https://star-history.com/#helmut-hoffer-von-ankershoffen/askhelmut">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=helmut-hoffer-von-ankershoffen/askhelmut&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=helmut-hoffer-von-ankershoffen/askhelmut&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=helmut-hoffer-von-ankershoffen/askhelmut&type=Date" />
 </picture>
</a>
