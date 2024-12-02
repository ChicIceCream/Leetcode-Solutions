class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        word_list = list(sentence.split())
        print(word_list)
        for i in range(len(word_list)):
            print(i, word_list[i])
            searchWordLength = len(searchWord)
            if searchWord in word_list[i][:searchWordLength]:
                return i + 1
            else:
                i + 1
        return -1