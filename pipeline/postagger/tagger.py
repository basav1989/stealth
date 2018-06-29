import nltk
import logging

class tagger:
	__doc__ = "this is a temporal model for POS tagging"
	def __init__(self):
		self.supportedModels = {}
		self.backend = "nltk"
		logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
		self.logger = logging.getLogger(__name__)

	def configure(self):
		self.models = []
		pos_tagger = nltk.tag.TnT()
		self.supportedModels["tnt"] = pos_tagger

	def startTraining(self, model):
		if model not in self.supportedModels:
			self.logger.debug("unsupported model")
			return
		self.logger.debug("started training")


	def pos(self, stmt):
		text = nltk.word_tokenize(stmt)
		possequence = nltk.pos_tag(text)
		return possequence


