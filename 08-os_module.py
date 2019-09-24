import os

print(dir(os))

print(os.getcwd())  # current working direc

# os.chdir('/Users/utkarsh/PycharmProjects/')

print(os.getcwd())

print(os.listdir())

# os.mkdir('folder name')
# os.makedirs('folder name/sub directory')
# os.removedirs('folder name/sub directory')
# os.removedirs('folder name')

# os.rename('ifelse.py','ifelseloop.py')
print(os.listdir())

print(os.stat('ifelseloop.py'))

from datetime import datetime

print(datetime.fromtimestamp(os.stat('ifelseloop.py').st_mtime))

# for dirpath, dirnames, filenames in os.walk('/Users/utkarsh/PycharmProjects/'):  #topdown
#     print("dirpath :" , dirpath)
#     print("dirnames :" , dirnames)
#     print("filenames :" , dirnames)
#     print()

print(os.environ.get('HOME'))
file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path)

# learn with open method

print(os.path.basename('tmp/text.txt'))
print(os.path.dirname('tmp/text.txt'))
print(os.path.split('tmp/text.txt'))
print(os.path.exists('tmp/text.txt'))
print(os.path.isdir('tmp/text.txt'))
print(os.path.isfile('tmp/text.txt'))
print(os.path.splitext('tmp/text.txt'))
print(dir(os.path))
