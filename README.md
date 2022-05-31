# Macro Application for General/VideoGame Purpose
---
This application is for marcos in any application with Spotify intergration. This is mainly for video game application as DirectX conflict with some of the libaries out there for python.
At the moment, this application is mainly for League of Legends All Chat. However, later
this application will be general use. Another feature with this application is the integration with Spotify and Genius. This means that the macro can display the current song that you are listening to in spotify.

![keyboard](https://m.media-amazon.com/images/I/71TBg4r1oNL._AC_SY450_.jpg)

## Repo Organization
---
* Assets
    * All the images used in the GUI
* Data
    * HotkeyEvents
        * Stores all the keybind text files
        * Song.txt is for the spotify feature(Clean)
    * Settings
        * OrginalTextSong.txt is for the spotify feature(Dirty)
        * api.txt stores the api keys for spotify and genius api
        * banlist.txt stores the banned words for spotify(Inappropriate are not allowed on github so the text file is not uploaded)
        * keybind.txt stores the info for each text file
* fileFunctins.py
    * Stores the file related functions
* macro.py
    * Has the main class
* main.py
    * file that has to be RUN and contains GUI

## How to Run
---
* Main Feature
    * Download Repository
    * Install libraries that are in the main, marco, and fileFunctions programs
    * Run 'main.py'
* Macro File
    * Needs to be a text file
    * Each line is the macro

## Spotify Feature
---
* Spotify API
    * Go to https://developer.spotify.com/ 
    * Get Client ID and Secret ID
    * Make URI to http://google.com
* Genius API
    * Go to https://genius.com/developers
    * Get Clinet Access Token
    * Make URI to http://google.com
* Input those keys to login screen on GUI and make sure you are login on Spotify


