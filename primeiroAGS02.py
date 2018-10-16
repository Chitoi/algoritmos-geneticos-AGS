from random import random

pop1, pop2, pop3, pop4 = [], [], [], []
best = [] 
tot1, tot2, tot3, tot4 = 0, 0, 0, 0
valor1, valor2, valor3, valor4 = 0, 0, 0, 0

def item_um(n):
    """
    Definindo aleatoriamento qual quantidade
    do item 1
    """
    if n <= 0.250:
        return 0
    elif n > 0.250 and n <= 0.500:
        return 1
    elif n > 0.500 and n <= 0.750:
        return 2
    elif n > 0.750 and n <= 1.000:
        return 3

def item_dois(n):
    """
    Definindo aleatoriamento qual quantidade
    do item 2
    """
    if n <= 0.333:
        return 0
    elif n > 0.333 and n <= 0.667:
        return 1
    elif n > 0.667 and n <= 1.000:
        return 2

def item_tres(n):
    """
    Definindo aleatoriamento qual quantidade
    do item 3
    """
    if n <= 0.167:
        return 0
    elif n > 0.167 and n <= 0.333:
        return 1
    elif n > 0.333 and n <= 0.500:
        return 2
    elif n > 0.500 and n <= 0.667:
        return 3
    elif n > 0.667 and n <= 0.834:
        return 4
    elif n > 0.834 and n <= 1.000:
        return 5


def criando_populacao():
    """
    gerando a primeira população aleatoria
    """
    pop_temp = []
    total = 0
    valor = 0
    while True:
        total = 0
        for t in range(0,3):
            if t == 0:
                n = random()
                pop_temp.append(item_um(n))
            elif t == 1:
                n = random()
                pop_temp.append(item_dois(n))
            elif t == 2:
                n = random()
                pop_temp.append(item_tres(n))
                
        for i in range(len(pop_temp)):
            if i == 0:
                total = (pop_temp[i] * 3)
                valor = (pop_temp[i] * 40)
            elif i == 1:    
                total += (pop_temp[i] * 5)
                valor += (pop_temp[i] * 100)
            elif i == 2:    
                total += (pop_temp[i] * 2)
                valor += (pop_temp[i] * 50)
                    
        if total > 40:
            pop_temp.clear()
        else:
            break
    t = []
    t.append(total)
    v = []
    v.append(valor)
    return v, t, pop_temp


def cross_over():
    def escolhendo_crossover():
        m = random()
        p = random()
    
        if m <= 0.800:
            m = 0
        else:
            m = 1

        if p <= 0.800:
            p = 2
        else:
            p = 3
        return m, p
 
    m, p = escolhendo_crossover()

    total = 0
    total2 = 0
    contador = 0
    while True:
        
        total = 0
        total2=0
        def escolhendo_cromosom():
            c = random()
            if c <= 0.333:
                c = 0
            elif c > 0.333 and c <= 0.666:
                c = 1
            elif c > 0.666 and c <= 1.000:
                c = 2
            return c

        c = escolhendo_cromosom()
        c1 = 0
        c2 = 0
    
        c1 = best[m][2][c]
        c2 = best[p][2][c]

        best[m][2][c] = c2
        best[p][2][c] = c1
        valor, valor2 = 0, 0
        for i in range(len(best)):
            if i == 0:
                total  = (best[m][2][i] * 3)
                valor = (best[m][2][i] * 40)
                
                total2 = (best[p][2][i] * 3)
                valor2 = (best[p][2][i] * 40)
            elif i == 1:
                total  += (best[m][2][i] * 5)
                valor  += (best[m][2][i] * 100)
                
                total2 += (best[p][2][i] * 5)
                valor2 += (best[p][2][i] * 100)
            elif i == 2:
                total  += (best[m][2][i] * 2)
                valor  += (best[m][2][i] * 50)
                
                total2 += (best[p][2][i] * 2)
                valor2 += (best[p][2][i] * 50)
                
        contador += 1
        if total <= 40 and total2 <= 40:
            best[m][1][0] = total
            best[m][0][0] = valor
            best[p][1][0] = total2
            best[p][0][0] = valor2
            break
        elif contador == 100:
            print(f'Contador atingiu maximo de tentativas {contador}')
            best[m][2][c] = c1
            best[p][2][c] = c2   
            break
        else:
            print('-='*40)
            print(f'Não deu certo {best} ----{best[m][2][c]}')
            print(f'Não deu certo {best} ----{best[p][2][c]}')
            best[m][2][c] = c1
            best[p][2][c] = c2   
    return c1, c2, m, p



def mutacao(m, p):
    n = random()
    iten = []
    m1, it, total, esc, contador = 0, 0, 0, 0, 0
    if n <= 0.10:
        esc = random()
        while True:
            total = 0
            if esc <= 0.50:
                n = random()
                i = random()
                if n <= 0.333:
                    iten = item_um(i)
                    it = 0
                elif n > 0.333 and n <= 0.666:
                    iten = item_dois(i)
                    it = 1
                elif n > 0.666 and n <= 1.000:
                    iten = item_tres(i)
                    it = 2
                m1 = best[m][2][it]
                best[m][2][it] = iten
                
            elif esc > 0.50 and esc <= 1.00:
                n = random()
                i = random()
                if n <= 0.333:
                    iten = item_um(i)
                    it = 0
                elif n > 0.333 and n <= 0.666:
                    iten = item_dois(i)
                    it = 1
                elif n > 0.666 and n <= 1.000:
                    it = 2
                    iten = item_tres(i)
                m1 = best[p][2][it] 
                best[p][2][it] = iten
                
            valor = 0 
            if esc <=  0.50:
                for i in range(len(best)):
                    if i == 0:
                        total  = (best[m][2][i] * 3)
                        valor  = (best[m][2][i] * 40)
                    elif i == 1:
                        total  += (best[m][2][i] * 5)
                        valor  += (best[m][2][i] * 100)
                    elif i == 2:
                        total  += (best[m][2][i] * 2)
                        valor  += (best[m][2][i] * 50)
                best[m][1][0] = total
                best[m][0][0] = valor
                
            elif esc > 0.50 and esc <= 1.00:
                for i in range(len(best)):
                    if i == 0:
                        total  = (best[p][2][i] * 3)
                        valor  = (best[p][2][i] * 40)
                    elif i == 1:
                        total  += (best[p][2][i] * 5)
                        valor  += (best[p][2][i] * 100)
                    elif i == 2:
                        total  += (best[p][2][i] * 2)
                        valor  += (best[p][2][i] * 50)
                best[p][1][0] = total
                best[p][0][0] = valor
                
            contador += 1 
            if total <= 40:
                print('-='*40)
                print('MUTAÇÃO CONCLUIDA ----')
                print(f'{best}')
                break
            elif contador == 100:
                print(f'Contador atingiu maximo de tentativas {contador}')
                break
            else:
                if esc <=  0.50:
                    best[m][2][it] = m1
                elif esc > 0.50 and esc <= 1.00:
                    best[p][2][it] = m1

                    
pop1 = criando_populacao()
pop2 = criando_populacao()
pop3 = criando_populacao()
pop4 = criando_populacao()

best.append(pop1)
best.append(pop2)
best.append(pop3)
best.append(pop4)

print(f'Primeira população {best}')
print('-='*40)
best.sort(reverse = True)
print('-='*40)
print(best)

#for i in range(0,1000):
cont_max = 0
while True:
    #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    c1, c2, m, p = cross_over()

    #=-=-=-=-=-=-=-=-=-=-=-=--==-=--=-=-=-=-=-=-=
    best.sort(reverse = True)

    print('-='*40)
    print('-='*40)
    print(c1)
    print('-='*40)
    print(c2)
    print('-='*40)
    print(f'População depois de sofrer crossover  --{best}')
    print('-='*40)
    mutacao(m, p)
    best.sort(reverse = True)  
    print('-='*40)
    print(f'População depois de sofrer mutação ---{best}')
    print('-='*40)
    cont_max += 1
    if (best[0][0][0] >= 450 and best[1][0][0] >= 450 ) or cont_max == 410:
        print(f'Contador maximo  --- {cont_max}')
        break
    else:
        pass
            
        
        
    
        
   
    

        

    




    
