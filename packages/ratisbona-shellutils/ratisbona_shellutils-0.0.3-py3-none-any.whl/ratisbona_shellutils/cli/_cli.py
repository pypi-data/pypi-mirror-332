from ratisbona_utils.strings import Alignment

from ratisbona_utils.terminals.vt100 import color_text

from ratisbona_utils.boxdrawing import draw_box, LineStyle


def blue_dosbox(text: str) -> str:
    box = draw_box(text, width=80, alignment=Alignment.CENTER, linestyle=LineStyle.DOUBLE)
    return color_text(box, background=(0, 0, 128), foreground=(255, 255, 255))