def decodeSubString(s, start):
  res = []

  def extract_number():
      digits = []
      while res and '0' <= res[-1] <= '9':
          digits.append(res.pop())
      
      return int(''.join(reversed(digits)))

  i = start
  while i < len(s):
      if s[i] == '[':
          sub_str, end = decodeSubString(s, i+1)
          for _ in range(extract_number()):
              res.extend(sub_str)
          i = end + 1
          continue
      if s[i] == ']':
          return res, i
      else:
          res.append(s[i])
          i += 1

  return res, len(s)


def decodeString(s):
   return ''.join(decodeSubString(s, 0)[0])

print decodeString('2[a2[b]c]')
# abbcabbc
