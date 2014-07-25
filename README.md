#### shapepaper (WIP name)

## Intro

The idea behind shapepaper is pretty simple, I wanted minimalistic wallpapers that wouldn't get bland. This is essentially accomplished by taking a random colored background and placing a random slightly darker image over it.

## Prerequisites

You *must* install these prerequisites as this script is unbelievably simple and at the moment it will not test for them, simply spit out an error message.

- Python 2 or 3
- Pillow or PIL
- The aggdraw module (explained below)

It is possible to creat this script without the aggdraw module however I chose aggdraw fairly early into "development" and simply stuck with it, I may eventually make a branch that doesn't require it.

## Install and Usage

#Install

... what install?

#Usage

The script simply outputs the background to file.png (easily changed). If you have a resolution != 1920x1080 you can change the resx and resy variable at the top of the script to your resolution. The command I use is simply `python shapepaper.py && feh --bg-fill file.png`. Change feh to your prefered bg setter if you want.




