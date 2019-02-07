# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Wild Dog")
define f = Character("You")

default torch = False

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene background1

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show prototypeboy

    # These display lines of dialogue.
    "You find yourself in a dark, lonely forest"
    "With naught to see except for lumber"
    "There are very little options available"

    menu:
        "What will you do?"

        "Woot":
            jump examine_surroundings

        "woot2":
            jump headfirst


    label examine_surroundings

    "You find a torch to light your way. You then go into the dark and creepy forest"

    $ torch = True

    jump lost

    label headfirst

    "You rush in headfirst into the dark forest"

    jump lost

    label lost

    "After a few minutes of exploring the dark forest, you start to notice that you're going in circles"

    if torch:
        "Luckily you found a torch and"
    else:
        "You continue to stumble through the dark"


    e "This is the Linear Prototype."

    hide prototypeboy

    show grapeboy

    f "And I'm a different Character"

    hide grapeboy

    show prototypeboy

    e "The Story Progresses through many different mediums"

    e "You must choose the fate of grapeboy."



    scene background2

    show prototypeboy

    e "This is the conclusion"

    # This ends the game.

    return
