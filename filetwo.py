import fileone

print("Top level in filetwo.py")

fileone.func()

if __name__ == "__main__":
	print("filetwo.py is being executed direclty")
else:
	print("filetwo.py is being imported into another package")