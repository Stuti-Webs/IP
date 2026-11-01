s = "Python Programming"

# Q1 Creation and indexing
print(s[0], s[-1], s[len(s) // 2])

# Q2 Slicing
print(s[:5], s[-4:], s[2:7])             # [start:end] -> end is not included

# Q3 Slicing with step
print(s[::2], s[::-1])                   # every 2nd char; reversed

# Q4 Immutability
try:
    s[0] = "J"
except TypeError as e:
    print("Error:", e)
s2 = "J" + s[1:]                         # build a new string instead
print(s2)

# Q5 in / not in
print("Prog" in s, "Java" not in s)
print("Substring found" if "gram" in s else "Not found")

# Q6 find() vs index()
print(s.find("gram"), s.find("xyz"))      # find returns -1 if missing
try:
    print(s.index("xyz"))
except ValueError as e:
    print("index() error:", e)            # index raises an error if missing

# Q7 Counting
print(s.count("o"), s.count("Pro"))

# Q8 Case conversion
print(s.upper(), s.lower(), s.title(), sep="\n")

# Q9 strip, replace, f-string
raw = "   hello world   "
print(f"[{raw.strip()}]")
print(raw.strip().replace("world", "Python"))
name, lang = "Stuti", "Python"
print(f"{name} is learning {lang}")

# Q10 split and join
sentence = "learning python is fun"
parts = sentence.split()
print(parts)
print("-".join(parts))

# Q11 Palindrome checker
word = input("Enter a word: ").lower()
print("Palindrome" if word == word[::-1] else "Not a palindrome")

# Q12 Text analyzer
text = input("Enter a paragraph: ").lower()
words = text.split()
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
print("Word count:", len(words))
print("Character count:", len(text))
print("Most frequent word:", max(freq, key=freq.get))