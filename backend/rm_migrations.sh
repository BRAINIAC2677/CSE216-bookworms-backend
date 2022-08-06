#!/bin/bash

# run this from the root of the django project where the manage.py located
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path '*/migrations/*.pyc' -delete
