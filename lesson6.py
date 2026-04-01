import os
path = os.path.normpath("D:\lesson6")
os.mkdir(path)
# file = open("file.txt", "r")
# print(file.read())
# file.close()
# file = open("file.txt", "w")
# file.write("Hello world!")
# file.close()
# file = open("file.txt", "a")
# file.write(" Hello user!")
# file.close()
import os
path = "C:\Windows"
for path, dirnames, filenames in os.walk(path):
    print(f"path – {path}")
    print(f"dirnames – {dirnames}")
    print(f"filenames – {filenames}")