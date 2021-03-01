def repeatedString(s, n):
    slist = list(s)
    lengthS = len(s)
    print(lengthS)
    current = 0
    nlist = []
    if lengthS == 1 and slist[0] =='a':
        return n
    elif lengthS == 1 and slist[0] !='a':
        return 0
    elif lengthS < n:
        stringmultiple = n // lengthS
        print('string mulitple',stringmultiple)
        numbchar = stringmultiple*lengthS
        counta = stringmultiple*slist.count('a')
        print("number of as", counta)
        charleft = n - numbchar
        print(" characters left", charleft)
        while current <= charleft-1:
            nlist.append(slist[current])
            print(nlist)
            print(counta + nlist.count('a'))
            current += 1
        return counta + nlist.count('a')
    elif lengthS >= n:
        print(n)
        while current < n:
            nlist.append(slist[current])
            print(nlist)
            current += 1
            #print(current)
            #print('number of as', nlist.count('a'))
        return nlist.count('a')
    else:
        return 0



#repeatedString('a',10000)
repeatedString('ababa',3)
#repeatedString('kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm',736778906400)
#repeatedString('epsxyyflvrrrxzvnoenvpegvuonodjoxfwdmcvwctmekpsnamchznsoxaklzjgrqruyzavshfbmuhdwwmpbkwcuomqhiyvuztwvq',549382313570)