from typing import List


class Solution:
    def longestCommonPrefix(self, words: List[str]) -> str:
        if not words:
            return ""

            # Start with the first word as the prefix
        prefix = words[0]

        # Compare the current prefix with each word
        for word in words[1:]:
            # Reduce the prefix length until it matches the start of each word
            while word[:len(prefix)] != prefix and prefix:
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix

    # Example usage
    words = ["flower", "flow", "flight"]