def func():
	print(" function running in fileone.py")
	
print("top level print inside fileone.py")

if __name__ == "__main__":
	print("fileone.py is being run directly")
else:
	print("fileone.py is being imported into another module")