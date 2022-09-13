#!/bin/zsh

poetry cache clear . --all
rm -rf poetry.lock
poetry install
