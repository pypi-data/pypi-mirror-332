from typing import Callable, List, Literal, Tuple, Union
from re import compile

hyphenated_regex = compile(r'(?<=-)(?=(?!-).)')

LOREM_IPSUM_W = 'Lorem ipsum odor amet, consectetuer adipiscing elit.'
LOREM_IPSUM_S = ('Lorem ipsum odor amet, consectetuer adipiscing elit. In malesuada eros natoque '
                 'urna felis diam aptent donec. Cubilia libero morbi fusce tempus, luctus aenean '
                 'augue. Mus senectus rutrum phasellus fusce dictum platea. Eros a integer nec '
                 'fusce erat urna.')
LOREM_IPSUM_P = ('Lorem ipsum odor amet, consectetuer adipiscing elit. Nulla porta ex condimentum '
                 'velit facilisi; consequat congue. Tristique duis sociosqu aliquam semper sit id. '
                 'Nisi morbi purus, nascetur elit pellentesque venenatis. Velit commodo molestie '
                 'potenti placerat faucibus convallis. Himenaeos dapibus ipsum natoque nam dapibus '
                 'habitasse diam. Viverra ac porttitor cras tempor cras. Pharetra habitant nibh '
                 'dui ipsum scelerisque cras? Efficitur phasellus etiam congue taciti tortor quam. '
                 'Volutpat quam vulputate condimentum hendrerit justo congue iaculis nisl nullam.'
                 '\n\nInceptos tempus nostra fringilla arcu; tellus blandit facilisi risus. Platea '
                 'bibendum tristique lectus nunc placerat id aliquam. Eu arcu nisl mattis potenti '
                 'elementum. Dignissim vivamus montes volutpat litora felis fusce ultrices. '
                 'Vulputate magna nascetur bibendum inceptos scelerisque morbi posuere. Consequat '
                 'dolor netus augue augue tristique curabitur habitasse bibendum. Consectetur est '
                 'per eros semper, magnis interdum libero. Arcu adipiscing litora metus fringilla '
                 'varius gravida congue tellus adipiscing. Blandit nulla mauris nullam ante metus '
                 'curae scelerisque.\n\nSem varius sodales ut volutpat imperdiet turpis primis '
                 'nullam. At gravida tincidunt phasellus lacus duis integer eros penatibus. '
                 'Interdum mauris molestie posuere nascetur dignissim himenaeos; magna et quisque. '
                 'Dignissim malesuada etiam donec vehicula aliquet bibendum. Magna dapibus sapien '
                 'semper parturient id dis? Pretium orci ante leo, porta tincidunt molestie. '
                 'Malesuada dictumst commodo consequat interdum nisi fusce cras rhoncus feugiat.'
                 '\n\nHimenaeos mattis commodo suspendisse maecenas cras arcu. Habitasse id '
                 'facilisi praesent justo molestie felis luctus suspendisse. Imperdiet ipsum '
                 'praesent nunc mauris mattis curabitur. Et consectetur morbi auctor feugiat enim '
                 'ridiculus arcu. Ultricies magna blandit eget; vivamus sollicitudin nisl proin. '
                 'Sollicitudin sociosqu et finibus elit vestibulum sapien nec odio euismod. Turpis '
                 'eleifend amet quis auctor cursus. Vehicula pharetra sapien praesent amet purus '
                 'ante. Risus blandit cubilia lorem hendrerit penatibus in magnis.\n\nAmet posuere '
                 'nunc; maecenas consequat risus potenti. Volutpat leo lacinia sapien nulla '
                 'sagittis dignissim mauris ultrices aliquet. Nisi pretium interdum luctus donec '
                 'magna suscipit. Dapibus tristique felis natoque malesuada augue? Justo faucibus '
                 'tincidunt congue arcu sem; fusce aliquet proin. Commodo neque nibh; tempus ad '
                 'tortor netus. Mattis ultricies nec maximus porttitor non mauris?')

def mono(

    text: str,
    width: Union[int, float] = 70,
    lenfunc: Callable[[str], Union[int, float]] = len,

) -> List[str]:

    """
    Wraps the given text into lines of specified width.

    Parameters:
        text (str): The text to be wrapped.
        width (int | float, optional): The maximum width of each line. Defaults to 70.
        lenfunc (Callable[[str], int | float], optional): A function to calculate
                                                          the length of a string. Defaults to len.

    Returns:
        list[str]: A list of strings, where each string is a line of the wrapped text.
    """

    assert isinstance(text, str), "text must be a string"
    assert isinstance(width, (int, float)), "width must be an integer or float"
    assert callable(lenfunc), "lenfunc must be a callable function"

    assert width > 0, "width must be greater than 0"

    parts = []
    current_char = ''

    for char in text:
        if lenfunc(current_char + char) <= width:
            current_char += char
        else:
            parts.append(current_char)
            current_char = char

    if current_char:
        parts.append(current_char)

    return parts

def word(

    text: str,
    width: Union[int, float] = 70,
    lenfunc: Callable[[str], Union[int, float]] = len,

) -> List[str]:

    """
    Wraps the input text into lines of specified width.

    Parameters:
        text (str): The input text to be wrapped.
        width (int | float, optional): The maximum width of each line. Defaults to 70.
        lenfunc (Callable[[str], int | float], optional): A function to calculate
                                                          the length of a string. Defaults to len.

    Returns:
        list[str]: A list of strings, where each string is a line of wrapped text.
    """

    assert isinstance(text, str), "text must be a string"
    assert isinstance(width, (int, float)), "width must be an integer or float"
    assert callable(lenfunc), "lenfunc must be a callable function"

    assert width > 0, "width must be greater than 0"

    lines = []
    current_line = ''

    for word in text.split():
        test_line = current_line + ' ' + word if current_line else word

        if lenfunc(test_line) <= width:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)

            current_line = ''

            for part in hyphenated_regex.split(word):
                for wrapped_part in mono(part, width, lenfunc):
                    if lenfunc(current_line + wrapped_part) <= width:
                        current_line += wrapped_part
                    else:
                        if current_line:
                            lines.append(current_line)
                        current_line = wrapped_part

    if current_line:
        lines.append(current_line)

    return lines

def wrap(

    text: str,
    width: Union[int, float] = 70,
    lenfunc: Callable[[str], Union[int, float]] = len,
    method: Literal['mono', 'word'] = 'word',
    preserve_empty: bool = True

) -> List[str]:

    """
    Wraps the given text into lines of specified width.

    Parameters:
        text (str): The text to be wrapped.
        width (int | float, optional): The maximum width of each line. Defaults to 70.
        lenfunc (Callable[[str], int | float], optional): A function to calculate
                                                          the length of a string. Defaults to len.
        method (Literal['mono', 'word'], optional): The method to use for wrapping.
                                                    'mono' for character-based wrapping, 'word'
                                                    for word-based wrapping. Defaults to 'word'.
        preserve_empty (bool, optional): Whether to preserve empty lines. Defaults to True.

    Returns:
        list[str]: A list of wrapped lines.
    """

    assert isinstance(text, str), "text must be a string"
    assert isinstance(width, (int, float)), "width must be an integer or float"
    assert callable(lenfunc), "lenfunc must be a callable function"

    assert width > 0, "width must be greater than 0"

    wrapped_lines = []

    if method == 'mono':
        wrapfunc = mono
    elif method == 'word':
        wrapfunc = word
    else:
        raise ValueError(f"{method=} is invalid, must be 'mono' or 'word'")

    for line in text.splitlines():
        wrapped_line = wrapfunc(line, width, lenfunc)
        if wrapped_line:
            wrapped_lines.extend(wrapped_line)
        elif preserve_empty:
            wrapped_lines.append('')

    return wrapped_lines

def align(

    text: str,
    width: Union[int, float] = 70,
    linegap: Union[int, float] = 0,
    sizefunc: Callable[[str], Tuple[Union[int, float], Union[int, float]]] = lambda s : (len(s), 1),
    method: Literal['mono', 'word'] = 'word',
    alignment: Literal['left', 'center', 'right', 'fill'] = 'left',
    preserve_empty: bool = True

) -> List[Tuple[Union[int, float], Union[int, float], str]]:

    """
    Wraps and aligns text within a specified width and yields the position and content of each line.

    Parameters:
        text (str): The text to be wrapped and aligned.
        width (int | float, optional): The maximum width of each line. Defaults to 70.
        linegap (int | float, optional): The vertical gap between lines. Defaults to 0.
        sizefunc (Callable[[str], tuple[int | float, int | float]], optional): A function that
                                                                               returns the width and
                                                                               height of a given
                                                                               string. Defaults to a
                                                                               lambda function that
                                                                               returns the length of
                                                                               the string and 1.
        method (Literal['mono', 'word'], optional): The method to use for wrapping.
                                                    'mono' for character-based wrapping, 'word'
                                                    for word-based wrapping. Defaults to 'word'.
        alignment (Literal['left', 'center', 'right', 'fill'], optional): The alignment of the text.
                                                                          'left', 'center', 'right',
                                                                          or 'fill'.
                                                                          Defaults to 'left'.
        preserve_empty (bool, optional): Whether to preserve empty lines. Defaults to True.

    Returns:
        list[tuple[int | float, int | float, str]]: A list of tuples containing the position and
                                                    content of each line.
    """

    assert isinstance(linegap, (int, float)), "linegap must be an integer or float"
    assert callable(sizefunc), "sizefunc must be a callable function"

    assert linegap >= 0, "linegap must be equal to or greater than 0"

    wrapped = []
    offset_y = 0

    for line in wrap(text, width, lambda s : sizefunc(s)[0], method, preserve_empty):

        width_line, height_line = sizefunc(line)

        if alignment == 'left':
            wrapped.append((0, offset_y, line))

        elif alignment == 'center':
            wrapped.append(((width - width_line) / 2, offset_y, line))

        elif alignment == 'right':
            wrapped.append((width - width_line, offset_y, line))

        elif alignment == 'fill':
            offset_x = 0
            words = line.split()
            total_words = len(words)
            widths = {i: sizefunc(w)[0] for i, w in enumerate(words)}
            total_words_width = sum(widths.values())
            extra_space = width - total_words_width

            if total_words > 1:
                space_between_words = extra_space / (total_words - 1)
            else:
                space_between_words = extra_space

            for i, w in enumerate(words):
                wrapped.append((offset_x, offset_y, w))
                offset_x += widths[i] + space_between_words

        else:
            raise ValueError(
                f"{alignment=} is invalid, must be 'left', 'center', 'right', or 'fill'"
            )

        offset_y += height_line + linegap

    return wrapped

def shorten(

    text: str,
    width: Union[int, float] = 70,
    start: int = 0,
    lenfunc: Callable[[str], Union[int, float]] = len,
    placeholder: str = '...'

) -> str:

    """
    Shortens the given text to fit within the specified width, optionally including a placeholder.

    Parameters:
        text (str): The text to be shortened.
        width (int | float, optional): The maximum width of the shortened text. Defaults to 70.
        start (int, optional): The starting index of the text to be shortened. Defaults to 0.
        lenfunc (Callable[[str], int | float], optional): A function to calculate
                                                          the length of a string. Defaults to len.
        placeholder (str, optional): The placeholder to append to the shortened text.
                                     Defaults to '...'.

    Returns:
        str: The shortened text with the placeholder appended if necessary.
    """

    assert isinstance(text, str), "text must be a string"
    assert isinstance(width, (int, float)), "width must be an integer or float"
    assert isinstance(start, int), "start must be an integer"
    assert callable(lenfunc), "lenfunc must be a callable function"
    assert isinstance(placeholder, str), "placeholder must be a string"

    assert width >= lenfunc(placeholder), "width must be greater than length of the placeholder"
    assert start >= 0, "start must be equal to or greater than 0"

    if start == 0:
        current_char = ''
    else:
        current_char = placeholder

    for char in text[start:]:
        if lenfunc(current_char + char + placeholder) <= width:
            current_char += char
        else:
            return current_char + placeholder

    return current_char