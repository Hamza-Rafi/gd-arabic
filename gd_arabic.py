#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "camel-tools>=1.5.7",
# ]
# ///

import sys
from camel_tools.tokenizers.word import simple_word_tokenize
from camel_tools.disambig.mle import MLEDisambiguator

css = """
<style>
  .gd-arabic {
    font-size: 2rem;
    direction: rtl;
    text-align: right;
    font-family: "Amiri", "Scheherazade", "Traditional Arabic", serif;
  }
  .gd-arabic a {
    color: royalblue;
    text-decoration: none;
  }
  .gd-arabic a b {
    background-color: #ddeeff;
    border-radius: 0.2rem;
    font-weight: 500;
  }
</style>
"""


def main():
    mle = MLEDisambiguator.pretrained()

    word = sys.argv[1] if len(sys.argv) > 1 else ""
    sentence = sys.argv[2] if len(sys.argv) > 2 else word

    tokens = simple_word_tokenize(sentence)
    disambig = mle.disambiguate(tokens)

    lemmas = [d.analyses[0].analysis["lex"] for d in disambig]

    parts = []
    for token, lemma in zip(tokens, lemmas):
        parts.append("")
        if token == word:
            parts.append(f'<a href="bword:{lemma}" title="{lemma}"><b>{token}</b></a>')
        else:
            parts.append(f'<a href="bword:{lemma}" title="{lemma}">{token}</a>')

    print(f'<div class="gd-arabic">{" ".join(parts)}</div>')

    print(css)


if __name__ == "__main__":
    main()
