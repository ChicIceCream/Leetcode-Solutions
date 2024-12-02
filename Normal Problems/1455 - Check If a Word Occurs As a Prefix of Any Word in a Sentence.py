class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        # split up the words so only words print, without this part, it will give every letter instead
        word_list = list(sentence.split())
        # print(word_list)
        for i in range(len(word_list)):
            # print(i, word_list[i])
            # to search through only the prefix part
            searchWordLength = len(searchWord)
            if searchWord in word_list[i][:searchWordLength]:
                return i + 1
            else:
                i + 1
        return -1