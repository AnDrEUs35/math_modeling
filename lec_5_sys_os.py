import sys, os

print(os.getcwd())

os.system("echo hi!")

#os.system('python3 lec_5_sys_os.py')

print('python version is:', sys.version)
print(sys.path)
print(sys.platform)

print(dir(sys)) # функции любого объекта
print(dir(os))
