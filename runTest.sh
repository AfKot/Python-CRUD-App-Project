#! /bin/bash

python3 -m venv venv

activate() {
    . venv/bin/activate
}

activate

python3 -m pytest --cov-report term-missing --cov application/ tests/