import math

eightEighths='█'
eighths={
  7:'▉',
  6:'▊',
  5:'▋',
  4:'▌',
  3:'▍',
  2:'▎',
  1:'▏',
}
empty=' '

def mkbar(len,eighths=eighths,eightEights=eightEighths,empty=empty):
  ret=''
  rounded=round(len*8) / 8
  ret=eightEighths*math.floor(rounded)
  ret+=eighths[(rounded-math.floor(rounded))*8]
  return ret

print(mkbar(6.34))
print(mkbar(3.45))
print(mkbar(7.93))
