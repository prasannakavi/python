import re
email='harikagadi@gmail.com'
data=re.findall('[a-zA-Z]+[a-zA-Z0-9]*\@gmail\.com','email')
print(data)