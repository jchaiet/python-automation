#!/usr/bin/env bash

function automate() {
	cd
	python /path/to/automate.py $1 #update path to automate program
	cd path/to/directory/$1 #update path to desired directory for new projects
	git init
	git remote add origin git@github.com:USERNAME/$1.git #update USERNAME to username
	touch README.md
	git add .
	git commit -m "Initial commit"
	git push -u origin master
	sublime .
}