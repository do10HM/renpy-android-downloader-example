# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # The url to updates.json, on your web server.
    define url = "http://127.0.0.1/updates.json"

    # Disable saving in the downloader game.
    define config.save = False

    define e = Character("Eileen", image="eileen")

    label splashscreen:

        scene bg washington
        show eileen happy at left


        e "Welcome to the downloader game."

        e "This will download the main game onto your phone, so you can play it."

        e "The url is [url]"

        $ downloader = updater.start_game_download(url)
        if downloader.download_total:
            $ download_mb = int(round(downloader.download_total / 1024 / 1024, 0))
            e "To play this game, you'll need to download [download_mb] megabytes of data. If you're not on WiFi, you could be charged for it. Tap the screen to proceed."
        else:
            e "To play this game, you'll need to download some data. If you're not on WiFi, you could be charged for it. Tap the screen to proceed."
            $ updater.continue_game_download()
    return
