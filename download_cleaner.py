
import os
user = os.getenv("USER") #Takes the value of the systems user variable

def check_directory(directory_name):
	if os.path.exists(directory_name): #Checks if the directory exist
		print(f"{directory_name} \N{HEAVY CHECK MARK}")
	else:
		os.mkdir(directory_name) #Creates the directory
		print(f"Creating {directory_name} Directory")



def item_destination(file,file_extention, directory):
	if file.endswith(file_extention): #Checks the extention of the file
		os.system(f"mv {file} {directory}")
		print(f"Moved {item} to {directory}") #Moves the file accordingly


print(f"""

---------------------------------------------------------------------------
				       					  |
				       					  |
The working Directory is{os.getcwd()} 					  |
                                      					  |
                                      					  |
--------------------------------------------------------------------------
 """)
change_directory = os.chdir(f'/home/{user}/Downloads') 
download_items = os.listdir() #Like ls in linux list the items

print("\n=============================================")

check_directory("ISO")
check_directory("EXE")

print("==================================================")

for item in download_items:
	item_destination(item,'.iso', 'ISO')
	item_destination(item,'.png', '~/Pictures')
	item_destination(item,'.jpg', '~/Pictures')
	item_destination(item,'.txt', '~/Documents')
	item_destination(item,'.pdf', '~/Documents')
	item_destination(item,'.mp3', '~/Music')
	item_destination(item,'.mkv', 'Videos')
	item_destination(item,'.mp4', 'Videos')
	item_destination(item, '.sh', 'EXE')
	item_destination(item,'.py', 'EXE')
	item_destination(item,'.AppImage', 'EXE')




