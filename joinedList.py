def joinedList(n):
    x = [ i for i in range(1,n+1)]
    a = [ i for i in range(1,n+1)]
    a.reverse()
    return x + a

def removePunctuation(s):
  s = list(s)
  for i in range(len(s)):
    if not(ord(s[i]) in range(65,91)) and not((ord(s[i]) in range(97,123))):
      s[i] = ' '
    else:
      continue
  return ''.join(s)
  
s = "She sells seashells, ...., but at home.. (She's afraid of water)"
print(joinedList(10))
print(removePunctuation(s))

