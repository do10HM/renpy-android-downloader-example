This is intended to be an example of a working Downloader and Game pair following the documentation at https://www.renpy.org/doc/html/downloader.html#downloader-for-large-games-on-mobile.

# Requirements
Ren'Py 8.2.1

# Setup
Steps provided for Windows but should work on other platforms.

## Set up Ren'Py
1. Download Ren'Py 8.2.1. If using an already-existing version, recommend deleting RAPT so it re-installs.
2. Open Ren'Py. In Preferences, change the Projects Directory to this repo's projects/ folder.

## Game Setup
1. In Ren'Py, highlight the Game project.
2. Select Actions>Build Distributions.
3. Uncheck everything except:
  * Check Build Packages>Game-Only Update for Mobile
  * Check Options>Build Updates
  * Check Options>Force Recompile
4. Select Build.

## Serve Files
1. In Terminal, navigate to the <project>/projects/Game-1.0-dists folder.
2. Run `python -m http.server 80` to begin serving files.
3. Run ipconfig and note the local IP address of the hosting computer, like `192.168.1.15`.

## Downloader Setup
1. In Ren'Py, highlight the Downloader project.
2. Open <project>/projects/Downloader/game/script.rpy. Edit the url to use the url you are hosting the files from, like `define url = "http://192.168.1.15/updates.json"`
3. If this is not a new installation of Ren'Py, run Other>Clean.
4. Run Install SDK if needed.
5. Run Generate Keys.
6. Run Build Package. Install optionally.

# Testing
1. Install the apk built in the Downloader Setup phase onto a device or simulator and launch it.
2. Start `adb logcat` to monitor logs.
3. Progress through the prompts until the download begins.
4. You should see activity on your local web server, like "::ffff:192.168.86.224 - "GET /updates.json HTTP/1.1" 200
5. The Game should load after downloading the files!

# ISSUE: PROTOCOL ERROR
Reproduced in Ren'Py renpy-8.2.2.24030501+nightly-sdk

Following the steps above for this project, the files download. I then see: 

An error occured when trying to download game data:

ProtocolError: ('Connection broken: IncompleteRead(3952381 bytes read, 219 more expected)', IncompleteRead(3952381 bytes read, 219 more expected))
This game cannot be run until the game data has been downloaded.

When I tap 'retry', it repeats, with slightly different bytes.

[ADB log filtered for the bundle id](https://github.com/do10HM/renpy-android-downloader-example/blob/issue/protocol-error/Results/adb_log.txt)
[Video](https://github.com/do10HM/renpy-android-downloader-example/blob/issue/protocol-error/Results/Screen_recording_20240309_150218.webm)
