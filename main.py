def easy_unpack(elements: list) -> list:
  """
        returns a tuple with 3 elements - first, third and second to the last
  """
  i = [0, 2, -2]
  elements = [elements[x] for x in i]

  return elements

if __name__ == '__main__':

  assert easy_unpack([1, 2, 3, 4, 5, 6, 7, 9]) == [1, 3, 7]
  assert easy_unpack([1, 1, 1, 1]) == [1, 1, 1]
  assert easy_unpack([6, 3, 7]) == [6, 7, 3]
  print('Done! Go Check!')