import sys
fh = open(sys.argv[1],"r")
fe = open("upper","w")
line = fh.readline().strip()
while line:
  if line.isupper():
   fe.write(line + '\n')
  if line.isnumeric():
   print("Número: " + str(line))
  line = fh.readline().strip()
fh.close()
fe.close()
