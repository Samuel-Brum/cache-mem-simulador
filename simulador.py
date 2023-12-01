import sys

cache_size = sys.argv[1]
line_size = sys.argv[2]
associativity = sys.argv[3]
file_name = sys.argv[4]

class cache(cache_size, line_size, associativity):
  """Summary
  
  Args:
    cache_size (int):
    line_size (int):
    group_size (int):


  Returns:

  """
  index_size = cache_size / (line_size * associativity)

with open("exemplo.txt", mode='r') as file:
  hex_values =  [line.strip()[2:] for line in file]

def hex_2_bin(hex: str) -> str:
  bin = ''
  for char in hex:
    bin += hex_dict[char]
  return bin

bin_values = [hex_2_bin(hex) for hex in hex_values]
