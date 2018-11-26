# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("PrototypeBoy")
define f = Character("PrototypeGrape")


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

    e "This is the Linear Prototype."

    hide prototypeboy

    show grapeboy

    f "And I'm a different Character"

    hide grapeboy

    show prototypeboy

    e "The Story Progresses through many different mediums"

    e "You must choose the fate of grapeboy."

    menu:
        "What is the ultimate fate of Grapeboy?"

        "Pet him.":
            "Why are you petting him, he's a grape"

        "Kill Him!":
            "Well done... You just killed a poor innocent grape"

        "Leave him alone":
            "He remains prideful and not dead."

    scene background2

    show prototypeboy

    e "This is the conclusion"

    # This ends the game.

    return
