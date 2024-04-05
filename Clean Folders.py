import os
import shutil  

# path = input("path: ")
# dst = input("dest: ")

path = "e:/dst"
dst = "e:/tar"

rec = 1

# exts = ["jpg", "jpeg", "png", "bpm", "mp3", "mp4", "wmv", "zip", "rm", "pdf", "wma", "tif", "wav", "ico", "gif", "tmp", ]
exts = ["wav"]

def search(m_path: str):
    if m_path == dst:
        return 
    global rec
    ls = os.listdir(m_path)
    for name in ls:
        p = m_path + "/" + name
        if os.path.isdir(p):
            rec += 1
            print(rec)
            search(p)
            rec -= 1
        else:
            if False:
                print(f"rec: {rec}: name: {p}")

            for ext in exts:
                if p.split(".")[-1] == ext:
                    shutil.move(p, dst + "/" + name)
                    break
                else:
                    try:
                        shutil.move(p, dst + "/" + name)
                        pass
                    except :
                        pass
                    continue

search(path)
