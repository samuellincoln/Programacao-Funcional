pathr = "C:\\Users\\samue\\Software\\eclipse-workspace\\PythonDB\\randomfile.txt"
pathw = "C:\\Users\\samue\\Software\\eclipse-workspace\\PythonDB\\randomfileout.txt"
fr = open (pathr, "r")
fw = open (pathw, "w")
l = lambda : [fw.write (line) for line in fr if "programacao" in line]
l ()
fw.close ()
