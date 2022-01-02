#/bin/python3
import os
def filter():
	filePath = input("Enter file to filter path: ")
	outPut = input("Enter output path: ")
	realFilePath = os.path.realpath(filePath)
	realOutputPath = os.path.realpath(outPut)
	
	with open(realFilePath, "rb") as f:
		reader = f.read().decode("utf-8") 
		splitter = reader.split(" ")
	for word in splitter:
		if word.startswith("http"):
			with open(realOutputPath, "a") as f:
				f.write(word+"\n")
	print(f"File save in {realOutputPath}")
filter()
		
