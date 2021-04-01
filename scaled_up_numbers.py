from typing import Dict,List
font3x5 = {
    "0": [' ██','█ █','█ █','█ █','██ '],
    "1": [' █ ', '██ ', ' █ ', ' █ ', ' █ '],
    "2": ['██ ','  █',' █ ','█  ','███'],
    "3": ['██ ','  █',' █ ','  █','██ '],
    "4": ['█ █','█ █','███','  █','  █'],
    "5": ['███','█  ','██ ','  █','██ '],
    "6": [' ██','█  ','███','█ █','███'],
    "7": ['███','  █',' █ ','█  ','█  '],
    "8": ['███','█ █','███','█ █','███'],
    "9": ['███','█ █','███','  █','██ '],
    ",": ['   ','   ','   ',' █ ','█  '],
    ".": ['   ','   ','   ','   ',' █ '],
    "%": ['█  ','  █',' █ ','█  ','  █'],
}
emptyBlock='　'

def scaled_up_number(number:str,font:Dict[str,List[str]]=font3x5,leadingPad:int=4)->str:
  ret = ''
  for line in range(len(font['0'])):
    ret+=(leadingPad-1)*emptyBlock
    for char in number:
      ret+=emptyBlock+font3x5[char][line]
    ret+='\n'
  return ret

print(scaled_up_number('2,310.456789%'))
 
