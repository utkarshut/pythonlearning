import subprocess

#subprocess.run('ls -la',shell=True)
p1 = subprocess.run(['ls', '-la'],capture_output=True, text=True)

print(p1.args)

print(p1.returncode)  # o ->no error

#print(p1.stdout.decode())

print(p1.stdout)


# in other file

with open('45-output.txt', 'w') as f:
    p1 = subprocess.run(['ls', '-la'],stdout=f,text=True)


# cat command on text.txt file to print content of other