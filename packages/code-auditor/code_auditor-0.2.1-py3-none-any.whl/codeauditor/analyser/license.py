"""License analyser module."""
import json
import os
import re
from hashlib import md5
from pathlib import Path

from . import Analyser
from ..processor import ProcessorType
from ..report import Report


"""Maximum number of tokens per signature."""
MAX_TOKENS = 20

"""Reduced token size."""
TOKEN_SIZE = 4


def get_signature(text: str, max_tokens: int=MAX_TOKENS) -> list[str]:
    """Returns signature.

    Args:
        text (str): Textual content.
        max_tokens (int): Maximum number of tokens (default = MAX_TOKENS)

    Returns:
        List of token strings.
    """
    tokens = []

    text = re.sub(r'\r', '', text)
    text = re.sub(r'\n(\s*\n)+', '.', text, flags=re.M)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\. ]', '', text)

    for row in re.split(r'\.+', text):

        row = row.strip().lower()
        if not row:
            continue

        hash = md5()
        hash.update(row.encode())
        val = hash.hexdigest()

        tokens.append(val)

        if max_tokens and len(tokens) == max_tokens:
            break

    return tokens


def save_signatures(
    repo: str='.',
    suffix: str='.json',
    path: str='signatures.json',
    max_tokens: int=MAX_TOKENS,
    token_size: int=TOKEN_SIZE,
    skip_tokens: list[str]=None
):
    """Stores the license signatures.

    Args:
        repo (str): Path of the repository of the licenses (default = '.')
        suffix (str): License file suffix (default = '.json')
        path (str): Path of the signatures file (default = 'signatures.json')
        max_tokens (int): Number of maximum tokens (default = MAX_TOKENS)
        token_size (int): Token size (default = TOKEN_SIZE)

    Raises:
        ValueError("Invalid token size."): If token size is invalid.
    """
    result = {
        '_MAX_TOKENS': max_tokens,
        '_TOKEN_SIZE': token_size,
    }
    lookup = {}

    for root, dirs, files in os.walk(repo):

        for file in files:

            filepath = Path(os.path.join(root, file))
            if filepath.suffix != suffix:
                continue

            id = filepath.stem

            skip = False
            for token in skip_tokens if skip_tokens else []:
                if token in id:
                    skip = True
                    break

            if skip:
                continue

            with open(filepath, 'r', encoding='utf-8') as file:

                if suffix == '.json':
                    data = json.load(file)

                    if not 'text' in data:
                        continue

                    text = data['text']

                elif suffix == '.txt':
                    text = file.read()

            tokens = get_signature(text, max_tokens)

            if token_size:

                tiny_tokens = []

                for token in tokens:

                    tiny_token = token[:token_size] + token[-token_size:]

                    if tiny_token not in lookup:
                        lookup[tiny_token] = token

                    elif token != lookup[tiny_token]:
                        raise ValueError("Invalid token size.")

                    tiny_tokens.append(tiny_token)

                result[id] = tiny_tokens

            else:

                result[id] = tokens

    with open(path, 'w') as file:
        json.dump(result, file)


def find_license(text: str, filename: str='signatures.json') -> tuple:
    """Finds the possible license identifiers given the license content.

    Args:
        text (str): Textual content of the license.
        filename (str): File name of the signatures file (default = 'signatures.json')

    Returns:
        Tuple of possible license identifiers and the minimum score.

    Raises:
        Valuerror("Invalid signatures file."): If signatures file is invalid.
    """
    with open(filename, 'r') as file:
        signatures = json.load(file)

    if '_MAX_TOKENS' not in signatures or '_TOKEN_SIZE' not in signatures:
        raise ValueError("Invalid signatures file.")

    max_tokens = signatures['_MAX_TOKENS']
    token_size = signatures['_TOKEN_SIZE']

    sign = set()
    for token in get_signature(text, max_tokens):
        if token_size:
            token = token[:token_size] + token[-token_size:]
        sign.add(token)

    ids = []
    min_score = -1

    for id, tokens in signatures.items():

        if id == '_MAX_TOKENS' or id == '_TOKEN_SIZE':
            continue

        tokens = set(tokens)

        score = len(tokens - sign) + len(sign - tokens)

        if score == min_score:
            ids.append(id)

        elif min_score < 0 or score < min_score:
            min_score = score
            ids = [id]

    return (ids, min_score)


class License(Analyser):
    """License analyser class."""

    @classmethod
    def get_type(cls) -> ProcessorType:
        """Returns analyser type."""
        return ProcessorType.LICENSE


    @classmethod
    def includes(cls, path: Path) -> list[str]:
        """Returns file and directory patterns to be included in the analysis.

        Args:
            path (Path): Path of the code base.

        Returns:
            List of file and directory patterns.
        """
        return [
            '/licen[cs]e',
            '/licen[cs]e.md',
            '/licen[cs]e.txt'
        ]


    @classmethod
    def analyse_content(cls, content: str, report: Report, path: Path=None) -> dict:
        """Analyses content.

        Args:
            content (str): Content.
            report (Report): Analysis report.
            path (Path): Path of the content file (optional).

        Returns:
            Dictionary of the analysis results.
        """
        ids, score = find_license(content, Path(__file__).parent / 'data/licenses.json')

        result = {
            'ids': ids,
            'score': score
        }

        return result
