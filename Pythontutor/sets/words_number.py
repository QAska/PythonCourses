"""
Дан текст: в первой строке записано число строк, далее идут сами строки.
Определите, сколько различных слов содержится в этом тексте.

Словом считается последовательность непробельных символов идущих подряд,
слова разделены одним или большим числом пробелов или символами конца строки.
"""

n = int(input())
A = []
for i in range(n):
    for element in input().split():
        A.append(element)
print(len(set(A)))


# variant_1:
words = set()
for _ in range(int(input())):
    words.update(input().split())
print(len(words))