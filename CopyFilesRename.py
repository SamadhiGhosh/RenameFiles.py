import shutil
import os
import fnmatch
from pathlib import Path

dir_path = "/Users/user/Downloads/Training Pics/Gesicht"
dest_path = "/Users/user/Downloads/My Docs"
count = 0

"""Method 1"""
for file in os.listdir(dir_path):
	# print(file)
	dir_path = os.path.abspath(file)
	dest_path = dest_path + file
	# print(dir_path)
	# print(os.path.isfile(dir_path))
	count += 1
	# print(count)
	if count < 10:
			shutil.copy(dir_path,dest_path)
			print("true")
	# if os.path.isfile(os.path.join(dir_path, file)):
		
		
	# 
	# 	
# 	if os.path.isfile(os.path.join(dir_path, files)):
# 		count += 1


"""Method 2"""
# for root_dir, cur_dir, files in os.walk(dir_path):
	# count += len(files)
	# for file in files:
	# 	count += 1
	# 	print(file)
	# 	source = dir_path + file
	# 	destination = dest_path + file
	# 	if os.path.isfile(source):
			# shutil.copy(source, destination)
			# print("true")

"""Method 3"""
# for files in os.scandir(dir_path):
# 	if files.is_file():
# 		count += 1

"""Method 4"""
# count = len(fnmatch.filter(os.listdir(dir_path),"*.*"))



# print("No of Files found", count)