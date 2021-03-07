#!/bin/zsh

watch "templates/*" -r "./make_pages.py" &
watch "data/*" -r "./make_pages.py" &

sass --watch sass/app.scss:static/css/app.css &

