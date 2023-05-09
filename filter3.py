import os

path = "C:\\Users\\Akash\\OneDrive\\Desktop\\text"
subdirs = [os.path.join(path, name) for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
for subdir in subdirs:
    print(subdir,":",len(os.listdir(subdir)))
