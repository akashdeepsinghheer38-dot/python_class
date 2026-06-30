#---------file handling
#1.le handling in python means reading from and writing to files/folder stored on
# disk using python.
#2. your python code can open a file , pull  out data of it, put data into it and 
#also close it properly .

#------what is file
# files are store of data and information on the specific path of device.

# types of file
#1. text file (.txt,.csv,.json)
#2. binary file (images,video,audio)

# types of file paths.
#1. absolute path : The complete path from the root of the filesystem.
#2. relative path : The path relative to where your current folder (current working dir)

# file mode
#1. a : append ,a+ : append and read
#2. w : write, w+ : write and read
#3. r : read, r+ : read and write
#4. x : strictly create files

# python file handling methods.
#1. open(file_name,mode) : open file
#2. close() : close file.
#3. flush () : memory cleanup.

#4. read() : file read.
#5. readlines() : file read line by line.
#6. write() : writes data in file only take string.

#1. create a file in strict mode.
# try:
 
#     file=open("strict.txt","x")
#     print("file created...")
# except Exception as e:
#     print("error : File nahi ban sakti pehle se hai")

# file=open("write.txt","w")
# file.write("this is python file handling....")
# file.write("this is new line of python file handling....")

# print("file created....")
 
file=open("write.txt","w")
file.write("this is completely python fle handling...")
file.seek(0)
r=file.read(4)
print("File created and written...")
print(f"File content : {r}")

# with open("demo.txt","r") as f:
#     r=f.read()
#     if r.isdigit():
#         print(r)