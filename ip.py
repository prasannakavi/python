st=input('')
temp=st.split('.')
if len(temp)==4:
    for i in temp:
        if i.isnumric():
            out='yes'
        else:
            out='No'
            break
    else:
        out='No'
print=(out)

