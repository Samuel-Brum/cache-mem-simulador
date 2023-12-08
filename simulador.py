import sys
import math

cache_size = sys.argv[1]
line_size = sys.argv[2]
associativity = sys.argv[3]
file_name = sys.argv[4]

with open(file_name, mode='r') as file:
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

bin_dict = dict(map(reversed, hex_dict.items())) # dicionário invertido

def hex_2_bin(hex: str) -> str:
  """Converte de hexadecimal para binário
  
  Args:
    hex (str): string contendo número hexadecimal
  Returns:
    string contendo número binário
  """

  bin = ''
  for char in hex:
    bin += hex_dict[char]
  return bin

def bin_2_hex(bin: str) -> str:
  """Converte de binário para hexadecimal

  Args:
    bin (str): string contendo número binário
  Returns:
    string contendo número hexadecimal
  """

  hex = ''
  separated = [(bin[i:i+4]) for i in range(0, len(bin), 4)] # separa grupos de 4 bits do endereço binário
  for four_bits in separated: 
    hex += bin_dict[four_bits]
  return hex

bin_values = [hex_2_bin(hex) for hex in hex_values] # gera lista com valores de memória em binário (como string)

offset = math.ceil(math.log2(line_size))

bin_offset = [bin[:len(bin) - offset].rjust(32, '0') for bin in bin_values] # remove offset do cache

hex_offset = ["0x" + bin_2_hex(bin) for bin in bin_offset] # converte de volta para hexadecimal (como string)

class Cache:
  def __init__(self, cache_size, line_size, associativity):
    self.no_of_indexes = cache_size / (line_size * associativity)
    self.index = {k:v for (k, v) in zip([str(i).rjust(3, '0') for i in range(self.no_of_indexes)], [[0, ''] for i in range(self.no_of_indexes)])} # serve como banco de memória da cache
    self.hits = 0
    self.misses = 0

  def search(self, address: str) -> int:
    if address in self.index.values():
      self.hits += 1
    else:
      self.misses += 1






