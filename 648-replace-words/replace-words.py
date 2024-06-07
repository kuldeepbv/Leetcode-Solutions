class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentence_list = sentence.split(' ')
        dictionary.sort()

        for i, word in enumerate(sentence_list):
            for check_word in dictionary:
                if check_word == word[:len(check_word)]:
                    sentence_list[i] = check_word
                    break

        return ' '.join(sentence_list)