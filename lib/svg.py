from typing import Any, Generator, List, Literal

from lib.models import Curve, Word


def generateSvgPath(curves: List[Curve], offset: tuple[float, float]) -> Generator[str, Any, None]:
    for curve in curves:
        # curve.scale(scale)
        curve.translate(offset[0], offset[1])

        yield f"<path d=\"M {curve.start[0]} {curve.start[1]} C {curve.control1[0]} {curve.control1[1]}, {curve.control2[0]} {curve.control2[1]}, {curve.end[0]} {curve.end[1]}\" fill=\"none\" stroke=\"black\" stroke-width=\"2\" />"

def generateSvg(wordList: List[Word]) -> str:

    svg = ""
    height = 120
    word_offset: tuple[float, float] = (0,0)
    additional_width = 30

    for word in wordList:
        paths: Generator[str, Any, None] = generateSvgPath(word.curves, word_offset)
        for path in paths:
            svg += f"\n{path}"
        word_offset = (word_offset[0] + word.width + additional_width, word_offset[1])

    width = word_offset[0] + wordList[-1].width + additional_width
    lines = '<line x1="0" x2="100%" stroke="gray" y1="25" y2="25" stroke-dasharray="3"/><line x1="0" x2="100%" stroke="gray" y1="50" y2="50"/><line x1="0" x2="100%" stroke="gray" y1="75" y2="75"/><line x1="0" x2="100%" stroke="gray" y1="100" y2="100" stroke-dasharray="3"/>'

    svg = f"<svg width=\"{width}\" height=\"{height}\">\n{lines}\n{svg}\n\n</svg>"

    return svg