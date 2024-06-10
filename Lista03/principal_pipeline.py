import os

#Letra a)
dir_lib = "." + os.sep + "lib"
cmd = r"python " + dir_lib + os.sep + "tes_a.py -i " + "." + os.sep + "genoma.fasta"
os.system(cmd)

#letra b)
cmd = r"python " + dir_lib + os.sep + "tes_b.py -i " +  "genoma.fasta"
os.system(cmd)

#letra c)
cmd = r"python " + dir_lib + os.sep + "tes_c.py -i " + "." + os.sep + "genoma.fasta"
os.system(cmd)

#letra d)
cmd = r"python " +dir_lib + os.sep + "d.py -i " + "." + os.sep + "genoma.fasta"
os.system(cmd)

#letra e)
cmd = r"python " +dir_lib + os.sep + "e.py -i " + "." + os.sep + "genoma.fasta"
os.system(cmd)
