from lib import parse
from lib import wordlist
from lib.render import render_words_to_svg

def text_to_svg(text: str, filename: str) -> None:

    wlist = wordlist.wordlist()
    wlist.load("lib/wordlist.txt")

    words = parse.convert_text(text, [wlist])[0]
    render_words_to_svg(words, filename)