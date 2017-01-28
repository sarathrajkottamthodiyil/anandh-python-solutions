def filereverse(filename):
	f = open(filename).read()

	print f[::-1]


filereverse('task.txt')

