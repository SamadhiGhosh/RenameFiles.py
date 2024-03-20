
import os

directory = "/Users/user/Downloads/Darjeeling-Siliguri M Corp"
files = sorted(os.listdir(directory))
print(f"Total files: {len(files)}")
print(files)

i = 1

for file in files:
	if file.endswith('.xls'):
		print(file)
		src = os.path.join(directory, file)  # Full path of the source file
		dst = os.path.join(directory, f"RCCount_Beneficiary_{i}.xls")  # Full path of the destination file
		
		os.rename(src, dst)
		i += 1

