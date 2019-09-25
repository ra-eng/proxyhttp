def getdic(getheader):
    dic = {}
    #print("getheader \n")
    print(getheader)
    for line in getheader:
        #print("lineeee "+ line)
        if line.startswith("GET"): 
            parts = line.split()
            dic[parts[0]] = []
            for i in range(1,3) :
                dic[parts[0]].append(parts[i].rstrip("\r"))
        else : 
            try :
                parts = line.split(": ")
                print(parts)
                dic[parts[0]] = parts[1].rstrip("\r")
            except: 
                continue

    return dic

    def makeheader(dir, ext) :
        buffer = dir[1]+" 200 OK\r\n"+"Content-type: "+ext