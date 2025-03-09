"""Implements the `style()` function: applies foreground and background colors, and font styles."""

from typing import Any, Generator, Optional, Tuple
from .types import Color, FontStyle
from .validate import validate_color, validate_fontstyle
from .const import COLORS_RGB_MAP, FONT_STYLE_CODES, COMBINATOR, HEX_PREFIX, RGB_DELIMITER, RESET


def get_rgb_values(color: Color) -> Tuple[int, ...]:
    """Converts given color to individual rgb values."""
    if color.startswith(HEX_PREFIX):
        return tuple(int(color[1:][i : i + 2], base=16) for i in range(0, 6, 2))
    if RGB_DELIMITER in color:
        return tuple(map(int, color.split(RGB_DELIMITER)))
    return COLORS_RGB_MAP[color]


def _get_fontstyle_codes(fontstyle: FontStyle) -> Generator[int, None, None]:
    """Converts given font styles to font style codes."""
    for font_style in fontstyle.split(COMBINATOR):
        yield FONT_STYLE_CODES[font_style]


def style(
    text: Any,
    fg: Optional[Color] = None,
    bg: Optional[Color] = None,
    fs: Optional[FontStyle] = None,
) -> str:
    """
    Applies foreground color, background color, and font style to text.

    Args:
        text (str): The text to be styled.
        fg (Color | None): Foreground color for the text. Defaults to `None`.
        bg (Color | None): Background color for the text. Defaults to `None`.
        fs (FontStyle | None): Font style(s) for the text. Defaults to `None`.

    Returns:
        str: Styled text if any of `fg`, `bg`, or `fs` is specified else `text`.
    """
    text = f"{text}"
    if (fg or bg or fs) and text:
        fg_code = bg_code = fs_code = ""
        if fg := validate_color(fg):
            fg_code = f"\033[38;2;{';'.join(map(str, get_rgb_values(fg)))}m"
        if bg := validate_color(bg):
            bg_code = f"\033[48;2;{';'.join(map(str, get_rgb_values(bg)))}m"
        if fs := validate_fontstyle(fs):
            fs_code = "".join((f"\033[{code}m" for code in _get_fontstyle_codes(fs)))
        styles = fg_code + bg_code + fs_code
        styled_text = styles + text.replace(RESET, f"{RESET}{styles}")
        styled_text = styled_text.replace("\n", f"{RESET}\n{styles}")
        styled_text += RESET if not styled_text.endswith(RESET) else ""
        return styled_text
    return text
