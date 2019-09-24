import os

print(os.getcwd())

for f in os.listdir():
    # print(f)
    # print(os.path.splitext(f))
    filename, fileext = os.path.splitext(f)
    # print(filename.split('_'))
    if fileext == '.py':
        filename, num = filename.rsplit('_', 1)
        num = num.strip().zfill(2)
        newname = '{}-{}{}'.format(num, filename, fileext)
        os.rename(f, newname)
        print('{}-{}{}'.format(num, filename, fileext))
