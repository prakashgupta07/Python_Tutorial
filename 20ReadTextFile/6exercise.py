#read data from html file and write link from html file
with open('file.html','r') as webpage:
        with open('file1.txt','w') as wf:
                for line in webpage.readlines():
                        if '<a href=' in line:
                                pos=line.find('<a href=')
                                first_quotes=line.find('\"',pos)
                                second_quotes=line.find('\"',first_quotes+1)
                                url=line[first_quotes+1:second_quotes]
                                wf.write(url+'\n')
