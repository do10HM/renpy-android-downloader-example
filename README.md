This is intended to be an example of a working Downloader and Game pair following the documentation at https://www.renpy.org/doc/html/downloader.html#downloader-for-large-games-on-mobile.

# Requirements
Ren'Py 8.2.1

# Setup
Steps provided for Windows but should work on other platforms.

## Set up Ren'Py
Download Ren'Py 8.2.1. If using an already-existing version, recommend deleting RAPT so it re-installs.
Open Ren'Py. In Preferences, change the Projects Directory to this repo's projects/ folder.

## Game Setup
In Ren'Py, highlight the Game project.
Select Actions>Build Distributions.
Uncheck everything except:
  Check Build Packages>Game-Only Update for Mobile
  Check Options>Build Updates
  Check Options>Force Recompile
Select Build.

## Serve Files
In Terminal, navigate to the <project>/projects/Game-1.0-dists folder.
Run `python -m http.server 80` to begin serving files.
Run ipconfig and note the local IP address of the hosting computer, like `192.168.1.15`.

## Downloader Setup
In Ren'Py, highlight the Downloader project.
Open <project>/projects/Downloader/game/script.rpy. Edit the url to use the url you are hosting the files from, like `define url = "http://192.168.1.15/updates.json"`

If this is not a new installation of Ren'Py, run Other>Clean.
Run Install SDK if needed.
Run Generate Keys.
Run Build Package.

# Testing
Install the apk built in the Downloader Setup phase onto a device or simulator and launch it.
Start `adb logcat` to monitor logs.
Progress through the prompts until the download begins.
You should see activity on your local web server, like "::ffff:192.168.86.224 - "GET /updates.json HTTP/1.1" 200
The Game should load after downloading the files!

# ISSUE: PROTOCOL ERROR
Reproduced in Ren'Py renpy-8.2.2.24030501+nightly-sdk
Following the steps above for this project, the files download. I then see: 

An error occured when trying to download game data:
ProtocolError: ('Connection broken: IncompleteRead(3952381 bytes read, 219 more expected)', IncompleteRead(3952381 bytes read, 219 more expected))
This game cannot be run until the game data has been downloaded.

When I tap 'retry', it repeats, with slightly different bytes.

[ADB log filtered for the bundle id](https://github.com/do10HM/renpy-android-downloader-example/blob/issue/protocol-error/Results/adb_log.txt)
[Video](https://github.com/do10HM/renpy-android-downloader-example/blob/issue/protocol-error/Results/Screen_recording_20240309_150218.webm)
