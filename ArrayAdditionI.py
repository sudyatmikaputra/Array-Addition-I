def combination(numlist):
  if len(numlist) == 0:
    return [[]]
  comb = []
  for c in combination(numlist[1:]):
    comb += [c, c+[numlist[0]]]
  return comb

def ArrayAdditionI(arr):
  cond = False
  maxval = max(arr)
  arr.remove(maxval)
  newarr = arr
  
  combin = combination(newarr)
  for i in range(len(combin)):
    res = sum(combin[i])
    if res == maxval :
      cond = True

  return cond

# keep this function call here 
print(ArrayAdditionI(input()))