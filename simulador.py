import sys

cache_size = sys.argv[1]
line_size = sys.argv[2]
group_size = sys.argv[3]
file_name = sys.argv[4]

class cache(cache_size, line_size, group_size):
  """Summary
  
  Args:
    cache_size (int):
    line_size (int):
    group_size (int):


  Returns:

  """


with open(file_name, mode='r'):
  hex_values = []


