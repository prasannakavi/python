import re
st='AP01AB23457823HDJS4134'
data=re.findall('AP[0-3]\d[A-Z]{2}\d{4}',st)
print(data)