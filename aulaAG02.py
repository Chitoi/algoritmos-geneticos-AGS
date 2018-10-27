from random import random, randint, shuffle


def gerando_pop(n_iten, valor_max):
    pop_temp = []
    pop = []

    for i in range(0, n_iten):
        pop_temp.append(int(randint(1, valor_max)))


    pop.append(sum(pop_temp))
    pop.append(pop_temp)

    return pop

def mutacao(pop1, pop2, n_iten):
    print('@@' * 20)
    print('---DENTRO DA MUTAÇÃO')

    print(f'Pop 1 {pop1}')
    n = int(randint(1, n_iten) - 1)
    val = int(randint(1, 9))
    pop1[n] = val
    print(f'MUTAÇÃO 1--> indice {n} --> valor {val} -->mutação concluida --> {pop1}')
    print()

    print(f'Pop 2 {pop2}')
    n = int(randint(1, n_iten) - 1)
    val = int(randint(1, 9))
    pop2[n] = val
    print(f'MUTAÇÃO 2--> indice {n} --> valor {val} -->mutação concluida --> {pop2}')
    print()

    return pop1, pop2

def crossover(n_iten,pop):
    filho1 = []
    filho2 = []
    pop_temp1 = []
    pop_temp2 = []

    print()
    print('-*-' * 20)
    print(f'------INICIO DO CROSSOVER------------')
    print(f'Escolhidos para crossover: ')
    print(f'{pop[0]} |--| {pop[1]}')
    print()
    print('-=' * 20)
    print()

    corte = int(randint(1, n_iten) - 1)
    print(f'Ponto de corte --> indice {corte}')
    if corte == 0:
        print(f'Ponto de corte igual a 0 --> corte recebe +1')
        corte = 1
        print(f'Corte --> {corte}')
        print()
        print('-=' * 20)
        print()

    print(f'----Crossover----')
    taxa = randint(1, 100)
    if taxa <= 90:
        print(f'Foi para crossover --> TAXA {taxa}')
        print()
        for i in range(0, n_iten):
            if i < corte:
                c1 = pop[0][1][i]
                pop_temp1.append(c1)
                c1 = pop[1][1][i]
                pop_temp2.append(c1)
            elif i >= corte:
                c1 = pop[1][1][i]
                pop_temp1.append(c1)
                c1 = pop[0][1][i]
                pop_temp2.append(c1)

        print('Crossover OK')
        print(pop_temp1)
        print(pop_temp2)

        muta = int(randint(1, 100))
        if muta <= 50:
            print(f'---INDO PARA MUTAÇÃO--- TAXA --> {muta}')
            print()
            pop_temp1, pop_temp2 = mutacao(pop_temp1, pop_temp2, n_iten)
            print(f'RECEBENDO MUTAÇÃO ->> 1 {pop_temp1} -->> 2 {pop_temp2}')
            print()

        total = sum(pop_temp1)
        filho1.append(total)
        filho1.append(pop_temp1)

        total = sum(pop_temp2)
        filho2.append(total)
        filho2.append(pop_temp2)

        print()
        print('Crossover conluido FIM')
        print(filho1)
        print(filho2)
        print()

    else:
        print('#-*' * 30)
        print(f'Não foi para o crossover TAXA -> {taxa}')
        filho1 = pop[0]
        filho2 = pop[1]
        print(filho1)
        print(filho2)
        print('#-*' * 30)
        print()

    return filho1, filho2

def montando_torneio(pop):
    aux = int(len(pop) - 1)
    tam = int(len(pop) / 5)
    pop_temp1 = []
    pop_temp2 = []

    ind_sort1 = []
    ind_sort2 = []

    print()
    print('-+' * 20)
    print()
    print('----MONTANDO TORNEIO----')
    print()

    for i in range(0, tam):
        while True:
            sort = int(randint(0, aux))
            if sort not in ind_sort1:
                ind_sort1.append(sort)
                break

    print('Primeiro torneio de indice')
    for i in range(len(ind_sort1)):
        print(ind_sort1[i])
    print()

    for i in range(0, tam):
        while True:
            sort = int(randint(0, aux))
            if sort not in ind_sort2:
                ind_sort2.append(sort)
                break

    print('Segundo torneio de indice')
    for i in range(len(ind_sort2)):
        print(ind_sort2[i])
    print()

    for i in range(0, tam):
        aux1 = ind_sort1[i]
        aux2 = ind_sort2[i]
        pop_temp1.append(pop[aux1])
        pop_temp2.append(pop[aux2])

    pop_temp1.sort(reverse=True)
    pop_temp2.sort(reverse=True)

    print(f'Primeiro torneio---')
    for i in range(0, tam):
        print(f'{pop_temp1[i]}')
    print()

    print(f'Segundo torneio---')
    for i in range(0, tam):
        print(f'{pop_temp2[i]}')
    print()

    return pop_temp1, pop_temp2, tam

def escolhendo_do_torneio(pop, n_iten):
    flag = 0
    pop_fin = []
    pop_temp1 = []
    pop_temp2 = []

    pop_temp1, pop_temp2, tam = montando_torneio(pop)

    i = 0
    y = 0
    cont_break = 0
    print()
    print('Escolhendo do torneio ')
    print()

    while True:
        flag = 0

        porcent = 100 / n_iten

        for j in range(0, n_iten):
            print(f'VALOR DE i {i} -- Valor de y {y}')
            if pop_temp1[i][1][j] != pop_temp2[y][1][j]:
                flag += 1

        cont_break += 1
        percent = porcent * flag

        print(f'Porcentagem de diferença {percent}')
        print()
        if percent >= 40:
            pop_fin.append(pop_temp1[i])
            pop_fin.append(pop_temp2[y])
            print(f'1- Escolhidos')
            print(pop_fin[0])
            print(pop_fin[1])
            print()
            break
        elif cont_break == 50:
            pop_temp1.clear()
            pop_temp2.clear()
            pop_temp1, pop_temp2 = montando_torneio(pop)
            i = 0
            y = 0
            cont_break = 0
        else:
            if (cont_break <= tam - 1) \
                or (cont_break > tam * 2 and cont_break <= tam * 2 -1) \
                or (cont_break >= tam * 4 and cont_break <= tam * 4 -1) \
                or (cont_break >= tam * 6 and cont_break <= tam * 6 -1)\
                or (cont_break >= tam * 8 and cont_break <= tam * 8 -1):
                y += 1
                i = 0
            elif (cont_break >= tam and cont_break <= tam - 1) \
                or (cont_break >= tam * 3 and cont_break <= tam * 3 -1) \
                or (cont_break >= tam * 5 and cont_break <= tam * 5 -1)\
                or (cont_break >= tam * 7 and cont_break <= tam * 7 -1) \
                or (cont_break >= tam * 9 and cont_break <= tam * 9 -1):
                i += 1
                y = 0
    return pop_fin




def metodo_torneio(pop, n_iten, gerac):
    pop_filho = []
    for i in range(0, gerac):
        pop_aux = []
        x = []
        y = []

        pop_aux = escolhendo_do_torneio(pop, n_iten)
        x, y = crossover(n_iten, pop_aux)

        pop_filho.append(x)
        pop_filho.append(y)

    return pop_filho

def main():
    n_iten = 5
    valor_max = 9
    pop = []
    pop1 = []
    GERAC = 50

    pop_filho1 = []
    pop_filho2 = []
    pop_filho3 = []
    pop_filho4 = []

    for i in range(0, GERAC):
        pop.append(gerando_pop(n_iten, valor_max))

    pop.sort(reverse = True)
    for i in range(0, GERAC):
        print(pop[i])

    print()
    print('%%' * 30)
    print()

    shuffle(pop)
    for i in range(0, GERAC):
        print(pop[i])
    print()

    pop_filho1 = metodo_torneio(pop, n_iten, GERAC)

    pop_filho1.sort(reverse=True)
    print(f'Metodo Torneio --')

    for i in range(0, GERAC):
        print(pop_filho1[i])

    print()
    print('-=' * 30)
    print()
    print(f'Metodo Torneio -- GERAÇÃO 2')
    for i in range(0, int(GERAC / 2)):
        pop_filho2.append(pop_filho1[i])
    pop.sort(reverse=True)
    for i in range(0, int(GERAC / 2)):
        pop_filho2.append(pop[i])
    for i in range(0, GERAC):
        print(pop_filho2[i])
    print()
    print('-=' * 30)
    print()
    shuffle(pop_filho2)
    pop_filho3 = metodo_torneio(pop_filho2, n_iten, GERAC)

    pop_filho3.sort(reverse=True)
    for i in range(0, GERAC):
        print(pop_filho3[i])

main()
