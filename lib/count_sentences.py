#!/usr/bin/env python3

class MyString:
  def __init__(self, value = ''):
    self.value = value

  @property
  def value(self):
    return self._value

  @value.setter
  def value(self, value):
    if not isinstance (value, str):
      print("The value must be a string.")
    else:
      self._value = value

  def is_sentence(self):
    if self.value.endswith('.'):
      return True
    else:
      return False