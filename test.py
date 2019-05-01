def block_text(text, length=7):
    final_text = ""
    while len(text) >= length:
        final_text += text[0:length] + "\n"
        text = text[length:]
        print(final_text, text)
    print(final_text)
        # print(final_text, text)

block_text("Come to Steves house for an absolute rager! It's totally wild and will be the night of your life!", 30)
