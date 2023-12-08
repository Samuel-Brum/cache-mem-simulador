import sys
import math

cache_size = int(sys.argv[1])
line_size = int(sys.argv[2])
associativity = int(sys.argv[3])
file_name = sys.argv[4]

class Cache:
  def __init__(self, cache_size, line_size, associativity):
    self.no_of_indexes = cache_size // line_size
    self.associativity = associativity
    self.no_of_groups = self.no_of_indexes // associativity
    
    self.index = dict() # serve como banco de memória da cache
    for i in range(self.no_of_indexes):
      self.index[i] = [0, ''] 

    self.hits = 0
    self.misses = 0
    
    # Dicionário das filas de acesso de cada conjunto, indexado pelo endereço inicial de cada conjunto
    self.group_queues: dict[int, list] = dict()
    for i in range(self.no_of_groups):
      self.group_queues[i * associativity] = []

  def search(self, address: str) -> int: 
    address_dec = int(address, 16)
    group_address = (address_dec % self.no_of_groups) * associativity

    found = False
    for i in range(group_address, group_address + self.associativity): # Para cada indice do grupo
      if self.index[i][1] == address: # Encontrou o endereço dentro da memória
        self.hits += 1
                
        self.group_queues[group_address].remove(i % associativity)
        self.group_queues[group_address].append(i % associativity)
        found = True
        break
        
    if not found:
      self.misses += 1
      if len(self.group_queues[group_address]) == associativity: # Caso não tenha espaço livre substitui o último
        index_to_replace = self.group_queues[group_address].pop(0)
        self.index[group_address + index_to_replace][0] = 1
        self.index[group_address + index_to_replace][1] = address
        self.group_queues[group_address].append(index_to_replace)
      else:                                                      # Se tiver espaço livre, usa ele
        index_to_insert = len(self.group_queues[group_address])
        self.index[group_address + index_to_insert][0] = 1
        self.index[group_address + index_to_insert][1] = address
        self.group_queues[group_address].append(index_to_insert)

  def print(self):
    output = ""
    output += "================\n"
    output += "IDX V ** ADDR **\n"
    for block_address in range(self.no_of_indexes):
      valid, memory_address = self.index[block_address]
      output += f"{str(block_address).rjust(3, '0')} {valid}"
      output += f" {memory_address}\n" if valid == 1 else "\n"
    return output

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

offset = math.ceil(math.log2(line_size)) # Desloca o número de bits necessário para representar o endereço dentro da linha

bin_offset = [bin[:len(bin) - offset].rjust(32, '0') for bin in bin_values] # remove offset do cache

hex_offset = ["0x" + bin_2_hex(bin) for bin in bin_offset] # converte de volta para hexadecimal (como string)

cache = Cache(cache_size, line_size, associativity) # inicializa cache

with open("output.txt", mode='w') as file:
  for address in hex_offset:
    cache.search(address)
    file.write(cache.print())
      
  file.write(f"\n#hits: {cache.hits}\n")
  file.write(f"#miss: {cache.misses}\n")

    







