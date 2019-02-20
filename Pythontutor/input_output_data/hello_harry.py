"""
Напишите программу, которая приветствует пользователя, выводя слово Hello, введенное имя и знаки препинания по образцу.

name = input()
print("Hello, " + name.title() + "!")
"""

def hello(name):
    return "Hello, " + name.title() + "!"

def test_hello_1():
    assert hello('Harry') == "Hello, Harry!"

def test_hello_2():
    assert hello('Mr. Potter') == "Hello, Mr. Potter!"

def test_hello_3():
    assert hello('Lord Voldemort') == "Hello, Lord Voldemort!"