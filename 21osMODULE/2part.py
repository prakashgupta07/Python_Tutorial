import os
import shutil
os.chdir(r'D:\\')
# print(os.listdir())
fileiter=os.walk(r'D:\\')
# for current_path,folder_name,file_name in fileiter:
        # print(f'current path :{current_path}')
        # print(f'file_name :{file_name}')
        # print(f'folder_name :{folder_name}')
# os.rmdir('prakash')# remove empty folder
# os.mkdir('prakash')# make single folder
# os.makedirs('prakash/movie')#made folder inside folder
# os.removedirs('prakash/movie')#delete folder inside folder(all)

# shutil.rmtree('prakash')# it delete non-empty folder
#note:- it detete permanently

### file copy
# shutil.copy('new','excel/new')
###copy folder
# shutil.copytree('pra','excel/pra1')

## move file,folder
# shutil.move('file.txt','excel/file1.txt')
# shutil.move('pra','excel/pra1')
