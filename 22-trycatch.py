try:
    f = open('xyz.txt')
    var = bad_var
    pass
except FileNotFoundError:
    print('file not exsist')
except Exception as e:
    print('something wrong')
    print(e)
    pass
else:
    print(f.read())
    f.close()
    pass
finally:
    print('finally::::')
    pass
