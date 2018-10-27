from random import random, randint

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

def valida_cromosom(qtd_caditen, pop_temp, peso):
    valor, total = 0, 0
    cont = 0
    result = 1000
    
    for i in range(len(pop_temp)):
        valor += (pop_temp[i] * qtd_caditen[i])
        total += (pop_temp[i] * peso[i]) 
                   
    if valor <= result:
        result = 1
    else:
        result = 0
    return result, valor, total

def criando_populacao(n_itens, qtd_caditen, peso):
    pop_temp = []
    pop_final = []
    valor = []
    peso1 = []
    valida = 0
    vl, pes = 0, 0
    
    #--QUANTAS POPULAÇÃO SERAO CRIADAS
    while True:
        #INICIO DA POPULAÇÃO
        for j in range(0, n_itens):
            qtd = qtd_caditen[j]
            pop_temp.append(item_randon(qtd))
                
        va, vl, pes = valida_cromosom(qtd_caditen, pop_temp, peso)

        if va == 1:
            valor.append(vl)
            peso1.append(pes)
            
            pop_final.append(peso1)
            pop_final.append(valor)
            pop_final.append(pop_temp)
            break
        else:
            pop_temp.clear()
    return pop_final

def cross_over(pop_temp, n_itens, qtd_caditen, peso):
    
    final = []
    result, valor, total = 0, 0, 0
    
    
    while True:
        novo = []
        for i in range(0, n_itens):
            n = random()
            if n <= 0.600:
                c1 = pop_temp[0][2][i]
                novo.append(c1)
            elif n >0.600:
                c1 = pop_temp[1][2][i]
                novo.append(c1)
                    
        result, valor, total = valida_cromosom(qtd_caditen, novo, peso)
        if result == 1:
            break
            
        
    
    n1 = random()
    if n1 < 0.100:
        while True:
            novo_mutac = []
            novo_mutac = mutacao_crosover(novo, n_itens, qtd_caditen)
            result, valor, total = valida_cromosom(qtd_caditen, novo_mutac, peso)

            if result == 1:
            
                v = []
                t = []
            
                v.append(valor)
                t.append(total)
            
                novo_mutac.append(t)
                novo_mutac.append(v)
                novo_mutac.append(novo)
                
                return novo_mutac
                
                break
            else:
                novo_mutac.clear()    
    else:
        v = []
        t = []
            
        v.append(valor)
        t.append(total)
            
        final.append(t)
        final.append(v)
        final.append(novo)
        
        return final
    

def mutacao_crosover(pop_temp, n_itens, qtd_caditen):

    n = int(randint(0, n_itens-1))  
    iten = qtd_caditen[n]
    esc = int(randint(0, iten))
    pop_temp[n] = esc
            
    return pop_temp


#---------PARTE DE TESTE ----------------
qtd_caditen = []
peso = []
pop1 = []
melhor = []
qtd_pop = int(input('Quantidade de população!  '))
n_itens = int(input('Quantidade itens na  população! '))
for i in range(0, n_itens):
    qtd_caditen.append(int(input(f'Quantidade de itens para o iten {i+1}  ')))
    peso.append(int(input(f'Peso para o iten {i+1} ')))

for i in range(0, qtd_pop):
    pop1.append(criando_populacao(n_itens, qtd_caditen, peso))
    

pop1.sort(reverse = True)
for i in range(len(pop1)):
    print(f' {pop1[i]} ')
print('*-*'*10)

melhor.append(pop1[0])
contador = 0

while True:
    crosover1 = []
    crosover2 = []
    
    crosover1.append(cross_over(pop1, n_itens, qtd_caditen, peso))

    crosover2.append(cross_over(pop1, n_itens, qtd_caditen, peso))
    
    
    print(melhor)
    print(f'Corsover 1 -- {crosover1}')
    print(f'Corsover 2 -- {crosover2}')
    
    me1 = melhor[0][0][0]
    cr1 = crosover1[0][0][0]
    if cr1 > me1:
        melhor[0][0] = crosover1[0][0]
        melhor[0][1] = crosover1[0][1]
        melhor[0][2] = crosover1[0][2]
        
    me1 = melhor[0][0]   
    cr1 = crosover1[0][0]    
    if cr1 > me1:
        melhor[0][0] = crosover2[0][0]
        melhor[0][1] = crosover2[0][1]
        melhor[0][2] = crosover2[0][2] 
    
    while True:
        pop1.sort()
        print('Ordenado')
        for i in range(len(pop1)):
            print(f' {pop1[i]} ')
        print()
        if crosover1[0][0] > pop1[0][0]:
            
            pop1[0][0] = crosover1[0][0]
            pop1[0][1] = crosover1[0][1]
            pop1[0][2] = crosover1[0][2]
            crosover1.clear()
            break
        else:
            break
        
    
        
    while True:
        pop1.sort()
        print('Ordenado')
        for i in range(len(pop1)):
            print(f' {pop1[i]} ')
        print()
        if crosover2[0][0] > pop1[0][0]:
            
            pop1[0][0] = crosover2[0][0]
            pop1[0][1] = crosover2[0][1]
            pop1[0][2] = crosover2[0][2]
            crosover2.clear()
            break
        else:
            break
        
    pop1.sort(reverse = True)
    
    print(f'-|- {contador} -|-'*10)
    for i in range(len(pop1)):
        print(f' {pop1[i]} ')
    print('-|-'*10)
    print()
    print('++'*10)
    print(f'Melhor --- {melhor}')
    print('-|-'*10)
    
    contador+=1
    if contador == 30:
        break
print('---------------||||||------------'*5)            
print(f'-|- {contador} -|-'*10)
for i in range(len(pop1)):
    print(f' {pop1[i]} ')
print('-|-'*10)
print()
print('++'*10)
print(f'Melhor --- {melhor}')
print('-|-'*10)
