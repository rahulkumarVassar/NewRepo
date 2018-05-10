import csv

List=[]
#Added new line abcd
def read(f_name):
	with open(f_name,'r') as csvfile:
		red = csv.DictReader(csvfile)
		for row in red:
			List.append(dict(row))
			print(dict(row))
read('test.csv')
#added another line
print("\n")
print(List[6])
print(List[6]['ID'])


