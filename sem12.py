import re


class Word:
    allowed_languages = ['русский', 'французский']

    def __init__(self, glossed: str, gloss: str, language):
        self.glossed = glossed
        self.gloss = gloss
        if language not in self.allowed_languages:
            decision = input("Языка нет в списке доступных. Желаете его добавить? [д/н]", )
            if decision == "д":
                self.allowed_languages.append(language)
                self.language = language
            else:
                raise(ValueError("Выберите поддерживаемый язык "
                                 f"Список поддерживаемых языков {self.allowed_languages}"))
        else:
            self.language = language

    def __len__(self) -> int:
        word = re.sub(r'[-.=:]', '', self.glossed)
        return len(word)

    def __str__(self) -> str:
        return f'{self.glossed}\n{self.gloss}'

    def count_morphemes(self, blocks):
        return len(self.glossed.split(blocks))

    __repr__ = __str__


print(Word('мам-а=aaa.a', 'mother-NOM.SG', 'русский').count_morphemes('.-='))
