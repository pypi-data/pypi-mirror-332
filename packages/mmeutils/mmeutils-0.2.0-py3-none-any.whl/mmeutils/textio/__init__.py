"""Text Input/Output Utility Functions"""

#region Imports

from rich.text import Text
from typing import List

#enregion

#region Exports

__all__: List[str] = [
    'strip_rich_tags',
]

#endregion

#region Functions

def print_error(message: str) -> None:
    print(message)


def print_warning(message: str) -> None:
    print(message)


def strip_rich_tags(text: str) -> str:
    """Strips Rich package formatting tags from a text string.
    Primarily used for logging purposes or other forms of text storage.

    :param text: Input text with Rich color and format specifiers.
    :type text: str

    :return: A plain Python string.
    :rtype: str
    """
    rendered_text = Text.from_markup(text)
    return rendered_text.plain

#endregion
