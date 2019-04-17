# Find all file with given suffix in a given path
import os
from collections import deque

def dir_by_file(suffix: str, path = "./") -> list:
    """
    os.chdir()
    os.listdir()
    os.path.isdir()
    os.path.splitext()
    os.path.abspath()
    """
    path = str(path.replace("\\", "/"))
    if suffix[0] != '.':
        suffix = "." + suffix
    try:
        os.chdir(path)
    except:
        assert("UNKNOWN ERROR")
    dq1 = deque([d for d in os.listdir(path) if os.path.isdir(d) or os.path.splitext(d)[1] == suffix])
    if ".git" in dq1:
        dq1.remove(".git")
    dq2 = []
    while len(dq1) != 0:
        ele = dq1.popleft()
        if ele == []:
            continue
        if os.path.isdir(os.path.abspath(ele)):
            dbf_ele = dir_by_file(suffix, os.path.abspath(ele))
            dq1.extend(dbf_ele)
            os.chdir(path)
        else:
            dq2.append(os.path.abspath(ele))
    return dq2

if __name__ == "__main__":
    print(os.getcwd())
    mdl = dir_by_file(".md", os.getcwd())
    print(mdl)

# os.path.abspath() 的陷阱 !!!
# 并不是直接返回绝对路径, 而是当前路径+文件(夹)名
