import nltk
import logging
from nltk.corpus import conll2007
from nltk.corpus.reader import ConllCorpusReader
import os
import collections
from sklearn import preprocessing

class entityDetector:
    __doc__ = "classify tokens/phrases as entities"
    def __init__(self):
        self.supportedEntities = ["person", "organisation", "food", "location", "date"]
        self.logger = logging.getLogger(__name__)
    def train(self, data):
        self.logger.debug(data)
        self.logger.debug(dir(conll2007))
    def test(self):
        ner_tags = collections.Counter()
        corpus_root = "/home/basavaraj.r/gmb-2.2.0"  # Make sure you set the proper path to the unzipped corpus
        for root, dirs, files in os.walk(corpus_root):
            for filename in files:
                if filename.endswith(".tags"):
                    with open(os.path.join(root, filename), 'rb') as file_handle:
                        file_content = file_handle.read().decode('utf-8').strip()
                        annotated_sentences = file_content.split('\n\n')  # Split sentences
                        for annotated_sentence in annotated_sentences:
                            annotated_tokens = [seq for seq in annotated_sentence.split('\n') if seq]  # Split words
                            standard_form_tokens = []
                            for idx, annotated_token in enumerate(annotated_tokens):
                                annotations = annotated_token.split('\t')  # Split annotations
                                word, tag, ner = annotations[0], annotations[1], annotations[3]
                                ner_tags[ner] += 1
        print(ner_tags)
