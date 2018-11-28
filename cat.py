import sys

if len(sys.argv) != 2:
  sys.stderr.write('to run with one arguments\n')
  exit()
try:
  fh = open(sys.argv[1],"r")
except FileNotFoundError:
  sys.stderr.write(sys.argv[1] + ' not exists \n')
  exit()
fe = open("upper","w")
line = fh.readline().strip()
while line:
  if line.isupper():
   fe.write(line + '\n')
  print(line + '(no numérico)'
  if line.isnumeric():
   print("Número: " + str(line) + '(numérico)')
  line = fh.readline().strip()
print('solo se admiten numeros')
fh.close()
fe.close()
