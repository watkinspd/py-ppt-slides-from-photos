# py-ppt-slides-from-photos
Create a powerpoint presentation slide deck from a file folder of screenshots, photos or image files

## What is this for?
I often build presentations that involve many screen shots. There are a couple of common scenarios.
1. Build a powerpoint deck with screen shots of a system demo as a failsafe for a presentation, or as a way to speed up a demo, or so you can roll a demo forward/backward with audience during q&a
2. Fast way to push a lot of content sourced from the intertubes into a presentation


## python-pptx to the rescue
I could not find a feature for this in powerpoint. After much searching I found this brilliant python library 
https://python-pptx.readthedocs.io/en/latest/index.html

I hacked together this small python app that builds a sorted array of files that are in a directory and adds each one as a slide in a powerpoint deck. They are sized to fill the slide.


## Example workflow:
The directory you feed this app is expected to contain all the images you want put into the powerpoint deck. Each image being its own slide. Images are assumed to have .jpeg, .png, .tiff .gif extensions.

1. Take a bunch of screen shots and move the files into a directory, or
2. Export a selected set of files from apple photos into their own directory

Note: I found that if I exported photos from apple photos the filename sequence doesnt work correctly, whereas it will generate files with a modified date in the order they were exported with.


## Sequencing the slides
There are two ways to control the sequence of the resulting slides:
1 - default behaviour is the list of files is sorted by the files last modified date
2 - you can specify the -f optin and it will sort by filename


## Pre-requisites:
This work assumes you have your machine setup to run python apps locally.

## To install and run:

```
git clone https://github.com/watkinspd/py-ppt-slides-from-photos.git
cd ./py-ppt-slides-from-photos
pip install -r requirements.txt
python photoslides.py -h
```



