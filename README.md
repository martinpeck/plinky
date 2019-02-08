# Plinky

> A Python base link shorterner that couldn't be more stupid*

- Plinky uses configuration to redirect short urls to longer ones.
- It doesn't generate short urls.
- Deal with it.

## How to use it
For local testing, create a .env file in the root of your application. Within that file you'll want the following environment variables...

```
SHORTCUT_FILE = ./shorturls/example_shorturls.yaml
SEGMENT_WRITE_KEY=your_key_goes_here
```
The yaml file containing your shorturls needs to be set up. If you don't want to use Segment.io to track events you don't need to set up the Segment write key.

For deployment, you'll want to set these environment variables on the host machine.

## Running Locally
I use `foreman` to run my webserver. If you want to see debug message then do this...

`foreman run python plinky.py`

... as this will load the environment.

To run it as Heroku would, run with the following command...

`foreman start`

## Shorturls in Yaml - The Rules
- Always have a default value. This is the url that is used when a given shorturl can't be found.
- Last shorturl wins. If you have several with the same value they last one will be used

## TODO

There is plenty that could be improved. Please raise issues in GitHub if you have suggestions.
https://github.com/martinpeck/plinky/issues
