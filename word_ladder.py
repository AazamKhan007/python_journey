from collections import deque, defaultdict
from typing import List

def build_pattern_dict(word_list: List[str]) -> dict:
    """
    Build a mapping from generic patterns (with one wildcard '*') to words.
    Example: "hot" -> "*ot", "h*t", "ho*"
    """
    patterns = defaultdict(list)
    for word in word_list:
        for i in range(len(word)):
            pattern = word[:i] + '*' + word[i+1:]
            patterns[pattern].append(word)
    return patterns

def ladder_length(begin_word: str, end_word: str, word_list: List[str]) -> int:
    """
    Returns the length of the shortest transformation sequence from begin_word to end_word.
    Uses BFS with intermediate wildcard patterns for efficiency.
    """
    if end_word not in word_list:
        return 0

    L = len(begin_word)
    patterns = build_pattern_dict(word_list + [begin_word])

    visited = set([begin_word])
    q = deque([(begin_word, 1)])  # (current_word, level)

    while q:
        word, level = q.popleft()
        if word == end_word:
            return level

        # iterate through all generic patterns of current word
        for i in range(L):
            pattern = word[:i] + '*' + word[i+1:]
            for neighbor in patterns.get(pattern, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append((neighbor, level + 1))
            # clear list to prevent reprocessing same pattern (optimization)
            patterns[pattern] = []

    return 0

if __name__ == "__main__":
    begin = "hit"
    end = "cog"
    word_list = ["hot","dot","dog","lot","log","cog"]
    print("Shortest Transformation Sequence Length:",
          ladder_length(begin, end, word_list))
