#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "camel-tools>=1.5.7",
# ]
# ///

# https://pymotw.com/3/socket/uds.html

import json
import os
import sys
import socket
from camel_tools.tokenizers.word import simple_word_tokenize
from camel_tools.disambig.mle import MLEDisambiguator

SOCKET_PATH = "/tmp/gd-arabic.sock"


def main():
    try:
        os.unlink(SOCKET_PATH)
    except OSError:
        if os.path.exists(SOCKET_PATH):
            raise

    mle = MLEDisambiguator.pretrained()
    print("Model Loaded")

    # wait for a request from the client
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.bind(SOCKET_PATH)
    sock.listen(1)

    print("Server is listening for incoming connections...")

    try:
        while True:
            conn, _ = sock.accept()
            try:
                data = conn.recv(65536).decode("utf-8")
                if data:
                    response = handle_request(mle, data)
                    conn.sendall(response.encode("utf-8"))
            except Exception as e:
                conn.sendall(json.dumps({"error": e}).encode("utf-8"))
            finally:
                conn.close()
    finally:
        sock.close()
        os.remove(SOCKET_PATH)


def handle_request(mle, data):
    request = json.loads(data)

    sentence = request.get("sentence", "")

    tokens = simple_word_tokenize(sentence)
    disambig = mle.disambiguate(tokens)

    lemmas = [d.analyses[0].analysis["lex"] for d in disambig]

    return json.dumps({"tokens": tokens, "lemmas": lemmas})


if __name__ == "__main__":
    main()
