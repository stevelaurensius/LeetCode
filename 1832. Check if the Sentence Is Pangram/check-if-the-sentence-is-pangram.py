class Solution:
    def checkIfPangram(self, sentence):
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        sentence = set(sentence)
        for char in sentence:
            if char in alphabet:
                alphabet.remove(char)
        return alphabet == []