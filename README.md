# aws-step-functions-pydantic

[![Documentation](https://readthedocs.org/projects/aws-step-functions-pydantic/badge/?version=latest)](https://aws-step-functions-pydantic.readthedocs.io/en/latest/)
[![CI Status](https://github.com/lmmx/aws-step-functions-pydantic/actions/workflows/master.yml/badge.svg)](https://github.com/lmmx/aws-step-functions-pydantic/actions/workflows/master.yml)
[![Coverage](https://codecov.io/gh/lmmx/aws-step-functions-pydantic/branch/master/graph/badge.svg)](https://codecov.io/github/lmmx/aws-step-functions-pydantic)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Pydantic models for AWS step functions

[Read The Docs](https://aws-step-functions-pydantic.readthedocs.io/en/latest/)

## Usage

```py
from aws_sfn_pydantic import StateMachine
import yaml

model = StateMachine.model_validate_json('...')
print(yaml.dump(m.model_dump(exclude_unset=True), sort_keys=False))
```

## Requires

- Python 3.10+

## Installation

```sh
pip install aws-step-functions-pydantic
```

> _aws-step-functions-pydantic_ is available from [PyPI](https://pypi.org/project/aws-step-functions-pydantic), and
> the code is on [GitHub](https://github.com/lmmx/aws-step-functions-pydantic)
