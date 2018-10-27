from random import random, randint, shuffle

def item_randon(n):
    result = 0
    
    if n > 0:
        n+=1
        porcent = (100 / n)/100
        aux, r = -1,0
        a = random()
        i = 0
        while True:
            r = r + porcent
            if a > aux and a <= r:
                result = i
                break
            else:
                pass
            aux = r
            i+=1    
    return result

def valida_cromosom(qtd_caditen, pop_temp, peso, result):
    valor, total = 0, 0
    cont = 0
    
    
    for i in range(len(pop_temp)):
        valor += pop_temp[i] * qtd_caditen[i]
        total += pop_temp[i] * peso[i] 
                   
    if valor <= result:
        result = 1
    else:
        result = 0
    return result, valor, total

def criando_populacao(n_itens, qtd_caditen, peso, result):
    pop_temp = []
    final = []
    valida = 0
    vl, pes = 0, 0
    
    #--QUANTAS POPULAÇÃO SERAO CRIADAS
    while True:
        #INICIO DA POPULAÇÃO
        for j in range(0, n_itens):
            qtd = qtd_caditen[j]
            pop_temp.append(item_randon(qtd))
                
        va, vl, pes = valida_cromosom(qtd_caditen, pop_temp, peso, result)
       
        if va == 1:
            final.append(pes)
            final.append(vl)
            final.append(pop_temp)
            break
        else:
            pop_temp.clear()
    return final

def mutacao_crosover(pop_temp, n_itens, qtd_caditen):

    n = int(randint(0, n_itens-1))  
    iten = qtd_caditen[n]
    esc = int(randint(0, iten))
    pop_temp[n] = esc
        
    return pop_temp

def cross_over(pop_temp, n_itens, qtd_caditen, peso, g_max):
    print(f'------INICIO CROSSOVER------')
    print(f'DENTRO DO CROSOVER {pop_temp}')   
    final = []
    final2 = [] 
    result, valor, total = 0, 0, 0
    result2, valor2, total2 = 0, 0, 0
    flag = 0
    fil1 = []
    fil2 = []

    cont_break = 0
    while True:
        corte = int(randint(1, n_itens) - 1)
        print(f'Ponto de corte {corte}')
        if corte == 0:
            print(f'Ponto de corte igual a 0 {corte}')
            corte = 1;
            
        for i in range(0, n_itens):
            if i < corte:
                c1 = pop_temp[0][2][i]
                fil1.append(c1)
                c1 = pop_temp[1][2][i]
                fil2.append(c1)
            elif i >= corte:
                c1 = pop_temp[1][2][i]
                fil1.append(c1)
                c1 = pop_temp[0][2][i]
                fil2.append(c1)
        print(f'filho 1 ->{fil1}')
        print(f'filho 2 ->{fil2}')
        print()
        result, valor, total = valida_cromosom(qtd_caditen, fil1, peso, g_max)
        result2, valor2, total2 = valida_cromosom(qtd_caditen, fil2, peso, g_max)
        print(f'resultado 1 {result} -- valor 2 {result2}')
        if result == 1 or result2 ==1:
            break
        
        
    n1 = random()
    if n1 <= 0.050:
        novo_mutac = []
        while True:
            novo_mutac = []
            no1 = []
            no1 = fil1.copy()
            print(f'Selecionado para mutação -- {fil1}')
            novo_mutac = mutacao_crosover(no1, n_itens, qtd_caditen)
            print(f'CROMOSOMO DEPOIS DA MUTAÇÃO -- {novo_mutac}')
            result, valor, total = valida_cromosom(qtd_caditen, novo_mutac, peso, g_max)
            print(f'Depois da mutação ---------{fil1}')
            if result == 1 or cont_break == 10:
                break
            else:
                novo_mutac.clear()
                no1.clear()
                cont_break+=1
                print(f'contador de parada mutação 1º {cont_break}')
        final.append(total)
        final.append(valor)
        final.append(novo_mutac)
        print(f'Crosove COM MUTAÇÃO -+- {final}')
        flag+=1
        
    else:
        #print(f'FALG {flag}')
        final.append(total)
        final.append(valor)
        final.append(fil1)
        
    cont_break = 0
    n1 = random()
    if n1 <= 0.050:
        novo_mutac = []
        while True:
            novo_mutac = []
            no1 = []
            no1 = fil2.copy()
            print(f'Selecionado para mutação -- {fil2}')
            novo_mutac = mutacao_crosover(no1, n_itens, qtd_caditen)
            print(f'CROMOSOMO DEPOIS DA MUTAÇÃO -- {novo_mutac}')
            result2, valor2, total2 = valida_cromosom(qtd_caditen, novo_mutac, peso, g_max)
            print(f'Depois da mutação ---------{fil2}')
            if result == 1 or cont_break == 10:
                break
            else:
                novo_mutac.clear()
                no1.clear()
                cont_break+=1
                print(f'contador de parada mutação 2º {cont_break}')
        final2.append(total2)
        final2.append(valor2)
        final2.append(novo_mutac)
        print(f'Crosove COM MUTAÇÃO -+- {final2}')
        flag+=1
        
    else:
        print(f'FALG {flag}')
        final2.append(total2)
        final2.append(valor2)
        final2.append(fil2)
            
    print(f'Resultado do cromos 1 --> {final}')
    print(f'Resultado do cromos 2 --> {final2}')
    return final, final2 

#--------- ENTRADA DE DADOS ----------------

qtd_caditen = []
peso = []
pop1 = []
valida = 0
geracoes = 0
qtd_pop = int(input('Quantidade de população!  '))
geracoes = int(input('Quantidade de gerações'))
valida = int(input('Valor maximo !!'))
n_itens = int(input('Quantidade itens na  população! '))

for i in range(0, n_itens):
    qtd_caditen.append(int(input(f'Quantidade de itens para o iten {i+1}  ')))
    peso.append(int(input(f'Peso para o iten {i+1} ')))

for i in range(0, qtd_pop):
    pop1.append(criando_populacao(n_itens, qtd_caditen, peso, valida))
    
pop1.sort(reverse = True)

for i in range(len(pop1)):
    print(f' {pop1[i]} ')
print('*-*'*10)
print(len(pop1))
print()
shuffle(pop1)
for i in range(len(pop1)):
    print(f' {pop1[i]} ')
print('*-*'*10)
print(len(pop1))
print()
#---------PARTE DE crossover ----------------
filhos = []

pop_pai = []

def criando_roleta():
    pai1 = []
    pai2 = []
    aux = int(len(pop1) - 1)
    r_sort1 = []
    r_sort2 = []
    
    for i in  range(0, 5):
        while True:
            sort = int(randint(0, aux))
            if sort not in r_sort1:
                r_sort1.append(sort)
                break
            
    for i in  range(0, 5):
        while True:
            sort = int(randint(0, aux))
            if sort not in r_sort2:
                r_sort2.append(sort)
                break
            
    for i in range(0, 5):
        aux1 = r_sort1[i]
        aux2 = r_sort2[i]
        pai1.append(pop1[aux1])
        pai2.append(pop1[aux2])
        
    pai1.sort(reverse = True)
    pai2.sort(reverse = True)
    
    return pai1, pai2

print()
print()

flag = 0

def escolhendo_da_roleta():
    cont_break = 0
    pop_pai = []
    pai1 = []
    pai2 = []
    pai1, pai2 = criando_roleta()
    i = 0
    while True:
        flag = 0
        porcent = 100 / n_itens
        for j in range(0, n_itens):
            if pai1[i][2][j] != pai2[i][2][j]:
                flag+=1
                    
        cont_break += 1
        percent = porcent * flag
        print(f'PRIM {porcent} -- {flag}')
        print(f'PRIM {percent}')
        print(f'Contador de parada {cont_break}')
        if percent >= 50:
            pop_pai.append(pai1[i])
            pop_pai.append(pai2[i])
            print(f'Prim - pai-> {pop_pai}')
            break  
        flag = 0
        
        while True:
            cont_break = 0
            flag = 0
            y = i+1
            print(f'valor de i --{i}')
            print(f'valor de y --{y}')
            if y < 5 and i < 5:
                for j in range(0, n_itens):
                    if pai1[i][2][j] != pai2[y][2][j]:
                        flag+=1
            cont_break+=1
            percent = porcent * flag
            print(f'PRIM2 {porcent} -- {flag}')
            print(f'PRIM2 {percent}')
            if percent >= 50 or cont_break == 50:
                pop_pai.append(pai1[i])
                pop_pai.append(pai2[y])
                print(f'SEC {pop_pai}')
                print(f'Contador de parada {cont_break}')
                break
            i = randint(0,5) - 1
            print(f'valor de aleatorio {i}')  
        if percent >= 50 or cont_break == 50:
            print(f'Contador de parada {cont_break}')
            break
       
    return pop_pai
    
print()
"""
pop_pai = escolhendo_da_roleta()
for i in range(len(pop_pai)):
    print('escolhidos')
    print(pop_pai[i])
print()
print()
"""


for i in range(0, geracoes):
    pop_pai = escolhendo_da_roleta()
    filhos_temp1 = []
    filhos_temp2 = []
    print('PARTE 1 -----')
    print(f'ESCOLHAS PARA CROSOVER {pop_pai}')
    print()
    filhos_temp1, filhos_temp2 = cross_over(pop_pai, n_itens, qtd_caditen, peso, valida)
    print(f'geração {i} -- filho 1- {filhos_temp1} filho 2-- {filhos_temp2}')
    
    if filhos_temp1[1] <= valida:
        filhos.append(filhos_temp1.copy())
    elif filhos_temp2[1] <= valida: 
        filhos.append(filhos_temp2.copy())
        
        
    filhos_temp1.clear()
    filhos_temp2.clear()
    print('%%'*30)
    print()
filhos.sort(reverse = True)
for i in range(len(filhos)):
    print(f'{filhos[i]}')
print()
print(len(filhos))

"""
#--------------///------------------------------------------------
aux = len(pop1) - 1
for i in range(0, qtd_pop):
    crosover1 = []
    crosover1.append(cross_over(pop1, n_itens, qtd_caditen, peso, valida))
    #print(f'Corsover 1  -- {crosover1}')
    
   
    if pop1[aux][0] <  crosover1[0][0]:
       # print(f'POP 1 {pop1[aux]} é menor que  <  CROSOVER {crosover1}')
        pop1[aux] = crosover1[0]
       # print(f'FEITO ALTERAÇÃO {pop1[aux]}')
       
  
    pop1.sort(reverse = True)

    #print()   
    crosover1.clear()
    #print('___'*10)



print('++'*10)
    
print('*-*'*10)

for i in range(len(pop1)):
    print(f' {pop1[i]} ')
print('*-*'*10)

print(aux)
"""

