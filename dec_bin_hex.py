jeito = False
while True:
    if jeito == True:
        print('\n')
    else:
        pass
    ini = int(input('Valor inicial: '))
    fim = int(input('Valor final: '))
    qBit = int(input('Quantidade de bits (dever ser 8, 16, 32): '))

    hexa = 0
    casa = 0

    if qBit == 8 and (ini > 255 or fim > 255):
        print('Com 8 bits o valor maximo fica em 255')
        break
    elif qBit == 16 and (ini > 65535 or fim > 65535):
        print('com 16 bits o valor maximo fica em 65535')
        break
    elif qBit == 32 and (ini > 4294967295 or fim > 4294967295):
        print('Com 32 bits o valor maximo fica em 4294967295')
        break
    elif qBit != 8 and qBit != 16 and qBit != 32:
        print('A quantidade de bits deve ser 8, 16, 32')
        break
    else:
        print("Resultados")
        
        for a in range(ini, fim+1):
                num = a
                lst = []
                hlist = []
    
                while num >= 1:
                    lst.insert(0,int(num%2))
                    num = int(num/2)
                for _ in range(len(lst), qBit):
                    lst.insert(0,0)
                
                for b in range(qBit-1, -1,-1):
                    casa += 1
                    if lst[b] == 1:
                        if casa == 1:
                            hexa += 1
                        elif casa == 2:
                            hexa += 2
                        elif casa == 3:
                            hexa += 4
                        elif casa == 4:
                            hexa += 8
                    if casa == 4:
                        casa = 0
                        if hexa >= 10:
                            if hexa == 10:
                                hlist.insert(0,"A")
                            elif hexa == 11:
                                hlist.insert(0,"B")
                            elif hexa == 12:
                                hlist.insert(0,"C")
                            elif hexa == 13:
                                hlist.insert(0,"D")
                            elif hexa == 14:
                                hlist.insert(0,"E")
                            elif hexa == 15:
                                hlist.insert(0,"F")
                        else:
                            hlist.insert(0,hexa)
                        hexa = 0
                print(f'{a:=8}  {"".join(map(str,lst))}  {"".join(map(str,hlist))}')
        repeat = input('\nFazer a conversão novamente? [S/N] ').strip().upper()
        if repeat == 'S' or repeat == 'SIM':
            jeito = True
            pass
        else:
            break
