phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

panic1 = ''.join(plist[1:3])
panic2 = ''.join(plist[5])
panic3 = ''.join(plist[4])
panic4 = ''.join(plist[-5:-7:-1])

new_phrase = panic1 + panic2 + panic3 + panic4

#new_phrase = ''.join(plist[1:3])
#new_phrase = new_phrase + ''.join([plist[5], plist[4], plist[7], plist[6]])

print(plist)
print(new_phrase)