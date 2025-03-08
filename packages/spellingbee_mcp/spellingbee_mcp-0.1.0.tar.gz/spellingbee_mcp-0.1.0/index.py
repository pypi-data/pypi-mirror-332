# server.py
from mcp.server.fastmcp import FastMCP
import os
import pathlib

# Get the path to corpora.txt in the same directory as this file
current_dir = pathlib.Path(__file__).parent
corpora_path = os.path.join(current_dir, "corpora.txt")

# Create an MCP server
mcp = FastMCP("mcp-spellingbee")

# Add an addition tool
@mcp.tool()
def get_longest_word(used_words, letters_array):
    """
    Reads words from 'corpora.txt', filters them using the letters in `letters_array`,
    excludes those in `used_words`, and returns the longest valid word.

    :param used_words: List of words already used (these won't be returned).
    :param letters_array: List of allowed letters (e.g. ['a', 'p', 'l', 'e']).
    :return: The longest valid unused word, or 'No valid words found' if none exist.
    """
    # Convert letters_array to a set for efficient checks
    valid_letters = set(letters_array)

    # Read all words from 'corpora.txt' and apply filtering
    valid_words = []

    with open(corpora_path, "r", encoding="utf-8") as file:
        for line in file:
            word = line.strip().lower()
            if word and set(word).issubset(valid_letters):
                valid_words.append(word)

    # Remove words that have already been used
    valid_words = [w for w in valid_words if w not in used_words]

    # Sort by length in descending order
    valid_words.sort(key=len, reverse=True)

    # Return the longest word if any remain, otherwise a fallback message
    return valid_words[0] if valid_words else "No valid words found"

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
