#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "camel-tools>=1.5.7",
# ]
# ///

import json
import sys
import socket

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

SOCKET_PATH = "/tmp/gd-arabic.sock"


def main():
    word = sys.argv[1] if len(sys.argv) > 1 else ""
    sentence = sys.argv[2] if len(sys.argv) > 2 else ""

    # connect to server
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    try:
        sock.connect(SOCKET_PATH)
    except socket.error as e:
        print("<div>Server not running. Start the gd-arabic service.</div>")
        sys.exit(1)

    request = json.dumps({"sentence": sentence})
    sock.sendall(request.encode("utf-8"))

    response = sock.recv(65536).decode("utf-8")
    sock.close()

    data = json.loads(response)
    if "error" in data:
        print(f'<div style="color:red">Error: {data["error"]}</div>')
        sys.exit(1)

    tokens = data["tokens"]
    lemmas = data["lemmas"]

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
