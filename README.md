some of this might be out of date... 

my personal website / portfolio

first do

    >>> ./test

and go to http://localhost:8000/ in a browser to see the site


in separate terminal window, do

    >>> ./live_updating.sh


this makes some watchers run in the background. any changes to templates or app.scss will re-run `make_pages.py` so if you refresh the browser you'll see the updates. when you close the terminal that started the live updating, it kills the processes that got started by live updating.

Note: I thought about putting the "test" script in live_updating, but it didn't kill itself properly and caused the http address to be held up, i think. anyway a weird bug to look into later.
 

