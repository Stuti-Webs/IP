# Run this file from inside the IP folder; it creates its text files there.

# Q1 Writing to a file
f = open("sample.txt", "w")
f.write("Hello, this is line one.\n")
f.write("Python makes file handling easy.\n")
f.write("This is line three.\n")
f.close()                                # always close a manually opened file

# Q2 Reading the entire file
f = open("sample.txt", "r")
print(f.read())
f.close()

# Q3 Reading line by line
f = open("sample.txt")
print("readline:", f.readline().strip())
f.close()
for line in open("sample.txt"):
    print("loop:", line.strip())

# Q4 with statement (closes the file automatically, even if an error happens)
with open("sample.txt", "w") as f:
    f.write("Line one\nLine two\nLine three\n")
with open("sample.txt") as f:
    print(f.read())

# Q5 Append mode
with open("sample.txt", "a") as f:
    f.write("Line four (appended)\n")
with open("sample.txt") as f:
    print(f.read())                      # old lines are still there

# Q6 Count lines, words, characters
with open("sample.txt") as f:
    content = f.read()
print("Lines:", len(content.splitlines()))
print("Words:", len(content.split()))
print("Characters:", len(content))

# Q7 Search a word
word = input("Word to search: ")
print(f"'{word}' appears {content.lower().count(word.lower())} time(s)")

# Q8 Copy a file
with open("sample.txt") as src, open("copy.txt", "w") as dst:
    dst.write(src.read())
with open("copy.txt") as f:
    print("Copy:", f.read())

# Q9 Filter lines by keyword
with open("sample.txt") as src, open("filtered.txt", "w") as dst:
    for line in src:
        if "Line" in line:
            dst.write(line)
print(open("filtered.txt").read())

# Q10 Student record file system
with open("students.txt", "w") as f:
    f.write("101,Asha,85\n102,Ravi,78\n103,Meena,92\n")
print(f"{'Roll':<6}{'Name':<10}{'Marks'}")
with open("students.txt") as f:
    for line in f:
        roll, name, marks = line.strip().split(",")
        print(f"{roll:<6}{name:<10}{marks}")

# Q11 File exceptions
try:
    with open("missing_file.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("Sorry, that file does not exist.")

# Q12 Update file content
with open("sample.txt") as f:
    text = f.read()
text = text.replace("Line", "Row")
with open("sample.txt", "w") as f:
    f.write(text)
print(open("sample.txt").read())