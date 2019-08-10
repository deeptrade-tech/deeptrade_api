#!/bin/bash

read -p 'Your commit message: ' messvar

git add .
git commit -m "$messvar"
git push origin master

