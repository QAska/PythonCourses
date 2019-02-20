print("Python")
print("\tPython")                               #tab

print("Languages:\nPython\nC\nJavaScript")      #line break

print("\nLanguages:\n\tPython\n\tC\n\tJavaScript")

favorite_language = 'python '
print("'" + favorite_language + "'")
print("'" + favorite_language.rstrip() + "'")   #remove right sapce
print("'" + favorite_language + "'")
favorite_language = favorite_language.rstrip()
print("'" + favorite_language + "'")

favorite_language = ' python '
print("'" + favorite_language.rstrip() + "'")
print("'" + favorite_language.lstrip() + "'")
print("'" + favorite_language.strip() + "'")
#most often used to clean user input before saving it in the program