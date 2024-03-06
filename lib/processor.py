from lib import parse
from lib import wordlist
from lib.render import render_words_to_svg

wlist = wordlist.wordlist()
wlist.load("lib/wordlist.txt")

def text_to_svg(text: str) -> None:
    words = parse.convert_text(text, [wlist])[0]
    return render_words_to_svg(words)