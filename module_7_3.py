import sys


def str_clean(str_, nongrata):
    new_str = str_
    for subs in nongrata:
        new_str = new_str.replace(subs, '')
    return new_str


class WordsFinder():
    def __init__(self, *files):
        self.file_names = files

    def get_all_words(self):
        all_words = dict()

        punctuses = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for f in self.file_names:
            words = []
            with open(f, 'r', encoding='utf-8') as file:
                str_ = file.read().lower()
                str_ = str_clean(str_, punctuses)
                arr = str_.split()
                words += arr
                all_words.update({f: words})

        return all_words

    def find(self, word):
        d = self.get_all_words()
        res = dict()
        for file, words in d.items():
            flag = False
            for i, w in enumerate(words):
                print(file, i, w)
                if w == word.lower():
                    res.update({file: i + 1})

                    flag = True
                    break
            if not flag:
                res.update({file: None})

        return res

    def count(self, word):
        d = self.get_all_words()
        res = dict()
        for file in d:
            res.update({file: d[file].count(word.lower())})
        return res


finder2 = WordsFinder(r"test_file.txt")

print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
