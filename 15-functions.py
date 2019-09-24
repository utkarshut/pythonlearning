def student(*args, **kwargs):
    print(args)
    print(kwargs)


student('math', 'john', name='john', age='20')

info = ['math', 'john']
detail = {'name': 'john', 'age': 23}

student(info, detail)

student(*info, **detail)
