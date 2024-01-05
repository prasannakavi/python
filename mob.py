import re
mob='+91-98736656873'
data=re.findall('\+91-[4789][0-9]{9}',mob)
print(data)
