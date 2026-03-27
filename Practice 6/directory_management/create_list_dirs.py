import os

# текущая папка
print("Текущая директория:", os.getcwd())

# создаём папку
os.mkdir("test_folder")

# создаём вложенные папки
os.makedirs("parent/child/grandchild")

# список файлов и папок
print("Содержимое:", os.listdir())