#!/usr/bin/env python3

class MyString:
  #initialize the class
  def __init__(self, value = ''):
    self.value = value

  #Define properties
  @property
  def value(self):
    return self._value

  @value.setter
  def value(self, value):
    if not isinstance (value, str):
      print("The value must be a string.")
    else:
      self._value = value

#Define Methods:
  def is_sentence(self):
    if self.value.endswith('.'):
      return True
    else:
      return False
    
  def is_question(self):
    if self.value.endswith ("?"):
      return True
    else:
      return False
  def is_exclamation(self):
    if self.value.endswith("!"):
      return True
    else:
      return False
    
  def count_sentences(self):
    #replace all question marks and exclamation marks with periods
    sentences = self.value.replace("?",".").replace("!",".").split(".") #split on periods
    #return the number of non-empty sentences in the list.
    return len([sentence for sentence in sentences if sentence.strip()])
  
result = MyString()
result.value = "This is a string! It has three sentences. Right?"
print(result.count_sentences())