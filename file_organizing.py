import os
import shutil

src = os.getcwd()
files = os.listdir(src)

# does not work for problems of year before 2000
for file in files:
    if file.startswith("CCC"):
        year = int(file.split("'")[1].split()[0])
        if year >= 95:
            continue
        year += 2000
        dest = os.path.join(src, str(year))
        if not os.path.exists(dest):
            os.makedirs(dest)
        shutil.move(os.path.join(src, file), dest)
        print(f"Successfully moved file: {file}")
