import os
os.chdir('c:/Users/ERARAM SAI TEJA GOUD/OneDrive/Desktop/Python Class practice/class work/work_file')
if not os.path.exists('sample_folder'):
    os.mkdir('Sample_folder')
filepath=os.path.join('sample_folder','sample.txt')
with open (filepath,'w+') as f:
    f.write("Welcome to python world coders!!!")
    f.seek(0)
    print(f.read())
    f.seek(0)
    print(f.readlines())
    f.seek(0)
    print(f.readline())

print(os.path.getsize(filepath))
print(os.path.abspath(filepath))
