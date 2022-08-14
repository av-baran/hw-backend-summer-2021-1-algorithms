from typing import Optional

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """
    words = text.split()
    longest_word = ''
    shortest_word = next(iter(words), '')
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
        if len(word) < len(shortest_word):
            shortest_word = word
    if longest_word == '':
        longest_word = None
    if shortest_word == '':
        shortest_word = None
    
    return (shortest_word, longest_word)
