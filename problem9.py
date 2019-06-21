data = str()

while len(data) < 500:
    temp = input()
    data += temp
    if len(data) > 500:
        data = data[:500]
        break

data = data.lower()

_repeated_chars = {}

for s in data:
  if s in _repeated_chars:
    _repeated_chars[s] += 1
  else:
    _repeated_chars[s] = 1

repeated_chars = []

for key in _repeated_chars:
  if _repeated_chars[key] > 1:
    repeated_chars.append(key)

print("Repeated characters in descending order: ", end='')
print(repeated_chars[::-1])

data = data.split()

_repeated_words = {}

for s in data:
  if s in _repeated_words:
    _repeated_words[s] += 1
  else:
    _repeated_words[s] = 1

repeated_words = []

for key in _repeated_words:
  if _repeated_words[key] > 1:
    repeated_words.append(key)

print("Repeated words in descending order: ", end='')
print(repeated_words[::-1])

for key in _repeated_chars:
  if _repeated_chars[key] > 1:
    repeated_chars.append(key)