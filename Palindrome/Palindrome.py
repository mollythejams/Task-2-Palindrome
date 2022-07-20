def isPalindrome(InputString,TrashSymbolString):
  head=0
  tail=len(InputString)-1
  while(head <= tail):
    while(InputString[head] in TrashSymbolString):
      head+=1  
    while(InputString[tail] in TrashSymbolString):
      tail-=1
    if InputString[head] != InputString[tail]:
      return False
    head += 1
    tail-=1
  return True

print(isPalindrome("r@@.ac.>e!!!!car", '[}.>!!@%'))