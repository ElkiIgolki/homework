class WordsFinder:
    def __init__(self, *file_names: list):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        pun = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for name in self.file_names:
            with open(name, 'r', encoding='utf-8') as file:
                words = file.read().lower()
                for p in pun:
                    words = words.replace(p, '')
                words1 = words.split()
                all_words[name] = words1
        return all_words

    def find(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        result = {}
        for name, words1 in all_words.items():
            if word in words1:
                result[name] = words1.index(word) + 1
            else:
                result[name] = None
        return result

    def count(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        result = {}
        for name, words1 in all_words.items():
            a = 0
            for i in words1:
                if i == word:
                    a += 1
            result[name] = a
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего