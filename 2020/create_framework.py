#!/usr/bin/env python3

import os
import stat


# Create exercise files, add preample and change permissions one file at a time
for i in range(3, 26):
    # Create folder for the lecture
    filepath = "./day%d" % i
    os.mkdir(filepath)
    os.chdir(filepath)
    for j in [1, 2]:
        filename = "day%d_%d.py" % (i, j)     # Create file
        f = open(filename,"w+")
        # Preample
        f.write("#!/usr/bin/env python3\n")
        f.write("# Author: Mathias Rahbek-Borre\n")
        f.write("# Advent of code - day %d part %d:\n" % (i, j))
        f.close()
        # Give tile execute permissions
        st = os.stat("./%s" % filename)
        os.chmod("./%s" % filename, st.st_mode | 0o111 )
    os.chdir("..")
