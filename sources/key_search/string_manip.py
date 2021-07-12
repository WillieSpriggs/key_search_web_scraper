delimeters = ['.', '!', '?']

def splitParagraphIntoSentences(paragraph: str):
  sentences = [paragraph]
  for delimeter in delimeters:
    sentences = splitSentencesByDelimeter(sentences, delimeter)
  
  return sentences

def splitSentencesByDelimeter(paragraph: list, delimeter: str):
  split_paragraph = []

  for sentence in paragraph:
    split_sentences = sentence.split(delimeter)
    for split_sentence in split_sentences:
      if (split_sentence != ""): 
        split_sentence = trimSpaces(split_sentence)
        if (split_sentence[-1] not in delimeters):
          split_paragraph.append(split_sentence + delimeter)
        else:
          split_paragraph.append(split_sentence)

  return split_paragraph

def trimSpaces(sentence: str):
  if (len(sentence) > 0):
    if (sentence[0] == " "):
      sentence = sentence[1:]

  if (len(sentence) > 0):
    if (sentence[-1] == " "):
      sentence = sentence[:-1]

  return sentence
