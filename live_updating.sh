#!/bin/bash

runwatch "templates/*" -r "./make_pages.py" &

sass --watch sass/app.scss:static/css/app.css &
