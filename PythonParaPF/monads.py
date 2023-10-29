import os
filepath = lambda folderpath, filename : ((folderpath + "\\") if folderpath != "" else "") + filename 
filelines = lambda folderpath, filename : [open (filepath (folderpath, filename)).readline()]

maybe_filelines = lambda f, fpath, fname : f (fpath, fname) if fname in os.listdir (fpath) else None

print (maybe_filelines (filelines, "C:\\Users\\samue\\Software\\eclipse-workspace\\PythonDB\\", "randomfile.txt"))
