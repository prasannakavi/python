import re
with open(r"C:\Users\administrator.MCA\Desktop\content.txt\content.txt",'r+')as file:
    data=file.read()
    data1=re.sub('a','@',data)
    file.write(data1)
    