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