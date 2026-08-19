#Convert emoji

import demoji

def remove_emoji(msg):
    print(demoji.replace(msg,""))

def replace_emoji_with_text(msg):
    print(demoji.replace_with_desc(msg))

def find_emojis(msg):
    print(demoji.findall(msg))

def main():
    emoji = "Hello world! 😭😂"
    remove_emoji(emoji)
    replace_emoji_with_text(emoji)
    find_emojis(emoji)

if __name__ == '__main__':
    main()