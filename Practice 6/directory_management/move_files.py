import shutil
import os

# создадим файл
with open("example.txt", "w") as f:
    f.write("Hello!")

# копирование
shutil.copy("example.txt", "copy_example.txt")

# перемещение
shutil.move("copy_example.txt", "test_folder/copy_example.txt")

# удаление
os.remove("example.txt")