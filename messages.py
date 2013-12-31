#A place to store game messages without hard-coding them into the source.

messages = {
"NO-DOOR":"There doesn't seem to be a room in that direction...",
"NEW-ROOM":"You open the door, and walk into a room.",
"NO-ITEM":"404 item not found.",
"LOOK-NAME":"This room's name is {}.",
"LOOK-ITEMS":"You look around, and find the following items:",
"LOOK-THINGS":"You also see the following things in the room",
"TAKE-ACT":"The {} has taken your {}!",
"GIVE-ACT":"The {} has given you a {}!",
"TELE-ACT":"The {} has teleported you!",
"INVALID-COMMAND":"I don't know what you mean by {}.",
"HELPTEXT":"""
move,go: Moves your player in the specified direction
    format: go <up/down/left/right>
    Directions can be given using up,down,left,right or north,south,east,west
    If there is not a door in the direction, a message will be given.
    If there is a door, your player will be moved, with a message.

take: Adds any specified item to your inventory
    format: take <item/all>
    You can either specify an item, or use all,everything to take everything.

inv,inventory: Prints the contents of your inventory.
    format: inv
    Doesn't take any input, prints every item in your inventory, 1 per line.

search,look: Looks around
    format: look
    Prints the name of the room you are in, every item in it, and every thing.

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
