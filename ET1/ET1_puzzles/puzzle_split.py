import fileinput
from pprint import pp



puzzles = []

for line in fileinput.input():
    cur_puz = line
    puzzles.append(cur_puz)
    
    
pp(puzzles)

for i,puz in enumerate(puzzles):
    f = open("ET1puzzle"+str(i+1)+".txt", "a")
    f.write(puz)
    f.close()
