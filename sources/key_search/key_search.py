from . import string_manip as manip

def keySearch(paragraphs: list, keywords: list, num_supporting: int):
  sentences = []
  for paragraph in paragraphs:
    sentences.extend(manip.splitParagraphIntoSentences(paragraph))

  return findKeySentences(sentences, keywords, num_supporting)

def findKeySentences(sentences: list, keywords: list, num_supporting: int):
  key_sentences = {}
  
  for i in range(len(sentences)):
    if any(key.lower() in sentences[i].lower() for key in keywords):
      for j in range(i-num_supporting, i+num_supporting+1):
        if ((j >= 0) and (j < len(sentences)) and (j not in key_sentences)):
          key_sentences[j] = sentences[j]

  return list(key_sentences.values())
