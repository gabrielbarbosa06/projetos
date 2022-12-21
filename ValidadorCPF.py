validade = list()
qvalid = 0
qinva = 0
cpfnum = list()
cpfnum2 = list()
i = 10
testecpf = dict()
tdig1 = 0
tdig2 = 0
dig1 = 0
dig2 = 0
while True:
    i = 10
    cpf = input('Digite seu CPF: ') 
    testecpf['cpf'] = cpf
    for a in cpf:
        a = int(a)
        cpfnum.append(a)
    while len(cpfnum) < 11 or len(cpfnum) > 11:
        cpf = input('CPF com menos de 11 diitos, insira outro: ') 
        testecpf['cpf'] = cpf
        cpfnum.clear()
        for a in cpf:
            a = int(a)
            cpfnum.append(a)
    for x in range (0, 9):
        cpfnum2.append(cpfnum[x])
        if i >= 2:
            tdig1 = tdig1 + (cpfnum[x] * i)
            i = i - 1
    if tdig1 % 11 < 2:
        dig1 = 0
    else:
        dig1 = 11 - (tdig1 % 11)
    i = 11
    cpfnum2.append(dig1)
    for x in range (0, 10):
        if i >= 2:
            tdig2 = tdig2 + (cpfnum2[x] * i)
            i = i - 1
    if tdig2 % 11 < 2:
        dig2 = 0
    else:
        dig2 = 11 - (tdig2 % 11)
    if dig1 == cpfnum[9] and dig2 == cpfnum[10]:
        testecpf['validade'] = 'válido'
        qvalid = qvalid + 1
    else:
        testecpf['validade'] = 'inválido'
        qinva = qinva + 1
    validade.append(testecpf.copy())
    cpfnum.clear()
    cpfnum2.clear()
    tdig1 = 0
    tdig2 = 0
    resp = input('Deseja testar mais um cpf?[s/n]')
    if resp == 's':
        print('=-'*40)
    else:
        print(f"Quantidade CPFs testados: {len(validade)}")
        print(f"Quantidade de CPFs válidos: {qvalid}")
        print(f"Quantidade de CPFs inválidos: {qinva}")
        porvalid = int((qvalid / len(validade)) * 100)
        porinva = int((qinva / len(validade)) * 100)
        print(f'Porcentagem de CPFs válidos: {porvalid}%')
        print(f'Porcentagem de CPFs inválidos: {porinva}%')
        break
