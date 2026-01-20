words = "hello hi 12 12hi"
lists = list(words)
for char in lists[:]:
    if char == ' ':
        lists.remove(char)

print(lists)