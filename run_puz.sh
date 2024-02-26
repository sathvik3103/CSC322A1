python3 ./src/sudtosat.py <${1} >./tmp/puzzle.cnf
minisat tmp/puzzle.cnf tmp/assign.txt >./results/stat.txt
python3 ./src/sattosud.py <./tmp/assign.txt >./results/solution.txt
