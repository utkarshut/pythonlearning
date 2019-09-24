with open('35-sample.txt', 'w') as f:
    f.write(
        '"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure rep')

#context manager using class
class Open_file():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        pass

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with Open_file('35-sample.txt', 'w') as f:
    f.write('testing')
print(f.closed)

#context manager using function

from contextlib import contextmanager

@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)
        yield f
    finally:
        f.close()

with open_file('35-sample.txt', 'w') as f:
    f.write('testin ddg')


import os

@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield    # ready to do in that operation
    finally:
        os.chdir(cwd)

with change_dir('35-context-manager'):
    print(os.listdir())
