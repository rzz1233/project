# 二、封装一个函数，把一个文件中的内容，复制到另外一个文件中

def copy_file(copy_file,w_file):
    with open(copy_file, "r", encoding="utf-8") as f:
        str = f.read()

    with open(w_file, "w", encoding="utf-8") as f:
        f.write(str)



copy_file("demo.txt", "demo1.txt")