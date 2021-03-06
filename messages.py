#A place to store game messages without hard-coding them into the source.

messages = {
    "NO-DOOR": "There doesn't seem to be a room in that direction...",
    "NEW-ROOM": "You open the door, and walk into a room.",
    "NO-ITEM": "404 item not found.",
    "NO-DIR": "But where do you want to go?",
    "INVALID-DIR": "You don't know how to go there.",
    "NO-THING": "418 I'm a teapot, I don't know what you're talking about.",
    #Works a lot better if you've seen the NO-ITEM first
    "LOOK-NAME": "This room's name is {}.",
    "LOOK-ITEMS": "You look around, and find the following items:",
    "LOOK-THINGS": "You also see the following things in the room",
    "TAKE-ACT": "The {} has taken your {}!",
    "NAN": "That isn't a number... We're using base 10.",
    "TAKE-ACT-FAILED": "The {} has tried to take a {}!",
    "GIVE-ACT": "The {} has given you a {}!",
    "TELE-ACT": "The {} has teleported you!",
    "INVALID-COMMAND": "I don't know what you mean by {}.",
    "HELPTEXT": """
    move,go: Moves your player in the specified direction
        format: go <up/down/left/right>
        Directions can be given using up,down,left,right,
        or using north,south,east,west, they act the same.
        If there is not a door in the direction, a message will be given.
        If there is a door, your player will be moved, with a message.

    take: Adds any specified item to your inventory
        format: take <item/all>
        You can either specify an item, or use all to take everything.

    inv,inventory: Prints the contents of your inventory.
        format: inv
        Doesn't take any input, prints every item that you have, 1 per line.

    search,look: Looks around
        format: look
        Prints the name of the room you are in, every item in it,
        and every thing in the room. You can't look at specific items yet.

    use: Uses one item on a thing.
        format: use <item> on <thing>
        When given both the name of an item, and a thing, will attempt to use
        the item on the thing. No message will be printed if this fails.

    help: Prints the help text
        format: help
        I'm assuming you know how to invoke the help text.
    """
}


def getmsg(code):
    return messages[code]
