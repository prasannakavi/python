import re
with open(r"C:\Users\administrator.MCA\Desktop\content.txt\content.txt",'r')as file:
    data=file.read()
    out=re.findall(' a[a-z]',data)
    print(out)
