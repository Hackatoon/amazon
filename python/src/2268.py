class Solution:
    def sort_by_char_repeat(self, string):
        """Sorts a string by the count of each character, keeping all characters.

        Args:
            string: The string to sort.

        Returns:
            A string sorted by the count of each character, with the most frequent
            characters appearing first (repeated characters grouped together).
        """

        char_counts = Counter(string)
        sorted_chars = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)

        result = []
        for char, count in sorted_chars:
            result.extend([char] * count)  # Extend with char repeated by its count
        return ''.join(result)

    def minimumKeypresses(self, s: str) -> int:

        s = self.sort_by_char_repeat(s)

        index_empty = 0

        count = 1

        result = 0

        l = [0] * 26

        for letter in s:

            index_letter = ord(letter) - ord('a') 

            if l[index_letter] == 0:

                l[index_letter] = count

                index_empty += 1

                if index_empty > 8:

                    count += 1

                    index_empty = 0
            
            result += l[index_letter]


        return result
