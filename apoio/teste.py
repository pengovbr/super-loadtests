f = open('cpfs.csv')

for l in f:
    #print l
    s = l.split(',')

    u = s[0]
    
    u = u.replace('usuario', '')
    u = int(u)
    
    v = (u + 20) % 20
    
    f2 = open('cpfs_cadastrar.csv.old', 'a')
    
    if(v in (1,2)):
        print u
        f2.write(l)
    
    f2.close()
    
