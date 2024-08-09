class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        middle = len(s) // 2
        first_part = s[:middle]
        second_part = s[middle:]
        first_part_vowels = 0
        second_part_vowels = 0
        for x, y in zip(first_part, second_part):
            if x.lower() in ['a', 'i', 'u', 'e', 'o']:
                first_part_vowels += 1
            if y.lower() in ['a', 'i', 'u', 'e', 'o']:
                second_part_vowels += 1
        return first_part_vowels == second_part_vowels
