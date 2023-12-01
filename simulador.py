import sys

cache_size = sys.argv[1]
line_size = sys.argv[2]
associativity = sys.argv[3]
file_name = sys.argv[4]

with open("exemplo.txt", mode='r') as file:
  hex_values =  [line.strip()[2:] for line in file]

hex_dict = {'0': '0000',
            '1': '0001', 
            '2': '0010', 
            '3': '0011', 
            '4': '0100', 
            '5': '0101', 
            '6': '0110', 
            '7': '0111', 
            '8': '1000', 
            '9': '1001', 
            'A': '1010', 
            'B': '1011', 
            'C': '1100', 
            'D': '1101', 
            'E': '1110', 
            'F': '1111'}

bin_dict = dict(map(reversed, hex_dict.items()))

def hex_2_bin(hex: str) -> str:
  bin = ''
  for char in hex:
    bin += hex_dict[char]
  return bin

def bin_2_hex(bin: str) -> str:
  hex = ''
  for char in bin: 
    hex += bin_dict[char]
  return hex

bin_values = [hex_2_bin(hex) for hex in hex_values] # gera lista com valores de memória em binário (como string)

class cache(cache_size, line_size, associativity):
  """Summary
  
  Args:
    cache_size (int):
    line_size (int):
    group_size (int):


  Returns:

  """
  no_of_indexes = cache_size / (line_size * associativity)


