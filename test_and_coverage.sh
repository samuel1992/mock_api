#!/bin/sh

echo "\nChecking coverage for Python code\n"

COV_THRESHOLD=100;
coverage run --source=api --omit='api/migrations/*' manage.py test
coverage report -m
