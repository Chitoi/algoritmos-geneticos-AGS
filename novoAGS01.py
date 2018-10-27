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
    result = 300
    
    for i in range(len(pop_temp)):
        valor += pop_temp[i] * qtd_caditen[i]
        total += pop_temp[i] * peso[i] 
                   
    if valor <= result:
        result = 1
    else:
        result = 0
    return result, valor, total

def criando_populacao(n_itens, qtd_caditen, peso):
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
                
        va, vl, pes = valida_cromosom(qtd_caditen, pop_temp, peso)
       
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

def cross_over(pop_temp, n_itens, qtd_caditen, peso):
    final = []
    result, valor, total = 0, 0, 0
    flag = 0
    novo = []
    while True:
        
        for i in range(0, n_itens):
            n = random()
            if n <= 0.600:
                c1 = pop_temp[0][2][i]
                novo.append(c1)
            elif n >0.600:
                c1 = pop_temp[1][2][i]
                novo.append(c1)
        #print(f'CROSOVER -- INICIO -- {novo}')
        
        n1 = random()
        if n1 <= 0.100:
            novo_mutac = []
            while True:
                novo_mutac = []
                no1 = []
                no1 = novo.copy()
               # print(f'Selecionado para mutação -- {novo}')
                novo_mutac = mutacao_crosover(no1, n_itens, qtd_caditen)
               # print(f'CROMOSOMO DEPOIS DA MUTAÇÃO -- {novo_mutac}')
                result, valor, total = valida_cromosom(qtd_caditen, novo_mutac, peso)
               # print(f'Depois da mutação ---------{novo}')
                if result == 1:
                    break
                else:
                    novo_mutac.clear()
                    no1.clear()
            final.append(total)
            final.append(valor)
            final.append(novo_mutac)
            #print(f'Crosove COM MUTAÇÃO -+- {final}')
            flag+=1
            return final
        
        else:
            result, valor, total = valida_cromosom(qtd_caditen, novo, peso)
            
        if result == 1:
            #print(f'FALG {flag}')
            final.append(total)
            final.append(valor)
            final.append(novo)
            break
        else:
            novo.clear()
    return final

#--------- ENTRADA DE DADOS ----------------

qtd_caditen = []
peso = []
pop1 = []

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

#---------PARTE DE crossover ----------------

crosover2 = []

aux = len(pop1) - 1
for i in range(0, qtd_pop):
    crosover1 = []
    crosover1.append(cross_over(pop1, n_itens, qtd_caditen, peso))
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
