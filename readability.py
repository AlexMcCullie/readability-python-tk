import re  # regex


class Readability:
    def __init__(self):
        # readability routines
        self.document = ""
        self.words = []
        self.word_count = 0
        self.sentence_count = 0
        self.syllable_count = 0
        self.flesch_index = 0

    def __count_sentences(self):
        regex_match = re.findall('[^.!?]+[.!?]', self.document)
        self.sentence_count = len(regex_match)
        if self.sentence_count < 1:
            self.sentence_count = 1

    def __separate_words(self):
        self.words = re.findall('\S+', self.document)
        self.word_count = len(self.words)

    def __count_text_syllables(self):
        document_syllable_count = 0
        for word in self.words:
            word_syllable_count = 0
            adjusted_word = re.sub("[ayiou][eayiou][eayiou]|[ayiou][eayiou]", "i", word)
            adjusted_word = re.sub("e[eayiou]|ed", "e", adjusted_word)
            adjusted_word = re.sub("ise|ize|ive|ice|ure|ance|ince|are", "i", adjusted_word)
            regex_match = re.findall('[aeiouy]*', adjusted_word)
            for vowel in regex_match:
                if vowel != "":
                    word_syllable_count = word_syllable_count + 1
            # remove last e
            if adjusted_word[-1].lower() == 'e':
                word_syllable_count = word_syllable_count - 1
            # every word at least one syllable
            if word_syllable_count < 1:
                word_syllable_count = 1
            document_syllable_count = document_syllable_count + word_syllable_count
        self.syllable_count = document_syllable_count

    def __calculate_flesch_index(self):
        self.flesch_index = 206.835 - (84.6 * self.syllable_count / self.word_count) \
                            - (1.015 * self.word_count / self.sentence_count)

    def calculate_readability(self, document):
        self.document = document
        self.__count_sentences()
        self.__separate_words()
        self.__count_text_syllables()
        self.__calculate_flesch_index()
        return self.sentence_count, self.word_count, \
            self.syllable_count, self.flesch_index
