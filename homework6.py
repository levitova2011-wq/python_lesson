import os
# a = ""
# b = ""
# c = ""
# d = ""
# e = ""
# f = ""
# g = ""
# h = ""
# i = ""
# j = ""
# k = ""
# print("Enter the path:\n")
# a = input("Only name: ")
# print("If you have printed all path, tap Enter")
# b = input("Only name: ")
# if b != "":
#     c = input("Only name: ")
#     if c != "":
#         d = input("Only name: ")
#         if d != "":
#             e = input("Only name: ")
#             if e != "":
#                 f = input("Only name: ")
#                 if f != "":
#                     g = input("Only name: ")
#                     if g != "":
#                         h = input("Only name: ")
#                         if h != "":
#                             i = input("Only name: ")
#                             if i != "":
#                                 j = input("Only name: ")
#                                 if j != "":
#                                     k = input("Only name: ")
# path = f"{a}:\{b}\{c}\{d}\{e}\{f}\{g}\{h}\{i}\{j}\{k}"
# for path, dirnames, filenames in os.walk(path):
#     print(f"path – {path}")
#     print(f"dirnames – {dirnames}")
#     print(f"filenames – {filenames}")
#
# path = os.path.normpath("D:\\Dir_1")
# os.mkdir(path)
# path = os.path.normpath("D:\\Dir_1\\file_1")
# os.mkdir(path)
# path = os.path.normpath("D:\\Dir_1\\Dir_2")
# os.mkdir(path)
# path = os.path.normpath("D:\\Dir_1\\Dir_3")
# os.mkdir(path)
# path = os.path.normpath("D:\\Dir_1\\Dir_2\\file_2")
# os.mkdir(path)
# path = os.path.normpath("D:\\Dir_1\\Dir_2\\file_3")
# os.mkdir(path)
# path = os.path.normpath("D:\\Dir_1\\Dir_3\\file_4")
# os.mkdir(path)

name_of_file = input("Enter the name of this file: ")
text = input("Enter the text: ")
file = open(f"{name_of_file}.txt", "w")
file.write(text)
file.close()