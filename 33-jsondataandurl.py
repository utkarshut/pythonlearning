import  json

#Performs the following translations in decoding by default:

#JSON  =>  Python

# object => dict
#
# array  =>  list
#
# string => str
#
# number (int) =>int
#
# number (real) =>float
#
# true  => True
#
# false => False
#
# null =>  None




people_string = '''
{
"people":[
{"name":"john","phone":1234, "email":"asdsad.cdd"},
{"name":"johnds","phone":123234, "email":"asdsadvdfv.cdd"}
]
}
'''

data = json.loads(people_string)


print(type(data))

print(data)

for person in data['people']:
    del person['phone']
    print(person)

new_string = json.dumps(data, indent=2, sort_keys=True)

print(new_string)


with open('33-jsondata.json') as f:
    data = json.load(f)

for state in data['states']:
    del state['code']
    print(state['name'], state['dial_code'])

with open('33-new_states.json', 'w') as f:
    json.dump(data, f, indent=2)


from urllib.request import  urlopen

with urlopen("http://ergast.com/api/f1/2004/1/results.json?format=json") as response:
    source = response.read()


data = json.loads(source)

print(json.dumps(data, indent=2))
