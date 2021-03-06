# pylint: disable=no-self-use,invalid-name

from deep_qa.data.tokenizers.word_splitter import SimpleWordSplitter
from deep_qa.data.tokenizers.word_splitter import SpacyWordSplitter


class TestSimpleWordSplitter:
    word_splitter = SimpleWordSplitter()
    def test_tokenize_handles_complex_punctuation(self):
        sentence = "this (sentence) has 'crazy' \"punctuation\"."
        expected_tokens = ["this", "(", "sentence", ")", "has", "'", "crazy", "'", '"',
                           "punctuation", '"', "."]
        tokens = self.word_splitter.split_words(sentence)
        assert tokens == expected_tokens

    def test_tokenize_handles_contraction(self):
        sentence = "it ain't joe's problem; would've been yesterday"
        expected_tokens = ["it", "ai", "n't", "joe", "'s", "problem", ";", "would", "'ve", "been",
                           "yesterday"]
        tokens = self.word_splitter.split_words(sentence)
        assert tokens == expected_tokens

    def test_tokenize_handles_multiple_contraction(self):
        sentence = "wouldn't've"
        expected_tokens = ["would", "n't", "'ve"]
        tokens = self.word_splitter.split_words(sentence)
        assert tokens == expected_tokens

    def test_tokenize_handles_final_apostrophe(self):
        sentence = "the jones' house"
        expected_tokens = ["the", "jones", "'", "house"]
        tokens = self.word_splitter.split_words(sentence)
        assert tokens == expected_tokens

    def test_tokenize_handles_special_cases(self):
        sentence = "mr. and mrs. jones, etc., went to, e.g., the store"
        expected_tokens = ["mr.", "and", "mrs.", "jones", ",", "etc.", ",", "went", "to", ",",
                           "e.g.", ",", "the", "store"]
        tokens = self.word_splitter.split_words(sentence)
        assert tokens == expected_tokens


class TestSpacyWordSplitter:
    word_splitter = SpacyWordSplitter()
    def test_tokenize_handles_complex_punctuation(self):
        sentence = "this (sentence) has 'crazy' \"punctuation\"."
        expected_tokens = ["this", "(", "sentence", ")", "has", "'", "crazy", "'", '"',
                           "punctuation", '"', "."]
        tokens = self.word_splitter.split_words(sentence)
        assert tokens == expected_tokens

    def test_tokenize_handles_contraction(self):
        # note that "would've" is kept together, while "ain't" is not.
        sentence = "it ain't joe's problem; would've been yesterday"
        expected_tokens = ["it", "ai", "n't", "joe", "'s", "problem", ";", "would've", "been",
                           "yesterday"]
        tokens = self.word_splitter.split_words(sentence)
        assert tokens == expected_tokens

    def test_tokenize_handles_multiple_contraction(self):
        sentence = "wouldn't've"
        expected_tokens = ["would", "n't", "'ve"]
        tokens = self.word_splitter.split_words(sentence)
        assert tokens == expected_tokens

    def test_tokenize_handles_final_apostrophe(self):
        sentence = "the jones' house"
        expected_tokens = ["the", "jones", "'", "house"]
        tokens = self.word_splitter.split_words(sentence)
        assert tokens == expected_tokens

    def test_tokenize_handles_special_cases(self):
        # note that the etc. doesn't quite work --- we can special case this if we want.
        sentence = "Mr. and Mrs. Jones, etc., went to, e.g., the store"
        expected_tokens = ["mr.", "and", "mrs.", "jones", ",", "etc", ".", ",", "went", "to", ",",
                           "e.g.", ",", "the", "store"]
        tokens = self.word_splitter.split_words(sentence)
        assert tokens == expected_tokens
