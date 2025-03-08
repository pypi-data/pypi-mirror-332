import ast
import time
import os
import sys
from semantic_text_splitter import TextSplitter
from tokenizers import Tokenizer


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # base_path = os.path.abspath(".")
        base_path = os.path.dirname(os.path.realpath(__file__))

    return os.path.join(base_path, relative_path)


def semaitc_splitter(content: str = None, max_characters: int = 800):
    if content:
        # Maximum number of characters in a chunk
        # max_characters = 1000
        # Optionally can also have the splitter not trim whitespace for you
        # tokenizer = Tokenizer.from_pretrained("bert-base-uncased")
        # Maximum number of tokens in a chunk
        # max_tokens = 1000
        splitter = TextSplitter.from_tiktoken_model("gpt-3.5-turbo")
        # splitter = TextSplitter.from_huggingface_tokenizer(tokenizer)
        # splitter = TextSplitter(trim_chunks=False)

        chunks = splitter.chunks(content, max_characters)

        return chunks
    return None
