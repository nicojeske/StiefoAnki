from typing import List

from lib import symbols
from lib.models import Curve, Word
from lib.svg import generateSvg

SCALE = 25
OFFSET = (20, 75)

def generate_word_list(words: List[str]) -> List[Word]:
    wordList: List[Word] = []
    for word in words:
        curveInfo = symbols.stiefoWortZuKurve(word)[0]
        wordWidth = curveInfo[0] * SCALE
        curves = curveInfo[1]
        curves = [(OFFSET[0] + curve[0] * SCALE, OFFSET[1] - curve[1] * SCALE) for curve in curves]

        wordCurves: List[Curve] = []
        for i in range(1, len(curves), 3):

            wordCurves.append(Curve(
                curves[i-1],
                curves[i],
                curves[i+1],
                curves[i+2]))
            
        wordList.append(Word(word, wordCurves, wordWidth))
    return wordList

def render_words_to_svg(words: List[str]):
    wordList = generate_word_list(words)
    return generateSvg(wordList)
