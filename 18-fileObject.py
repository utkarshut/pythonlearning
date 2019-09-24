f = open('filereadsample.txt','r')   #r read w write a append r+ read write

print(f.name)

print(f.mode)

f.close()


with open('filereadsample.txt','r')  as f: # dont neeed to clse file with context manager
    # fcontetnt=f.read()
    # fcontentline=f.readline()
    # print(fcontentline,end='')
    # print(fcontetnt,end='')
    for line in f:
        print(line, end='')


with open('filereadsample.txt','r')  as f:  # no memory issue
    size_to_read=10
    f_content =f.read(size_to_read)
    while len(f_content)>0:
        print(f_content,end='')
        f_content=f.read(size_to_read)

# f.tell() tell the current index position  in file
#f.seek(index) set the position in file

with open('test.txt','w') as f:
    f.write('ut')

with open('filereadsample.txt','r')  as rf:
    with open('test.txt','w') as wf:
        for line in rf:
            wf.write(line)

# for copying images
#
# with open('a.jpg','rb')  as rf:
#     with open('b.jpg','wb') as wf:
#         for line in rf:
#             wf.write(line)

# copying images with chunk data for memory optimixe
# with open('a.jpg','rb')  as rf:
#     with open('b.jpg','wb') as wf:
#         chunksize=4096
#         rfcontent =rf.read(chunksize)
#         while leng(rfcontent)>0:
#             wf.write(rfcontent)
#             rfcontent =rf.read(chunksize)
