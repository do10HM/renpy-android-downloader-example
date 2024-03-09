This is intended to be an example of a working Downloader and Game pair following the documentation at https://www.renpy.org/doc/html/downloader.html#downloader-for-large-games-on-mobile.

# Requirements
Ren'Py 8.2.1

# Setup
Steps provided for Windows but should work on other platforms.

## Set up Ren'Py
Download Ren'Py 8.2.1. If using an already-existing version, recommend deleting RAPT so it re-installs.
Open Ren'Py. In Preferences, change the Projects Directory to this repo's projects/ folder.

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
6. Run Build Package.

# Testing
1. Install the apk built in the Downloader Setup phase onto a device or simulator and launch it.
2. Start `adb logcat` to monitor logs.
3. Progress through the prompts until the download begins.
4. You should see activity on your local web server, like "::ffff:192.168.86.224 - "GET /updates.json HTTP/1.1" 200
5. The Game should load after downloading the files!
