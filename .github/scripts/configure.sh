#!/bin/sh

git clone https://github.com/iamogbz/py-boilerplate ../$REPO_NAME
cd ../$REPO_NAME
git remote set-url origin $REPO_URL
make upstream
