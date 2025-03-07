"""
The MIT License (MIT)

Copyright 2025 devs_des1re

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import requests
from bs4 import BeautifulSoup

from .errors import *

def get_antonyms(term: str):
    """
    Gets the antonyms of a term.

    Parameters
    ----------
    term :class:`str` : The term you want to get the antonyms for.

    Returns
    ----------
    A list of antonyms.

    Raises
    ----------
    TermException :class:`errors.TermException`
        If the term is not a single word.
    APIException :class:`errors.APIException`
        If no synonyms have been found.
    """
    if len(term.split()) > 1:
        raise TermException("A term can only be a single word.")
    else:
        response = requests.get(f"https://www.synonym.com/synonyms/{term}")
        if response.status_code != 200:
            raise APIException("No antonyms found.")
        data = BeautifulSoup(response.text, "html.parser")
        section = data.find("div", {"data-section": "antonyms"})
        synonyms = section.find_all("a")
        return [synonym.text.strip() for synonym in synonyms]