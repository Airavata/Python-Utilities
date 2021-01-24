import os  
filenames  = os.listdir(".")
for filename in filenames:
    meta_filename = os.path.splitext(filename)
    if meta_filename[1] != ".py":
        try:
            os.rename(filename,meta_filename[0]+'.jpg')
        except OSError as e:
            print("Renaming failed for file "+filename)
            continue