#first away to find more one link in  line

with open('file.html','r') as webpage:
        with open('output.txt','a') as wf:
                page=webpage.read()
                link=True
                while link:
                        pos=page.find('<a href=')
                        if pos==-1:
                                link=False
                        else:
                                first=page.find('\"',pos)
                                second=page.find('\"',first+1)
                                url=page[first+1:second]
                                wf.write(url+'\n')
                                page=page[second:]

#second away to find more one link in  line
# with open('file.html','r') as webpage:
#         with open('file1.txt','w') as wf:
#                 for line in webpage.readlines():
#                         length=len(line)
#                         for i in range(length):
#                                 if line[i:i+8]=='<a href=':
#                                         pos=i+8
#                                         first_quotes=line.find('\"',pos)
#                                         second_quotes=line.find('\"',first_quotes+1)
#                                         url=line[first_quotes+1:second_quotes]
#                                         wf.write(url+'\n')

                