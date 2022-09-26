from ast import Or


print("Enter a word")
word = input()

len = len(word)
i = 0
v = 0
c = 0

while(i < len):
    if word[i] == "A" or word[i] == 'e' or word[i] == 'i' or word[i] == 'o' or word[i] == 'u' or word[i] == 'y' or word[i] == 'A' or word[i] == 'E' or word[i] == 'I' or word[i] == 'O' or word[i] == 'U' or word[i] == 'Y':
        v  = v + 1
    else:
        c = c + 1
    i = i + 1

print("Word length is " + str(len) + ". Word has " + str(v) + " vowels and " + str(c) + " consonants.")

