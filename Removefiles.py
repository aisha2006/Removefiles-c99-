import os
import shutil
import time

def main():
	path = input("Enter the name of the file or folder: ")
	days = 30
	seconds = time.time() - (days * 24 * 60 * 60)

	if os.path.exists(path):
		for root_folder, folders, files in os.walk(path):
			if seconds >= get_file_or_folder_age(root_folder):
				remove_folder(root_folder)	
				break

			else:
				for folder in folders:
					folder_path = os.path.join(root_folder, folder)
					if seconds >= get_file_or_folder_age(folder_path):	
						remove_folder(folder_path)
				for file in files:
					file_path = os.path.join(root_folder, file)
					if seconds >= get_file_or_folder_age(file_path):
						remove_file(file_path)
						deleted_files_count += 1 

		else:
			if seconds >= get_file_or_folder_age(path):

			
				remove_file(path)
			

	else:
		print(f'"{path}" is not found')

def remove_folder(path):
	shutil.rmtree(path)
	print(f"{path} is removed successfully")

def remove_file(path):
	os.remove(path)
	print(f"{path} is removed successfully")

def get_file_or_folder_age(path):
	# getting ctime of the file/folder
	# time will be in seconds
	ctime = os.stat(path).st_ctime

	# returning the time
	return ctime

if __name__ == '__main__':
	main()