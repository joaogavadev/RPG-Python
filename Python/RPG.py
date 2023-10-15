import random

def roda_1_dado():
    return random.randint(1, 6)
#armazenando resultado dos dados
dado1 = roda_1_dado()
dado_Energia1 = roda_1_dado()
dado_Energia2 = roda_1_dado()
dado_Sorte = roda_1_dado()

#armazenando os perks em variaveis para alterar futuramente
habilidade = 6 + dado1
energia = 12 + dado_Energia1 + dado_Energia2
sorte = 6 + dado_Sorte

garota_espirito = False

ativos = []


def batalha_dupla(habilidade_monstro, habilidade_monstro2, energia_monstro,energia_monstro2,  habilidade, sorte, energia, nome):

    print("Se inicia a batalha em dupla!")
    habilidade_inicial_monstro = habilidade_monstro
    habilidade_inicial_monstro2 = habilidade_monstro2
    habilidade_inicial_perso = habilidade
    
    while energia_monstro > 0 and energia_monstro2 > 0 and energia > 0:
        # Exiba informações sobre a batalha, como a energia do monstro e habilidade do personagem

        habilidade_monstro = habilidade_inicial_monstro
        habilidade = habilidade_inicial_perso
        habilidade_monstro2 = habilidade_inicial_monstro2
        #rodando dados da primeira criatura
        input("\nPressione Enter para rodar os dados para Habilidade da primeira criatura...")
        x = roda_1_dado()
        y = roda_1_dado()
        print(f"\nO primeiro dado tirou: {x}.")
        print(f"O segundo dado tirou: {y}.")
        monst_habil_soma = x + y
        habilidade_monstro = habilidade_monstro + monst_habil_soma

        input(f"\nPressione Enter para vizualizar as informações da criatura {nome}")

        print(f"\nx--------------x--------------x-----{nome}----x--------------x--------------x")

        print(f"\nEnergia da criatura: {energia_monstro}\nHabilidade da criatura: {habilidade_monstro}")

        print("\nx--------------x--------------x-------------------------x--------------x--------------x")

        input("\n\nPressione Enter para rodar os dados para SUA Habilidade...")

        k = roda_1_dado()
        j = roda_1_dado()
        char_hab_soma = habilidade + k + j

        print(f"\nO primeiro dado tirou: {k}")
        print(f"\nO segundo dado tirou: {j}")


        input("\nPressione Enter para vizualizar as informações do seu personagem...")


        print("\nx--------------x--------------x-------------------------x--------------x--------------x")

        print(f"\nSua Energia: {energia}")
        print(f"\nSua Habilidade: {char_hab_soma}")
        print(f"\nSua Sorte: {sorte}")


        print("\nx--------------x--------------x-------------------------x--------------x--------------x")
        
        print(habilidade_monstro)
        print(char_hab_soma)

        input("\n\nPressione Enter para começar a batalha...")

        if char_hab_soma > habilidade_monstro:
            print("\nA sua habilidade é maior que a do oponente. Você ataca e não sofre dano.")

            escolha = input("\nVocê deseja tentar sua sorte para causar o dobro de dano?\n(1. Sim - 2. Não)")

            if escolha == '1':
                input("\nPressione Enter para testar sua sorte...")
                #variavel dos dados
                sorte_atq1 = random.randint(1, 6)
                sorte_atq2 = random.randint(1, 6)

                print(f"\nO primeiro dado tirou: {sorte_atq1}.")
                print(f"O segundo dado tirou {sorte_atq2}.")

                input("\nAperte Enter para ver o resultado...")

                #variavel de soma dos dados
                soma_srt = sorte_atq1 + sorte_atq2

                if soma_srt <= sorte:
                    sorte = sorte - 1
                    print("\nVocê teve sorte! Você dá o dobro de dano, porém perde 1 de Sorte.")
                    dano_personagem = 4
                    energia_monstro = energia_monstro - dano_personagem
                else:
                    sorte = sorte - 1
                    print("\nVocê teve má sorte! A criatura causa o dobro de dano em você, e você perde 1 de Sorte!")
                    dano_monstro = 4
                    energia = energia - dano_monstro
            else:
                print("\nVocê escolhe atacar sem sorte para dano bonus.\nVocê da 2 de dano na criatura.")
                dano_personagem = 2
                energia_monstro = energia_monstro - dano_personagem



        elif habilidade_monstro > char_hab_soma:
            print("\nA habilidade da criatura é maior que a sua, Você toma 2 de dano.")

            print("\nGostaria de testar sua sorte para realizar uma manobra evasiva? Nenhum dano será infligido a você, mas você perderá 1 ponto de sorte.")
            escolha = input("\n(1. Sim - 2. Não): \n")
            if escolha == '1':
                input("Aperte Enter para testar sua sorte...")

                a = roda_1_dado()
                b = roda_1_dado()

                print(f"\nO dado 1 tirou: {a}.")
                print(f"\nO dado 2 tirou: {b}.")

                input("Aperte Enter para ver o resultado...")

                soma_evasiva = a + b

                if soma_evasiva <= sorte:
                    print("\nVocê deu sorte! Não toma nenhum dano, mas perde 1 ponto de Sorte.")
                    sorte = sorte - 1



                else:
                    print("\nVocê não deu sorte! Você toma o dobro de dano, e perde 1 ponto de sorte.")
                    energia = energia - 4
                    sorte = sorte - 1


            elif escolha == '2':
                print("\nVocê escolhe não usar a sorte. Você toma 2 de dano.")
                energia = energia - 2



        elif habilidade_monstro == char_hab_soma:
            print("\nO valor de habilidade dos dois é igual. Nada acontece.")
        
        
        
        
        
        
        
        print("\nx--------------x--------------x-------------------------x--------------x--------------x")

        print(f"\nSua Energia: {energia}                 Energia da criatura: {energia_monstro}")    
        print(f"\nSua Habilidade: {char_hab_soma}       -      Habilidade da criatura: {habilidade_monstro}")
        print(f"\nSua Sorte: {sorte}")


        print("\nx--------------x--------------x-------------------------x--------------x--------------x")

    


    return energia, sorte
    


def usar_sorte(sorte):
    dado_1 = random.randint(1, 6)
    dado_2 = random.randint(1, 6)
    soma_dados = dado_1 + dado_2
    input("\nPressione Enter para rodar o primeiro dado para testar sua sorte...")
    print(f"\nO primeiro dado resultou em: {dado_1}")
    input("\nPressione Enter para rodar seu proximo dado...")
    print(f"O segundo dado resultado em: {dado_2}")
    print(f"\nA soma dos dados é {soma_dados},e seu nivel de sorte atual é {sorte}")

    if soma_dados <= sorte :
        return True
    else:
        return False

def usar_habilidade(habilidade):
    dado_1 = random.randint(1, 6)
    dado_2 = random.randint(1, 6)
    soma_dados = dado_1 + dado_2
    input("\nPressione Enter para rodar o primeiro dado para testar sua sorte...")
    print(f"\nO primeiro dado resultou em: {dado_1}")
    input("\nPressione Enter para rodar seu proximo dado...")
    print(f"O segundo dado resultado em: {dado_2}")
    print(f"\nA soma dos dados é {soma_dados}, e seu nivel de habilidade atual é {habilidade}")

    if soma_dados <= habilidade :
        return True
    else:
        return False
    
def alterar_habilidade(habilidade, valor):
    habilidade += valor
    return habilidade


mochila = []

def tutorial():
    rep = "s"
    while rep == "s":
        print("\nx-------------x-------------x-------------x-------------x-------------xTUTORIALx-------------x-------------x-------------x-------------x-------------x--------x")
        print("\n   Reposição de Habilidade, Energia e Sorte")

        print("\n   Habilidade, Energia e Sorte ")

        print("\nO índice de HABILIDADE reflete sua perícia como espadachim e sua aptidão geral como lutador; quanto mais alto, melhor.\n\nO índice de ENERGIA expressa sua condição geral, determinação de sobreviver, força de vontade e aptidão de uma maneira global; quanto mais alto, maior sua sobrevida.\n\nO índice de SORTE indica o quanto você é naturalmente uma pessoa de sorte. Sorte e magia são fatos da vida no reino da fantasia que você está prestes a explorar.")

        print("\nx-------------x-------------x-------------x-------------x-------------x--------x-------------x-------------x-------------x-------------x-------------x--------x")


        input("\nPressione Enter para continuar...")

        print("\nx-------------x-------------x-------------x-------------x-------------x--------x-------------x-------------x-------------x-------------x-------------x--------x")

        print("\n   Energia e Provisões")
        print("\nSeu índice de ENERGIA mudará muito durante a aventura, à medida que você luta com monstros e empreende tarefas árduas. Ao se aproximar de sua meta, seu nível de ENERGIA poderá estar perigosamente baixo, e as batalhas serão particularmente arriscadas; portanto tenha cuidado!\n\nSua mochila contém Provisões suficientes para 10 refeições. Você poderá descansar e comer a qualquer momento, exceto quando estiver no meio de uma Batalha. Uma refeição repõe 4 pontos de ENERGIA. Quando comer, acrescente 4 pontos a seu índice de ENERGIA e deduza 1 ponto de suas Provisões. É fornecido um quadro separado de Provisões Restantes na sua Folha de Aventuras. Não se esqueça que você tem um longo caminho a percorrer, por isso use suas Provisões com sabedoria!\n\nLembre-se também que o seu índice de ENERGIA nunca poderá exceder o valor Inicial, a não ser que isso seja especificamente indicado. Beber a Poção de Força restabelecerá imediatamente seu índice Inicial de ENERGIA.")

        print("\nx-------------x-------------x-------------x-------------x-------------x--------x-------------x-------------x-------------x-------------x-------------x--------x")

        input("\nPressione Enter para continuar...")

        print("\nx-------------x-------------x-------------x-------------x-------------x--------x-------------x-------------x-------------x-------------x-------------x--------x")

        print("\n   Sorte")
        print("\nAcréscimos a seu índice de SORTE serão concedidos, no decorrer da aventura, quando você tiver uma sorte particularmente grande. Os detalhes são dados nas páginas do livro. Lembre- se que, a exemplo dos índices de ENERGIA e HABILIDADE, seu índice de SORTE nunca poderá ultrapassar o valor Inicial, a não ser que isso seja especificamente indicado. Beber a Poção da Fortuna recoloca a sua SORTE no nível Inicial, a qualquer momento, além de aumentar sua SORTE Inicial em 1 ponto.")


        print("\nx-------------x-------------x-------------x-------------x-------------x--------x-------------x-------------x-------------x-------------x-------------x--------x")


        input("\nPressione Enter para continuar...")

        print("\nx-------------x-------------x-------------x-------------x-------------x--------x-------------x-------------x-------------x-------------x-------------x--------x")

        print("\n   Equipamentos e Poções")
        print("\nVocê começará sua aventura com o mínimo essencial de equipamento, mas poderá achar ou comprar outros itens durante a viagem. Você está armado com uma espada e um escudo, veste uma armadura de couro e tem uma mochila para pôr provisões e quaisquer tesouros que venha a encontrar.\n\nAlém disso, você poderá levar uma garrafa com uma poção mágica que o ajudará na missão. Escolha uma destas:\n\nPoção da Habilidade - repõe os pontos de HABILIDADE.\nPoção da Força - repõe os pontos de ENERGIA.\nPoção da Fortuna - repõe os pontos de SORTE e acrescenta 1 ponto à SORTE Inicial.\n\nEssas poções poderão ser tomadas a qualquer momento da aventura (exceto durante um Combate). Uma dose de poção restabelecerá os níveis Iniciais dos índices de HABILIDADE, ENERGIA e SORTE (além disso, a Poção da Fortuna acrescentará 1 ponto a seu nível Inicial de SORTE).\n\nCada garrafa de poção contém o bastante para uma dose, isto é, a característica pode ser restituída uma vez durante a aventura. Quando usar a poção, registre o fato na sua Folha de Aventuras.\n\nLembre-se também que você só poderá levar uma das três poções em sua viagem: escolha com sabedoria!")

        print("\nx-------------x-------------x-------------x-------------x-------------x--------x-------------x-------------x-------------x-------------x-------------x--------x")

        input("\nPressione Enter para continuar...")

        print("\nx-------------x-------------x-------------x-------------x-------------x--------x-------------x-------------x-------------x-------------x-------------x--------x")

        print("\n   Combates")
        print("\nMuitas vezes você se defrontará com instruções para que lute contra algum tipo de criatura. Pode ser que exista uma opção de fuga, mas, se não houver - ou se você resolver atacar a criatura de qualquer maneira -, o combate será travado como se segue.\n\nPrimeiro, os índices de HABILIDADE e ENERGIA da criatura será registrado no primeiro quadro vazio de Encontros com Monstros da sua Folha de Aventuras.\nOs índices de cada criatura são dados a cada encontro. \n\nA sequência de combate é a seguinte: \n\n1- Jogue os dois dados uma vez para a criatura. Some o número obtido ao índice de HABILIDADE dela. Esse total é a Força de Ataque da criatura. \n\n2- Jogue os dois dados uma vez para você. Some o número obtido ao seu índice atual de HABILIDADE. Esse total é a sua Força de Ataque.\n\n3- Se sua Força de Ataque for maior que a da criatura, você a feriu. Siga para o item 4. Se a Força de Ataque da criatura for maior que a sua ela o feriu. Siga para o item 5. Se os dois totais de Força de Ataque forem iguais, vocês conseguiram evitar os golpes um do outro - comece a próxima Série de Ataque a partir do item 1 acima.\n\n4- Você feriu a criatura, subtraia 2 pontos do índice de ENERGIA dela.Você poderá usar sua SORTE para causar danos mais graves.\n\n5- A criatura feriu você, subtraia 2 pontos de seu índice de ENERGIA. Novamente, você poderá usar sua SORTE nessa fase.\n\n6- Faça os ajustes apropriados no índice de ENERGIA da criatura ou no seu próprio (e no seu índice de SORTE, se a tiver usado - veja adiante).\n\n7- Comece a próxima Série de Ataque, retornando a seu índice de HABILIDADE atual e repetindo os itens de 1-6. Esta sequência continua até que um dos índices de ENERGIA - seu, ou da criatura - fique reduzido a zero (morte).")

        print("\nx-------------x-------------x-------------x-------------x-------------x--------x-------------x-------------x-------------x-------------x-------------x--------x")


        input("\nPressione Enter para continuar...")

        print("\nx-------------x-------------x-------------x-------------x-------------x--------x-------------x-------------x-------------x-------------x-------------x--------x")

        print("\n   Fuga")
        print("\nEm algumas páginas pode haver a opção de escapar de um combate, caso as coisas estejam indo mal para você. Porém, ao escapar da criatura, esta automaticamente lhe causará um ferimento (subtraia 2 pontos de ENERGIA). Esse é o preço da covardia. Repare que você poderá usar a SORTE, da maneira normal, nesse ferimento (veja adiante). Você só poderá Fugir se esta opção lhe for especificamente dada na página.")

        print("\nx-------------x-------------x-------------x-------------x-------------x--------x-------------x-------------x-------------x-------------x-------------x--------x")


        input("\nPressione Enter para continuar...")

        print("\nx-------------x-------------x-------------x-------------x-------------x--------x-------------x-------------x-------------x-------------x-------------x--------x")

        print("\n   Sorte")
        print("\nEm vários momentos da aventura, tanto em batalhas como em situações nas quais poderá ter ou não sorte (os detalhes dessas situações são dados nas próprias páginas), você poderá apelar para a sorte, a fim de tornar o resultado mais favorável. Mas tome cuidado! Usar a sorte é uma coisa arriscada, e, se você não tiver sorte, as consequências podem ser desastrosas.")
        
        print("\nO procedimento para usar a sorte é o seguinte: jogue os dois dados. Se o número obtido for igual ou menor que o seu índice de SORTE atual, você teve sorte, e o resultado lhe será favorável. Se o número obtido for maior que o seu índice de SORTE atual, você não teve sorte, e sofrerá as consequências.")

        print("\nEsse procedimento é conhecido como: Teste sua Sorte. Cada vez que Testar sua Sorte, você terá que subtrair 1 ponto do seu índice de SORTE do momento. Assim, você logo compreenderá que, quanto mais confiar na sorte, mais riscos correrá. ")

        print("\nx-------------x-------------x-------------x-------------x-------------x--------x-------------x-------------x-------------x-------------x-------------x--------x")


        input("\nPressione Enter para continuar...")


        print("\nx-------------x-------------x-------------x-------------x-------------x--------x-------------x-------------x-------------x-------------x-------------x--------x")


        print("\n   Sorte em combate")
        print("\nEm determinadas páginas, você será instruído a Testar sua Sorte, e saberá das conseqüências de ter ou não sorte. Porém, nos combates, você sempre terá a opção de usar a sorte, seja para causar um ferimento mais grave na criatura que acabou de ferir, seja para minimizar os efeitos de um ferimento que a criatura lhe causou.")

        print("\nSe você acabou de ferir a criatura, poderá Testar sua Sorte, conforme descrito acima. Se você tiver sorte, causou um ferimento grave, e poderá subtrair 2 pontos extras do índice de ENERGIA da criatura. Porém, se você não tiver sorte, o ferimento foi um mero arranhão, e terá que repor 1 ponto à ENERGIA da criatura (isto é, em vez dos 2 pontos normais de danos, você causou apenas 1).")


        print("\nSe a criatura tiver acabado de feri-lo, você poderá Testar sua Sorte, para tentar minimizar o ferimento. Se você tiver sorte, o ferimento foi um mero arranhão. Reponha 1 ponto de ENERGIA (isto é, em vez de 2 pontos normais de danos, ela causou apenas 1). Se você não tiver sorte, recebeu um ferimento mais grave. Subtraia 1 ponto extra de ENERGIA.\n\nLembre-se: você tem que subtrair 1 ponto de seu próprio Índice de SORTE a cada vez que Testar sua Sorte. ")


        print("\nx-------------x-------------x-------------x-------------x-------------x--------x-------------x-------------x-------------x-------------x-------------x--------x")


        print("\n   DICAS PARA O JOGO")
        print("\nHá um caminho seguro através do Calabouço da Morte, e você precisará fazer várias tentativas até encontrá-lo. Faça anotações e desenhe um mapa enquanto explora – esse mapa será de valor inestimável em aventuras futuras e lhe permitirá avançar rapidamente na direção das áreas inexploradas.\n\nNem todas as áreas contêm tesouros; muitas encerram apenas armadilhas e criaturas contra as quais você terá que medir forças. Há muitas passagens que levam a buscas inúteis, e, embora você possa de fato progredir até chegar ao seu destino final, não há qualquer garantia de que encontrará o que está procurando.\n\nVocê logo compreenderá que os itens não fazem sentido se forem lidos em ordem numérica. É essencial que você leia apenas os itens indicados, pois ler outros somente causará confusão, além de diminuir a emoção do jogo.\n\nO único caminho seguro envolve um mínimo de risco, e qualquer jogador, por mais fracos que sejam seus resultados iniciais nos dados, é capaz de chegar ao final com bastante facilidade.\n\n\n-Que a sorte dos deuses esteja com você na aventura à sua frente!-")

        print("\nx-------------x-------------x-------------x-------------x-------------x--------x-------------x-------------x-------------x-------------x-------------x--------x")

        rep = input("Deseja repetir o tutorial? ('S' ou 'N'): ")
#iniciando boas vindas + perks do personagem

def char_perks():
    print("\nBem vindo ao calabouco da morte!")
    print("x-------------x-------------x-------------x-------------x-------------x")
    print("Suas stats iniciais são:\nHabilidade = 6\nEnergia = 12\nSorte = 6")
    print("x-------------x-------------x-------------x-------------x-------------x")
    input("\nPressione enter para rodar um dado para Habilidade...")
    print(f"O dado tirou {dado1}")
    print("x-------------x-------------x-------------x-------------x-------------x")
    print(f"Suas stats agora são:\nHabilidade = 6 -> {habilidade}\nEnergia = 12\nSorte = 6")
    print("x-------------x-------------x-------------x-------------x-------------x")
    input("Pressione enter para rodar um dado para Energia...")
    print(f"O dado 1 tirou: {dado_Energia1}")
    input("Pressione enter para rodar o outro dado para Energia...")
    print(f"O dado 2 tirou: {dado_Energia2}")
    print("x-------------x-------------x-------------x-------------x-------------x")
    print(f"Suas stats agora são:\nHabilidade = 6 -> {habilidade}\nEnergia = 12 -> {energia}\nSorte = 6")
    print("x-------------x-------------x-------------x-------------x-------------x")
    input("Pressione enter para rodar o dado para Sorte...")
    print(f"O dado tirou: {dado_Sorte}")
    print("x-------------x-------------x-------------x-------------x-------------x")
    print(f"Essas são suas stats finais:\nHabilidade = 6 -> {habilidade}\nEnergia = 12 -> {energia}\nSorte = 6 -> {sorte}")
    print("x-------------x-------------x-------------x-------------x-------------x")

char_perks()

stats_final = (f"\nx---SEU PERSONAGEM--x\n|Habilidade = {habilidade}\n|Energia = {energia}\n|Sorte = {sorte}\nx---------x---------x\n")


def batalha(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome):
    print("\nA batalha começou! O que você deseja fazer?")

    habilidade_inicial_monstro = habilidade_monstro
    habilidade_inicial_perso = habilidade
    
    while energia_monstro > 0 and energia > 0:
        # Exiba informações sobre a batalha, como a energia do monstro e habilidade do personagem

        habilidade_monstro = habilidade_inicial_monstro
        habilidade = habilidade_inicial_perso
        input("\nPressione Enter para rodar os dados para Habilidade da criatura...")
        x = roda_1_dado()
        y = roda_1_dado()
        print(f"\nO primeiro dado tirou: {x}.")
        print(f"O segundo dado tirou: {y}.")
        monst_habil_soma = x + y
        habilidade_monstro = habilidade_monstro + monst_habil_soma

        input(f"\nPressione Enter para vizualizar as informações da criatura {nome}")

        print(f"\nx--------------x--------------x-----{nome}----x--------------x--------------x")

        print(f"\nEnergia da criatura: {energia_monstro}\nHabilidade da criatura: {habilidade_monstro}")

        print("\nx--------------x--------------x-------------------------x--------------x--------------x")

        input("\n\nPressione Enter para rodar os dados para SUA Habilidade...")

        k = roda_1_dado()
        j = roda_1_dado()
        char_hab_soma = habilidade + k + j

        print(f"\nO primeiro dado tirou: {k}")
        print(f"\nO segundo dado tirou: {j}")


        input("\nPressione Enter para vizualizar as informações do seu personagem...")


        print("\nx--------------x--------------x-------------------------x--------------x--------------x")

        print(f"\nSua Energia: {energia}")
        print(f"\nSua Habilidade: {char_hab_soma}")
        print(f"\nSua Sorte: {sorte}")


        print("\nx--------------x--------------x-------------------------x--------------x--------------x")
        
        print(habilidade_monstro)
        print(char_hab_soma)

        input("\n\nPressione Enter para começar a batalha...")

        if char_hab_soma > habilidade_monstro:
            print("\nA sua habilidade é maior que a do oponente. Você ataca e não sofre dano.")

            escolha = input("\nVocê deseja tentar sua sorte para causar o dobro de dano?\n(1. Sim - 2. Não)")

            if escolha == '1':
                input("\nPressione Enter para testar sua sorte...")
                #variavel dos dados
                sorte_atq1 = random.randint(1, 6)
                sorte_atq2 = random.randint(1, 6)

                print(f"\nO primeiro dado tirou: {sorte_atq1}.")
                print(f"O segundo dado tirou {sorte_atq2}.")

                input("\nAperte Enter para ver o resultado...")

                #variavel de soma dos dados
                soma_srt = sorte_atq1 + sorte_atq2

                if soma_srt <= sorte:
                    sorte = sorte - 1
                    print("\nVocê teve sorte! Você dá o dobro de dano, porém perde 1 de Sorte.")
                    dano_personagem = 4
                    energia_monstro = energia_monstro - dano_personagem
                else:
                    sorte = sorte - 1
                    print("\nVocê teve má sorte! A criatura causa o dobro de dano em você, e você perde 1 de Sorte!")
                    dano_monstro = 4
                    energia = energia - dano_monstro
            else:
                print("\nVocê escolhe atacar sem sorte para dano bonus.\nVocê da 2 de dano na criatura.")
                dano_personagem = 2
                energia_monstro = energia_monstro - dano_personagem



        elif habilidade_monstro > char_hab_soma:
            print("\nA habilidade da criatura é maior que a sua, Você toma 2 de dano.")

            print("\nGostaria de testar sua sorte para realizar uma manobra evasiva? Nenhum dano será infligido a você, mas você perderá 1 ponto de sorte.")
            escolha = input("\n(1. Sim - 2. Não): \n")
            if escolha == '1':
                input("Aperte Enter para testar sua sorte...")

                a = roda_1_dado()
                b = roda_1_dado()

                print(f"\nO dado 1 tirou: {a}.")
                print(f"\nO dado 2 tirou: {b}.")

                input("Aperte Enter para ver o resultado...")

                soma_evasiva = a + b

                if soma_evasiva <= sorte:
                    print("\nVocê deu sorte! Não toma nenhum dano, mas perde 1 ponto de Sorte.")
                    sorte = sorte - 1



                else:
                    print("\nVocê não deu sorte! Você toma o dobro de dano, e perde 1 ponto de sorte.")
                    energia = energia - 4
                    sorte = sorte - 1


            elif escolha == '2':
                print("\nVocê escolhe não usar a sorte. Você toma 2 de dano.")
                energia = energia - 2



        elif habilidade_monstro == char_hab_soma:
            print("\nO valor de habilidade dos dois é igual. Nada acontece.")
        
        
        
        
        
        
        
        print("\nx--------------x--------------x-------------------------x--------------x--------------x")

        print(f"\nSua Energia: {energia}                 Energia da criatura: {energia_monstro}")    
        print(f"\nSua Habilidade: {char_hab_soma}       -      Habilidade da criatura: {habilidade_monstro}")
        print(f"\nSua Sorte: {sorte}")


        print("\nx--------------x--------------x-------------------------x--------------x--------------x")


    energia_atlz = energia

    if energia <= 0:
        fim_de_jogo()


    return energia, sorte, energia_atlz
    
def batalha_fuga(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome):
    print("\nA batalha começou! O que você deseja fazer?")

    habilidade_inicial_monstro = habilidade_monstro
    habilidade_inicial_perso = habilidade
    
    while energia_monstro > 0 and energia > 0:
        # Exiba informações sobre a batalha, como a energia do monstro e habilidade do personagem

        habilidade_monstro = habilidade_inicial_monstro
        habilidade = habilidade_inicial_perso
        input("\nPressione Enter para rodar os dados para Habilidade da criatura...")
        x = roda_1_dado()
        y = roda_1_dado()
        print(f"\nO primeiro dado tirou: {x}.")
        print(f"O segundo dado tirou: {y}.")
        monst_habil_soma = x + y
        habilidade_monstro = habilidade_monstro + monst_habil_soma

        input(f"\nPressione Enter para vizualizar as informações da criatura {nome}")

        print(f"\nx--------------x--------------x-----{nome}----x--------------x--------------x")

        print(f"\nEnergia da criatura: {energia_monstro}\nHabilidade da criatura: {habilidade_monstro}")

        print("\nx--------------x--------------x-------------------------x--------------x--------------x")

        input("\n\nPressione Enter para rodar os dados para SUA Habilidade...")

        k = roda_1_dado()
        j = roda_1_dado()
        char_hab_soma = habilidade + k + j

        print(f"\nO primeiro dado tirou: {k}")
        print(f"\nO segundo dado tirou: {j}")


        input("\nPressione Enter para vizualizar as informações do seu personagem...")


        print("\nx--------------x--------------x-------------------------x--------------x--------------x")

        print(f"\nSua Energia: {energia}")
        print(f"\nSua Habilidade: {char_hab_soma}")
        print(f"\nSua Sorte: {sorte}")


        print("\nx--------------x--------------x-------------------------x--------------x--------------x")
        
        print(habilidade_monstro)
        print(char_hab_soma)

        input("\n\nPressione Enter para começar a batalha...")

        if char_hab_soma > habilidade_monstro:
            print("\nA sua habilidade é maior que a do oponente. Você ataca e não sofre dano.")

            escolha = input("\nVocê deseja tentar sua sorte para causar o dobro de dano?\n(1. Sim - 2. Não - 3. Tentar fuga.): ")

            if escolha == '1':
                input("\nPressione Enter para testar sua sorte...")
                #variavel dos dados
                sorte_atq1 = random.randint(1, 6)
                sorte_atq2 = random.randint(1, 6)

                print(f"\nO primeiro dado tirou: {sorte_atq1}.")
                print(f"O segundo dado tirou {sorte_atq2}.")

                input("\nAperte Enter para ver o resultado...")

                #variavel de soma dos dados
                soma_srt = sorte_atq1 + sorte_atq2

                if soma_srt <= sorte:
                    sorte = sorte - 1
                    print("\nVocê teve sorte! Você dá o dobro de dano, porém perde 1 de Sorte.")
                    dano_personagem = 4
                    energia_monstro = energia_monstro - dano_personagem
                else:
                    sorte = sorte - 1
                    print("\nVocê teve má sorte! A criatura causa o dobro de dano em você, e você perde 1 de Sorte!")
                    dano_monstro = 4
                    energia = energia - dano_monstro
            elif escolha == 2:
                print("\nVocê escolhe atacar sem sorte para dano bonus.\nVocê da 2 de dano na criatura.")
                dano_personagem = 2
                energia_monstro = energia_monstro - dano_personagem

            else:
                print("Você tentar usar sua sorte para fugir.")
                
                input("\nPressione Enter para rodar os dados para testar sua sorte de fuga...")
                fuga_sorte1 = roda_1_dado()
                print(f"\nO dado 1 tirou: {fuga_sorte1}.")

                fuga_sorte2 = roda_1_dado()
                print(f"\nO dado 2 tirou: {fuga_sorte2}.")

                soma_fuga = fuga_sorte2 + fuga_sorte1

                if soma_fuga <= sorte:
                    print("\nVocê teve sorte! Você consegue fugir.")
                    break
                else:
                    print("Você não teve sorte. Você perde 2 de sorte e toma o dobro de dano da criatura...")
                    sorte = sorte - 2
                    energia = energia - 2







        elif habilidade_monstro > char_hab_soma:
            print("\nA habilidade da criatura é maior que a sua, Você toma 2 de dano.")

            print("\nGostaria de testar sua sorte para realizar uma manobra evasiva? Nenhum dano será infligido a você, mas você perderá 1 ponto de sorte.")
            escolha = input("\n(1. Sim - 2. Não): \n")
            if escolha == '1':
                input("Aperte Enter para testar sua sorte...")

                a = roda_1_dado()
                b = roda_1_dado()

                print(f"\nO dado 1 tirou: {a}.")
                print(f"\nO dado 2 tirou: {b}.")

                input("Aperte Enter para ver o resultado...")

                soma_evasiva = a + b

                if soma_evasiva <= sorte:
                    print("\nVocê deu sorte! Não toma nenhum dano, mas perde 1 ponto de Sorte.")
                    sorte = sorte - 1



                else:
                    print("\nVocê não deu sorte! Você toma o dobro de dano, e perde 1 ponto de sorte.")
                    energia = energia - 4
                    sorte = sorte - 1


            elif escolha == '2':
                print("\nVocê escolhe não usar a sorte. Você toma 2 de dano.")
                energia = energia - 2



        elif habilidade_monstro == char_hab_soma:
            print("\nO valor de habilidade dos dois é igual. Nada acontece.")

    else:
        fim_de_jogo()


    return energia_monstro


energia_monstro = 0
habilidade_monstro = 0
nome = ""





def inicio():
    print("\n     A HISTORIA")
    escolha_historia = input("\nDeseja pular a história inicial? (1. Sim - 2. Não): ").lower()
    if escolha_historia == 'sim':
        aventura1()
    else:
        print("\nFang era uma cidade pequena e comum na província setentrional de Chiang Mai. Situada às margens do rio Kok, constituía-se num ponto de parada conveniente para os comerciantes e passageiros que se deslocavam pelo rio durante a maior parte do ano. Umas poucas barcaças, jangadas e, às vezes, um grande barco a vela podiam ser encontrados no atracadouro de Fang. Mas tudo isso foi há muito tempo, antes da criação da Prova dos Campeões. Agora, uma vez por ano, o rio fica apinhado de barcos, trazendo as pessoas que chegam de centenas de quilômetros ao redor, na esperança de testemunhara quebra de uma antiga tradição em Fang e ver alguém vitorioso na Prova dos Campeões. ")


        input("\nPressione Enter para continuar...")

        print("\nTodo ano, no dia 10 de maio, guerreiros e heróis vêm para Fang, a fim de enfrentar a prova mais importante de suas vidas. A sobrevivência é improvável, todavia muitos correm o risco, pois o prêmio é excelente - uma bolsa de 10 mil Peças de Ouro e a libertação de Chiang Mai. Contudo, tornar-se Campeão não é tarefa simples. Há alguns anos, um poderoso barão de Fang, chamado Sukumvit, resolveu chamar a atenção geral para a sua cidade, criando um campeonato sem igual. Com a ajuda dos habitantes, construiu um labirinto nas profundezas da encosta atrás de Fang, do qual só havia um modo de sair. O labirinto foi povoado com todos os tipos de monstros pavorosos, além de armadilhas e ardis mortais. Sukumvit o havia desenhado com detalhes meticulosos, de modo que quem quer que se dispusesse a enfrentar o desafio teria que usar tanto a inteligência quanto a habilidade com as armas. Quando finalmente ficou certo de que tudo estava pronto, resolveu testar o labirinto. Escolheu 10 de seus melhores guardas e mandou-os, muito bem armados, para o interior do labirinto. Nunca mais foram vistos. A história do infeliz destino dos guardas logo correu mundo")

        input("\nPressione Enter para continuar...")

        print("\nEntão, Sukumvit anunciou a primeira Prova dos Campeões. Emissários e editais divulgaram o desafio: 10 mil Peças de Ouro, e a libertação de Chiang Mai, para qualquer pessoa que sobrevivesse aos perigos do labirinto de Fang. No primeiro ano, 17 bravos guerreiros tentaram 'A Caminhada', como ficou mais tarde conhecida a prova. Ninguém retornou. Com o passar dos anos, a Prova dos Campeões atraía mais e mais desafiantes e espectadores. Fang prosperou e se preparava com meses de antecedência para o espetáculo que patrocinava a cada mês de maio. Acidade era decorada, contratavam-se músicos, dançarinos, comedores de fogo, ilusionistas e todo tipo de artistas, e se registravam as inscrições de indivíduos esperançosos que pretendiam realizar 'A Caminhada'. Na última semana de abril, as pessoas de Fang e seus visitantes iniciavam uma desvairada comemoração. Cantavam, bebiam, dançavam e riam até o raiar do dia 12 de maio, quando a cidade se amontoava nos portões do labirinto para ver o primeiro desafiante do ano avançar para enfrentar a Prova dos Campeões")

        input("\nPressione Enter para continuar...")

        print("\nTendo visto um dos comunicados de Sukumvit pregado em uma árvore, você resolve que este ano tentará 'A Caminhada'. Durante os últimos cinco anos, você tem-se sentido atraído, não pelas recompensas, mas pelo simples fato de que ninguém até hoje conseguiu emergir vitorioso do labirinto. Você pretende fazer com que este seja o ano no qual um Campeão será coroado! Reunindo uns poucos pertences, você parte imediatamente. Dois dias de caminhada para o oeste levam-no à costa, onde você entra na maldita Port Blacksand. Sem perder tempo nessa cidade de ladrões, você compra sua passagem em um pequeno barco que veleja em direção ao norte, para a foz do rio Kok; de lá, você sobe o rio de jangada por quatro dias, até finalmente chegar a Fang.")

        input("\nPressione Enter para continuar...")

        print("\nA Prova começa dentro de três dias, e a cidade está num clima quase histérico de excitação. Você faz sua inscrição e recebe um lenço roxo para amarrar em volta do braço, o qual informa a todos sua condição de candidato. Durante três dias, você goza da melhor hospitalidade de Fang, sendo tratado como um semideus. Durante a longa celebração, quase esquece seu propósito; mas, na noite anterior à Prova, a magnitude da tarefa à sua frente começa a dominar-lhe os pensamentos. Mais tarde, você é levado para um alojamento especial e conduzido a seu quarto. Há uma esplêndida cama de quatro colunas com lençóis de cetim para ajudá-lo a repousar. Mas há pouco tempo para dormir. ")

        input("\nPressione Enter para continuar...")

        print("\nLogo antes da aurora, um toque de clarim o desperta de seus vívidos sonhos povoados de poços flamejantes e aranhas negras gigantescas. Minutos depois alguém bate à porta, e soa uma voz de homem que diz: 'Seu desafio começará em breve. Por favor, esteja pronto para partir em 10 minutos.' Você sai da cama, caminha até a janela e abre os postigos. Pessoas já se acotovelam nas ruas, deslocando-se silenciosamente na bruma da manhã - espectadores a caminho do labirinto, sem dúvida, esperando garantir bons lugares para observar aos competidores. Você se afasta e caminha até uma mesa de madeira, onde está sua espada de confiança. Apanhando-a, golpeia o ar com um giro poderoso, imaginando que feras sua lâmina afiada poderá ter que enfrentar em breve. Em seguida, abre a porta que dá para o corredor. Um homem pequeno de olhos puxados o saúda, inclinando-se até o chão, quando você sai de seu quarto. 'Por favor, siga-me', ele diz. Ele vira para a esquerda e caminha rapidamente na direção das escadas no fim do corredor.")

        input("\nPressione Enter para continuar...")

        print("\nSaindo do alojamento, ele dispara por alamedas estreitas entre as casas, e você tem que andar depressa para acompanhá-lo. Logo chegam a uma estrada larga de terra batida, ladeada por multidões que vibram. Ao verem seu lenço roxo, eles gritam ainda mais alto e atiram-lhe flores. As sombras compridas lançadas pelas pessoas à sua frente vão diminuindo à medida que o brilhante sol dourado sobe no céu da manhã. Ali, diante da multidão ruidosa e vibrante, você se sente estranhamente solitário, consciente das provações que o esperam. De repente, você sente um puxão na camisa e vê seu pequeno guia acenando freneticamente para que o siga. Adiante, vê a encosta que se ergue e a entrada escura de um túnel que desaparece nas profundezas de seu interior. Ao se aproximar, repara em dois grandes pilares de pedra em cada um dos lados da entrada do túnel. Os pilares estão cobertos de entalhes ornamentados: serpentes que se contorcem, demônios, divindades, cada um deles parecendo gritar uma advertência silenciosa para aqueles que passam.")

        input("\nPressione Enter para continuar...")

        print("Você vê o próprio Barão Sukumvit de pé na entrada, esperando para cumprimentar os concorrentes da Prova dos Campeões. Você conta cinco outros fazendo fila orgulhosamente, seus lenços roxos visíveis para que todos os notem. Há dois bárbaros de peito nu, vestidos com peles. Eles estão completamente imóveis, as pernas retas e levemente afastadas, os braços esticados para frente, pousados no cabo de suas longas achas de guerra de dois gumes. ")

        input("\nPressione Enter para continuar...")

        print("Uma mulher-elfo esguia, de cabelos dourados e olhos verdes de felino, ajusta o cinturão de través, cheio de punhais, que lhe envolve a túnica de couro. Dos outros dois homens restantes, um está coberto da cabeça aos pés por uma armadura de chapas de ferro com um elmo emplumado e um escudo que exibe um timbre; o outro está envolto em vestes negras, somente seus olhos escuros aparecendo em meio aos panos pretos que lhe envolvem o rosto. Facas longas, um garrote de fio de aço e outras armas mortais silenciosas pendem-lhe do cinto. Os cinco concorrentes demonstram ter notado sua chegada com movimentos quase imperceptíveis de cabeça, e você se volta para olhar de frente, pela última vez, a multidão exultante. Subitamente, um silêncio cai sobre a multidão, quando o Barão Sukumvit dá um passo adiante, segurando seis varas de bambu. Você tira uma delas da mão estendida e lê a palavra 'Quinto'. Então, a Prova começa.")

        input("\nPressione Enter para continuar...")


        print("O cavaleiro é o primeiro. Ele saúda a multidão antes de desaparecer no túnel; meia hora depois é seguido pela mulher-elfo. Em seguida, vai um dos bárbaros; depois, o assassino negro. Agora é a sua vez de saudar a multidão. Segurando o lenço roxo bem alto, você enche os pulmões de ar fresco e puro uma última vez antes de se virar para passar entre os pilares de pedra e penetrar no labirinto do poderoso Barão Sukumvit, a fim de enfrentar perigos desconhecidos na 'Caminhada' pelo Calabouço da Morte. ")

        input("\nPressione Enter para continuar...")


        print("\n\n          SUA JORNADA E TRAJETO DE DECISÕES SE INICIA AGORA, TODA TOMADA DE DECISÃO A PARTIR DE AGORA TERÁ CONSEQUENCIAS, SEJAM BOAS OU RUINS, BOA SORTE!")

        
        input("\n\nPressione enter para iniciar sua aventura...\n\n")


    #inicialização do jogo + loop de tutorial


def fim_de_jogo():
    print("\nFim de jogo! Sua aventura termina aqui!")
    escolha = input("\nDeseja jogar novamente? (responda com 'S' ou 'N'): ").capitalize()
    
    if escolha == 'S':
        char_perks()
        inicio()
        aventura1()
    elif escolha == 'N':
        print("Até a próxima!")



def aventura1():
    print(f"{stats_final}\n")
    print("CAP 1\n")
    print("\nO clamor dos espectadores excitados some gradualmente atrás de você, que se aventura cada vez mais fundo na penumbra do túnel da caverna. ")

    print("\nGrandes cristais pendem do teto do túnel a intervalos de 20 metros, irradiando uma luz suave, apenas suficiente para que se veja por onde anda. À medida que seus olhos vão pouco a pouco se acostumando à quase escuridão, você começa a ver movimentos à sua volta. Aranhas e besouros sobem e descem pelas paredes entalhadas, desaparecendo em frestas e gretas ao sentir sua aproximação; ratazanas e ratos correm pelo chão à sua frente. Pingos de água caem em pequenas poças com um sinistro som gotejante que ecoa pelo túnel. O ar é frio, úmido e pesado. Depois de caminhar lentamente pelo túnel por uns cinco minutos, você chega a uma mesa de pedra encostada contra a parede à sua esquerda. Nela há seis caixas, uma das quais tem o seu nome pintado na tampa. Se você quiser abrir a caixa, vá para 270. Se preferir continuar caminhando para o norte, vá para 66.")

    escolha = input("\nIr para 270 ou 66?: \n")

    match escolha:
        case "270":
            aventura51(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome)
        case "66":
            aventura66()
        case _:
            print("Opção Invalida!")
#morte
def aventura2():
    print(stats_final)
    print("")
    print("CAP 2\n")
    print("\nO Escorpião consegue prendê-lo nas garras por tempo suficiente para mover a cauda segmentada para frente, por sobre a cabeça, e cravar em você o ferrão venenoso. O efeito é fatal, e você desaba no chão da Arena da Morte, imaginando se Throm conseguirá vencer.")

    fim_de_jogo()
#morte
def aventura3():
    print(stats_final)
    print("")
    print("CAP 3\n")
    print("\nO Gnomo sacode a cabeça e diz: 'Temo que você não tenha passado pela Prova dos Campeões. Os segredos do Calabouço da Morte do Barão Sukumvit ficarão guardados por mais um ano, pois você não terá permissão para sair daqui. Você foi indicado para ser meu servo pelo resto dos seus dias; preparará e modificará o subterrâneo para competidores futuros. Talvez em outra vida você tenha sucesso...' ")

    fim_de_jogo()
#morte
def aventura4():
    print(stats_final)
    print("")
    print("CAP 4\n")
    print("\na escuridão total, você não vê a curva do cano para baixo. Escorrega e, incapaz de se segurar no cano cheio de limo, desliza pela borda. Seus gritos ecoam pelo tubo, enquanto você cai 50 metros até o fundo. Você fracassou na Prova dos Campeões.")

    fim_de_jogo()
#sorte
def aventura5():
    print(stats_final)
    print("")
    print("CAP 5\n")
    print("Você se arrasta pelo chão e se vê no covil de uma tribo de TROGLODITAS. Ao engatinhar passando por eles, sua bainha bate em uma pedra. Teste sua Sorte. Se você tiver sorte, vá para 185. Se você não tiver sorte, vá para 395.")

    if usar_sorte(sorte):
        print("Voce deu sorte!")
        input("Pressione Enter para seguir para 185")
        aventura185()
    else:
        print("Você deu má sorte!")
        input("Pressione Enter para seguir para 395")
        aventura395()


#batalha
def aventura6():
    print(stats_final)
    print("")
    print("CAP 6\n")
    print("\nSabendo que o Mantécora disparará os espinhos da cauda, Você corre para se proteger atrás de um dos pilares. Antes que consiga chegar lá, uma saraivada de espinhos voa pelo ar, e um deles penetra-lhe o braço. Você perde 2 pontos de ENERGIA. Se ainda estiver vivo, não perca tempo e ataque o Mantécora com espada, antes que ele possa disparar mais espinhos. \n\nMANTÉCORA\nHABILIDADE 11  	ENERGIA 11 \n\nSe você vencer, vá para 364.")
#morte
def aventura7():
    print(stats_final)
    print("")
    print("CAP 7\n")
    print("\nAntes que você tenha tempo de chegar a uma porta, o rochedo já está sobre você, que grita de dor e medo quando ele o esmaga no chão. Sua aventura termina aqui.")
    fim_de_jogo()
#morte
def aventura8():
    print(stats_final)
    print("")
    print("CAP 8\n")
    print("\nO Demônio do Espelho agarra-o pelo pulso. Imediatamente, ele começa a puxá-lo na direção do espelho. A força dele é incrível, e, apesar de todos os seus esforços, você não consegue evitar que o arraste progressivamente na direção do espelho. Quando ele toca o espelho, parece desaparecer diretamente através dele. Horrorizado, você vê seu próprio braço desaparecer, seguido pelo resto do corpo. Você está agora em um mundo de espelhos de outra dimensão, do qual jamais retornará.")

    fim_de_jogo()
#nrm
def aventura9():
    print(stats_final)
    print("")
    print("CAP 9\n")
    print("Os Hobgoblins não têm nada que lhe seja útil, por isso você resolve abrir o saco no chão. Dentro, acha uma moringa de barro arrolhada. Você a desarrolha e cheira o líquido que contém. O odor é penetrante e acre. Se quiser beber um pouco do líquido, vá para 158. Se quiser mergulhar um pedaço de pano nele, vá para 375.")
    
    escolha = input("\nIr para 158 ou 375?: \n")
    match escolha:
        case '158':
            aventura158()
        case '375':
            aventura375()
        case _:
            print("Opção Invalida!")
#nrm - provisoes arruinadas
def aventura10():
    print(stats_final)
    print("")
    print("CAP 10\n")
    print("Ainda correndo o mais rápido possível, você enfia a mão na mochila e tira o tubo de madeira. Seu plano é ficar sob a água, respirando pelo tubo. Com sorte, os Trogloditas pensarão que você será arrastado até a morte rio abaixo, pois a torrente desaparece nas profundezas da montanha. Você segura o tubo entre os dentes e mergulha na água. Segurando-se em um dos pilares da ponte embaixo d'água, você fica absolutamente imóvel por 10 minutos. Quando finalmente acha que os Trogloditas foram embora, você sobe à superfície e olha em volta. Não há ninguém à vista, e você sai do rio e atravessa a ponte para a margem norte. Quaisquer Provisões restantes que você possa ter estão agora encharcadas e imprestáveis. Risque-as de sua Folha de Aventuras. Você segue pela vasta caverna até que, finalmente, vê um túnel na parede do outro lado. Você caminha até uma pesada porta de madeira, que está trancada. Se você tiver uma chave de ferro, vá para 86. Se não tiver, vá para 276. ")

    if 'chave de ferro' in mochila:
        input("Você tem a chave de ferro. Pressione Enter para seguir para 86...")
        aventura86()
    else:
        input("Você não tem a chave de ferro. Pressione Enter para seguir para 276...")
        aventura276()


def aventura11():
    print(stats_final)
    print("")
    print("CAP 11\n")
    print("Você olha para baixo e vê os corpos esparramados dos Guardiões Voadores imóveis no chão. Então, começa a forçar o olho de esmeralda do ídolo para retirá-lo com a ponta da espada. Finalmente, ele se solta, e você fica surpreso com o peso da jóia. Esperando que possa ser útil mais tarde, você o coloca na mochila. Se quiser agora retirar o olho direito, vá para 140. Se preferir descer do ídolo, vá para 46.")

    escolha = input("\nIr para 140 ou 46?")
    match escolha:
        case '140':
            aventura140()
        case '46':
            aventura46()
        case _:
            print("Opção Invalida.")

def aventura12():
    print(stats_final)
    print("")
    print("CAP 12\n")
    print("\nA porta abre para um grande aposento iluminado por velas, repleto das mais extraordinárias estátuas, de aparência real, representando guerreiros e cavaleiros. Um velho de cabelos brancos, trajando trapos esfarrapados, salta de trás de uma das estátuas e começa a dar risinhos. Uma centelha nos olhos dele faz com que você pense que algo se esconde por trás daquela aparência de idiota. Numa voz estridente, ele diz: 'Bom, mais uma pedra para meu jardim. Fico feliz que você tenha vindo se juntar a seus amigos. Sou um homem justo, e por isso vou lhe fazer uma pergunta. Se responder corretamente, ficará livre - mas, se sua resposta estiver errada, eu o transformarei em pedra!' Ele volta a dar risadinhas, obviamente feliz com sua chegada. Você: \nEsperará pela pergunta? - Vá para 382 \nVai atacá-lo com sua espada?	- Vá para 195 \nCorrerá para a porta? - Vá para 250.")
    
    escolha = input("\nIr para 382, 195 ou 250?: \n")
    match escolha:
        case '382':
            aventura382()
        case '195':
            aventura195()
        case '250':
            aventura250()
        case _:
            print("\nOpção Invalida.")

def aventura13():
    print(stats_final)
    print("")
    print("CAP 13\n")
    print("\nO túnel faz uma curva abrupta para a esquerda e se dirige para o norte, tanto quanto a sua vista alcança. As pegadas que você está seguindo começam a sumir à medida que o túnel vai ficando mais seco. Logo não vê mais o teto gotejante e as poças no chão. Você repara que o ar está se tornando mais quente, e se vê ofegante, embora esteja andando bem devagar. Em uma pequena reentrância da parede da esquerda, você vê um pedaço de bambu na vertical. Levantando-o, repara que ele está cheio de um líquido claro. Sua garganta está dolorosamente seca, e você se sente um pouco tonto por causa do calor no túnel. Se quiser beber o líquido, vá para 141. Se não quiser se arriscar a beber e preferir continuar para o norte, vá para 182.")
    
    escolha = input("\nIr para 141 ou 182?: \n")
    match escolha:
        case '141':
            aventura141()
        case '182':
            aventura182()
        case _:
            print("\nOpção Invalida")

def aventura14():
    print(stats_final)
    print("")
    print("CAP 14\n")
    print("\nO túnel conduz a uma câmara escura, coberta de espessas teias de aranha. Abrindo caminho entre elas, você tropeça em um pequeno cofre de madeira. Se quiser tentar abrir o cofre, vá para 157. Se preferir continuar para o norte, vá para 310.")

    escolha = input("Ir para 157 ou 310?: \n")
    match escolha:
        case '157':
            aventura157()
    match escolha:
        case '310':
            aventura310()
        case _:
            print("\nOpção Invalida.")

def aventura15():
    print(stats_final)
    print("")
    print("CAP 15\n")
    print("\nUma sensação de cócegas desce pela sua espinha enquanto você se arrasta cuidadosamente para fora do aposento. De volta ao túnel, você solta um suspiro de alívio e fecha a porta com força. Feliz com sua boa sorte, parte para o oeste mais uma vez. Vá para 74.")
    input("Pressione Enter para ir para 74...")
    aventura74()
#GEMAS - Arrumar HP
def aventura16():
    print(stats_final)
    print("")
    print("CAP 16\n")
    print("\nVocê só teve tempo de ouvir o Gnomo dizer: 'Três crânios', antes que um raio branco de energia disparasse da fechadura e o atingisse no peito, derrubando-o inconsciente. Jogue um dado, some 1 ao número obtido e reduza este total da sua ENERGIA. Se você ainda estiver vivo, recupera a consciência e o Gnomo manda que tente de novo. Você escolheu as gemas erradas da outra vez; portanto, não tentará aquela combinação novamente. \n\n   A                B             C\nESMERALDA       DIAMANTE       SAFIRA          FIQUE EM 16\nDIAMANTE         SAFIRA       ESMERALDA        VÁ PARA 392\nSAFIRA          ESMERALDA       DIAMANTE       VÁ PARA 177\nESMERALDA       SAFIRA       DIAMANTE          VÁ PARA 287\nDIAMANTE       ESMERALDA       SAFIRA          VÁ PARA 132\nSAFIRA          DIAMANTE      ESMERALDA        VÁ PARA 249")
    escolha = input("Ficar em 16 ou ir para 392, 177, 287, 132 ou 249")
    match escolha:
        case '16':
            aventura16()
        case '392':
            aventura392()
        case '177':
            aventura177()
        case '287':
            aventura287()
        case '132':
            aventura132()
        case '249':
            aventura249()
        case _:
            print("\nOpção Invalida.")

def aventura17():
    print(stats_final)
    print("")
    print("CAP 17\n")
    print("\nVocê não é forte o bastante para forçar e abrir a pesada porta. A água já está na cintura agora, e você está exausto por causa dos esforços. O nível da água sobe rapidamente, e você se vê boiando cada vez mais alto. Até que seu rosto fica imprensado contra o teto. Logo fica completamente imerso e não tem como prender a respiração por mais tempo. Sua aventura termina aqui. ")

    fim_de_jogo()

#JOGAR DADO 
def aventura18():
    print(stats_final)
    print("")
    print("CAP 18\n")
    print("\nPara sorte sua, os dentes da naja se cravam na munhequeira de couro que você está usando. A serpente se enrosca de novo bem depressa, pronta para lançar outro ataque, quando o Anão ordena que você faça mais uma tentativa. Jogue dois dados. Se o total for igual ou menor que sua HABILIDADE, vá para 55. Se o total for maior que sua HABILIDADE, vá para 202 ")
    sorte = input()#<-- dados jogados, IF dado <= sua habilidade = aventura55()  -----> elif dado >= sua habilidade = aventura202()
#morte
def aventura19(): 
    print(stats_final)
    print("\nCAP 19")
    print("\nVocê não consegue resistir ao olhar hipnótico da Medusa quando seus olhares se encontram. Sente os membros enrijecerem e entra em pânico, indefeso, enquanto se transforma em pedra. Sua aventura termina aqui.")
    
    fim_de_jogo()

def aventura20(energia, habilidade, sorte, stats_final):
    print(stats_final)
    print("\nCAP 20")
    print("\nSomente sua incrível força poderia resistir à mordida da aranha venenosa. Contudo, você está enfraquecido e repara que sua mão está tremendo ao colocar a Peça de Ouro no bolso. Reduza sua HABILIDADE em 1 ponto. Você amaldiçoa a pessoa que largou a mochila e parte para o norte de novo. Vá para 279. ")

    energia = energia - 1

    stats_final = (f"\nx---SEU PERSONAGEM--x\n|Habilidade = {habilidade}\n|Energia = {energia}\n|Sorte = {sorte}\nx---------x---------x\n")

    input("\nPressione Enter para retornar para 279...")

    aventura279()

def aventura21():
    print(stats_final)
    print("\nCAP 21")
    print("O ferimento não teve qualquer efeito sobre a Besta Sangrenta, que continua a atacá-lo tão furiosamente quanto antes. Continue o combate e, logo que vença uma Série de Ataques. Teste sua Sorte. Se você tiver sorte, vá para 97. Se não tiver sorte, vá para 116.")

    x = roda_1_dado()
    print(f"\nO dado 1 tirou: {x}.")
    y = roda_1_dado()
    print(f"\nO dado 2 tirou: {y}.")
    soma = x + y

    print(f"\nA soma dos dados deu {soma}, sua sorte é {sorte}.")

    if soma <= sorte:
        input("\nVoce deu sorte!\nPressione Enter para ir para 97...")
        sorte = sorte - 1

        aventura97()

    else:
        input("\nVocê não teve sorte!\nPressione Enter para ir para 116...")
        sorte = sorte - 1

        aventura116()




def aventura22():
    print(stats_final)
    print("\nCAP 22")
    print("\nEmbora vocês fiquem um pouco perturbados na companhia um do outro, sabendo que só pode haver um vencedor na Prova dos Campeões, ambos estão contentes por compartilhar os benefícios de uma aliança temporária. Contam um ao outro as explorações que fizeram até agora, falam dos monstros e armadilhas que encontraram e dos perigos que venceram. Caminhando em frente, vocês logo chegam à borda de um poço largo. É profundo e escuro demais para verem-lhe o fundo. O Bárbaro se oferece para ajudá-lo descer ao fundo com a corda dele, dizendo que tem uma tocha com a qual você poderá iluminar o caminho. Você:\n\nAceitará a oferta do Bárbaro? - Vá para 63\nOferece-se para ajudar a descida dele, já que ele está tão ansioso para investigar o poço? - Vá para 184\nSugerirá que, em vez disso, ambos pulem por cima do poço? - Vá para 311 ")
    escolha = input("\nIr para 63, 184 ou 311?: ")

    match escolha:
        case '63':
            aventura63()
        case '184':
            aventura184()
        case '311':
            aventura311()
        case _:
            print("\nOpção Invalida!")
            aventura22()

def aventura23():
    print(stats_final)
    print("\nCAP 23")
    print("\nO papel traz uma advertência simples, escrita em sangue seco: 'Cuidado com os Juízes da Prova.' Você recoloca o papel no prego e corre de volta pelo túnel para se reunir ao Bárbaro. Vá para 154.")

    input("\nPressione Enter para ir para 154...")
    aventura154()

def aventura24():
    print(stats_final)
    print("\nCAP 24")
    print("\nColocada em uma alcova em arco na parede do túnel, você vê uma cadeira de madeira ornamentada, esculpida na forma de uma ave de rapina de aparência demoníaca. Se você quiser se sentar na cadeira, vá para 324. Se preferir continuar seguindo para o norte, vá para 188. ")
    escolha = input("Ir para 324 ou 188?: ")
    match escolha:
        case '324':
            aventura324()
        case '188':
            aventura188()
        case _:
            print("Opção Invalida!")
            aventura24()

def aventura25():
    print(stats_final)
    print("\nCAP 25")
    print("\nEmbora a temperatura no túnel esteja mais alta do que você conseguiria normalmente tolerar, o líquido do bambu mantém-no vivo. Vá para 197. ")

    input("Pressione Enter para ir para 197...")

    aventura197()

def aventura26(habilidade):
    print(stats_final)
    print("\nCAP 26")
    print("\nA pílula faz com que você se sinta mole e letárgico. Você perde 2 pontos de HABILIDADE. O Anão diz que agora você pode prosseguir para o segundo estágio do teste. Ele pega uma cesta de vime e lhe diz que ela contém uma serpente. Vira a cesta e a serpente cai no chão. É uma naja, e se ergue no ar, pronta para dar o bote. O Anão diz que pretende testar suas reações. Você deverá agarrar a naja, com as mãos nuas, pelo pescoço, evitando as presas mortais. Você se agacha, tensionando os músculos para o momento decisivo. Jogue dois dados. Se o total for igual ou menor que sua HABILIDADE, vá para 55. Se o total for maior que sua HABILIDADE, vá para 202. ")

    habilidade = habilidade - 2


    input("\nAperte Enter para rodar os dados...")
    x = roda_1_dado()
    print(f"\nO dado 1 tirou: {x}.")
    y = roda_1_dado()
    print(f"\nO dado 2 tirou: {y}.")
    soma = x + y

    print(f"\nA soma dos dados deu {soma}, sua habilidade é {habilidade}.")

    if soma <= sorte:
        input("\nVoce deu sorte!\nPressione Enter para ir para 55...")
        aventura55()

    else:
        input("\nVocê não teve sorte!\nPressione Enter para ir para 202...")
        aventura202()

def aventura27():
    print(stats_final)
    print("\nCAP 27")
    print("\nVocê caminha até o apavorado homem e corta a corrente com sua espada. Ele cai de joelhos e se inclina, agradecendo, repetidamente. Diz que, há quatro anos, entrou na Prova dos Campeões, mas fracassou. Ele caiu em um poço e teve que ser resgatado por um Juiz da Prova, um dos administradores do calabouço do Barão Sukumvit. Foi-lhe, então, oferecida a opção de morrer ou servir como lacaio no Calabouço da Morte. Para sobreviver, ele trabalhou como escravo, até que não pôde mais suportar e tentou escapar. Lástima, não teve êxito e foi capturado pelos Orcas, os guardas volantes do Juiz da Prova. Como corretivo, cortaram-lhe uma das mãos e condenaram-no a um ano de prisão nessa cela. Você pergunta se ele tem alguma informação que lhe possa ser útil. Ele coça a cabeça: “Bem, não cheguei a me sair exatamente bem aqui, mas, de fato, sei que você precisa juntar gemas e pedras preciosas, se espera escapar. Não sei por que, mas é isso.” Sem mais dizer, o esfarrapado prisioneiro dispara para fora do aposento, virando à esquerda no túnel. Você resolve prosseguir para o norte e vira à direita no túnel. Vá para 78. ")

    input("\nPressione Enter para seguir para 78...")
    aventura78()

def aventura28(habilidade):
    print(stats_final)
    print("\nCAP 28")
    print("\nA cota de malha do Anão é de ferro da melhor qualidade, obviamente feita por um mestre armeiro. Você a tira do corpo dele e a coloca sobre sua cabeça. Acrescente 1 ponto de HABILIDADE. Não há mais nada de útil na câmara, portanto você decide investigar o novo túnel. Vá para 213. ")

    habilidade = habilidade + 1

    input("\nPressione Enter para seguir para 213...")
    aventura213()

def aventura29():
    print(stats_final)
    print("\nCAP 29")
    print("\nO túnel conduz ao norte por alguma distância, antes de chegar a um beco sem saída. A entrada de um escorrega se projeta da parede leste do túnel. Parece ser a única maneira de sair. Você resolve se arriscar e sobe no escorrega. Deslizando suavemente, você desce em um aposento, onde aterrissa de costas. Vá para 90.")

    input("Pressione Enter para ir para 90...")
    aventura90()

def aventura30(sorte):
    print(stats_final)
    print("\nCAP 30")
    print("\nDando um passo à frente, você salta para a borda do outro lado do poço. Teste sua Sorte. Se você tiver sorte, vá para 160. Se não tiver sorte, vá para 319. ")

    input("Pressione Enter para rodar os dados...")
    x = roda_1_dado()
    print(f"\nO dado 1 tirou: {x}.")
    y = roda_1_dado()
    print(f"\nO dado 2 tirou: {y}.")
    soma = x + y

    print(f"\nA soma dos dados deu {soma}, sua sorte é {sorte}.")

    if soma <= sorte:
        input("\nVoce deu sorte!\nPressione Enter para ir para 160 ...")
        sorte = sorte - 1
        aventura160()

    else:
        input("\nVocê não teve sorte!\nPressione Enter para ir para 319...")
        sorte = sorte - 1
        aventura319()

def aventura31():
    print(stats_final)
    print("\nCAP 31")
    print("\nO Gnomo sorri e diz: “Bom. Agora, você possui uma safira?” Se você de fato tiver uma safira, vá para 376. Se não, volte para 3. ")
    if 'safira' in mochila:
        input("\nVocê tem uma safira.\n\nPressione Enter para ir para 376...")
        aventura376()
    elif 'safira' not in mochila:
        input("\nVocê não possui uma safia.\n\nPressione Enter para voltar para 3...")
        aventura3()

def aventura32():
    print(stats_final)
    print("\nCAP 32")
    print("\nVocê logo chega a uma outra encruzilhada no túnel. Um braço leva para o leste, mas as pegadas úmidas que você vem seguindo continuam para o norte, e você resolve continuar na trilha delas. Vá para 37. ")

    input("Pressione Enter para ir para 37...")

    aventura37()

def aventura33(habilidade):
    print(stats_final)
    print("CAP 33")
    print("\nFoi um erro ter tateado no interior do buraco com o braço da espada. Está coberto de marcas de sucção e dá a sensação de ter sido esmagado. Você perde 3 pontos de HABILIDADE. Você dá uma espiada para dentro do buraco e vê o toco do tentáculo ensanguentado que pende inerte. Cuidadosamente, retira o gancho e a bolsa de couro, na qual encontra um minúsculo sino de latão. Você guarda suas novas posses na mochila e segue para o norte. Vá para 292. ")

    habilidade = habilidade - 3

    input("\nPressione Enter para ir para 292...")
    aventura292()

def aventura34():
    print(stats_final)
    print("\nCAP 34")
    print("\nVocê tenta forçar por baixo da esmeralda com a ponta da espada. Para sua grande surpresa, a esmeralda se despedaça com o contato, soltando um jato de gás venenoso diretamente no seu rosto. O gás o faz desmaiar, e você solta a corda, despenca do ídolo e cai no chão de pedra. Sua aventura termina aqui. ")

    fim_de_jogo()

def aventura35():
    print(stats_final)
    print("\nCAP 35")
    print("\nO túnel continua para o oeste por várias centenas de metros, terminando finalmente em alguns degraus que conduzem a um alçapão fechado. Você sobe os degraus lentamente, ouvindo vozes abafadas acima. Na penumbra, você pode ver que o alçapão não está trancado. Se quiser bater na porta do alçapão, vá para 333. Se preferir irromper pela porta com a espada desembainhada, vá para 124. ")
    escolha = input("Ir para 333 ou 124?: ")
    match escolha:
        case '333':
            aventura333()
        case '124':
            aventura124()
        case _:
            print("Opção Invalid!")
            aventura35()

def aventura36(energia, habilidade):
    print(stats_final)
    print("\nCAP 36")
    print("\nEmbora você jamais tenha corrido tanto em toda a sua vida, o rochedo chega cada vez mais perto. Jogue dois dados. Se o total for igual ou menor que os seus índices tanto de HABILIDADE quanto de ENERGIA, vá para 340. Se o total for maior que qualquer um dos seus índices de HABILIDADE ou ENERGIA, volte para 7. ")

    x = roda_1_dado()
    input("Pressione Enter para rodar os dados...")
    print(f"\nO valor do dado 1 é: {x}")
    input("\n...")
    y = roda_1_dado()
    print(f"\nO valor do dado 2 é: {y}")
    soma = x + y
    print(f"\nA soma dos dados é {soma}")
    input("\n...")

    print(f"\nSua habilidade é {habilidade}\nSua energia é {energia}")

    if soma > energia or soma > habilidade:
        input("\n...")
        input("\nO valor dos dados é maior que sua habilidade/energia.\nPressione Enter para ir para 7...")
        aventura7()
    else:
        input("\n...")
        input(f"O valor dos dados é maior que sua habilidade/energia.\nPressione Enter para seguir para 340...")
        aventura340()

def aventura37():
    print(stats_final)
    print("\nCAP 37")
    print("\nA passagem se alarga em uma ampla caverna, mais escura, mas muito mais seca. As pegadas desaparecem gradualmente à sua frente. Há um grande ídolo no centro da caverna, com cerca de seis metros de altura. Os olhos da estátua são jóias, cada uma do tamanho do seu punho. Duas criaturas empalhadas, com aparência de pássaros, encontram-se de pé em cada lado do ídolo. Se você quiser subir no ídolo para pegar as jóias, vá para 351. Se preferir atravessar a caverna para o túnel na parede do outro lado, vá para 239. ")

    escolha = input("Ir para 351 ou 239?")
    match escolha:
        case '351':
            aventura351()
        case '239':
            aventura239()
        case _:
            print("Opção Invalida!")
    
def aventura38(energia):
    print(stats_final)
    print("\nCAP 38")
    print("\nEm silêncio, o homem fica de lado enquanto você engole a água e devora o pão. Uma dor aguda lhe invade o estômago, e você cai de joelhos. O velho olha para você com desprezo e diz: “Bem, o que pode esperar quem come comida envenenada?”. Você perde 3 pontos de ENERGIA. Ele se afasta, arrastando os pés, e o deixa se contorcendo em dores no chão. Se ainda estiver vivo, você acaba recuperando força bastante para continuar para o oeste. Vá para 109. ")
    energia = energia - 3

    if energia > 0:
        input("Você consegue sair vivo, porém está ferido.\nPressione Enter para seguir para 109...")
        aventura109()
    else:
        fim_de_jogo()


def aventura39(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome):
    print("\nVocê consegue se desviar das pernas estendidas da Mosca Gigante que mergulha sobre você. Recuando, você desembainha a espada e se prepara para lutar contra o horroroso inseto, quando ele se volta para atacá-lo outra vez. \n\nMOSCA GIGANTE        HABILIDADE 7        ENERGIA 8\n\nSe você vencer, vá para 111. Você pode Fugir, correndo de volta para o túnel, para prosseguir para o norte. Vá para 267. ")
    habilidade_monstro = 7
    energia_monstro = 8
    nome = "MOSCA GIGANTE"


    batalha_fuga(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome)

    print(energia_monstro)

    if energia_monstro <= 0:
        input("Pressione Enter para ir para 111...")
        aventura111()
    if energia_monstro > 0:
        input("Pressione Enter para ir para 267...")
        aventura267()

def aventura40(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome):
    print(stats_final)
    print("\nCAP 40")
    print("\nVocê chama o Anão, dizendo que está pronto para lutar contra o MINOTAURO. A porta de madeira se ergue lentamente, e você vê a assustadora fera, meio homem, meio touro, entrar na arena. Ele bufa e expele vapor pelas narinas, enquanto vai ficando mais e mais furioso, pronto para atacar. Súbito, arranca adiante, girando uma acha de dois gumes.\n\nMINOTAURO        HABILIDADE 9        ENERGIA 9\n\nSe você vencer, vá para 163.")

    habilidade_monstro = 9
    energia_monstro = 9
    nome = "MINOTAURO"

    batalha(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome)

    input(f"\nVocê derrotou o {nome}!\n\nPressione Enter para ir para 163...")

    aventura63()

def aventura41():
    print(stats_final)
    print("CAP 41")
    print("\nVocê caminha lentamente para a alcova, verificando cuidadosamente o chão para não cair em outras armadilhas ocultas. Você vê que a taça contém um líquido vermelho efervescente. Você:\n\nBeberá o líquido vermelho? - Vá para 98\nDeixará a taça e caminhará de volta para procurar o Bárbaro (se você ainda não tiver feito isso)? - Vá para 126\nDeixará a câmara para continuar para o oeste? - Vá para 83")

    escolha = input("\nIr para 98, 126 ou 83...")

    match escolha:
        case '98':
            aventura98()
        case '126':
            aventura126()
        case '83':
            aventura83()
        case _:
            print("Opção Invalida!")
            aventura41()


def aventura42(habilidade, energia):
    print(stats_final)
    print("\nCAP 42")
    print("\nOs dentes da naja se cravam fundo no seu pulso e você sente o veneno se alastrando pelo corpo. Você perde 5 pontos de ENERGIA. Se você ainda estiver vivo, o Anão não tem pena, e lhe diz para tentar outra vez. Jogue dois dados. Se o total for igual ou menor que sua HABILIDADE, vá para 55. Se o total for maior, vá para 202. ")

    energia = energia - 5

    if energia > 0:

    
        x = roda_1_dado()
        print(f"\nO dado 1 tirou: {x}.")
        y = roda_1_dado()
        print(f"\nO dado 2 tirou: {y}.")
        soma = x + y

        print(f"\nA soma dos dados deu {soma}, sua habilidade é {habilidade}.")

        if soma <= sorte:
            input("\nSua habilidade é maior que o valor dos dados!\nPressione Enter para ir para 55...")
            aventura55()

        else:
            input("\nVocê não teve sorte!\nPressione Enter para ir para 202...")
            aventura202()
    else:
        fim_de_jogo()



def aventura43():
    print(stats_final)
    print("\nCAP 43")
    print("\nO túnel vira abruptamente para a direita e continua para o norte, até onde a vista alcança. Há uma porta entreaberta na parede do lado esquerdo. Você ouve alguém gritando por socorro, a voz vindo do outro lado da porta. Se você quiser abrir a porta, vá para 200. Se preferir continuar para o norte, vá para 316. ")

    escolha = input("Ir para 200 ou 316?: ")
    match escolha:
        case '200':
            aventura200()
        case '316':
            aventura316()
        case _:
            print("Opção Invalida!")
            aventura43()


def aventura44():
    print("\nVocê está a apenas alguns metros da porta quando ouve o velho atrás de si enunciar umas palavras estranhas. Instantaneamente, sente os músculos endurecerem e a pele esticar. Você entra em pânico, mas não há nada que possa fazer para impedir a petrificação do seu corpo. Sua aventura termina aqui. ")

    fim_de_jogo()


def aventura45():
    print(stats_final)
    print("\nAP 45")
    print("\nO disco, afiado como uma navalha, atinge-lhe as costas com terrível efeito. Você perde 1 ponto de HABILIDADE e 4 pontos de ENERGIA. Se ainda estiver vivo, você luta para se tirar o disco das costas, enquanto o Ninja lhe atira mais um. Vá para 312 ")


    habilidade = habilidade - 1
    energia = energia - 4

    if energia > 0:
        input("\nVocê sobrevive, porém fica ferido.\n\nPressione Enter para ir para 312...")
        aventura312()

    else:
        fim_de_jogo()


def aventura46():
    print(stats_final)
    print("\nCAP 46")
    print("\nVocê desce cuidadosamente do ídolo e, sem perder mais tempo na caverna, corre para o túnel adiante na parede norte. Vá para 239. ")

    input("Pressione Enter para ir para 239...")
    aventura239()


def aventura47():
    print(stats_final)
    print("\nCAP 47")
    print("\nVocê tem um tubo oco de madeira? Se tiver, volte para 10. Se não tiver, vá para 335. ")

    if 'tubo oco de madeira' in mochila:
        input("Você tem um tubo oco de madeira na mochila.\n\nPressione Enter para ir para 10...")

        aventura10()

    else:
        input("Você não tem um tubo oco de madeira.\n\nPressione Enter para ir para 335...")
        
        aventura335()


def aventura48():
    print(stats_final)
    print("\nCAP 48")
    print("\nSomente sua força imensa e determinação inquebrantável evitam que você caia inconsciente ao solo. Você aperta os dentes e, resoluto, segue adiante. Vá para 197.")

    input("\nPressione Enter para ir para 197...")
    aventura197()


def aventura49():
    print(stats_final)
    print("\nCAP 49")
    print("\nVocê dá uma espiada, virando a esquina, e vê duas pequenas criaturas correndo de você. Vestem roupas largas e usam chapéus pontudos e desengonçados. São os travessos LEPRECHAUNS. Se você quiser segui-los, vá para 205. Se preferir caminhar de volta para a última encruzilhada e seguir para o norte, vá para 241. ")

    escolha = input("Ir para 205 ou 241?: ")
    match escolha:
        case '205':
            aventura205()
        case '241':
            aventura241()
        case _:
            print("Opção Invalida!")
            aventura49()




def aventura50():
    print(stats_final)
    print("\nCAP 50")
    print("\nVocê acorda e vê Throm puxando o anel do seu dedo. Ele joga o anel no chão e o esmaga com a acha de guerra. Em seguida, grunhindo para expressar que desaprova sua atitude, sai caminhando para o leste. Com esforço, você se levanta e o segue cambaleante. Vá para 221. ")

    input("\nPressione Enter para ir para 221...")

    aventura221()


def aventura51(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome):
    print(stats_final)
    print("\nCAP 51")
    print("\nOs Hobgoblins não estão preparados para o seu ataque, e você consegue matar o primeiro antes que ele possa puxar da espada. Você se volta para enfrentar o outro Hobgoblin, que rosna de ódio.\n\nHOBGOBLIN        HABILIDADE 6        ENERGIA 5 \n\nSe você vencer, volte para 9. ")
    habilidade_monstro = 6
    energia_monstro = 5
    nome = "HOGOBLIN"


    batalha(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome)

    input("\nVocê derrotou o HOGOBLIN!\n\nPressione Enter para voltar para 9...")

    aventura9()


def aventura52():
    print(stats_final)
    print("\nCAP 52")
    print("\nAo abrir o livro, você vê que ele começa a se desintegrar. As páginas se transformando em poeira nas suas mãos. Mas você consegue salvar alguns fragmentos e ler o manuscrito. O livro parece ser sobre monstros, e, do que você pode concluir, contém uma descrição completa de um ser chamado Besta Sangrenta. É uma horrível criatura inchada, com pele grossa e coberta de espinhos e úlceras faciais que se abrem para se tornar falsos olhos, cujo objetivo é esconder o único ponto fraco da Besta Sangrenta - seus olhos verdadeiros. Essas monstruosidades geralmente habitam poços de lodo fétido que exalam gás venenoso, tão forte que pode facilmente deixar uma pessoa inconsciente. A Besta Sangrenta, embora pesada demais para sair da poça de lodo, tem uma língua longa e poderosa que se enrosca em torno de suas vítimas para arrastá-las para o interior da poça. Quando a carne das vítimas começa a apodrecer no lodo abjeto, a Besta Sangrenta a devora. Você conta a Throm sobre a grotesca Besta Sangrenta, mas ele simplesmente sacode os ombros e lhe diz para seguir adiante. Se você ainda não o fez, poderá abrir o livro preto - vá para 138. Do contrário, você deve prosseguir para o norte com Throm - vá para 369. ")  

    escolha = input("\nIr para 138 ou 360?: ")
    match escolha:
        case '138':
            aventura138()
        case '360':
            aventura360()
        case _:
            print("\nOpção Invalida!")
            aventura52()


def aventura53():
    print(stats_final)
    print("\nCAP 53")
    print("\nA Besta Sangrenta é inchada demais para sair da poça, mas, com a longa e poderosa língua, varre as cercanias e tenta alcançar a sua perna. Felizmente, você caiu fora do seu alcance. O ar, ao nível do chão, não contém nenhum dos vapores venenosos, mas você acorda com dor na garganta. Você cobre a boca com a manga da camisa para poder respirar através dela, e decide o que fazer. \n\nSe você quiser correr, contornando a poça, na direção do túnel, vá para 370. \nSe preferir atacar a Besta Sangrenta com sua espada, vá para 348. ")

    escolha = input("\nIr para 370 ou 348?: ")
    match escolha:
        case '370':
            aventura370()
        case '348':
            aventura348()
        case _:
            print("\nOpção Invalida!")
            aventura52()


def aventura54():
    print(stats_final)
    print("\nCAP 54")
    print("\nO laço se solta e você consegue tirá-lo do pescoço do ídolo com uma sacudidela. Ele cai ao chão com um ruído alto. Você enrola a corda rapidamente e a coloca na mochila. Sem perder mais tempo na caverna, corre para o túnel na parede norte. Vá para 239.")

    input("\nPressione Enter para ir para 239...")

    aventura239()


def aventura55():
    print(stats_final)
    print("\nCAP 55")
    print("\nCom a velocidade de um raio, você estica a mão e segura a naja logo abaixo da boca aberta. Você a ergue e, como braço estendido, sacode-a na frente do Anão. Ele fica impassível, mas, com seu jeito calmo e sem expressão, diz: “Por favor, coloque a naja de volta na cesta e prepare-se para a parte final do teste. Siga-me.” Você faz o que ele disse e o segue de volta para a câmara, onde Throm está andando de um lado para o outro, evidentemente nervoso. Você acena para ele, enquanto o Anão abre uma segunda porta secreta e manda que você entre por ela e espere por ele. Outra vez você obedece, e se vê em outro aposento circular, embora este se assemelhe a uma pequena arena. O chão é coberto de areia, e uma pequena sacada circunda a parede da arena. No lado oposto ao da porta secreta pela qual você entrou, há uma porta de madeira de aparência agourenta. De repente, você ouve um grito, e olha para cima, vendo o Anão sorridente na sacada. Ele joga dois pedaços de papel para você. Num deles, estão escritas as palavras SEI PORCÃO, e no outro, RUIM NO ATO. Com a voz sempre calma, ele diz: “Se você rearrumar as letras das palavras, descobrirá os nomes de duas criaturas. Você pode escolher com qual delas quer lutar na minha Arena da Morte.” \n\nSe você puder identificar a criatura rearrumando as letras de SEI PORCÃO, vá para 143. \nSe puder identificar a criatura rearrumando as letras de RUIM NO ATO, volte para 40. \nSe você não puder identificar nenhuma das duas criaturas, vá para 347. ")

    criatura = input("\n\nDigite o nome da criatura que deseja lutar: ").capitalize()
    match criatura:
        case 'MINOTAURO':
            input("\nVocê escolheu lutar com MINOTAURO.\nPressione Enter para ir para 40...")
            aventura40()
        case 'ESCORPIÃO':
            input("\nVocê escolheu lutar com ESCORPIÃO.\nPressione Enter para ir para 143...")
            aventura143()
        case 'ESCORPIAO':
            input("\nVocê escolheu lutar com ESCORPIÃO.\nPressione Enter para ir para 143...")
            aventura143()
        case _:
            input("\nVocê não conseguiu identificar nenhuma das criatura.\nPressione Enter para seguir para 347...")
            aventura347()




def aventura56():
    print(stats_final)
    print("\nCAP 56")
    print("\nVocê vê que a obstrução é causada por um objeto grande e marrom, parecendo um rochedo. Você o toca com a mão e fica surpreso ao descobrir que é macio e esponjoso. \nSe você quiser tentar subir por cima dele, vá para 373. \nSe preferir cortá-lo ao meio com sua espada, vá para 215. ")

    escolha = input("\nIr para 373 ou 215?: ")
    match escolha:
        case '373':
            aventura373()
        case '215':
            aventura215()
        case _:
            print("Opção Invalida!")
            aventura56()

def aventura57(energia):
    print(stats_final)
    print("\nCAP 57")
    print("\nEmbora você já tenha examinado a arca cuidadosamente, em busca de quaisquer mecanismos ocultos, não consegue ver a armadilha dentro dela. Ao levantar a tampa, uma bola de ferro pendente de uma corda é lançada para trás, partindo a cápsula de vidro fixada no lado de dentro da tampa. Uma nuvem de gás venenoso é instantaneamente liberado no ar, e você cambaleia, recuando, enquanto tosse e se engasga. Você perde 4 pontos de ENERGIA. Se ainda estiver vivo, vá para 198. ")

    energia = energia - 4

    if energia >= 0:
        input("\nVocê sobrevive, mas saí ferido.\n\nPressione Enter para seguir para 198...")
        
        aventura198()

    else:
        fim_de_jogo()


def aventura58():
    print(stats_final)
    print("\nCAP 58")
    print("\nVocê caminha lentamente entre os postes, tomando cuidado para não tocar em nenhum deles. Jogue dois dados. Se o total for igual ou menor que seu índice de HABILIDADE, vá para 80. Se o total for maior que seu índice de HABILIDADE, vá para 246. ")

    x = roda_1_dado()
    print(f"\nO dado 1 tirou {x}.")
    y  = roda_1_dado()
    print(f"\nO dado 2 tirou {y}.")
    soma = x + y
    if soma <= habilidade:
        print(f"\nSua Habilidade ({habilidade}) é maior do o total tirado nos dados ({soma}) ")
        input("\nPressione Enter para ir para 80...")
        aventura80()
    else:
        print(f"\nSua Habilidade ({habilidade}) é menor do o total tirado nos dados ({soma}) ")
        input("\nPressione Enter para ir para 246...")
        aventura246()




def aventura59():
    print(stats_final)
    print("\nCAP 59")
    print("\nAdiante, a distância, você ouve o som de passos lentos vindo na sua direção. Sem saber o que ou quem poderia estar se aproximando, você olha em volta, em busca de um lugar para se esconder. Encontra uma fenda grande na parede do túnel onde não bate luz. Se você quiser defrontar-se com o recém-chegado de espada na mão, vá para 341. Se preferir esconder-se nas sombras, vá para 283. ")

    escolha = input("\nIr para 341 ou 283?: ")
    match escolha:
        case '341':
            aventura341()
        case '283':
            aventura283()
        case _:
            print("\nOpção Invalida!")
            aventura59()

def aventura60():
    print(stats_final)
    print("\nCAP 60")
    print("\nO túnel termina em uma grande porta de carvalho. Throm não perde tempo e vai logo testando a maçaneta, ficando algo admirado ao descobrir que a porta não está trancada. Ele a empurra e vocês se deparam com uma câmara iluminada por tochas. Sentado sozinho em uma cadeira ornamentada, há um ANÃO, que os convida a entrar na câmara. Ao fazê-lo, a porta de carvalho se fecha atrás de vocês. “Aventureiros, vocês se saíram muito bem até agora”, diz o Anão com voz profunda. “Contudo, como vocês dois sabem, só pode haver um vencedor na Prova dos Campeões. Como Juiz da Prova, é minha obrigação para com o Barão Sukumvit só permitir que o mais capaz continue. Portanto, tenho que preparar um teste de inteligência e força para eliminar um de vocês. Por favor, não tentem livrar-se de mim. Seria completamente estúpido, pois, como vocês podem ver, não há nenhuma maneira óbvia de sair desta câmara, e somente eu sei onde está a saída oculta. Agora, se vocês não se importassem de decidir entre vocês quem irá primeiro, eu tratarei de fazer as preparações necessárias.” Você olha para Throm, subitamente com raiva de que a eficaz associação de vocês pudesse ter que terminar. Ele se inclina e sussurra no seu ouvido que vocês deveriam tentar matar o Anão e preocupar- se com a saída depois. Se você quiser unir-se a Throm no ataque ao Anão, vá para 179. Se você preferir convencer Throm seguir em frente com o teste do Anão, vá para 365. ")



    escolha = input("Ir para 179 ou 365?: ")
    match escolha:
        case '179':
            aventura179()
        case '365':
            aventura365()
        case _:
            print("\nOpção Invalida!")
            aventura59()


def aventura61():
    print(stats_final)
    print("\nCAP 61")
    print("\nApesar do terrível ruído de campainha nos seus ouvidos, você ouve passos descendo pelo túnel. Seus gritos altos atraíram um guardião do túnel. Há um HOBGOBLIN de pé junto a você. Ele sorri doentiamente enquanto pressiona a ponta da espada contra seu pescoço. Você não tem como se defender e impedir que ele o trespasse. Sua aventura termina aqui. ")

    fim_de_jogo()


def aventura62():
    print(stats_final)
    print("\nCAP 62")
    print("\nO Gnomo pula no ar, gritando: “Belo trabalho – ninguém jamais conseguiu encontrar todas as três gemas antes! Agora, prepare-separa o teste final, o qual eu explicarei uma vez e somente uma vez. Como você pode ver, a fechadura desta porta tem três ranhuras, com as etiquetas A, B e C, cada uma delas construída para aceitar uma gema específica. Você tem porque pôr uma das suas três gemas em cada uma das ranhuras na ordem certa. Se conseguir isso na primeira tentativa, ótimo. Porém, se puser as gemas nas ranhuras erradas, você será atingido por um raio de energia da fechadura, o que lhe causará ferimentos. De qualquer maneira, como eu disse, tenho permissão para ajudá-lo um pouco. Se você colocar uma gema em sua ranhura correta, mas puser as outras duas erradas, eu gritarei: ‘Uma coroa e dois crânios.’ Se você colocar todas as três gemas incorretamente, eu gritarei: ‘Três crânios.’ Você terá permissão para tentar repetidamente até que tenha êxito ou morra. Está pronto?” Você faz um aceno de cabeça e caminha adiante para colocar as três gemas nas ranhuras. Resolva que gemas colocará nas ranhuras com etiquetas: \n\n   A                B             C\nESMERALDA       DIAMANTE       SAFIRA          FIQUE EM 16\nDIAMANTE         SAFIRA       ESMERALDA        VÁ PARA 392\nSAFIRA          ESMERALDA       DIAMANTE       VÁ PARA 177\nESMERALDA       SAFIRA       DIAMANTE          VÁ PARA 287\nDIAMANTE       ESMERALDA       SAFIRA          VÁ PARA 132\nSAFIRA          DIAMANTE      ESMERALDA        VÁ PARA 249")

    escolha = input("Você irá para 16, 392, 177, 287, 132 ou 249?: \n")
    match escolha:
        case '16':
            aventura16()
        case '392':
            aventura392()
        case '177':
            aventura177()
        case '287':
            aventura287()
        case '132':
            aventura132()
        case '249':
            aventura249()
        case _:
            print("Opção invalida.")
            aventura62()


def aventura63():
    print(stats_final)
    print("\nCAP 63")
    print("\nVocê amarra a corda na cintura e segura a tocha que Throm, seu aliado Bárbaro, lhe dá, já acesa. Segurando a corda frouxa, Throm o vai descendo-o lentamente por sobre a borda do poço até as profundezas escuras. Você pode ver, com a luz da tocha, que os lados do poço são extremamente lisos. Você desce por uns 20 metros antes de chegar ao fundo do poço. Ali, vê um outro túnel que segue para o norte, e chama Throm para contar-lhe a descoberta. Ele responde, dizendo que vai amarrar a corda em uma rocha proeminente na borda do poço e descerá. Você ouve o Bárbaro descendo, e logo estão juntos de novo. Throm recupera a corda, sacudindo-a para soltá-la da rocha, e vocês partem para o norte pelo novo túnel. Vá para 194.")

    input("\nPressione Enter para ir para 194...")

    aventura194()


def aventura64(habilidade):
    print("\nLogo que você põe o anel no dedo, todo seu corpo começa a tremer. Jogue dois dados. Se o total for igual ou menor que o seu índice de HABILIDADE, vá para 115. Se o total for maior que o seu índice de HABILIDADE, vá para 190.")

    x = roda_1_dado()
    y  = roda_1_dado()
    soma = x + y
    if soma <= habilidade:
        print(f"\nSua Habilidade ({habilidade}) é maior do o total tirado nos dados ({soma}) ")
        input("\nPressione Enter para ir para 115...")
        aventura115()
    else:
        print(f"\nSua Habilidade ({habilidade}) é menor do o total tirado nos dados ({soma}) ")
        input("\nPressione Enter para ir para 190...")
        aventura190()



def aventura65():
    print("\nVocê bebeu uma Poção encontrada dentro de um livro de couro preto? Se beber, vá para 345. Se não, vá para 372.")

    if 'poção livro preto' in ativos:
        input("Pressione Enter para ir para 345...")
        aventura345()
    else:
        input("Pressione Enter para ir para 372..")
        aventura372()


def aventura66():
    print(stats_final)

    print("\nCAP 66")

    print(f"\n{stats_final}")

    print("\nDepois de caminhar pelo túnel por alguns minutos, você chega a uma encruzilhada. Uma seta branca pintada na parede aponta para o oeste. No chão, você vê pegadas molhadas, feitas por aqueles que entraram antes de você. É difícil ter certeza, mas parece que três deles seguiram a direção da seta, enquanto um resolveu ir para o leste. Se você quiser ir para o oeste, vá para 293. Se preferir ir para o leste, vá para 119.")

    escolha = input("\nIr para 293 ou 119?: \n")

    match escolha:
        case '293':
            aventura293()
        case '119':
            aventura119()
        case _:
            print("\nOpção Invalida!")
            aventura66()


def aventura67(sorte):
    print(stats_final)
    print("\nCAP 67")
    print("\nVocê se agarra a um dos pilares submersos da ponte e gruda nele, prendendo a respiração. Enquanto isso, os Trogloditas chegam à margem e concluem que você deve ter sido arrastado rio abaixo para morte certa, já que o rio desaparece nas profundezas da montanha. A essa altura, seus pulmões estão estourando de falta de ar. Teste sua Sorte outra vez. Se você tiver sorte, vá para 146. Se não tiver sorte, vá para 219. ")

    x = roda_1_dado()
    y  = roda_1_dado()
    soma = x + y
    if soma <= sorte:
        print(f"\nSua Sorte ({sorte}) é maior do o total tirado nos dados ({soma}) ")
        input("\nPressione Enter para ir para 146...")
        aventura146()
    else:
        print(f"\nSua Sorte ({sorte}) é menor do o total tirado nos dados ({soma}) ")
        input("\nPressione Enter para ir para 219...")
        aventura219()



def aventura68():
    print(stats_final)
    print("\nCAP 68")
    print("\nVocê desce a passagem e logo se encontra de pé na borda de um poço profundo e escuro. A passagem continua para o leste, do outro lado do poço. Você pensa que provavelmente conseguirá pular por cima do poço, mas não tem certeza. Há uma corda que pende do teto e desce sobre o centro do poço. Você: \n\nJogará seu escudo por cima do poço e depois pulará? - Vá para 271 \nPulará por cima do poço carregando todas as suas posses? - Volte para 30 \nUsará a espada para trazer a corda até você, de modo a poder usá-la para atravessar até a outra margem? - Vá para 212 ")

    escolha = input("\nIr para 271, 30 OU 212?: \n")

    match escolha:
        case '217':
            aventura217()
        case '30':
            aventura30()
        case '212':
            aventura212()
        case _:
            print("\nOpção Invalida!")
            aventura68()


def aventura69():
    print(stats_final)
    print("\nCAP 69")
    print("\nErva não nota que você abriu a porta. Você se esgueira para fora do aposento, fecha a porta silenciosamente e se vê no fim de um outro túnel. Vá para 305.")


    input("\nPressione Enter para ir para 305...")
    aventura305()


def aventura70():
    print(stats_final)
    print("\nCAP 70")
    print("\nVocê consegue mergulhar para o lado, por pouco, antes que o rochedo despenque sobre o chão do túnel, rachando a pedra. Enquanto se limpa, nota que há luz do sol no fim do túnel. Você corre para lá, alegre com a bela visão do céu azule das árvores verdes. Ao correr para fora do túnel, você espera ser cumprimentado por multidões vibrantes, mas fica horrorizado com o que vê. Não há recepção de herói que possa vir das pessoas à sua volta. Estão todos mortos. Você está, na realidade, de pé em uma câmara fria, o chão coberto de cadáveres e esqueletos com armaduras - a saída para a vitória era apenas uma ilusão! Só os restos dos aventureiros do passado são reais. Você corre de volta para o túnel, mas colide com uma barreira invisível. Você caiu na armadilha e está condenado a terminar seus dias na câmara dos mortos. ")

    fim_de_jogo()

def aventura71():
    print(stats_final)
    print("\nCAP 71")
    print("\nMais uma vez, você estica a mão para o pergaminho, só que dessa vez ele está em meio a uma pilha de ossos quebrados. Ao desenrolá-lo, você vê o mapa de um aposento com o desenho de uma criatura pavorosa dentro. Embaixo da figura do monstro, há uma rima que diz: \n\n“Se você encontrar o Mantécora,\nÉ bom de sua cauda cuidar.\nProteja-se dos espinhos\nQue irão voar pelo ar. \n\nVocê enrola o pedaço de pergaminho e o coloca na mochila. Repetindo a rima muitas vezes para si mesmo, você caminha para o outro lado, em direção à alcova. Vá para 128. ")

    input("Pressione Enter para ir para 128...")
    aventura128()


def aventura72(habilidade):
    global nv_habilidade, nv_statfinal
    print(f"{stats_final}\n")
    print("CAP 72\n")
    print("\nO Espelho se quebra, lançando fragmentos de vidro por toda parte. As quatro faces do Demônio do Espelho gritam de agonia, e aparecem rachaduras em todas elas. Em seguida, elas também se partem e caem ao chão numa pilha de cacos de vidro. Infelizmente ao quebrar o espelho, você cortou seriamente o braço com que segura a espada. Embora sua força não tenha sido afetada, sua habilidade com as armas foi prejudicada. Você perde 2 pontos de HABILIDADE antes de continuar na sua jornada para o norte. Vá para 122 ")
    
    nv_habilidade = alterar_habilidade(habilidade, -2)

    print(f"\nsua habilidade era {habilidade}")

    print(f"\nsua habilidade agora é {nv_habilidade} apos perder 2 pontos")

    input("\nAperte Enter para ir para 122...")

    nv_statfinal = (f"\nx---SEU PERSONAGEM--x\n|Habilidade = {nv_habilidade}\n|Energia = {energia}\n|Sorte = {sorte}\nx---------x---------x")

    aventura122()

    return habilidade




def aventura73():
    print(stats_final)
    print("\nCAP 73")
    print("\nSe você ainda não o tiver feito, poderá caminhar de volta à procura do Bárbaro - vá para 126. Do contrário, saia da câmara para continuar para o oeste - vá para 83.")

    escolha = input("\nIr para 126 ou 83?: ")
    match escolha:
        case '126':
            aventura126()
        case '83':
            aventura83()
        case _:
            print("\nOpção Invalida!")
            aventura73()


def aventura74():
    print(stats_final)
    print("\nCAP 74")
    print("\nO túnel faz uma curva fechada para a direita, e você se vê em uma espécie de galeria, coberta de espelhos por uns 20 metros. Um esqueleto humano parece estar sendo arrastado a meio caminho através de um espelho da parede da direita. Súbito, um ser grotesco, com quatro braços e quatro faces que gritam, emerge do espelho, barrando-lhe a passagem. Caminha lentamente na sua direção, todos os braços estendidos para agarrá-lo. É o DEMÔNIO DO ESPELHO, de outro plano dimensional, que veio para levar seu, espírito. Você:\n\nFará um desejo (se estiver usando um Anel dos Desejos)? - Vá para 265\nTentará quebrar os espelhos? - Vá para 300\nAtacará o Demônio do Espelho com sua espada? - Vá para 327")

    escolha = input("\nIr para 265, 300 ou 327?: ")
    match escolha:
        case '265':
            aventura265()
        case '300':
            aventura300()
        case '327':
            aventura327()
        case _:
            print("\nOpção Invalida!")
            aventura74()

def aventura75():
    print(stats_final)
    print("\nCAP 75")
    print("\nVocê esfrega o líquido nos seus ferimentos, mas eles não saram. Olhando fixamente para a garrafa vazia, você fica se perguntando o que o líquido seria exatamente. Se você ainda não o tiver feito, poderá abrir o livro vermelho - volte para 52. Do contrário, você deve continuar para o norte com Throm - vá para 369. ")

    escolha = input("\nIr para 126 ou 83?: ")
    match escolha:
        case '217':
            aventura217()
        case '30':
            aventura30()
        case '212':
            aventura212()
        case _:
            print("\nOpção Invalida!")
            aventura68()


def aventura76():
    print(stats_final)
    print("\nCAP 76")
    print("\nVocê dá a volta pela enorme massa morta do Verme da Rocha e dá uma espiada dentro da escuridão de seu buraco perfurado. Você só consegue ver alguns metros, mas pode notar que ele se inclina levemente e é tímido por causa da gosma secretada pelo Verme da Rocha. Se você quiser explorar o buraco de broca, vá para 317. Se preferir caminhar para o oeste pelo túnel, vá para 117. ")

    escolha = input("\nIr para 317 ou 117?: ")
    match escolha:
        case '317':
            aventura317()
        case '117':
            aventura117()
        case _:
            print("\nOpção Invalida!")
            aventura76()


def aventura77():
    print(stats_final)
    print("\nCAP 77")
    print("\nVocê cambaleia pela porta aberta para outro túnel, no fim do qual está a visão bem-vinda da luz do dia. Com grande surpresa, você vê o Gnomo caído, morto, na metade do caminho do túnel, com uma seta de besta cravada na cabeça. O Gnomo, no esforço por libertar-se, caiu na armadilha final do Barão Sukumvit. Você passa por ele rumo à luz do sol brilhante. Vá para 400. ")

    input("Pressione Enter para ir para 400...")
    aventura400()


def aventura78():
    print(stats_final)
    print("\nCAP 78")
    print("\nHá um cano com cerca de um metro de diâmetro aberto na parede da direita. Está escuro demais para se ver muito abaixo nele. Você grita dentro do cano de ferro e ouve sua voz ecoar por alguns instantes até desaparecer. Se você quiser engatinhar pelo cano, vá para 301. Se preferir continuar para o norte, vá para 142.")

    escolha = input("\nIr para 301 ou 143?")
    match escolha:
        case '301':
            aventura301()
        case '143':
            aventura143()
        case _:
            print("\nOpção Invalida!")
            aventura78()


def aventura79(sorte):
    print(stats_final)
    print("\nCAP 79")
    print("\nVocê segura os braços da cadeira firmemente, esperando que uma onda de energia se espalhasse pelo seu corpo. Teste sua Sorte. Se você tiver sorte, vá para 106. Se não tiver sorte, vá para 383. ")

    input("\nPressione Enter para rodar os dados...")
    x = roda_1_dado()
    print(f"\nO dado 1 tirou: {x}.")
    y = roda_1_dado()
    print(f"\nO dado 2 tirou: {y}.")
    soma = x + y

    print(f"\nA soma dos dados deu {soma}, sua sorte é {sorte}.")

    if soma <= sorte:
        input("\nVoce deu sorte!\nPressione Enter para ir para 106 ...")
        sorte = sorte - 1
        aventura106()

    else:
        input("\nVocê não teve sorte!\nPressione Enter para ir para 383...")
        sorte = sorte - 1
        aventura383()



def aventura80():
    print(stats_final)
    print("\nCAP 80")
    print("\nVocê vai com calma e consegue passar pelo último poste sem ter tocado em nenhum deles. Corre para o leste, ainda seguindo os dois pares de pegadas. Vá para 313.")

    input("\nPressione Enter para ir para 80...")

    aventura80()


def aventura81():
    print("\nA única mobília no quarto do Goblin consiste em uma mesa, duas cadeiras e um armário de parede. Há duas portas fechadas, uma na parede oeste, outra na parede norte. Você: \n\nAbrirá o armário? - Vá para 307\nAbrirá a porta do oeste? - Vá para 263\nAbrirá a porta do norte? - Vá para 136 ")

    escolha = input("\nIr para 307, 263 ou 136?: ")

    match escolha:
        case '307':
            aventura307()
        case '30':
            aventura30()
        case '263':
            aventura263()
        case '136':
            aventura136()
        case _:
            print("\nOpção Invalida!")
            aventura81()


def aventura82():
    print(stats_final)
    print("\nCAP 82")
    print("\nQuando o Diabo do Poço bate como corpo contra a parede, você solta a corda e cai em segurança no chão. Você corre na direção das portas duplas e fica aliviado ao senti-las se abrirem quando as empurra; deixa que elas se fechem atrás de si e segue para o norte pelo túnel. Vá para 214. ")

    input("\nPressione Enter para ir 214...")

    aventura214()


def aventura83():
    print(stats_final)
    print("\nCAP 83")
    print("\nA passagem logo conduz a uma encruzilhada. Você repara em mais pegadas no chão, possivelmente uns três pares, dirigindo-se ao norte pela passagem do sul. Resolve segui-las. Volte para 37. ")

    input("\nPressione Enter para ir para 37...")

    aventura37()


def aventura84():
    print(stats_final)
    print("\nCAP 84")
    print("\nJogue dois dados. Se o total for maior que 8, vá para 152. Se for 8 ou menos, vá para 121. ")


    input("\nPressione Enter para rodar os dados...")
    x = roda_1_dado()
    print(f"\nO dado 1 tirou: {x}.")
    y = roda_1_dado()
    print(f"\nO dado 2 tirou: {y}.")
    soma = x + y

    print(f"\nA soma dos dados deu {soma}, sua sorte é {sorte}.")

    if soma > 8:
        input("\nPressione Enter para ir para 152 ...")
        sorte = sorte - 1
        aventura152()

    else:
        input("\nPressione Enter para ir para 121...")
        sorte = sorte - 1
        aventura121()




def aventura85():
    print(stats_final)
    print("\nCAP 85")
    print("\nAntes que você possa fazer qualquer outra coisa, o velho murmura umas palavras estranhas. Você sente os músculos se enrijecerem e a pele se esticar. Começa a entrar em pânico, mas não há nada que possa fazer para impedir a petrificação do seu corpo. Sua aventura termina aqui. ")
    
    fim_de_jogo()


def aventura86():
    print(stats_final)
    print("\nCAP 86")
    print("\nA chave gira na fechadura, e a porta se abre para um cruzamento de quatro caminhos do túnel. Não há nada a ser visto a leste ou a oeste, a não ser os já conhecidos cristais do teto que continuam a produzir luz fraca. Subitamente, você ouve um chamado: 'Por aqui, por aqui, você está no caminho certo.' A voz parece estar vindo de algum lugar bem à sua frente. Não resistindo à curiosidade, você resolve atender ao chamado. Vá para 187. ")

    input("\nPressione Enter para ir para 187...")

    aventura187()


def aventura87():
    print(stats_final)
    print("\nCAP 87")
    print("\nA porta se abre para um aposento grande. Vá para 381. ")

    input("\nPressione Enter para ir para 381...")
    aventura381()


def aventura88():
    print(stats_final)
    print("\nCAP 88")
    print("\nLogo que os TROGLODITAS o vêem pegam os arcos e correm para cercá-lo. Para seu horror, o líder dá um passo adiante e declara que você é prisioneiro deles e terá que se submetera uma prova, segundo o rito milenar, a Corrida da Flecha. Se você estiver disposto a participar da Corrida da Flecha, vá para 343. Se preferir tentar lutar para fugir, vá para 268. ")

    escolha = input("\nIr para 343 ou 268?: ")
    match escolha:
        case '343':
            aventura343()
        case '268':
            aventura268()
        case _:
            print("\nOpção Invalida!")
            aventura88()



def aventura89(sorte):
    print(stats_final)
    print("\nCAP 89")
    print("\nDe volta à solidez do chão da caverna, você tenta sacudir a corda para que saia do pescoço do ídolo. Teste sua Sorte. Se você tiver sorte, volte para 54. Se não tiver sorte, vá para 261. ")

    input("\nPressione Enter para rodar os dados...")
    x = roda_1_dado()
    print(f"\nO dado 1 tirou: {x}.")
    y = roda_1_dado()
    print(f"\nO dado 2 tirou: {y}.")
    soma = x + y

    print(f"\nA soma dos dados deu {soma}, sua sorte é {sorte}.")

    if soma <= sorte:
        input("\nVoce deu sorte!\nPressione Enter para ir para 54 ...")
        sorte = sorte - 1
        aventura54()

    else:
        input("\nVocê não teve sorte!\nPressione Enter para ir para 261...")
        sorte = sorte - 1
        aventura261()



def aventura90():
    print(stats_final)
    print("\nCAP 90")
    print("\nLogo que se levanta, você se defronta com o quadro mais repulsivo que seus olhos jamais viram. Ali, na sua frente, chafurda numa poça circular de lodo fétido uma criatura inchada, inacreditavelmente horrível. O corpo é verde e coberto de ameaçadores espinhos. A cara é um amontoado de feridas vermelhas, uma das quais subitamente se abre para revelar mais um dos muitos olhos sinistros que tudo vêem. Um caminho estreito contorna a borda da poça e leva a um outro túnel na parede do outro lado. Se você já tiver lido detalhes sobre a abjeta BESTA SANGRENTA em um livro encadernado em couro, vá para 172. Se você não tiver lido o livro, vá para 357. ")

    if 'livro best sangrenta' not in mochila:
        input("\nPressione Enter para ir para 375...")
        aventura375()
    else:
        input("\nPressione Enter para ir para 172...")
        aventura172()


def aventura91(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome):
    print(stats_final)
    print("\nCAP 91")
    print("\nA maça de ferro do Orca atinge-lhe o braço, jogando sua espada no chão. Você terá que lutar com as mãos nuas, o que lhe reduz a HABILIDADE em 4 pontos enquanto durar o combate. Felizmente, o túnel é estreito demais para os dois Orcas atacarem-no ao mesmo tempo. Lute com um de cada vez.\n\n                        HABILIDADE          ENERGIA\nPrimeiro ORCA     -         5                  5\nSegundo ORCA      -         6                  4\n\nSe você vencer, vá para 257.")

    habilidade = habilidade - 4
    habilidade_monstro = 5
    energia_monstro = 5
    nome = "Primeiro ORCA"

    batalha(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome)

    print("Parabens, você vencêu o primeiro ORCA, vez do segundo ORCA.")
    habilidade_monstro = 6
    energia_monstro = 4
    nome = "Segundo ORCA"

    batalha(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome)

    input("Parabens! voce venceu! Pressione Enter para seguir para 257...")

    aventura257()

    


def aventura92():
    print(stats_final)
    print("\nCAP 92")
    print("\nReunindo todas as suas forças, você desfere um golpe final no Demônio do Espelho com sua espada. Com um som de estourar os tímpanos, abrem-se rachaduras no rosto e membros do monstro. As várias bocas gritam de agonia nos estertores da morte, antes do Demônio se despedaçar completamente numa pilha de minúsculos cacos. Você solta um enorme suspiro de alívio e depois se apressa a seguir em frente. Vá para 122. ")

    input("Pressione Enter para seguir para 122...")
    aventura122()


def aventura93():
    print(stats_final)
    print("\nCAP 93")
    print("\nA porta se abre para um pequeno e escuro aposento, contendo apenas, na parede do lado oposto, uma robusta arca de madeira em cima de uma prateleira. No chão, coberto de poeira espessa, você pode ver claramente pegadas frescas que vão até a arca e retornam à porta. Você se pergunta se um dos seus rivais está à sua frente na “Caminhada” ou se a arca só foi posta na prateleira recentemente por um dos Juízes da Prova. Se você quiser entrar no aposento e abrir a arca, vá para 284. Se preferir continuar percorrendo o túnel, vá para 230. ")

    escolha = input("\nIr para 284 ou 230?: ")
    match escolha:
        case '284':
            aventura284()
        case '30':
            aventura30()
        case '230':
            aventura230()
        case _:
            print("\nOpção Invalida!")
            aventura93()



def aventura94():
    print(stats_final)
    print("CAP 94")
    print("\nRespirando fundo, você se debruça sobre o poço e mergulha o braço na massa de vermes que se contorcem. Eles são frios e viscosos, e o contato é extremamente desagradável, mas, pelo menos, são inofensivos, e você consegue pegar o punhal pelo cabo. Ao sacudi-lo firmemente, ele sai da rachadura em que a ponta estava cravada. Admirando-lhe a beleza, e imaginando se ele teria um dia pertencido a um competidor de pouca sorte, você põe o punhal ornamentado de opala firmemente no cinto e sai da caverna. Vá para 174. ")
    


    input("Pressione Enter para ir para 174...")
    aventura174()


def aventura95(habilidade):
    print("\nO anel de ferro está preso a um pequeno alçapão. É fácil □uxa□-lo, e, dentro de um pequeno compartimento, você encontra um escudo, finamente trabalhado, feito do mais puro ferro. Maravilhado com o esplendor da peça, você a amarra ao seu braço. Acrescente 1 ponto de HABILIDADE. Você caminha na direção das portas duplas e as empurra. Vá para 248.")

    habilidade = habilidade - 1
    input("Pressione Enter para ir para 248...")
    aventura248()



def aventura96():
    print(stats_final)
    print("CAP 96")
    print("\nSeu segundo golpe também não consegue partir o espelho. O Demônio do Espelho estica um braço, agarra-lhe o pulso e começa a puxá-lo na direção do espelho. A força é incrível, e, apesar de todos os seus esforços, você não consegue resistir. A cada segundo, você chega mais perto do espelho. Quando o Demônio do Espelho toca o espelho, desaparece através dele. Com horror, você vê seu próprio braço desaparecer também através do espelho, e o resto do corpo logo tem o mesmo destino. Você está agora em um mundo de espelhos de outra dimensão, do qual jamais retornará.")

    fim_de_jogo()


def aventura97():
    print("\nVocê não sabe, mas a Besta Sangrenta só tem um ponto fraco: seus olhos reais. Mais por sorte do que por propósito, você crava sua lâmina profundamente em um deles, e a Besta Sangrenta desaba de volta na poça. Depois de medonhas convulsões, ela afunda sob a superfície oleosa da poça. Sem esperar para ver se ela vai se recuperar, você corre e entra no túnel, ansioso por se afastar da câmara tóxica da Besta Sangrenta o mais rápido possível. Vá para 134.")
    input("Pressione Enter para ir para 134...")
    aventura134()

def aventura98(sorte):
    print("\nErguendo a taça, você aciona um mecanismo de mola, e um dardo é disparado da perna da mesa de madeira. Teste sua Sorte. Se você tiver sorte, vá para 105. Se não tiver sorte, vá para 235.")

    input("\nPressione Enter para rodar os dados...")
    x = roda_1_dado()
    print(f"\nO dado 1 tirou: {x}.")
    y = roda_1_dado()
    print(f"\nO dado 2 tirou: {y}.")
    soma = x + y

    print(f"\nA soma dos dados deu {soma}, sua sorte é {sorte}.")

    if soma <= sorte:
        input("\nVoce deu sorte!\nPressione Enter para ir para 105 ...")
        sorte = sorte - 1
        aventura105()

    else:
        input("\nVocê não teve sorte!\nPressione Enter para ir para 235...")
        sorte = sorte - 1
        aventura235()


def aventura99():
    print(stats_final)
    print("CAP 99")
    print("\nSorrindo, você diz a Erva que a acha muito parecida com Barriga Azeda. Então, enquanto ela olha com admiração para a pintura, você pega um banco quebrado, aproxima-se silenciosamente por trás dela e golpeia-lhe a cabeça com toda a força. Para seu imenso alívio, Erva cai sem sentidos. Se você quiser revistar-lhe o quarto, vá para 266. Se não, saia pela porta da parede leste. Você se encontrará no final de um túnel. Vá para 305.")


    escolha = input("\nIr para 266 ou 305?: ")
    match escolha:
        case '266':
            aventura266()
        case '305':
            aventura305()
        case _:
            print("\nOpção Invalida!")
            aventura99()



def aventura100():
    print(stats_final)
    print("CAP 100")
    print("\nAlguns metros adiante, descendo a passagem, você vê uma outra porta fechada na parede da esquerda. Há uma letra X na placa central da porta. Colocando o ouvido na porta, você escuta atentamente, mas não consegue ouvir nada. Se você quiser abrir a porta, volte para 87. Se preferir continuar caminhando para o norte, vá para 217.")
 
    escolha = input("\nIr para 87 ou 217?: ")
    match escolha:
        case '87':
            aventura87()
        case '217':
            aventura217()
        case _:
            print("\nOpção Invalida!")
            aventura100()


def aventura101():
    print(stats_final)
    print("CAP 101")
    print("\nA correnteza do rio é bastante forte, e, atrapalhado pela armadura e a mochila, você não está em condição de nadar contra ela. Em poucos segundos, é arrastado por baixo da ponte. De pé na margem do rio, os Trogloditas olham, riem e gracejam, enquanto você desce o rio para encontrar a morte nas profundezas da montanha.")

    fim_de_jogo()


def aventura102():
    print("\nVocê entra em um aposento pequeno e completamente vazio. Logo a porta se fecha atrás de você. Repentinamente, uma voz ressoa, vinda de lugar nenhum: 'Bem vindo ao Calabouço da Morte, o engenhoso labirinto assassino do meu senhor. Aventureiro, creio que você apresentará seus respeitos ao meu senhor, gritando seu nome?' Você gritará: \n\nSalve, Sukumvit?	- Vá para 133\nSukumvit é um verme? - Vá para 251 ")

    
    escolha = input("\nIr para 133 ou 251?: ")
    match escolha:
        case '133':
            aventura133()
        case '251':
            aventura251()
        case _:
            print("\nOpção Invalida!")
            aventura102()



def aventura103():
    print(stats_final)
    print("CAP 103")
    print("\nVocê respira o gás venenoso e começa a se engasgar. Você perde 3 pontos de ENERGIA. Se ainda estiver vivo, volte para 77. ")

    energia = energia - 3

    if energia > 0:
        input("Voce saiu vivo, mas ferido. Pressione Enter para ir para 77...")
        aventura77()

    else:
        fim_de_jogo()

def aventura104():
    print(stats_final)
    print("CAP 104")
    print("\nReagindo rapidamente, você consegue saltar por cima da língua estendida e correr para o túnel, deixando a Besta Sangrenta a chafurdar na poça à espera de outra vítima. Vá para 134. ")

    input("Pressione Enter para ir para 134...")

    aventura134()


def aventura105():
    print(stats_final)
    print("CAP 105")
    print("\nSeus reflexos são precisos, e você rapidamente pula de lado. O dardo passa assobiando, por pouco não o atingindo, e se choca contra a parede do outro lado. Você vê a taça jogada no chão, e o líquido vermelho escorrendo pela pedra cinzenta como pequenos riachos. Pelo menos a raça pode ser de alguma utilidade, portanto você a põe na mochila. Se você ainda não o tiver feito, poderá caminhar de volta para revistar o Bárbaro - vá para 126. Do contrário, saia da câmara para continuar para o oeste - volte para 83. ")
    
    escolha = input("\nIr para 126 ou 83?: ")
    match escolha:
        case '126':
            aventura126()
        case '83':
            aventura83()
        case _:
            print("\nOpção Invalida!")
            aventura105()


def aventura106():
    print(stats_final)
    print("CAP 106")
    print("\nAo apertar o braço da cadeira, você aciona a mola de um painel secreto, que salta no ar. Você encontra um frasco de vidro e lê o rótulo: 'Poção da Réplica - uma dose apenas. Este líquido fará com que seu corpo tome a forma de qualquer ser que esteja próximo.' Você coloca a estranha poção na mochila e continua para o norte. Vá para 188. ")

    mochila.append('Poção da Réplica')

    input("Pressione Enter para ir para 188...")

    aventura188()   


def aventura107():
    print(stats_final)
    print("CAP 107")
    print("\nVocê chega a uma porta em arco localizada na parede à direita do túnel. A pesada porta de pedra está fechada, mas há um trinco de ferro e uma maçaneta redonda. Se você quiser tentar a porta, vá para 168. Se, em vez disso, quiser continuar pelo túnel, vá para 267. ")

    input("Pressione Enter para ir para 267...")

    aventura267()


def aventura108():
    print(stats_final)
    print("CAP 108")
    print("\nHá um grande painel de vidro na parede à esquerda do túnel. Através dele, você pode ver um aposento intensamente iluminado por tochas com INSETOS GIGANTES de todas as formas possíveis. Abelhas, vespas, besouros, carrapatos – até os bichos do queijo têm mais de seis centímetros de comprimento. O ruído é ameaçador. No meio do aposento, uma coroa cravejada de jóias está colocada sobre uma pequena mesa. No meio da coroa, há uma jóia, parece um grande diamante. Você: \n\nQuebrará o vidro e tentará apanhar a coroa?	- Vá para 394 \nContinuará para o oeste? - Volte para 59 \nRetornará à encruzilhada para seguir para o norte? - Volte para 14 ")

    
    escolha = input("\nIr para 394, 59 ou 14?: ")
    match escolha:
        case '394':
            aventura394()
        case '59':
            aventura59()
        case '14':
            aventura14()
        case _:
            print("\nOpção Invalida!")
            aventura108()



def aventura109():
    print(stats_final)
    print("CAP 109")
    print("\nVocê chega a uma outra encruzilhada no túnel. Se quiser continuar seguindo para o oeste, volte para 43. Se quiser seguir para o norte, volte para 24. ")
    
    escolha = input("\nIr para 43 ou 24?: ")
    match escolha:
        case '43':
            aventura43()
        case '24':
            aventura24()
        case _:
            print("\nOpção Invalida!")
            aventura109()



def aventura110():
    print(stats_final)
    print("CAP 110")
    print("\nO túnel logo faz uma outra curva fechada para a direita. Seguindo para o leste, você chega a uma estranha obstrução: uma linha de 12 postes de madeira atravessados no túnel. Eles estão fixos às paredes a cerca de meio metro do chão, com um espaço de um metro entre eles. Se você quiser caminhar entre os postes, volte para 58. Se preferir subir pelos postes e passar por sobre a obstrução, vá para 223. ")

    
    escolha = input("\nIr para 58 ou 223?: ")
    match escolha:
        case '58':
            aventura58()
        case '223':
            aventura223()
        case _:
            print("\nOpção Invalida!")
            aventura110()


def aventura111():
    print(stats_final)
    print("Cap 111")
    print("\nVocê limpa o viscoso lodo amarelo da lâmina de sua espada e caminha rapidamente para a porta, de volta para o túnel, e segue para o norte. Vá para 267. ")

    input("Pressione Enter para ir para 267...")

    aventura267()


def aventura112():
    print(stats_final)
    print("CAP 112")
    print("\nA não ser pelas Provisões, que ficaram encharcadas e não servem mais para serem comidas, todas as suas outras posses permanecem intactas. Você as recoloca cuidadosamente na mochila e parte para o norte de novo. Vá para 356. ")

    input("Pressione Enter para ir para 356...")

    aventura356()


def aventura113():
    print(stats_final)
    print("CAP 113")
    print("\nA bola de madeira passa assobiando pelo crânio, atingindo a parede do outro lado com um estrondo. Se você quiser tentar outra vez com a outra bola, vá para 371. Se já tiver jogado duas vezes, ou não quiser tentar de novo, você pode fechar a porta e continuar pelo túnel - volte para 74. ")

    
    escolha = input("\nIr para 371 ou 74?: ")
    match escolha:
        case '371':
            aventura371()
        case '74':
            aventura74()
        case _:
            print("\nOpção Invalida!")
            aventura113()



def aventura114():
    print(stats_final)
    print("CAP 114")
    print("\nO Homem da Caverna está usando uma munhequeira de couro com quatro pequenos crânios de rato pendurados. Se você quiser coloca-la no seu próprio pulso, vá para 336. Se preferir prosseguir para o norte, vá para 298. ")

    escolha = input("Ir para 336 ou 298?: ")

    match escolha:
        case '336':
            aventura336()
        case '298':
            aventura298()
        case _:
            print("\nOpção invalida!")


def aventura115(energia):
    print(stats_final)
    print("CAP 115")
    print("\nSeu corpo continua a vibrar intensamente, e você se sente como se estivesse prestes a desmaiar. Mas sua força é grande, e você consegue resistir ao tremendo choque sofrido. Finalmente, você se acalma e começa a sentir a ação dos poderes benéficos do anel. Some 3 pontos de ENERGIA. Throm o olha ansioso, e você o tranquiliza, dizendo que está plenamente recuperado. Ele caminha para o leste, você o segue prontamente. Vá para 221. ")

    energia = energia + 3

    input("Pressione Enter para ir para 221...")

    aventura221()


def aventura116():
    print(stats_final)
    print("CAP 116")
    print("\nVocê não consegue acreditar que a Besta Sangrenta não tenha sido afetada pela nova ferida. Você hesita uma fração de segundo demais, e a fera dá um bote, partindo-lhe o crânio com as mandíbulas. Em seguida, arrasta-o para a poça, onde seu corpo, depois de decomposto, será devorado pela pavorosa criatura.")

    fim_de_jogo()


def aventura117():
    print(stats_final)
    print("CAP 117")
    print("\nDepois de longa caminhada túnel abaixo, você chega a um beco sem saída. Um grande espelho, que vai do chão até o teto, está colocado na parede do fundo e, na penumbra, você só consegue visualizar vagamente o seu próprio reflexo. Se quiser olhar o espelho mais de perto, vá para 329. Se preferir fazer a longa caminhada de volta para a última encruzilhada no túnel, a fim de prosseguir para o leste, vá para 135. ")
    
    escolha = input("\nIr para 329 ou 135?: ")
    match escolha:
        case '329':
            aventura329()
        case '135':
            aventura135()
        case _:
            print("\nOpção Invalida!")
            aventura117()



def aventura118():
    print(stats_final)
    print("CAP 118")
    print("\nApesar das estalactites que caem por toda parte, você consegue passar ileso pelo arco. Você olha ao redor e vê Throm disparando na sua direção, um braço por cima da cabeça paia protegê-la. Ele corre para o túnel e se encosta na parede fria, a respiração ofegante. Desculpa- se por ter iniciado o desabamento das rochas e lhe oferece a mão. Você diz a Throm que talvez fosse melhor ele usar a linguagem dos sinais no futuro, mesmo para rir! Os dois sorriem e partem para o leste mais uma vez. Volte para 60. ")

    input("Pressione Enter para ir para 60...")
    aventura60()

def aventura119():
    print(stats_final)
    print("CAP 119")
    print("\nAdiante, você pode ver um grande obstáculo no chão do túnel, embora esteja escuro demais para saber exatamente o que é. As pegadas molhadas que você vem seguindo continuam até a obstrução. Se você quiser continuar para o leste, volte para 56. Se preferir voltar para a encruzilhada e seguir para o oeste, vá para 293. ")


    escolha = input("\nIr para 56 ou 293?: ")
    match escolha:
        case '56':
            aventura56()
        case '293':
            aventura293()
        case _:
            print("\nOpção Invalida!")
            aventura119()



def aventura120():
    print(stats_final)
    print("CAP 120")
    print("\nJogados num buraco de mais ou menos um metro de profundidade, você vê um gancho de ferro e uma bolsa de couro. Se quiser esticar a mão para apanhá-los, vá para 228. Se preferir ignorar os objetos e continuar para o norte, vá para 292. ")

    escolha = input("\nIr para 228 ou 292?: ")
    match escolha:
        case '228':
            aventura228()
        case '292':
            aventura292()
        case _:
            print("\nOpção Invalida!")
            aventura120()




def aventura121():
    print(stats_final)
    print("CAP 121")
    print("\nO Anão olha para os dados. “Você não é muito bom nesse jogo, é?”, graceja. “Lamento, mas você terá que sofrer uma penalidade antes de continuar.” Ele retira duas pílulas do bolso. Uma está marcada com a letra S e a outra com a letra L. Pede que você escolha uma e engula. Se você escolher a pílula marcada com a letra S, volte para 26. Se quiser engolir a outra, vá para 354.")

    
    escolha = input("\nIr para 26 ou 354?: ")
    match escolha:
        case '26':
            aventura26()
        case '354':
            aventura354()
        case _:
            print("\nOpção Invalida!")
            aventura121()




def aventura122():
    print(stats_final)
    print("CAP 122")
    print("\nÀ sua frente, há dois lances de escadas de pedra, separados por um corrimão de crânios de ratazana. Você pode subir pelo lance de escadas da esquerda - vá para 176 - ou pelo da direita - vá para 384. ")


    escolha = input("\nIr para 176 ou 384?: ")
    match escolha:
        case '176':
            aventura176()
        case '384':
            aventura384()
        case _:
            print("\nOpção Invalida!")
            aventura122()





def aventura123(habilidade, energia):
    print(stats_final)
    print("CAP 123")
    print("\nO colar é um amuleto de força. Some 1 ponto de HABILIDADE e 1 ponto de ENERGIA e continue na sua missão. Vá para 282. ")

    habilidade = habilidade - 1
    energia = energia - 1

    input("Pressione Enter para ir para 282...")
    aventura282()


def aventura124():
    print(stats_final)
    print("CAP 124")
    print("Você abre o alçapão e sobe os degraus correndo, chegando a um aposento profundamente iluminado por lanternas. Dois GOBLINS afiam espadas curtas em uma pedra colocada no meio do chão. Você os pega desprevenidos, mas eles logo se recuperam e se projetam para frente a fim de atacá-lo.\n\n\n                        HABILIDADE          ENERGIA\nPrimeiro GOBLIN     -       5                  4\nSegundo GOBLIN      -       5                  5\n\nOs Goblins o atacarão separadamente em cada Série de Ataque, mas você deve escolher com qual dos dois vai lutar. Ataque o Goblin escolhido como numa batalha normal. Contra o outro, você tem que jogar os dados para determinar sua Força de Ataque da maneira usual, mas, mesmo que sua Força de Ataque seja maior, você não ferirá o Goblin. Compute isso simplesmente como se tivesse se defendido de um golpe dele. Porém, se a Força de Ataque dele for maior, ele o ferirá, da forma costumeira. Se você vencer, volte para 81.")

    #arrumar batalha em dupla



def aventura125(sorte):
    print(stats_final)
    print("CAP 125")
    print("\nVocê caminha para a porta na ponta dos pés, enquanto Erva segue tagarelando. Teste sua Sorte. Se você tiver sorte, volte para 69. Se não tiver sorte, vá para 139. ")

    input("\nPressione Enter para rodar os dados...")
    x = roda_1_dado()
    print(f"\nO dado 1 tirou: {x}.")
    y = roda_1_dado()
    print(f"\nO dado 2 tirou: {y}.")
    soma = x + y

    print(f"\nA soma dos dados deu {soma}, sua sorte é {sorte}.")

    if soma <= sorte:
        input("\nVoce deu sorte!\nPressione Enter para ir para 69 ...")
        sorte = sorte - 1
        aventura69()

    else:
        input("\nVocê não teve sorte!\nPressione Enter para ir para 139...")
        sorte = sorte - 1
        aventura139()




def aventura126():
    print(stats_final)
    print("CAP 126")
    print("\nA bolsa no cinto do Bárbaro contém apenas uma porção de carne seca de aparência estranha, embrulhada num pano. Você: \n\nComerá a carne seca? - Vá para 226\nDeixará a carne e caminhará para a alcova (se ainda não tiver feito isso)? - Volte para 41\nDeixará a câmara e seguirá para o oeste? - Volte para 83")
    
    escolha = input("\nIr para 226, 41 ou 83?: ")
    match escolha:
        case '226':
            aventura226()
        case '41':
            aventura41()
        case '83':
            aventura83()
        case _:
            print("\nOpção Invalida!")
            aventura126()




def aventura127():
    print(stats_final)
    print("CAP 127")
    print("\nA única maneira possível de sair do salão, tanto quanto você pode ver, é usando um escorrega na parede norte. Você resolve arriscar e sobe no escorrega. Desce deslizando suavemente e aterrissa de costas em outro aposento. Volte para 90. ")


    input("Pressione Enter para ir para 90...")
    aventura90()
    



def aventura128():
    print(stats_final)
    print("CAP 128")
    print("\nNa parte de trás da alcova, há uns degraus que conduzem a uma adega abaixo. Teias de aranha tocam-lhe o rosto enquanto você desce. O teto da adega é bastante baixo, e o chão está coberto de lixo e detritos. No meio da parede do outro lado, uma passagem em arco leva a outro túnel iluminado por cristais. Grandes cogumelos crescem no lixo à sua direita. Se você quiser atravessar a passagem em arco, volte para 35. Se preferir parar para comer alguns cogumelos, vá para 233. ")

    escolha = input("\nIr para 35 ou 233?: ")
    match escolha:
        case '35':
            aventura35()
        case '233':
            aventura233()
        case _:
            print("\nOpção Invalida!")
            aventura128()





def aventura129():
    print(stats_final)
    print("CAP 129")
    print("\nVocê amarra a corda ao gancho e o atira por cima da muralha. O gancho se prende na pedra, e você começa a se içar. De cima da muralha, vê um monstro gigantesco, semelhante a um dinossauro, circulando em um poço coberto de areia. O grosso couro da criatura é verde malhado, e de pé nas fortes pernas traseiras, deve atingir uns 10 metros de altura. As enormes mandíbulas deixam ver filas de dentes afiados como navalhas ao se abrirem e fecharem com força suficiente para triturar-lhe os ossos. Uma grande porta dupla na parede do outro lado do poço parece ser a única maneira de sair desta parte do calabouço. Você:\n\nDescerá pela corda para dentro do poço, a fim de enfrentar o DIABO DO POÇO? - Vá para 349 \nJogará seu amuleto de osso de macaco no poço (se você tiver um)? - Vá para 361 \nTentará, de cima da muralha, fisgar O DIABO DO POÇO com o gancho de ferro? - Vá para 167 ")

    escolha = input("\nIr para 349, 361 ou 167?: ")
    match escolha:
        case '349':
            aventura349()
        case '361':
                if 'amuleto de osso de macaco' in mochila:

                    aventura361()
                else:
                    input("Você não tem amuleto de osso de macaco na mochila... Pressione Enter para ir para 129 novamente...")
                    aventura129()
        case '167':
            aventura167()
        case _:
            print("\nOpção Invalida!")
            aventura129()





def aventura130(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome):
    print("\nOs Hobgoblins param de lutar imediatamente. Eles não entendem o que você está dizendo e rosnam agressivamente. Em seguida, desembainham as espadas curtas e avançam para □taca- lo. Lute com um de cada vez. \n\n\n                        HABILIDADE          ENERGIA\nPrimeiro HOBGOBLIN     -    5                  4\nSegundo HOBGOBLIN      -    5                  5\n\nSe você vencer, volte para 9.")

    habilidade_monstro = 5
    energia_monstro = 4
    nome = "Primeiro HOGLOBIN"

    batalha(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome)

    print("Parabens, voce derrotou o primeiro HOGOBLIN! Agora lute com o segundo HOGOBLIN")

    habilidade_monstro = 5
    energia_monstro = 5
    nome = "Segundo HOGLOBIN"

    batalha(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome)




def aventura131():
    print(stats_final)
    print("CAP 131")
    print("\nOs dardos da besta voam por cima de sua cabeça e se cravam na parede; felizmente, você ainda está agachado. Agora que a armadilha já disparou, você pode sair do aposento pela mesma porta pela qual entrou. De volta no túnel, você segue para o oeste. Volte para 74. ")


    input("Pressione Enter para ir para 74...")
    aventura74()



def aventura132():
    print("\nVocê só tem tempo de ouvir o Gnomo dizer: 'Uma coroa e dois crânios', antes de ser atingido no peito por um raio branco de energia disparado da fechadura. Você cai sem sentidos. Jogue um dado, some 1 ao número obtido e reduza esse total de sua ENERGIA. Se você ainda estiver vivo, recupera a consciência e o Gnomo manda que tente de novo. Você sabe que colocou uma gema na ranhura certa, mas qual? Você suspira e tenta uma nova combinação. \n\n   A                B             C\nESMERALDA       DIAMANTE       SAFIRA          VOLTE PARA 16\nDIAMANTE         SAFIRA       ESMERALDA        VÁ PARA 392\nSAFIRA          ESMERALDA       DIAMANTE       VÁ PARA 177\nESMERALDA       SAFIRA       DIAMANTE          VÁ PARA 287\nDIAMANTE       ESMERALDA       SAFIRA          FIQUE EM 132\nSAFIRA          DIAMANTE      ESMERALDA        VÁ PARA 249")

    escolha = input("Você irá para 16, 392, 177, 287, 132 ou 249?: \n")
    match escolha:
        case '16':
            aventura16()
        case '392':
            aventura392()
        case '177':
            aventura177()
        case '287':
            aventura287()
        case '132':
            aventura132()
        case '249':
            aventura249()
        case _:
            print("\nOpção Invalida.")


def aventura133(habilidade):
    print(stats_final)
    print("CAP 133")
    print("\nMais uma vez, a voz misteriosa ecoa, só que agora num tom cheio de desprezo e escárnio. 'Então, temos uma erva daninha em nosso meio, não?', zomba a voz. 'Meu senhor tem um presente especial para você, verme abjeto.' Súbito, começa a entrar água no aposento por um buraco no teto. Logo sobe até a altura dos seus tornozelos, e não parece haver qualquer meio de escapar. Você caminha na água até a porta. Está firmemente trancada, mas, no desespero, você tenta arrombá-la, batendo com o ombro. Jogue dois dados. Se o total for igual ou menor que o seu índice de HABILIDADE, vá para 178. Se o total for maior que o seu índice de HABILIDADE, volte para 17. ")


    input("\nPressione Enter para rodar os dados...")
    x = roda_1_dado()
    print(f"\nO dado 1 tirou: {x}.")
    y = roda_1_dado()
    print(f"\nO dado 2 tirou: {y}.")
    soma = x + y

    print(f"\nA soma dos dados deu {soma}, sua habilidade é {habilidade}.")

    if soma <= sorte:
        input("\nSua habilidade é maior!\nPressione Enter para ir para 178 ...")
        aventura178()

    else:
        input("\nSua habilidade é menor...\nPressione Enter para ir para 17...")
        aventura17()






def aventura134():
    print(stats_final)
    print("CAP 134")
    print("\nO túnel leva a um amplo aposento cujo teto é sustentado por diversos pilares de mármore. Ao entrar no aposento, você depara com uma estranha fera à sua direita. Tem corpo de leão, asas de dragão, rabo de escorpião e cabeça de velho barbudo. Se você tiver lido o poema escrito no Pergaminho do Guerreiro Esqueleto, vá para 222 Se não tiver lido esse poema, vá para 247. ")

    if 'poema do pergaminho do guerreiro esqueleto' in mochila:
        input()
        aventura222()
    else:
        input()
        aventura247(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome)


def aventura135():
    print(stats_final)
    print("CAP 135")
    print("\nPassando pelo buraco perfurado do Verme da Rocha, à sua esquerda, você logo chega à encruzilhada. Dá uma olhada rápida no túnel que conduz ao sul, mas não vê ninguém se aproximando. Apressando o passo, você segue velozmente para o leste. Volte para 68. ")

    input("Pressione Enter para ir para 68...")
    aventura68()


def aventura136():
    print("\nA porta abre para um outro túnel, que se inclina numa subida ao longe. Depois de percorrer essa subida por algum tempo, você chega a uma parte plana, onde numa porta na parede da direita encontra-se pregada uma mão já decomposta. Se você quiser abrir a porta, vá para 210. Se preferir continuar para o norte, volte para 78. ")
    
    escolha = input("\nIr para 210 ou 78?: ")
    match escolha:
        case '210':
            aventura210()
        case '78':
            aventura78()
        case _:
            print("\nOpção Invalida!")
            aventura136()



def aventura137():
    print(stats_final)
    print("")
    print("CAP 137\n")
    print("\nCaminhando pelo túnel, você se surpreende com um grande sino de ferro pendurado no teto. Se quiser tocar o sino, vá para 220. Se preferir contorná-lo e prosseguir para o oeste, vá para 362. ")
    escolha = input("Ir para 220 ou 362?: \n")
    match escolha:
        case '220':
            aventura220()
        case '362':
            aventura362()
        case _:
            print("Opção Invalida!")
            aventura137()


def aventura138():
    print(stats_final)
    print("CAP 138")
    print("\nAs páginas do livro estão unidas com lacre, mas um pequeno orifício foi cortado no meio delas, de tamanho suficiente para conter uma pequena garrafa arrolhada, na qual há um líquido de cor clara. Você mostra isso a Throm, que levanta a mão, indicando não querer que você sequer chegue perto dele com aquilo; a desconfiança que ele sente em relação às coisas desconhecidas fica evidente. Você:\n\nBeberá o líquido? - Vá para 397\nEsfregará o líquido nos seus ferimentos? - Volte para 75\nAbrirá o livro vermelho (Se ainda não fez isso)? - Volte para 52\nDeixará a garrafa e o livro de lado para continuar para o norte com Throm? - Vá para 369 ")
    
    escolha = input("\nIr para 397, 75, 52 ou 369?: ")
    match escolha:
        case '397':
            aventura397()
        case '75':
            aventura75()
        case '52':
            aventura52()
        case '369':
            aventura369()
        case _:
            print("\nOpção Invalida!")
            aventura138()



def aventura139(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome):
    print("\nAo tentar escapar, você é atacado ferozmente por Erva, que, com raiva, vira-se rapidamente, pega um banco quebrado e o atinge com ele. Você perde 2 pontos de ENERGIA. Se ainda estiver vivo, você consegue desembainhar a espada e lutar.\n\n\n                        HABILIDADE          ENERGIA\nERVA            -           9                  9\n\nSe você vencer, volte para 201.")

    energia_monstro = 9
    habilidade_monstro = 9
    nome = "ERVA"

    batalha(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome)

    input("parabens! voce venceu! siga para 201...")

    aventura201()


def aventura140():
    print("\nVocê tenta forçar o olho de esmeralda com a ponta da espada, procurando enfiá-la por baixo dele. Para sua grande surpresa, ele se despedaça com o contato, soltando um jato de gás venenoso direto no seu rosto. Você desmaia e cai para trás, chocando-se contra o ídolo várias vezes até parar no chão de pedra. Sua aventura termina aqui. ")

    fim_de_jogo()


def aventura141():
    print(stats_final)
    print("CAP 141")
    print("\nO Demônio do Espelho está quase em cima de você quando, reunindo todas as suas forças, você desfere um golpe decisivo contra o espelho com a espada. Jogue dois dados. Se o total for igual ou menor que a sua HABILIDADE, volte para 72. Se o total for maior que a sua HABILIDADE, volte para 96. ")

    if usar_habilidade(habilidade):
        print("\nVocê deu sorte!\n")

        input("\nPressione Enter para retornar para 72...")
        aventura72(habilidade)
    else:
        print("Você não deu sorte!")

        input("\nPression Enter para retornar para 96...")
        aventura96()


def aventura142():
    print(stats_final)
    print("CAP 142")
    print("\nHá uma nova ramificação no túnel à sua esquerda, e, à frente, você vê dois corpos estendidos no chão. Você pára e dá uma espiada no novo túnel, mas, não vendo nem portas nem criaturas, resolve seguir por ele. Com a espada na mão, você caminha na direção dos corpos estendidos. Vá para 338.")


    input("Pressione Enter para ir para 388...")
    aventura388()




def aventura143():
    print(stats_final)
    print("CAP 143")
    print("\nVocê chama o Anão, dizendo-lhe para mandar vir o ESCORPIÃO, pois você está pronto para lutar. Lentamente, a porta de madeira é erguida, e um enorme e grotesco escorpião negro se esgueira por baixo dela e entra no aposento. Você desembainha a espada em guarda e se prepara para enfrentar a sinistra criatura com pinças gigantescas e ferrão mortal.\n\n\n                        HABILIDADE          ENERGIA\nESCORPIÃO GIGANTE     -     10                  10\n\nO Escorpião o ataca com ambas as pinças, e você terá que considerar cada uma das pinças como uma entidade separada, como se lutasse contra duas criaturas. Ambas as pinças possuem HABILIDADE 10 e o atacarão separadamente em cada Série de Ataque, mas você terá que escolher qual delas enfrentará. Ataque uma pinça como numa batalha normal. Contra a outra pinça, você joga os dados para determinar sua Força de Ataque da forma costumeira, mas você não causará ferimentos ao Escorpião, mesmo que sua Força de Ataque seja maior; conte isso como se você tivesse apenas conseguido se defender de um golpe. É claro que, se a Força de Ataque da pinça for maior que a sua, você será ferido da maneira usual. Se, durante qualquer das Séries de Ataque, a Força de Ataque do Escorpião totalizar 22, volte para 2. Se você conseguir matar o Escorpião sem que ele atinja uma Força de Ataque de 22, vá para 163. ")

    #batalha em dupla


def aventura144():
    print(stats_final)
    print("CAP 144")
    print("\nAinda sorrindo, o velho olha para você e diz em voz baixa: 'Errado.' Volte para 85. ")

    
    input("Pressione Enter para ir para 85...")
    aventura85()





def aventura145(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome):
    print(stats_final)
    print("CAP 145")
    print("\nO Anão estava esperando seu movimento. Além disso, você não é tão rápido quanto deveria, devido ao sofrimento recente, por isso ele evita seu golpe facilmente, dizendo: “Eu poderia matá-lo agora, se quisesse, mas estou com saudades de uma luta corpo a corpo.” Em seguida, ele larga a besta no chão e puxa uma acha do cinto. Apesar da fadiga, você só pensa em vingança.\n\n\n                        HABILIDADE          ENERGIA\nANÃO            -           8                  6\n\nDurante cada Série de Ataque, você terá que reduzir sua Força de Ataque em 2, por causa da sua condição física. Se você vencer, volte para 28. ")  

    energia_monstro = 6
    habilidade_monstro = 8
    nome = "ANÃO"

    batalha(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome)

    input("Parabens! voce venceu a fera! Pressione Enter para seguir para 28...")

    aventura28()


def aventura146():
    print(stats_final)
    print("CAP 146")
    print("\nA dor nos pulmões força-o a subir à superfície para respirar. Felizmente, nenhum dos Trogloditas o vê e todos se dispersam. Você sai do rio e atravessa a ponte para a margem norte. Quaisquer Provisões restantes que você possa ter estão agora imprestáveis. Você segue pela vasta caverna até que, finalmente, vê um túnel na parede do outro lado. Você anda até ele e chega a uma pesada porta de madeira, que está trancada. Se você tiver uma chave de ferro, volte para 86. Se não tiver a chave, vá para 276. ")

    if 'chave de ferro' in mochila:
        input("Voce tem uma chave de ferro, siga para 86...")
        aventura86()
    else:
        input("Voce não tem a chave de ferro, siga para 276...")
        aventura276()


def aventura147():
    print(stats_final)
    print("CAP 147")
    print("\nA água no tubo de bambu é agradavelmente refrescante. Você ganha 1 ponto de ENERGIA. A água contém também uma solução mágica que lhe permite expor-se a temperaturas altíssimas sem sofrer danos. Jogando fora o bambu, você segue para o norte de novo com excelente disposição. Vá para 182. ")

    input("Pressione Enter para ir para 182...")
    aventura182()



#acabar amanha
def aventura148(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome):
    print(stats_final)
    print("CAP 148")
    print("\nNada há a fazer senão descer as escadas, na direção dos cachorros que latem. Você chega ao pé da escada com a espada na mão e enfrenta os dois gigantescos CÃES DE GUARDA, que saltam sobre você, um de cada vez. \n\n\n                                 HABILIDADE          ENERGIA\nPrimeiro CÃO DE GUARDA     -         7                  7\nSegundo CÃO DE GUARDA      -         7                  8\n\nSe você vencer, vá para 175. Você pode Fugir depois de matar o primeiro Cão de Guarda, correndo para leste pelo túnel. Vá para 315. ")

    habilidade_monstro = 7
    energia_monstro = 7
    nome = "Primeiro CÃO DE GUARDA"

    batalha_fuga(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome)

    input(f"Parabens! Você derrotou o {nome}, Pressione Enter para iniciar a batalha com o Segundo CÃO DE GUARDA...")

    habilidade_monstro = 7
    energia_monstro = 8
    nome = "Segundo CÃO DE GUARDA"

    batalha_fuga(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome)

    input("\nPressione Enter para ir para 315...")
    aventura315()


def aventura149(sorte):
    print(stats_final)
    print("CAP 149")
    print("\nVocê solta a corda e ouve ela cair no fundo do poço. O Bárbaro o amaldiçoa, prometendo matá-lo se seus caminhos se cruzarem outra vez. Você recua, toma distância e salta. Cai em segurança do outro lado do poço e continua para o oeste. Mais adiante no túnel, você pisa em uma parte do chão de pedra que se inclina para frente, disparando uma armadilha que solta um rochedo preso frouxamente no teto. Você olha para cima bem no momento em que o rochedo está prestes a cair sobre você. Teste sua Sorte. Se você tiver sorte,volte para 70. Se não tiver sorte, vá para 353.")

    input("\nPressione Enter para rodar os dados...")
    x = roda_1_dado()
    print(f"\nO dado 1 tirou: {x}.")
    y = roda_1_dado()
    print(f"\nO dado 2 tirou: {y}.")
    soma = x + y

    print(f"\nA soma dos dados deu {soma}, sua sorte é {sorte}.")

    if soma <= sorte:
        input("\nVoce deu sorte!\nPressione Enter para ir para 70 ...")
        sorte = sorte - 1
        aventura70()

    else:
        input("\nVocê não teve sorte!\nPressione Enter para ir para 353...")
        sorte = sorte - 1
        aventura353()



def aventura150():
    print(stats_final)
    print("CAP 150")
    print("\nTendo tido a boa idéia de não pôr o seu braço da espada dentro do buraco, os efeitos do tentáculo não são muito graves. Você perde 1 ponto de HABILIDADE. Enfiando novamente o braço no buraco, de lá retira o gancho e a bolsa de couro. Dentro da bolsa, você encontra um minúsculo sino de metal. Guarda suas novas posses na mochila e continua para o norte. Vá para 292. ")

    input("Pressione Enter para ir para 292...")
    aventura292()



#tem q fazer a batalha em dupla pqp
def aventura151(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome):
    print(stats_final)
    print(habilidade)
    print("\nCAP 151")
    print("\nQuando toca o olho de esmeralda do ídolo, você ouve um rangido abaixo. Ao olhar, fica abismado ao ver os dois pássaros empalhados voando. As asas das criaturas batem aos arrancos, mas logo estão acima de você e parecem prontos para atacar. Lute com um dos GUARDIÃES VOADORES de cada vez, mas reduza sua HABILIDADE em 2 pontos durante este combate, pois a posição restringe-lhe os movimentos. \n                                HABILIDADE          ENERGIA\nPrimeiro GUARDIÃO VOADOR     -       7                  8\nSegundo GUARDIÃO VOADOR      -       8                  8\n\nSe você vencer, vá para 240. ")

    habilidade = habilidade - 2

    habilidade_monstro = 7
    energia_monstro = 8
    nome = "Primeiro GUARDIÃO VOADOR"
    input("\nPressione Enter para iniciar a batalha...")
    batalha(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome)

    energia, sorte, energia_atualizada = batalha(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome)

    print(energia_atualizada)

    print("\nPrimeiro guardião derrotado. Vez do segundo GUARDIÃO VOADOR.")
    input("\nPressione Enter para iniciar a batalha...")
    habilidade_monstro = 8
    nome = "segundo GUARDIÃO VOADOR"
    batalha(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome)

    input("\n\nVocê derrotou o segundo GUARDIÃO VOADOR.\nPressione Enter para ir para 240...")

    print(habilidade)
    aventura240()


def aventura152():
    print(stats_final)
    print("CAP 152")
    print("\nO Anão o cumprimenta por ter adivinhado corretamente. Ele diz que agora você deverá seguir para a segunda fase do teste. Apanhando uma cesta de vime, ele lhe diz que há uma cobra dentro dela. Vira a cesta e a cobra cai ao chão; é uma naja, que se ergue no ar, pronta para o bote. O Anão diz que quer testar suas reações. De mãos vazias, você deverá segurar a naja pelo pescoço, evitando-lhe os dentes mortais. Você se agacha, tensionando os músculos para o momento decisivo. Jogue dois dados. Se o total for igual ou menor que a sua HABILIDADE, volte para 55. Se o total for maior que a sua HABILIDADE, vá para 202. ")
    
    input("\nPressione Enter para rodar os dados...")
    x = roda_1_dado()
    print(f"\nO dado 1 tirou: {x}.")
    y = roda_1_dado()
    print(f"\nO dado 2 tirou: {y}.")
    soma = x + y

    print(f"\nA soma dos dados deu {soma}, sua habilidade é {habilidade}.")

    if soma <= habilidade:
        input("\n\nPressione Enter para ir para 55 ...")
        aventura55()

    else:
        input("\nPressione Enter para ir para 202...")
        aventura202()


def aventura153():
    print(stats_final)
    print("CAP 153")
    print("\nA porta abre para um pequeno aposento, no qual há um crânio humano cujos olhos são jóias, pousado sobre um pedestal de mármore. Uma bateria de bestas com dardos está fixada à parede da esquerda, e duas pequenas bolas de madeira estão no chão, bem perto da porta. Você: \n\nEntrará no aposento e apanhará o crânio? - Vá para 390\nJogará, da porta, uma das bolas de madeira no crânio? - Vá para 371\nFechará a porta e continuará para o oeste, levando as bolas de madeira? - Volte para 74 ")
    
    escolha = input("\nIr para 390, 371, ou 74?: ")
    match escolha:
        case '190':
            aventura190()
        case '371':
            aventura371()
        case '74':
            aventura74()
        case _:
            print("\nOpção Invalida!")
            aventura153()

def aventura154():
    print(stats_final)
    print("CAP 154")
    print("\nCorrendo pelo túnel, você logo alcança o Bárbaro e diz a ele que a passagem do leste conduz a um beco sem saída. Ele faz um aceno com a cabeça, num entendimento silencioso, e ambos partem para o oeste. Volte para 22. ")

    input("\nPressione Enter para ir para 22...")
    aventura22()




def aventura155():
    print(stats_final)
    print("CAP 155")
    print("\nAs palavras do poema dela cruzam velozmente a sua mente: “Quando o corredor a água encontrar, não se apresse em recuar...” Está claro, é aqui que ela quer que você mergulhe na água. Agora, você deve decidir. Se quiser mergulhar na água, vá para 378. Se preferir caminhar de volta para o túnel, vá para 322. ")

    escolha = input("\nIr para 378 ou 322?: ")
    match escolha:
        case '378':
            aventura378()
        case '322':
            aventura322()
        case _:
            print("\nOpção Invalida!")
            aventura68()


def aventura156():
    print(stats_final)
    print("CAP 156")
    print("\nA pequena placa desliza e se abre facilmente, e você divisa um aposento com um poço profundo no chão atrás da porta. Na parede do outro lado, há dois ganchos de ferro, num dos quais está pendurado um rolo de corda. Se você quiser abrir a porta, pular por cima do poço e pegar a corda, vá para 208. Se preferir continuar para o norte pelo túnel, vá para 326. ")

    escolha = input("ir para 208 ou 326?")

    match escolha:
        case '208':
            mochila.append('corda')
            aventura208()
        case '326':
            aventura326()


def aventura157(sorte):
    print("\nO pequeno cofre se abre facilmente; dentro, uma bolsa de veludo negro contém uma pérola grande. Some 1 ponto de SORTE. Depois de pôr a pérola no bolso, você avança em meio às teias de aranha. Vá para 310. ")

    sorte = sorte + 1

    input("\nPressione Enter para ir para 12...")
    aventura12()






def aventura158(habilidade, energia):
    print(stats_final)
    print("\nCAP 158")
    print("\nVocê leva a moringa aos lábios e toma um gole. O líquido queima tanto que você larga a moringa e segura a garganta em agonia. Você engoliu ácido! Perde 1 ponto de HABILIDADE e 4 de ENERGIA. Se ainda estiver vivo, vá para 275.")
    habilidade = habilidade - 1
    energia = energia - 4
    if energia > 0:
        input(f"\nVocê resiste ao ácido e consegue sair vivo, porem ferido. Sua energia agora é {energia}.\nPressione Enter para seguir para 275...")
        aventura275()
    else:
        fim_de_jogo()

def aventura159():
    print(stats_final)
    print("CAP 159")
    print("\nSuas reações ainda estão lentas por causa do veneno em seu organismo, e, embora você tente pular por cima da língua estendida, suas pernas o traem. A língua pegajosa se enrosca em torno da sua perna, derrubando-o, e começa a □uxa-lo na direção da poça. A espada escorregou da sua mão, e você começa a entrar em pânico. Se você tiver um punhal, vá para 294. Se não tiver um punhal, vá para 334. ")
    
    if 'punhal' in mochila:
        input("Voce possui um Punhal na mochila. Pressione Enter para seguir para 294...")

        aventura294()
    else:
        input("Voce não possui um Punhal na mochila. Pressione Enter para seguir para 334...")
        aventura334()


def aventura160():
    print(stats_final)
    print("CAP 160")
    print("\nSua armadura e sua espada são pesadas e dificultam o salto, mas você aterrissa em segurança, por um triz, na borda do outro lado do poço. Você não perde tempo e se encaminha para o leste. Vá para 237.")

    input("\nPressione Enter para ir para 237...")
    aventura237()


def aventura161():
    print(stats_final)
    print("CAP 161")
    
    print("\nVocê passa sem parar pelos dois Leprechauns e segue para o norte, os risos e a gozação ainda ecoando nos seus ouvidos. Mais adiante no túnel, você pára para descansar e verificar seus pertences. Se você tinha gemas, elas agora sumiram. O Leprechaum que caiu sobre as suas costas roubou-as da mochila. Você amaldiçoa os Leprechauns ladrões e prossegue para o norte. Volte para 29.")

    input("\nPressione Enter para ir para 29...")
    aventura29()


def aventura162(sorte):
    print(stats_final)
    print("CAP 159")

    print("\nRetirando a tampada caixa na luz do túnel, você encontra uma chave de ferro e uma gema grande. É uma safira. Some 1 ponto de SORTE. Colocando as coisas cuidadosamente na mochila, você parte para o norte mais uma vez. Volte para 142. ")

    mochila.append('chave de ferro')

    sorte = sorte + 1

    input("\nPressione Enter para ir para 142...")
    aventura142()

def aventura163():
    print(stats_final)
    print("\nCAP 163")
    print("\nO Anão o chamada sacada, congratulando-o pela vitória. Ela joga um saco na arena e lhe diz para relaxar e recuperar as forças para a parte final do teste. Depois, ele sai, dizendo que estará de volta em 10 minutos. Você abre o saco e encontra uma moringa com vinho e galinha cozida. Se você quiser comer o que o Anão ofereceu, vá para 363. Se preferir simplesmente ficar sentado, esperando que ele volte, vá para 302. ")

    escolha = input("\nIr para 363 ou 302?: ")
    match escolha:
        case '363':
            aventura363()
        case '302':
            aventura302()
        case _:
            print("\nOpção Invalida!")
            aventura163()


def aventura164():
    print(stats_final)
    print("CAP 164")
    print("\nEnquanto você caminha, pingos de água voltam a cair do teto do túnel. Você vê pegadas úmidas, feitas pelas mesmas botas que você havia seguido anteriormente, se dirigindo para o oeste. As pegadas conduzem a uma porta de ferro fechada na parede do lado direito do túnel, mas não parecem continuar a partir dali. Se quiser abrir a porta, vá para 299. Se preferir continuar em frente para o oeste, volte para 83.")

    escolha = input("\nIr para 299 ou 83?: ")
    match escolha:
        case '299':
            aventura299()
        case '83':
            aventura83()
        case _:
            print("\nOpção Invalida!")
            aventura164()


def aventura165():
    print(stats_final)
    print("CAP 165")
    print("\nHá uma ranhura no cadeado, na qual você coloca a moeda. Imediatamente, o cadeado se abre, e você consegue desacorrentar as pernas-de-pau. Você as coloca nos ombros e, mais uma vez, parte para o norte. Vá para 234. ")

    input("\nPressione Enter para ir para 234...")
    aventura234()


def aventura166(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome):
    print(stats_final)
    print("CAP 166")
    print("\nAo tocar o olho de esmeralda do ídolo, você ouve um rangido abaixo de si. Olhando na direção do ruído. Você fica abismado ao ver os dois pássaros empalhados voando. As asas dele batem aos arrancos, mas logo estão sobre você e parecem prontos para atacar. Lute com um dos GUARDIÕES VOADORES de cada vez, mas reduza a sua HABILIDADE em 3 pontos durante este combate, pois a posição restringe-lhe os movimentos.\n                                HABILIDADE          ENERGIA\nPrimeiro GUARDIÃO VOADOR     -      7                  8\nSegundo GUARDIÃO VOADOR      -      8                  8\n\nSe você vencer, volte para 11. ")

    habilidade = habilidade - 3

    energia_monstro = 8
    habilidade_monstro = 7
    nome = "Primeiro GUARDIÃO VOADOR"
    batalha(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome)

    input(f"Parabens! Você derrotou o {nome}. Pressione Enter para iniciar a lutar com Segundo GUARDIÃO VOADOR...")

    energia_monstro = 8
    habilidade_monstro = 8
    nome = "segundo GUARDIÃO VOADOR"

    batalha(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome)

    input("Você vencer, pressione Enter para ir para 11...")

    aventura11()

    



def aventura167(energia):
    print(stats_final)
    print("CAP 167")
    print("\nVocê gira o gancho de ferro em torno da cabeça e o atira na fera lá embaixo. As enormes mandíbulas do Diabo do Poços e fecham firmemente sobre o gancho, e, em seguida, ele joga a cabeça para trás. Ainda segurando a corda, você é puxado do alto da muralha e despenca no fundo do poço. Você perde 4 pontos de ENERGIA. Se ainda estiver vivo, vá para 203. ")

    energia = energia - 4

    if energia > 0:
        input("Você sai vivo, mas ferido. Pressione Enter para seguir para 203...")
        aventura203()

    else:
        fim_de_jogo()


def aventura168():
    print(stats_final)
    print("\nCAP 168")
    print("\nLevantando o trinco e empurrando a pesada porta de pedra, você se vê em uma grande caverna. A luz é fraca e sombria, mas seus olhos logo se adaptam e você vê que as paredes são úmidas e revestidas de algas verdes. O chão está coberto de palha. A atmosfera é quente, úmida e fétida, e um zumbido suave enche o ar. Com cautela, você avança pela palha na direção de um dos cantos da caverna, onde parece haver um poço raso. Espiando com cuidado para dentro do poço, você fica enojado ao ver uma massa de vermes esbranquiçados que se contorcem, alguns deles chegando a meio metro de comprimento. Nauseado, você está prestes a ir embora quando repara que os corpos ondulantes dos vermes estão amontoados em torno de um punhal, cuja ponta está firmemente presa a uma fenda no fundo do poço. O cabo é envolto em couro negro com incrustações de opalas, e a lâmina é feita de um estranho metal lustrado preto-avermelhado. Você fica doido para pegar a arma, mas isso significaria enfiar a mão no meio daqueles vermes. \n\nVocê tenta apanhar o punhal - volte para 94\nou recua enojado e sai da caverna - vá para 267. ")

    escolha = input("\nIr para 94 ou 267?: ")
    match escolha:
        case '94':
            aventura94()
        case '267':
            aventura267()
        case _:
            print("\nOpção Invalida!")
            aventura168()


def aventura169():
    print(stats_final)
    print("\nCAP 169")
    print("\nEle olha desconfia do quando você lhe oferece uma parte das suas Provisões. Mas a fome é mais forte que o medo, e ele acaba pondo a comida na boca. Você pergunta o que ele está fazendo nos túneis, e ele explica que é servo de um dos Juízes da Prova, os controladores de seções do calabouço designados pelo Barão Sukumvit. Diz que gostaria de escapar, mas ninguém pode sair do calabouço, a fim de impedir que o segredo da construção seja revelado. Você diz-se um dos concorrentes na Prova dos Campeões e que apreciaria qualquer tipo de ajuda. Esfregando o queixo, ele vira-se para você e diz: “Tudo o que lhe posso dizer é que, em um dos túneis setentrionais, há uma cadeira esculpida na forma de um pássaro demoníaco; um painel secreto no braço da cadeira contém uma poção em um frasco de vidro. É uma Poção de Réplica. Agora, preciso realizar minhas tarefas. Boa sorte. Espero que nos encontremos de novo fora destes túneis infernais.” O homem sai se arrastando e você continua sua jornada para o oeste. Volte para 109. ")

    input("\nPressione Enter para ir para 109...")
    aventura109()


def aventura170():
    print(stats_final)
    print("\nCAP 170")
    print("\nAo se aproximar da figura prostrada, você vê que é um dos seus rivais na Prova dos Campeões. É, na realidade, a Mulher-elfo. Ela luta tenazmente pela vida, envolta no abraço de uma enorme JIBÓIA que lhe esmaga os ossos. Se você quiser ajudá-la, vá para 281. Se preferir deixá-la à própria sorte e retornar pelo túnel para seguir para o norte, vá para 192. ")

    escolha = input("\nIr para 281 ou 192?: ")
    match escolha:
        case '281':
            aventura281()
        case '192':
            aventura192()
        case _:
            print("\nOpção Invalida!")
            aventura170()



def aventura171(energia):
    print(stats_final)
    print("\nCAP 171")
    print("\nA porta abre para um pequeno aposento, mas, antes que saiba o que está acontecendo, você despenca no vazio havia um poço atrás da porta e você não o viu. Você cai pesadamente no fundo e se contorce em dores. Perde 4 pontos de ENERGIA. As paredes do poço são rugosas e têm muitos pontos onde apoiar os pés e as mãos; por isso, você consegue fazer a escalada e sair com bastante facilidade. Você amaldiçoa sua própria ansiedade e diz a si mesmo que doravante será mais cuidadoso. No interior do aposento, você vê dois ganchos de ferro numa das paredes. Há um rolo de corda pendurado em um deles; você o coloca na mochila, salta de volta por cima do poço e sai do aposento, dirigindo-se ao norte. Vá para 326. ")

    energia = energia - 4

    input("\nPressione Enter para ir para 326...")
    aventura326()

def aventura172(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome):
    print(stats_final)
    print("\nCAP 172")
    print("\nLembrando da descrição da abjeta Besta Sangrenta, e da advertência quanto aos gases tóxicos que exalam da poça da fera, você cobre a boca com a manga da camisa e, atento, avança, espada na mão, para a língua do monstro. Enquanto você contorna a poça, a fera se projeta para frente e estica a língua, mas você está prevenido e a perfura com um golpe da espada. A fera urra de dor e se estica, frenética, para fora da poça, tentando abocanhá-lo com as mandíbulas inundadas de sangue. Você golpeia-lhe a carantonha com a espada, na tentativa de atingir-lhe os olhos verdadeiros.\n\nBESTA SANGRENTA    -    HABILIDADE 12        ENERGIA 10\n\nQuando você vencer a sua segunda Série de Ataque, vá para 278. ")

    habilidade_monstro = 12
    energia_monstro = 10
    nome = "BESTA SANGRENTA"

    batalha(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome)

    input(f"Parabens! Você venceu a {nome}. Pressione Enter para seguir para 278...")


def aventura173():
    print(stats_final)
    print("\nCAP 173")
    print("\nA água fresca é revigorante e vem de uma fonte que foi salpicada com poeira de Duende. Se você ainda não o fez, poderá beber da outra fonte - vá para 337 - ou continuar para o norte - vá para 368. ")
    escolha = input("\nIr para 337 ou 368?: ")
    match escolha:
        case '337':
            aventura337()
        case '368':
            aventura368()
        case _:
            print("\nOpção Invalida!")
            aventura173()



def aventura174(sorte):
    print(stats_final)
    print("\nCAP 174")
    print("\nQuando você está retornando para a porta, o zumbido aumenta de intensidade, e você procura desesperadamente descobrir de onde ele vem. Ao olhar para o alto, você vê num relance a imensa e grotesca forma negra de uma MOSCA GIGANTE surgindo de uma reentrância no alto da parede da caverna. Ao se aproximar, você se dá conta de que ela tem pelo menos um metro e meio de comprimento. As asas opacas vibram, produzindo o abominável zumbido que você vem ouvindo; as seis pernas peludas estão posicionadas para agarrá-lo; abaixo dos olhos multifacetados, há uma longa probóscida, negra e lustrosa, que se movimenta malignamente para dentro e para fora. Você retirou o tesouro da Mosca Gigante do ninho de larvas, e agora deve enfrentar as consequências. Teste sua Sorte. Se você tiver sorte, volte para 39. Se não tiver sorte, vá para 350. ")

    input("\nPressione Enter para rodar os dados...")
    x = roda_1_dado()
    print(f"\nO dado 1 tirou: {x}.")
    y = roda_1_dado()
    print(f"\nO dado 2 tirou: {y}.")
    soma = x + y

    print(f"\nA soma dos dados deu {soma}, sua sorte é {sorte}.")

    if soma <= sorte:
        input("\nVoce deu sorte!\nPressione Enter para ir para 39 ...")
        sorte = sorte - 1
        aventura39()

    else:
        input("\nVocê não teve sorte!\nPressione Enter para ir para 350...")
        sorte = sorte - 1
        aventura350()


def aventura175(sorte):
    print(stats_final)
    print("\nCAP 175")
    print("\nPresa à coleira de um dos Cães de Guarda, há uma cápsula de metal. Você retira a parte de cima da cápsula e encontra um pequeno dente lá dentro. É um dente de Leprechaum, que lhe trará boa sorte. Some 2 pontos de SORTE. Você põe o dente no bolso e parte para o leste pelo túnel. Vá para 315. ")

    sorte = sorte + 2

    input("\nPressione Enter para ir para 315...")
    aventura315()



def aventura176():
    print(stats_final)
    print("\nCAP 176")
    print("\nCaminhando cuidadosamente, você vai subindo os degraus devagar. Logo chega ao topo sem problemas. Continue pelo túnel e vá para 277. ")
    input("\nPressione Enter para ir para 277...")
    aventura277()



def aventura177(sorte):
    print("\nVocê só tem tempo para ouvir o Gnomo gritar: “Três coroas!”, antes que a fechadura estale e abra. Quando a pesada porta gira lentamente para fora, o Gnomo corre na direção dela, jogando a bola de vidro a seus pés. Um gás verde escapa do vidro quebrado, e você tenta não o inspirar. Teste sua Sorte. Se você tiver sorte, vá para 243. Se não tiver sorte, volte para 103. ")


    input("\nPressione Enter para rodar os dados...")
    x = roda_1_dado()
    print(f"\nO dado 1 tirou: {x}.")
    y = roda_1_dado()
    print(f"\nO dado 2 tirou: {y}.")
    soma = x + y

    print(f"\nA soma dos dados deu {soma}, sua sorte é {sorte}.")

    if soma <= sorte:
        input("\nVoce deu sorte!\nPressione Enter para ir para 243 ...")
        sorte = sorte - 1
        aventura243()

    else:
        input("\nVocê não teve sorte!\nPressione Enter para ir para 103...")
        sorte = sorte - 1
        aventura103()


def aventura178():
    print(stats_final)
    print("\nCAP 178")
    print("\nA porta não resiste às violentas pancadas que  você desfere. A placa central racha e se despedaça; você abre a pontapés um buraco grande o bastante para por ele se esgueirar. Molhado, mas feliz por ter sobrevivido a essa ameaça, você parte para o norte de novo. Vá para 344. ")

    input("\nPressione Enter para ir para 344...")
    aventura344()


def aventura179():
    print(stats_final)
    print("\nCAP 179")
    print("\nQuando você parte na direção do Anão, ele tira do cinto dois dardos de mão e os atira contra você e Throm, atingindo-os nas pernas. Ambos ficam instantaneamente paralisados pelo veneno existente na ponta dos dardos. Você perde 2 pontos de ENERGIA. Como que pregado ao chão, você vê o Anão se aproximar e retirar-lhe o dardo coxa. Ele pergunta se agora você está disposto a entrar da em seu campeonato. Você se esforça para balançar a cabeça afirmativamente. Aos poucos, os efeitos do veneno se dissipam, e a mobilidade retorna. O Anão ordena que você o siga e que Throm espere o retorno dele. Ele abre uma porta secreta na parede da câmara, e vocês entram em um pequeno aposento circular. Ele fecha a porta atrás de você e lhe dá dois dados de osso, mandando que os jogue no chão.Você tira um seis e um dois, total oito. O Anão ordena um novo lançamento, mas desta vez você tem que adivinhar o total: será igual, maior ou menor que oito? \n\nSe você preferir igual a oito - vá para 290.\nSe optar por maior que oito - volte para 84.\nSe escolher menor que oito - vá para 191. ")

    energia = energia - 2

    escolha = input("\nIr para 290, 84 ou 191?: ")
    match escolha:
        case '290':
            aventura290()
        case '84':
            aventura84()
        case '191':
            aventura191()
        case _:
            print("\nOpção Invalida!")
            aventura179()


def aventura180(sorte):
    print(stats_final)
    print("\nCAP 180")
    print("\nVocê avança na direção da Besta Sangrenta; de repente, sente-se fraco. O gás que emana da poça é altamente tóxico, e você vai ao chão, inconsciente. Teste sua Sorte. Se você tiver sorte, volte para 53. Se não tiver, vá para 272. ")

    input("\nPressione Enter para rodar os dados...")
    x = roda_1_dado()
    print(f"\nO dado 1 tirou: {x}.")
    y = roda_1_dado()
    print(f"\nO dado 2 tirou: {y}.")
    soma = x + y

    print(f"\nA soma dos dados deu {soma}, sua sorte é {sorte}.")

    if soma <= sorte:
        input("\nVoce deu sorte!\nPressione Enter para ir para 53 ...")
        sorte = sorte - 1
        aventura53()

    else:
        input("\nVocê não teve sorte!\nPressione Enter para ir para 272...")
        sorte = sorte - 1
        aventura272()


def aventura181(sorte):
    print(stats_final)
    print("\nCAP 181")
    print("\nO túnel conduz a um salão com piso de mármore e pilares que se erguem até o teto. Ao atravessar o piso, suas passadas ecoam pelo salão. Os cabelos da sua nuca começam a ficar em pé, pois você pressente que está sendo observado. Sem que você saiba, um dos seus rivais se esconde atrás de um pilar. É o NINJA, o terrível assassino vestido com o manto negro. Sem qualquer ruído, ele sai do esconderijo e joga um disco estrelado nas suas costas. Uma voz interior manda que você se abaixe. Teste sua Sorte. Se você tiver sorte, vá para 312. Se não tiver sorte, volte para 45. ")

    input("\nPressione Enter para rodar os dados...")
    x = roda_1_dado()
    print(f"\nO dado 1 tirou: {x}.")
    y = roda_1_dado()
    print(f"\nO dado 2 tirou: {y}.")
    soma = x + y

    print(f"\nA soma dos dados deu {soma}, sua sorte é {sorte}.")

    if soma <= sorte:
        input("\nVoce deu sorte!\nPressione Enter para ir para 312 ...")
        sorte = sorte - 1
        aventura312()

    else:
        input("\nVocê não teve sorte!\nPressione Enter para ir para 45...")
        sorte = sorte - 1
        aventura45()


def aventura182():
    print(stats_final)
    print("\nCAP 182")
    print("\nA temperatura continua a subir, e você começa a pingar suor. Adiante, o calor se intensifica. Parece que você está numa fornalha. A situação é tão insuportável que você começa a desfalecer. Se você tiver bebido o líquido do tubo de bambu, volte para 25. Se não tiver parado para beber o líquido, vá para 242. ")

    if 'liquido do tubo de bambu' not in ativos:
        input("Você nao tomou o liquido. Pressione Enter para ir para 242...")
        aventura242()
    else:
        input("Você tomou o liquido. Pressione Enter para ir para 25...")
        aventura25()



def aventura183():
    print(stats_final)
    print("\nCAP 183")
    print("\nVocê sobe nas pernas-de-pau e dá alguns passos experimentais. Sua confiança aumenta, e logo você se sente capaz de enfrentar a caminhada pelo lodo. A fumaça sobe da base das pernas-de-pau: o lodo começa a corroê-las. Você segue em frente com firmeza e acaba atingindo terreno sólido de novo. Infelizmente, as pernas-de-pau ficam cobertas de lodo, e você é forçado a abandoná-las. Se quiser ir para o oeste, vá para 386. Se preferir continuar para o norte, vá para 218.")

    escolha = input("\nIr para 386 ou 218?: ")
    match escolha:
        case '386':
            aventura386()
        case '218':
            aventura218()
        case _:
            print("\nOpção Invalida!")
            aventura183()


def aventura184():
    print(stats_final)
    print("\nCAP 184")
    print("\nO Bárbaro, que se diz chamar Throm, amarra a corda em volta da cintura, dando-lhe a outra ponta. Ao acender a tocha, você nota um ar de desconfiança nos olhos do Bárbaro. Lentamente, ele sobe na borda do poço, enquanto você se firma no chão e segura a corda tensa. Ao abaixá-lo aos poucos, você vê os lados lisos do poço iluminados pela tocha de Throm. Ele finalmente chega ao fundo e grita que há um outro túnel rumo ao norte. Manda que você prenda a corda em uma rocha saliente na borda do poço e desça. Se você quiser ficar com o Bárbaro e seguir para o norte pelo túnel inferior, vá para 323. Se desejar abandoná-lo, pulando por cima do poço para se dirigir ao oeste, volte para 149. ")

    escolha = input("\nIr para 323 ou 149?: ")
    match escolha:
        case '323':
            aventura323()
        case '149':
            aventura149()
        case _:
            print("\nOpção Invalida!")
            aventura184()


def aventura185():
    print(stats_final)
    print("\nCAP 185")
    print("\nOs Trogloditas estão tão concentrados na dança tribal que não ouvem o ruído da sua espada, e você engatinha e passa. Quando acha que está suficientemente longe, você se levanta e corre pelo piso da caverna. À sua frente, corre um rio subterrâneo de leste para oeste através da caverna; sobre ele, uma ponte de madeira. Ao ouvir um barulho, você olha para trás e toma consciência de que foi descoberto. Os Trogloditas estão vindo atrás de você. Se quiser correr pela ponte, vá para 318. Se preferir mergulhar no rio, volte para 47. ")

    escolha = input("\nIr para 318 ou 47?: ")
    match escolha:
        case '318':
            aventura318()
        case '47':
            aventura47()
        case _:
            print("\nOpção Invalida!")
            aventura185()


def aventura186(sorte):
    print("\nLenta e cuidadosamente, você começa a escalar o ídolo. Quando está prestes a segurar na grande orelha, seu pé escorrega, Teste sua Sorte. Se você tiver sorte, vá para 260. Se não tiver sorte, vá para 358. ")

    input("\nPressione Enter para rodar os dados...")
    x = roda_1_dado()
    print(f"\nO dado 1 tirou: {x}.")
    y = roda_1_dado()
    print(f"\nO dado 2 tirou: {y}.")
    soma = x + y

    print(f"\nA soma dos dados deu {soma}, sua sorte é {sorte}.")

    if soma <= sorte:
        input("\nVoce deu sorte!\nPressione Enter para ir para 260 ...")
        sorte = sorte - 1
        aventura260()

    else:
        input("\nVocê não teve sorte!\nPressione Enter para ir para 358...")
        sorte = sorte - 1
        aventura358()


def aventura187(mochila):
    print("\nO túnel faz uma curva fechada para a direita, depois da qual você vê um velhinho de barba longa encolhido atrás de uma grande cesta de vime. A cesta está amarrada a uma corda cuja ponta desaparece no teto. Com aparência preocupada,o velho diz: “Não me ataque, estranho. Não sou nenhuma ameaça para você. Estou aqui simplesmente para ajudá-lo. Se você fizesse a gentileza de me oferecer algum tipo de remuneração, eu ficarei feliz em içá-lo na cesta para o nível superior. E, acredite-me, você deveria estar lá.” Se você quiser dar ao homem alguma coisa da sua mochila pelo serviço, vá para 360. Se preferir passar por ele e seguir pelo túnel, vá para 280. ")

    escolha = input("\nIr para 360 ou 280?: ")
    match escolha:
        case '360':
            print("Sua mochila: ", mochila)
            if not mochila:
                print("Sua mochila está vazia! Voce nao tem o que entregar.\n\nPressione Enter para seguir para 280...")
                aventura280()
            else:
                item_entregar = input("\nO que deseja entregar a ele?")
                if item_entregar in mochila:
                    mochila.remove(item_entregar)
                    print(f"\nVocê Entregou {item_entregar} a ele.")
                    input("\n\nPressione Enter para seguir para 360...")
                    aventura360()
        case '280':
            aventura280()
        case _:
            print("\nOpção Invalida!")
            aventura187()



def aventura188(garota_espirito):
    print(stats_final)
    print("CAP 188")
    print("\nO túnel começa a declinar e termina numa poça profunda. Se você conseguir se lembrar do poema da garota-espírito, volte para 155. Se não tiver encontrado a garota-espírito, vá para 224. ")

    if garota_espirito == True:
        input("Você se recorda do poema. Pressione Enter para seguir para 155...")
        aventura155()

    else:
        input("Você não se encontrou com a garota-espírito. Pressione Enter para seguir para 224...")
        aventura224()


def aventura189(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome):
    print(stats_final)
    print("CAP 189")

    print("As pontas da maça do Orca penetram dolorosamente na sua coxa esquerda. Você perde 3 pontos de ENERGIA. Você cambaleia para trás, mas consegue recuperar o equilíbrio a tempo de se defender. Felizmente, o túnel é estreito demais para que ambos os Orcas ataquem-no a um só tempo. Lute com um de cada vez. \n\n                        HABILIDADE          ENERGIA\nPrimeiro ORCA     -         5                  5\nSegundo ORCA      -         6                  4\n\nSe você vencer, vá para 257.")

    habilidade_monstro = 5
    energia_monstro = 5
    nome = "Primeiro ORCA"

    batalha(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome)

    print(f"Parabéns você venceu o {nome}, Pressione Enter para iniciar a batalha com o segundo ORCA...")

    habilidade_monstro = 6
    energia_monstro = 4
    nome = "Segundo ORCA"

    batalha(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome)

    input("Você saiu vitorioso dessa batalha. Pressione Enter para ir para 257...")
    aventura257()


def aventura190(energia):

    print(stats_final)
    print("CAP 190")
    print("\nSeu corpo vibra desenfreadamente, e você não consegue evitar o desmaio. Você perde 3 pontos de ENERGIA. Se ainda estiver vivo, volte para 50. ")

    energia = energia - 3
    if energia > 0:
        print("Você sobrevive, mas sai ferido. Pressione Enter para ir para 50...")
    else:
        fim_de_jogo()


def aventura191():
    print(stats_final)
    print("CAP 191")
    print("\nJogue dois dados. Se o total for menor que oito, volte para 152. Se o total for igual ou maior que oito, volte para 121. ")

    input("\nPressione Enter para rodar os dados...")
    x = roda_1_dado()
    print(f"\nO dado 1 tirou: {x}.")
    y = roda_1_dado()
    print(f"\nO dado 2 tirou: {y}.")
    soma = x + y

    print(f"\nA soma dos dados deu {soma}.")

    if soma < 8:
        input("\nPressione Enter para ir para 152 ...")
        aventura152()

    else:
        input("\nPressione Enter para ir para 121...")
        aventura121()



def aventura192():
    print(stats_final)
    print("CAP 192")
    print("\nCaminhando pelo túnel, você repara em uma grade de ferro no chão. Se quiser parar e levantá-la, volte para 120. Se preferir prosseguir, vá para 292.")

    escolha = input("\nIr para 120 ou 292?: ")
    match escolha:
        case '120':
            aventura120()
        case '292':
            aventura292()
        case _:
            print("\nOpção Invalida!")
            aventura192()


def aventura193():
    print("CAP 193\n")
    print("\nO ácido queima a parede do seu estômago, penetrando nos seus órgãos vitais. Você tomba inconsciente para nunca mais se recuperar. Sua aventura termina aqui.")

    fim_de_jogo()


def aventura194():
    print(stats_final)
    print("CAP 194")
    print("\nEm uma plataforma de pedra na parede do túnel, você vê dois livros empoeirados encadernado sem couro. Throm expressa seu desprezo pela palavra escrita com um grunhido, insistindo para que você deixe os livros de lado e siga adiante com ele.\n\nVocê: Abrirá o livro de couro vermelho? - Volte para 52\nAbrirá o livro de como preto? - Volte para 138\nContinuará para o norte pelo túnel? - Vá para 369 ")

    escolha = input("\nIr para 52, 138 ou 369?: ")
    match escolha:
        case '52':
            aventura52()
        case '138':
            aventura138()
        case '369':
            aventura369()
        case _:
            print("\nOpção Invalida!")
            aventura194()


def aventura195(energia):
    print(stats_final)
    print("CAP 195")
    print("\nVocê desembainha a espada e corre na direção do velho. Ele ergue o braço esquerdo e, subitamente, você esbarra em uma barreira invisível. “Não seja tolo, meus poderes são grandes!”, diz o velho calmamente. “Se você não acredita em mim, veja isto.” Saindo do nada, um punho voador lhe desfere um soco no rosto antes que você possa se esquivar.Você perde 1 ponto de ENERGIA. Você sacode a cabeça e esfrega o queixo. Parece que não tem alternativa senão tentar responder à pergunta do velho. Vá para 382. ")

    energia = energia - 1

    input("\nPressione Enter para ir para 382...")
    aventura382()


def aventura196():
    print(stats_final)
    print("CAP 196")
    print("\nVocê levanta o escudo bem a tempo de se proteger de uma saraivada de espinhos lançados contra seu coração pela cauda do Mantécora. Ileso, com os espinhos cravados no escudo, você desembainha a espada e avança para o Mantécora. \n\nMANTÉCORA    -    HABILIDADE 11        ENERGIA 11 \n\nSe você vencer, vá para 364. ")

    batalha(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome)


def aventura197():
    print(stats_final)
    print("CAP 197")
    print("\nGraças aos céus, a temperatura agora começa a cair rapidamente, e logo parece quase fresca de novo. No lado esquerdo do túnel, há uma porta fechada e nela, uma pequena placa de ferro que talvez possa ser aberta. Você:\n\nTentará abrir a porta? - Volte para 171\nTentará fazer deslizar a placa de ferro? - Volte para 156\nContinuará para o norte, subindo o túnel? - Vá para 326 ")
   
    escolha = input("\nIr para 171, 156 ou 326?: ")
    match escolha:
        case '171':
            aventura171()
        case '156':
            aventura156()
        case '326':
            aventura326()
        case _:
            print("\nOpção Invalida!")
            aventura197()


def aventura198():
    print(stats_final)
    print("CAP 198")

    print("\nQuando o gás se dissipa, você caminha de volta para a arca e olha dentro dela. Há uma corrente com pingente jogada no fundo, mas alguém já retirou a pedra que estava incrustada nele. Isso o aborrece tanto que você o atira ao chão e sai furioso do aposento, subindo o túnel. Vá para 230.")

    input("\nPressione Enter para ir para 230...")
    aventura230()


def aventura199():
    print(stats_final)
    print("CAP 199")
    print("\nOs dardos da besta são em número tão grande que é impossível evitá-los. Jogue um dado para determinar o número de dardos que lhe atingem o corpo, perdendo 2 pontos de ENERGIA para cada um deles. Se ainda estiver vivo, terá que descansar aqui por um longo tempo para se recuperar dos ferimentos. Perde 1 ponto de SORTE. Quando você, finalmente, se sente forte o bastante para seguir adiante, sai do aposento e continua para o oeste pelo túnel. Volte para 74. ")

    input("\nPressione Enter para rodar os dados...")
    x = roda_1_dado()

    sorte = sorte - 1
    energia = energia - x * 2

    print(f"\nO dado tirou: {x}.")
    print(f"\no numero de dardos recebidos é {x}, sua energia agora é {energia}.")


    if energia > 0:
        input("Você sobrevive mas sai ferido.\n\nPressione Enter para seguir para 74...")
    else:
        fim_de_jogo()

def aventura200():
    print(stats_final)
    print("CAP 200")
    print("\nA porta abre para um pequeno aposento como chão coberto de palha. No centro do aposento, há uma grande gaiola coberta de cerca de dois metros de altura; uma corda presa ao topo da cobertura de pano passa por um anel de ferro no teto e desce até o chão. Se você quiser levantar o pano, vá para 321. Se preferir sair do aposento e se dirigir para o norte pelo túnel, vá para 316.")

    escolha = input("\nIr para 321 ou 316?: ")
    match escolha:
        case '321':
            aventura321()
        case '316':
            aventura316()
        case _:
            print("\nOpção Invalida!")
            aventura200()



def aventura201():
    print(stats_final)
    print("CAP 201")

    print("\nVocê revista os armários e caixas no quarto de Erva mas não encontra nada, a não ser um osso velho. Há uma porta na parede leste da câmara, e você resolve sair. Pode levar o osso velho, se quiser. Você agora está de pé no final de um outro túnel. Vá para 305.")

    item = input("Deseja levar o osso? (1. Sim - 2. Não): ")

    match item:
        case '1':
            mochila.append('osso velho')
            input("\n*Osso adicionado a mochila.*\n\nPressione Enter para ir para 305...")
            aventura305()
        case '2':
            input("\nPressione Enter para ir para 305...")
            aventura305()



def aventura202(sorte):
    print(stats_final)
    print("CAP 202")
    print("\nAs reações da naja são mais rápidas do que as suas, e a cabeça estufada do animal se projeta para mordê-lo. Teste sua sorte. Se você tiver sorte, volte para 18. Se não tiver sorte, volte para 42.")

    input("\nPressione Enter para rodar os dados...")
    x = roda_1_dado()
    print(f"\nO dado 1 tirou: {x}.")
    y = roda_1_dado()
    print(f"\nO dado 2 tirou: {y}.")
    soma = x + y

    print(f"\nA soma dos dados deu {soma}, sua sorte é {sorte}.")

    if soma <= sorte:
        input("\nVoce deu sorte!\nPressione Enter para ir para 18 ...")
        sorte = sorte - 1
        aventura18()

    else:
        input("\nVocê não teve sorte!\nPressione Enter para ir para 42...")
        sorte = sorte - 1
        aventura42()



def aventura203(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome):
    print(stats_final)
    print("CAP 203")
    print("\nVocê se levanta com dificuldade e desembainha a espada. Faz isso bem a tempo, pois a assustadora fera se aproxima velozmente. Esta vai ser uma das lutas mais difíceis de sua vida.\n\nDIABO DO POÇO    -    HABILIDADE 12    -    ENERGIA 15\n\nSe você vencer, vá para 258.")

    energia_monstro = 15
    habilidade_monstro = 12
    nome = "DIABO DO POÇO"

    batalha(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome)

    print(f"Você conseguiu derrotar o {nome}!!\n\nPressione Enter para seguir para 258...")


def aventura204(sorte):
    print(stats_final)
    print("\nCAP 204")
    print("\nHá uma placa sensível à pressão no topo do pedestal, e, logo que o crânio é colocado de volta sobre ele, o mecanismo invisível é disparado. Imediatamente, uma chuva de dardos lançados pela besta atravessa o aposento. Teste sua Sorte. Se você tiver sorte, volte para 131. Se não tiver sorte, volte para 199.")

    input("\nPressione Enter para rodar os dados...")
    x = roda_1_dado()
    print(f"\nO dado 1 tirou: {x}.")
    y = roda_1_dado()
    print(f"\nO dado 2 tirou: {y}.")
    soma = x + y

    print(f"\nA soma dos dados deu {soma}, sua sorte é {sorte}.")

    if soma <= sorte:
        input("\nVoce deu sorte!\nPressione Enter para ir para 131 ...")
        sorte = sorte - 1
        aventura131()

    else:
        input("\nVocê não teve sorte!\nPressione Enter para ir para 199...")
        sorte = sorte - 1
        aventura199()



def aventura205():
    print(stats_final)
    print("\nCAP 205")
    print("\nCorrendo atrás dos Leprechauns, você ouve mais risos, só que agora eles vêm de trás de você. Você se vira e vê mais seis Leprechauns saindo de uma porta oculta na parede do túnel. De repente, mais um Leprechaun salta de uma plataforma fixada no teto e cai sobre suas costas. Livrando-se dele com um safanão, você desembainha a espada, o que faz com que os Leprechauns riam ainda mais alto. Se você quiser atacá-los, vá para 306. Se preferir tentar passar por eles, volte para 161. ")

    escolha = input("\nIr para 306 ou 161?: ")
    match escolha:
        case '306':
            aventura306()
        case '161':
            aventura161()
        case _:
            print("\nOpção Invalida!")
            aventura205()



def aventura206():
    print(stats_final)
    print("\nCAP 206")
    print("\nAs estalactites continuam a cair ao redor, mas você não tem força suficiente para fazer mais do que se arrastar na direção do arco. De repente, sente um braço em volta da cintura e se dá conta, em estado de semi-inconsciência, de que Throm o está carregando. Ele o põe na segurança do túnel e cuida dos seus ferimentos. Você resolve comer parte das Provisões para ajudar a recuperar as forças, e dá também uma parte para Throm, como agradecimento por ele tê-lo salvado. Ele se desculpa por ter iniciado o desabamento das rochas e lhe oferece a mão. Apesar da dor, você consegue sorrir e apertar a mão dele. Quando você finalmente se recupera, levanta-se e segue para o leste, com Throm caminhando à sua frente. Volte para 60.")

    input("\nPressione Enter para ir para 60...")
    aventura60()


def aventura207(energia):
    print(stats_final)
    print("\nCAP 207")
    print("\nVocê tira a camisa e a rasga ao meio, depois amarra cada um dos pedaços em volta de cada pé, a fim de se proteger em certa medida do lodo corrosivo, e dispara para cruzá-lo a passos largos. No terreno fume do outro lado do lodaçal, você tenta freneticamente, com a espada, arrancar a camisa que queima em seus pés. Porém, parte do lodo penetrou até seu tornozelo. Você perde 3 pontos de ENERGIA. Partindo para o norte de novo, você chega a uma encruzilhada. \n\nSe quiser ir para o oeste, vá para 386.\n\nSe preferir continuar para o norte, vá para 218.")

    energia = energia - 3

    escolha = input("\nIr para 386 ou 218?: ")
    match escolha:
        case '386':
            aventura386()
        case '218':
            aventura218()

        case _:
            print("\nOpção Invalida!")
            aventura207()


def aventura208():
    print(stats_final)
    print("\nCAP 208")
    print("\nA porta abre para o aposento; você toma distância e salta sobre o poço. Coloca a corda na mochila e salta de volta por sobre o poço para sair do aposento e prosseguir para o norte. Vá para 326. ")

    input("\nPressione Enter para ir para 326...")
    aventura326()


def aventura209():
    print(stats_final)
    print("\nCAP 209")
    print("\nVocê fica desolado ao descobrir que não apenas todas as suas Provisões restantes estão encharcadas e imprestáveis para comer, mas também que um dos seus tesouros desapareceu. Risque um item da sua Lista de Equipamentos ou uma de suas jóias ou poções. Você guarda cuidadosamente na mochila as posses que lhe restam e parte para o norte outra vez. Vá para 356. ")

    input("\nPressione Enter para ir para 356...")
    aventura356()




def aventura210():
    print(stats_final)
    print("\nCAP 210")
    print("\nVocê entra em um aposento no qual há um homem maltrapilho, de pé, acorrentado, à parede pelo braço esquerdo. Vendo que ele não tema mão direita, você se dá conta de que a mão pregada na porta deve ser dele. Implorando piedade, ele se encolhe para longe de você, tanto quanto as correntes permitem. Se você quiser libertá-lo das cadeias, volte para 27. Se preferir sair do aposento e se dirigir para o norte, volte para 78. ")


def aventura211(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome):
    print(stats_final)
    print("\nCAP 211")
    print("\nVocê consegue se livrar do aperto de Erva e desembainha a espada. Apanhando um banco quebrado para lhe servir de arma, ela avança na sua direção.\n\nERVA    -    HABILIDADE 9        ENERGIA 9\n\nSe você vencer, volte para 201.")

    energia_monstro = 9
    habilidade_monstro = 9

    batalha(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome)

    input("Você vence a batalha! Pressione Enter para seguir para 201...")

    aventura201()


def aventura212():
    print("\nSegurando a corda firmemente, você toma distância para o salto. Contudo, sob a luz fraca, você não nota que alguém enfraqueceu a corda, a ponto de parti-la em duas, logo acima do local em que você está segurando. Quando se lança por sobre o poço, a corda rompe e você grita de medo ao despencar de cabeça nas profundezas. Vá para 285. ")


    input("\nPressione Enter para voltar para 285...")

    aventura285(habilidade, energia)


def aventura213():
    print(stats_final)
    print("\nCAP 213")
    print("\nO túnel logo se divide em dois. Você ouve um zumbido que vem do ramo da direita. Se quiser caminhar para o oeste para investigar quem ou o que está fazendo o ruído, volte para 108. Se preferir continuar para o norte, volte para 14.")

    escolha = input("\nIr para 108 ou 14?: ")
    match escolha:
        case '108':
            aventura108()
        case '14':
            aventura14()
        case _:
            print("\nOpção Invalida!")
            aventura213()


def aventura214():
    print(stats_final)
    print("\nCAP 214")
    print("\nCaminhando em frente, você vê uma linha vermelha pintada no chão do túnel e nota um aviso na parede que diz: “Armas não são permitidas a partir deste ponto.” Se você quiser abandonar suas armas antes de continuar para o norte, vá para 389. Se preferir ignorar o aviso e prosseguir para o norte, volte para 181.")

    escolha = input("\nIr para 389 ou 181?: ")
    match escolha:
        case '389':
            aventura389()
        case '181':
            aventura181()
        case _:
            print("\nOpção Invalida!")
            aventura214()


def aventura215(energia):
    print(stats_final)
    print("\nCAP 215")
    print("\nSua espada arrebenta facilmente a fina casca externa da gigantesca bola de esporos. Uma espessa nuvem de esporos saída da bola se espalha e o envolve. Alguns dos esporos grudam- se à sua pele, que começa a coçar terrivelmente. Aparecem grandes caroços no seu rosto e braços, e sua pele parece estar em fogo. Você perde 2 pontos de ENERGIA. Coçando freneticamente os caroços, você passa por cima da bola de esporos, agora murcha, e segue para o oeste. Volte para 13. ")

    energia = energia - 2

    input("\nPressione Enter para ir para 13...")
    aventura13()

def aventura216():
    print(stats_final)
    print("\nCAP 216")
    print("\nReconhecendo a cabeça de serpentes da Medusa, você fecha os olhos para evitar o olhar mortal da criatura que o transformaria em pedra. \n\nSe você quiser entrar na gaiola com os olhos fechados para enfrentá-la com sua espada, vá para 308. \n\nSe preferir recuar para sair do aposento com os olhos fechados e continuar para o norte, vá para 316. ")

    escolha = input("\nIr para 308 ou 316?: ")
    match escolha:
        case '308':
            aventura308()
        case '316':
            aventura316()
        case _:
            print("\nOpção Invalida!")
            aventura216()


def aventura217(habilidade):
    print(stats_final)
    print("\nCAP 217")

    print("\nA passagem começa a subir lentamente, conduzindo-o sempre para o norte. Você não passa por uma única encruzilhada. Não há portas ou mesmo uma alcova para ser investigada, e você vai ficando mais relaxado enquanto segue adiante. Depois de certo tempo, você se torna tão temerário que não repara em um fino arame estendido bem baixo de lado a lado da passagem. Somente quando o seu pé o toca, e você ouve um ronco distante, é que se dá conta do erro que cometeu. O ronco cresce até um nível ensurdecedor, e subitamente surge da penumbra do túnel à sua frente um gigantesco rochedo que vem rolando na sua direção, ganhando velocidade a cada segundo. Largando o escudo, se tiver um (você perde 1 ponto de HABILIDADE), você se volta para fugir do rochedo que se aproxima. Volte para 36. ")

    if 'escudo' in mochila:
        habilidade = habilidade - 1
        mochila.remove('escudo')
        input("\nPressione Enter para ir para 36...")
        aventura36()
    else:
        input("\nPressione Enter para ir para 36...")
        aventura36()
    


def aventura218():
    print(stats_final)
    print("\nCAP 218")
    print("\nVocê logo chega a uma porta dupla na parede da esquerda. Apura os ouvidos, mas não percebe nada. Tenta a maçaneta, ela gira, você abre uma fresta na porta da esquerda e dá uma espiada. Um guerreiro armado jaz de bruços no chão de um aposento vazio, de paredes lisas e teto baixo. Ele deve estar morto, pois permanece inerte mesmo quando você grita por ele. Uma jóia grande, talvez um diamante, está caída logo adiante do braço esticado. Se você quiser entrar no aposento e pegar a jóia, volte para 65. Se preferir continuar para o norte, vá para 252. ")

    escolha = input("\nIr para 65 ou 252?: ")
    match escolha:
        case '65':
            aventura65()
        case '252':
            aventura252()
        case _:
            print("\nOpção Invalida!")
            aventura218()


def aventura219():
    print(stats_final)
    print("\nCAP 219")
    print("\nA dor nos pulmões força-o a subir à tona para respirar. Infelizmente, um dos Trogloditas o vê e grita pelos companheiros. Indefeso, você vê os arqueiros fazerem pontaria, e uma saraivada de flechas cai sobre você com impacto fatal. Seu corpo sem vida desce o rio boiando, penetrando nas profundezas ocultas da montanha. ")

    fim_de_jogo()


def aventura220():
    print(f"\n{stats_final}")
    print("CAP 220\n")
    print("\nUm 'bong' sombrio soa como um toque de sino fúnebre. Tudo vibra à sua volta, e você aperta os dentes quando sua cabeça também estremece. Todo seu corpo está tremendo, e você cai. Você tirita e tem calafrios, contorcendo-se convulsivamente no chão, à medida que as vibrações se intensificam. Procura desesperadamente uma maneira de parar o sino. Você:\n\nGritará o mais alto possível? - Volte para 61\nTentará abafar o sino com sua bota? - Vá para 346 ")

    escolha = input("Voltar para 61 ou 346?: \n")
    match escolha:
        case '61':
            aventura61()
        case '346':
            aventura346()
        case _:
            print("Opção Invalida!")
            aventura220()
        


def aventura221():
    print(stats_final)
    print("\nCAP 221")
    print("\nO túnel conduz a uma caverna úmida de teto alto, como chão coberto de rochas. Estalactites em forma de dentes pendem ameaçadoramente, os pingos constantes criando poças leitosas no chão. O túnel prossegue atravessando a passagem em arco, a qual é talhada na forma de uma boca demoníaca. Se você quiser examinara caverna, vá para 374. Se preferir prosseguir direto pela passagem em arco, volte para 60. ")

    escolha = input("\nIr para 374 ou 60?: ")
    match escolha:
        case '374':
            aventura374()
        case '60':
            aventura60()
        case _:
            print("\nOpção Invalida!")
            aventura221()


def aventura222():
    print(stats_final)
    print("\nCAP 222")
    print("\nVocê reconhece a fera - é um MANTÉCORA. Levando a sério a advertência do poema, você fica atento para a cauda dele, de cuja ponta sai uma profusão de espinhos afiados, grossos e duros como dardos de ferro. Se você tiver um escudo, volte para 196. Se não estiver carregando um escudo, volte para 6. ")

    if 'escudo' in mochila:
        input("Você tem um escudo. Pressione Enter para ir para 196...")
        aventura196()
    else:
        input("Você não tem um escudo. Pressione Enter para ir para 6...")
        aventura6()



def aventura223(energia):
    print(stats_final)
    print("\nCAP 223")
    print("\nVocê pisa com confiança no primeiro poste e avança para o próximo. Ao tocar o terceiro poste, ele imediatamente solta uma chuva de farpas afiadas, cada uma com vários centímetros de comprimento. Você perde 2 pontos de SORTE. As farpas voam em todas as direções a grande velocidade, e você não consegue evitá-las. Jogue dois dados para saber o número de farpas que lhe penetram a pele. Cada uma delas reduz sua ENERGIA em 1 ponto. Se você ainda estiver vivo, consegue arrastar-se por sobre os postes restantes e se senta para a dolorosa tarefa de retirar as farpas do corpo. Depois de descansar um pouco, você segue para o leste. Vá para 313. ")

    input("\nPressione Enter para rodar os dados...")
    x = roda_1_dado()
    print(f"\nO dado 1 tirou: {x}.")
    y = roda_1_dado()
    print(f"\nO dado 2 tirou: {y}.")
    soma = x + y

    energia = energia - soma

    

    print(f"\nO numero de farpastomadas é {soma}, sua energia agora é {energia}.")

    if energia > 0:       
        input("\nVoce sobrevive, porém sai ferido!\nPressione Enter para ir para 313 ...")
        aventura313()

    else:
        fim_de_jogo()

def aventura224():
    print(stats_final)
    print("\nCAP 224")
    print("\nParece não haver como continuar para o norte. Você dá meia-volta e retorna pelo túnel, passando pela cadeira de madeira. Logo chega à encruzilhada e vira à direita para seguir para o oeste. Volte para 43.")

    input("\nPressione Enter para ir para 43...")
    aventura43()


def aventura225(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome):
    print(stats_final)
    print("\nCAP 225")
    print("\nVocê reage prontamente e, com um golpe de espada, consegue cortar a língua estendida da Besta Sangrenta. A fera urra de dor e se atira para frente, tentando prendê-lo nas mandíbulas ensangüentadas. Esta será uma luta até a morte.\n\nBESTA SANGRENTA    -    HABILIDADE 12        ENERGIA 10\n\nQuando vencer a sua primeira Série de Ataque, Teste sua Sorte.\nSe você tiver sorte, volte para 97. Se não tiver sorte, volte para 21. ")


    energia_monstro = 10
    habilidade_monstro = 12
    nome = "BESTA SANGRENTA"

    batalha(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome)

    input("Você venceu a BESTA SANGRENTA. Pressione Enter para seguir para 21...")

    aventura21()


def aventura226():
    print(stats_final)
    print("\nCAP 226")
    print("\nA carne contém ervas que lhe aumentarão a força. Some 3 pontos seu índice de ENERGIA. Você pode caminhar até a alcova, se ainda não o fez - volte para 41 - ou sair da câmara e continuar para o oeste - volte para 83. ")

    escolha = input("\nIr para 41 ou 83?: ")
    match escolha:
        case '41':
            aventura41()
        case '83':
            aventura83()
        case _:
            print("\nOpção Invalida!")
            aventura226()



def aventura227():
    print(stats_final)
    print("\nCAP 227")
    print("\nAinda sorrindo, o velho olha para você. “Errado”, ele diz em voz baixa. Volte para 85. ")

    input("\nPressione Enter para ir para 85...")
    aventura85()



def aventura228(sorte):
    print("\nVocê enfia o braço no buraco e sente seu sangue gelar quando uma coisa quente e pegajosa se enrosca nele. Você consegue tirar o braço de dentro do buraco, mas um horrendo tentáculo, com ventosas incrivelmente fortes, está pendurado nele. Quando você consegue se libertar, cortando o tentáculo, seu braço dói e lateja. Teste sua Sorte.\nSe você tiver sorte, volte para 150. Se não tiver sorte, volte para 33. ")

    input("\nPressione Enter para rodar os dados...")
    x = roda_1_dado()
    print(f"\nO dado 1 tirou: {x}.")
    y = roda_1_dado()
    print(f"\nO dado 2 tirou: {y}.")
    soma = x + y

    print(f"\nA soma dos dados deu {soma}, sua sorte é {sorte}.")

    if soma <= sorte:
        input("\nVoce deu sorte!\nPressione Enter para ir para 150 ...")
        aventura150()

    else:
        input("\nVocê não teve sorte!\nPressione Enter para ir para 33...")
        aventura33()



def aventura229(garota_espirito):
    print("\nLogo que sua cabeça entra embaixo da luz azul, você ouve o som de vozes abafadas. Os rostos já não riem, e as expressões são agora máscaras de desespero e angústia. O rosto triste de uma menina paira à sua frente, ela começa a sussurrar um poema. Em transe, você ouve atentamente, acreditando que ela tem uma mensagem especial para você, enquanto ela recita: \n\n'Quando o corredor a água encontrar,\nNão se apresse em recuar.\nMergulhe depois dos pulmões encher,\nSe sua Prova espera vencer.'\n\nGuardando de cor o poema da garota-espírito, você atravessa o raio de luz e se dirige rapidamente para o norte. Volte para 107. ")

    garota_espirito = True

    input("\nPressione Enter para ir para 107...")
    aventura107()


    return garota_espirito


def aventura230():
    print(stats_final)
    print("\nCAP 230")

    print("\nO túnel começa a se alargar e abre para uma imensa caverna, de onde você pode ouvir o som de muitas vozes agudas. Você se aproxima silenciosamente da entrada e espia. Cerca de 20 minúsculos seres, com narizes e orelhas compridos, correm em círculo em volta de uma grande efígie de ouro. Você: \n\nAndará até eles para conversar? - Volte para 88.\nTentará se esgueirar e passar por eles? - Volte para 5\nBeberá a Poção da Réplica (se você a tiver) - Vá para 385")

    escolha = input("\nIr para 88, 5 ou 385?: ")
    match escolha:
        case '88':
            aventura88()
        case '5':
            aventura5()
        case '385':
            aventura385()
        case _:
            print("\nOpção Invalida!")
            aventura230()



def aventura231():
    print(stats_final)
    print("\nCAP 231")

    print("\nVocê encontra uma poça atrás dos Hobglobins mortos e toma grandes goles de água fresca o mais rápido possível. Isso neutraliza o ácido e, lentamente, você começa a se recuperar. Ainda com dor, você se levanta e parte para o norte. Volte para 110. ")

    input("\nPressione Enter para ir para 110...")
    aventura110()


def aventura232(armado):
    print(stats_final)
    print("\nCAP 232")
    print("\nSe você estiver desarmado, vá para 286. Se ainda estiver com suas armas, vá para 320. ")

    if armado == True:
        input("\nPressione Enter para ir para 286...")
        aventura286()
    else:
        input("\nPressione Enter para ir para 320...")
        aventura320()

        


def aventura233():
    print(stats_final)
    print("\nCAP 233")
    print("\nVocê parte um pedaço grande do cogumelo e o mastiga ansiosamente. De imediato, seu estômago incha, e você pode mesmo vê-lo estufando por baixo do cinto. Todo o seu corpo começa a se expandir, rasgando-lhe ruidosamente as roupas. Você fica cada vez maior, e logo seu rosto está imprensado de encontro ao teto. Os cogumelos que você comeu são muito procurados por mágicos para as poções de crescimento, mas para você eles significam a morte. Você está grande demais para poder algum dia sair da adega. Sua aventura termina aqui. ")

    fim_de_jogo()   


def aventura234():
    print(stats_final)
    print("\nCAP 234")
    print("\nUm pouco mais adiante, você chega a uma parte do túnel coberta de lodo verde e espesso. Parece ameaçador, por isso você resolve testá-lo primeiro com um pedaço de pano. A pasta corrosiva do lodo queima o pano instantaneamente, não deixando nem sinal dele. Se você estiver carregando um par de pernas-de-pau, volte para 183. Se não as tiver, volte para 207. ")
 
    fim_de_jogo()


def aventura235(energia):
    print(stats_final)
    print("\nCAP 235")
    print("\nVocê não tem tempo para reagir antes que o dardo se crave na sua coxa. Você perde 2 pontos de ENERGIA. Se ainda estiver vivo, volte para 73. ")

    energia = energia - 2

    if energia > 0:
        input("Você sai ferido, mas sobrevive. Pressione Enter para ir para 73...")
        aventura73()
    else:
        fim_de_jogo()
    
    return energia

def aventura236(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome):
    print(stats_final)
    print("\nCAP 216")
    print("\nO punho recua e prepara um novo ataque. Com a mão livre, você puxa a espada e tenta cortar a maçaneta da porta. Embora não o reconheça, você está sendo atacado pela forma fluida de um IMITADOR. \n\nIMITADOR    -    HABILIDADE 9        ENERGIA 8\n\nQuando vencer sua primeira Série de Ataque, vá para 314. ")

    energia_monstro = 8
    habilidade_monstro = 9
    nome = "IMITADOR"

    batalha(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome)

    input("Você venceu a batalha com o IMITADOR. POressione Enter para seguir para 314...")
    aventura314()


def aventura237():
    print(stats_final)
    print("\nCAP 237")
    print("\nO túnel faz uma curva súbita para a esquerda e continua para o norte até onde a vista alcança. Você logo chega a uma porta de madeira, fechada, na parede do lado esquerdo. Se você quiser abrir a porta, volte para 12. Se preferir continuar seguindo para o norte, volte para 100. ")

    escolha = input("\nIr para 12 ou 100?: ")
    match escolha:
        case '12':
            aventura12()
        case '100':
            aventura100()
        case _:
            print("\nOpção Invalida!")
            aventura237()



def aventura238(habilidade):
    print(stats_final)
    print("\nCAP 238")
    print("\nAo cair, você consegue agarrar a corda com as mãos. Lentamente, você se iça até o outro lado e sobe para o piso. Você retira o elmo do poste e o põe na cabeça. O elmo foi feito por um ferreiro altamente habilidoso. Some 1 ponto de HABILIDADE. Não querendo se arriscar a caminhar de volta pela corda bamba, você resolve engatinhar por ela. De volta ao terreno firme, em segurança, você atravessa a passagem em arco para seguir pelo túnel na direção norte. Vá para 291. ")

    habilidade = habilidade + 1

    input("\nPressione Enter para ir para 291...")
    aventura291()


def aventura239():
    print(stats_final)
    print("\nCAP 239")
    print("\nNão muito adiante, o túnel chega a uma porta fechada à sua esquerda. Colocando o ouvido na porta, você escuta, mas não ouve nada. Se você quiser abrir a porta, volte para 102. Se desejar prosseguir para o norte, vá para 344. ")

    input("\nPressione Enter para ir para 344...")
    aventura344()


def aventura240():
    print(stats_final)
    print("\nCAP 240")
    print("\nVocê olha para baixo e vê esparramados no chão os corpos inertes dos Guardiães Voadores. Você começa a forçar o olho esquerdo de esmeralda do ídolo com a ponta da espada. Finalmente, ele se solta e cai na sua mão; o peso da pedra o deixa surpreso. Esperando que seja de utilidade mais tarde, você a guarda na mochila. Se quiser agora forçar o olho direito, volte para 34. Se preferir descer do ídolo, volte para 89. ")

    escolha = input("Ir para 34 ou 89?: ")
    match escolha:
        case '34':
            aventura34()
        case '89':
            aventura89()
        case _:
            print("\nOpção Invalida.\n")
            aventura240()


def aventura241():
    print(stats_final)
    print("\nCAP 241")
    print("\nUma cortina de veludo marrom fecha uma passagem em arco na parede oriental do túnel. Se você quiser descerrar a cortina e atravessar a passagem em arco, vá para 393. Se preferir continuar para o norte, vá para 291. ")
    
    escolha = input("Ir para 393 ou 291?")
    match escolha:
        case '393':
            aventura393()
        case '291':
            aventura291()
        case _:
            print("Opção Invalida.")
            aventura241()


def aventura242(sorte, habilidade):
    print(stats_final)
    print("CAP 242")
    print("\nVocê sacode a cabeça, tentando desesperadamente manter a consciência, mas o calor é intenso demais, e você perde os sentidos. Jogue dois dados. Se o total for igual ou menor que a sua HABILIDADE, volte para 48. Se o total for maior que a sua HABILIDADE, vá para 366. ")
    input("\nPressione Enter para rodar os dados...")
    x = roda_1_dado()
    print(f"\nDado 1 tirou: {x}")
    y = roda_1_dado()
    print(f"\nDado 2 tirou: {y}")
    if x + y <= habilidade:
        print(f"\nA soma dos dados deu: {x + y}, e sua habilidade é {habilidade}.")
        input("\nPressione Enter para ir para 48...")
        aventura48()
    else:
        print(f"\nA soma dos dados deu: {x + y}, e sua habilidade é {habilidade}.")
        input("\nPressione Enter para ir para 366...")
        aventura366()


def aventura243():
    print("\nCobrindo o nariz e a boca com a mão, a fim de evitar inalar o gás, você segue o Gnomo pela porta aberta. Você entra em outro túnel, ao fim do qual aparece a visão bem vinda da luz do dia. Para sua grande surpresa, o Gnomo está morto no meio do caminho com um dardo de besta cravado na cabeça. Na ânsia por liberdade, o Gnomo caíra vítima da última armadilha do Barão Sukumvit. Você passa pelo infeliz e sai na luz brilhante do sol. Vá para 400. ")

    input("\nPressione Enter para ir para 400.")

    aventura400()


def aventura244():
    print("\nEle pega sua Peça de Ouro e lhe diz que, em um túnel setentrional, há uma cadeira de madeira esculpida na forma de um pássaro demoníaco. No braço da cadeira, um painel secreto contém uma poção em um frasco de vidro. “É uma Poção de Réplica, se eu bem me lembro. Boa sorte. Espero que nos encontremos de novo fora destes túneis infernais.” O homem sai arrastando os pés, e você continua sua jornada. Volte para 109. ")

    input("\nPressione Enter para voltar para 109...")

    aventura244()


def aventura245():
    print("\nVocê não tem outra alternativa senão abrir a porta, já que o muro é liso demais para ser escalado. Respirando fundo, você gira a maçaneta e entra em um poço coberto de areia. Ali, um monstro enorme com aparência de dinossauro, chegando a uns 10 metros de altura, está de pé nas imensas patas traseiras, diante de grandes portas duplas na parede do outro lado. Possui um couro grosso verde malhado e uma boca com filas de dentes afiados como navalhas. As mandíbulas da criatura se abrem e fecham com força capaz de pulverizar ossos. E mesmo você não consegue evitar o tremor ao se aproximar do Diabo do Poço com a espada na mão.\n\nDIABO DO POÇO    -    HABILIDADE 12        ENERGIA 15\n\nSe você vencer, vá para 258. ")



    habilidade_monstro = 12 
    energia_monstro = 15
    nome = "DIABO DO POÇO"


    batalha(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome)
    
    input(f"\nParabens! voce venceu o {nome}\nPressione Enter para seguir para 258...")

    aventura258()


def aventura246(energia):
    print(stats_final)
    print("\nCAP 246")
    print("\nApesar de toda a cautela, sua perna raspa em um dos postes, que imediatamente solta uma chuva de farpas afiadas, cada uma com vários centímetros de comprimento. Você perde 2 pontos de SORTE. Elas voam em todas as direções com grande velocidade, e você não consegue evitá-las. Jogue dois dados para determinar o número de farpas que se cravam na sua carne. Cada farpa reduz sua ENERGIA em 1 ponto. Se ainda estiver vivo, você senta para a dolorosa tarefa de retirar as farpas do corpo antes de partir para o leste. Vá para 313. ")
    sorte = sorte - 2

    x = roda_1_dado()
    print(f"\nO dado 1 tirou: {x}.")
    y = roda_1_dado()
    print(f"\nO dado 2 tirou: {y}.")
    soma = x + y

    print(f"\no total de farpas recebidas é {soma} sua energia diminui para {energia - soma}.")
    energia = energia - soma

    if energia <= soma:
        print("\nVocê nao resiste aos ferimentos, e acaba morrendo.")
        fim_de_jogo()
    else:
        input(f"Voce sai ferido, mas consegue sobreviver, sua energia agora é {energia}.\nPressione Enter para seguir para 313...")
        aventura313()


def aventura247(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome):
    print(stats_final)
    print("CAP 247")
    print("\nA fera diante de você é o temível MANTÉCORA. A ponta da cauda da criatura guarda uma profusão de espinhos pontudos, grossos e duros como dardos de ferro. Subitamente, ele sacode a cauda, lançando uma saraivada de espinhos na sua direção. Jogue um dado. O número obtido é a quantidade de espinhos que lhe penetrarão o corpo. Cada espinho custa-lhe 2 pontos de ENERGIA. Se você ainda estiver vivo, avança com dificuldade para atacar o Mantécora com sua espada, antes que ele tenha tempo de disparar mais espinhos.\n\nMANTÉCORA    -    HABILIDADE 11        ENERGIA 11\n\nSe você vencer, vá para 364. ")

    x = roda_1_dado()
    dano = x * 2
    energia = energia - dano

    if energia <= dano:
        print("\nVocê nao resiste ao ataque de espinhos.")

        fim_de_jogo()

    else:
        print(f"\nVocê sai ferido, mas consegue sobreviver, sua energia agora é {energia}.\nPressione Enter para iniciar a batalha com MANTÉCORA")

        habilidade_monstro = 11
        energia_monstro = 11
        nome = "MANTÉCORA"
        
        batalha(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome)



def aventura248():
    print("\nAs portas abrem para um túnel que segue para o norte. Você fecha as portas atrás de si e parte mais uma vez. Volte para 214. ")

    input("Pressione Enter para voltar para 214...")
    aventura214()


def aventura249():
    print("\nVocê só tem tempo de ouvir o Gnomo dizer: “Uma coroa e dois crânios”, antes que um raio branco de energia parta da fechadura e atinja-lhe o peito, derrubando-o sem sentidos. Jogue um dado, some 1 ao número obtido e reduza esse total de sua ENERGIA. Se ainda estiver vivo, você se recupera e ouve o Gnomo lhe dizer que tente de novo. Você sabe que colocou uma gema na ranhura certa, mas qual delas? Você suspira e tenta uma nova combinação.\n\n   A                B             C\nESMERALDA       DIAMANTE       SAFIRA          VOLTE PARA 16\nDIAMANTE         SAFIRA       ESMERALDA        VÁ PARA 392\nSAFIRA          ESMERALDA       DIAMANTE       VOLTE PARA 177\nESMERALDA       SAFIRA       DIAMANTE          VÁ PARA 287\nDIAMANTE       ESMERALDA       SAFIRA          VOLTE PARA 132\nSAFIRA          DIAMANTE      ESMERALDA        FIQUE EM 249 ")

    escolha = input("\nVocê irá para 16, 392, 177, 287, 132 ou 249?: \n")

    match escolha:
        case '16':
            aventura16()
        case '392':
            aventura392()
        case '177':
            aventura177()
        case '287':
            aventura287()
        case '132':
            aventura132()
        case '249':
            aventura249()
        case _:
            print("Opção invalida.")



def aventura250():
    print(stats_final)
    print("\nCAP 250")
    print("\nQuando você corre para a porta, o velho grita atrás de você: “Não corra, ninguém escapa de mim. Pare, ou eu o transformarei em pedra neste instante!” Você: \n\nContinua correndo? - Volte para 44\nVira-se para atacá-lo com a espada? - Volte para 195\nDiz a ele que responderá à pergunta? - Vá para 382 ")

    escolha = input("\nIr para 44, 195  ou 382?: ")
    match escolha:
        case '44':
            aventura44()
        case '195':
            aventura195()
        case '382':
            aventura382()
        case _:
            print("\nOpção Invalida!")
            aventura250()



def aventura251():
    print(stats_final)
    print("\nCAP 251")
    print("\nMais uma vez, ouve-se a voz misteriosa, só que agora, para sua grande surpresa, num tom bem menos ameaçador: “Bom, meu senhor gosta daqueles que demonstram ter espírito. Tome este presente para ajudá-lo. Isto lhe concederá um desejo, mas somente um desejo. Adeus.” Um anel de ouro, magicamente saído do nada, cai a seus pés com um tinido suave. Você o põe num dedo. A porta se abre e você entra de novo no túnel, rumo ao norte. Vá para 344. ")

    input("\nPressione Enter para ir para 344...")
    aventura344()


def aventura252():
    print(stats_final)
    print("\nCAP 252")
    print("\nO túnel continua para o norte por uma boa distância antes de chegar a um beco sem saída. A entrada de um escorrega é visível na parede do oeste, e essa parece ser a única alternativa, além da opção de retornar. Você resolve arriscar e sobe no escorrega. Desliza suavemente e aterrissa sobre as costas em um aposento. Volte para 90. ")

    input("\nPressione Enter para ir para 90...")
    aventura90()


def aventura253():
    print(stats_final)
    print("\nCAP 253")
    print("\nVocê tira o osso da mochila e o atira escada abaixo. Os latidos ficam mais altos, transformando-se em rosnados e ranger de dentes quando o osso cai no chão. Lentamente, você desce os degraus com a espada na mão, e vê os dois enormes CÃES DE GUARDA disputando o osso. Você passa correndo por eles e segue em frente pelo túnel. Vá para 315. ")

    input("\nPressione Enter para ir para 315...")
    aventura315()


def aventura254(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome):
    print(stats_final)
    print("\nCAP 254")
    print("\nVocê desembainha a espada e avança lentamente na direção do imenso e viscoso Verme da Rocha.\n\nVERME DA ROCHA    -    HABILIDADE 7        ENERGIA 11\n\nSe você vencer, volte para 76.\nVocê poderá fugir depois de duas Séries de Ataque, correndo para o oeste pelo túnel. Volte para 117. ")

    energia_monstro = 11
    habilidade_monstro = 7
    nome = "VERMA DA ROCHA"


    batalha_fuga(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome)

    if energia_monstro == 0:
        input("Você venceu o VERME DA ROCHA. Pressione Enter para ir para 76...")
        aventura76()

    else:
        input("Você fugiu da batalha, Pressione Enter para ir para 117...")
        aventura117()


def aventura255():
    print(stats_final)
    print("\nCAP 255")

    print("\nQuando corre contornando o caminho estreito, você se sente tonto. O gás da poça está fazendo efeito: sua visão começa a ficar embaçada, e você perde o equilíbrio. Você só tem uma vaga consciência da língua da Besta Sangrenta, enquanto ela se enrosca na sua perna e o arrasta para a poça de lodo. Depois de decomposto no lodo abjeto, seu corpo será saboreado pela ignóbil Besta Sangrenta. ")

    fim_de_jogo()


def aventura256():
    print(stats_final)
    print("\nCAP 256")

    print("\nLembrando do conselho do velho, você examina o braço da cadeira em busca de um painel secreto. Descobrindo uma fenda quase imperceptível, você a força e, súbito, um pequeno painel salta do braço. Ao perceber um pequeno frasco de vidro numa cavidade, você o apanha e lê o rótulo: “Poção de Réplica - uma dose apenas. Este líquido fará com que você assuma a forma de qualquer ser vivo que lhe esteja próximo.” Você põe a estranha poção na mochila e continua para o norte. Volte para 188. ")

    mochila.append('poção de réplica')

    input("\nPressione Enter para ir para 188...")
    aventura188()


def aventura257():
    print(stats_final)
    print("\nCAP 257")
    print("\nDentro dos bolsos de um dos Orcas, você acha uma Peça de Ouro e um tubo oco de madeira. Você guarda na mochila o que encontrou e parte para o oeste. Volte para 164.")

    input("\nPressione Enter para ir para 164...")
    aventura164()




def aventura258():
    print(stats_final)
    print("\nCAP 258")
    print("\nVocê está exausto e se senta para um descanso na cauda da fera morta. Olhando para baixo, a seus pés, você de repente nota um anel de ferro que se destaca na areia. Se você quiser puxar o anel, volte para 95. Se preferir sair do poço pelas portas duplas, volte para 248. ")

    escolha = input("\nIr para 95 ou 248?: ")
    match escolha:
        case '95':
            aventura95()
        case '248':
            aventura248()
        case _:
            print("\nOpção Invalida!")
            aventura258()


def aventura259():
    print(stats_final)
    print("\nCAP 259")
    print("\nIgnorando a dor, você, continua a correr. À sua frente, vê um rio subterrâneo que corre de leste para oeste atravessando a caverna, com uma ponte de madeira que liga uma margem a outra. Você olha para trás e vê os Trogloditas no seu encalço. Se você quiser correr pela ponte, vá para 318. Se desejar mergulhar no rio, volte para 47. ")

    escolha = input("\nIr para 318 ou 47?: ")
    match escolha:
        case '318':
            aventura318()
        case '47':
            aventura47()
        case _:
            print("\nOpção Invalida!")
            aventura259()


def aventura260():
    print(stats_final)
    print("\nCAP 260")
    print("\nVocê mal consegue se agarrar à orelha do ídolo e recuperar um ponto de apoio para os pés. Você se desloca pelo rosto da estátua. Sentado no nariz do ídolo, você desembainha a espada e considera qual dos olhos dele arrancará primeiro para levar a jóia.\n\nSe quiser arrancar primeiro o olho esquerdo - volte para 166.\n\nSe preferir arrancar o olho direito - volte para 140.")

    escolha = input("\nIr para 166 ou 140?: ")
    match escolha:
        case '166':
            aventura166()
        case '140':
            aventura140()
        case _:
            print("\nOpção Invalida!")
            aventura260()


def aventura261():
    print(stats_final)
    print("\nCAP 261")
    print("\nApesar de todos os esforços, você não consegue tirar o Laço do pescoço do ídolo. Finalmente, você desiste e o abandona para quem quer que venha depois de você. Não há nada mais de interesse na caverna, portanto você caminha até a parede norte e entra no túnel. Volte para 239. ")

    input("\nPressione Enter para ir para 239...")
    aventura239()



def aventura262():
    print(stats_final)
    print("\nCAP 262")
    print("\nA porta abre para um outro túnel que segue para o norte. Você topa com duas fontes de pedra, uma de cada lado do túnel, esculpidas na forma de querubins, de cujas bocas a água jorra e desce em cascata para pequenas conchas nos pés. Você:\n\nBeberá água na fonte da esquerda? - Vá para 337\nBeberá água na fonte da direita? - Volte para 173\nContinuará caminhando para o norte? - Vá para 368 ")

    escolha = input("\nIr para 337, 173 ou 368?: ")
    match escolha:
        case '337':
            aventura337()
        case '173':
            aventura173()
        case '555':
            aventura368()
        case _:
            print("\nOpção Invalida!")
            aventura262()



def aventura263():
    print(stats_final)
    print("\nCAP 263")

    print("\nA porta abre para um outro túnel. Caminhando para o oeste, você logo chega a uma porta na parede norte. Se quiser abrir a porta, volte para 153. Se preferir continuar para o oeste, volte para 74. ")

    escolha = input("\nIr para 153 ou 74?: ")
    match escolha:
        case '153':
            aventura153()
        case '74':
            aventura74()
        case _:
            print("\nOpção Invalida!")
            aventura263()


def aventura264():
    print("\nAdiante, na penumbra, você vê dois HOBGOBLINS se engalfinhando. Há uma bolsa de couro jogada no chão, e parece ser ela a razão da luta. Você:\n\nTentará conversar com eles? - Volte para 130\nVai atacá-los com sua espada? - Volte para 51\nTentará passar sem ser percebido? - Vá para 355 ")
    
    escolha = input("Ir para 130, 51 ou 355?: ")
    match escolha:
        case '130':
            aventura130()
        case '51':
            aventura51(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome)
        case '355':
            aventura355()
        case _:
            print("Opção Invalida!")
            aventura264()



def aventura265():
    print(stats_final)
    print("\nCAP 265")
    print("\nVocê esfrega seu anel mágico e deseja que o Demônio do Espelho seja transportado de volta ao próprio mundo e nunca mais retome. Ainda avançando na sua direção, o ser começa a se esvair e desaparece aos poucos. Por fim, ele some completamente, e você pode continuar sua jornada para o norte. Volte para 122. ")

    input("\nPressione Enter para ir para 122...")
    aventura122()


def aventura266():
    print(stats_final)
    print("\nCAP 266")
    print("\nVocê revista os armários e caixas no quarto de Erva, mas não encontra nada, exceto um osso velho, que pode levar com você, se quiser. Saindo da câmara pela porta do leste, você agora se encontra de pé no final de um outro túnel. Vá para 305. ")

    input("\nPressione Enter para ir para 305...")
    aventura305()



def aventura267():
    print(stats_final)
    print("\nCAP 267")
    print("\nO túnel logo termina em uma encruzilhada. Olhando para a esquerda e para a direita, você vê uma passagem estreita que desaparece na penumbra da distância. Se você quiser se dirigir para o oeste, vá para 352. Se preferir seguir para o leste, volte para 68. ")

    escolha = input("\nIr para 352 ou 68?: ")
    match escolha:
        case '352':
            aventura352()
        case '68':
            aventura68()
        case _:
            print("\nOpção Invalida!")
            aventura267()


def aventura268():
    print(stats_final)
    print("\nCAP 268")
    print("\nVocê salta para adiante e tenta agarrar o líder para usá-lo como refém. Contudo, os Trogloditas estavam prevenidos para sua tentativa, e seis dos arqueiros deles imediatamente disparam flechas em você. A pontaria deles é mortalmente precisa, e as seis flechas atingem o alvo. Você tomba sem vida. Os Trogloditas encerraram abruptamente sua jornada. ")

    fim_de_jogo()


def aventura269():
    print(stats_final)
    print("\nCAP 269")
    print("\nVocê esvazia o conteúdo do vidro na mão e o aplica às suas feridas. Os efeitos curativos são imediatos, e você se sente mais forte a cada momento. Acrescente 3 pontos de ENERGIA. Se você ainda não o fez, poderá comer o arroz e beber a água - vá para 330 - ou sair do salão, levando apenas o diamante com você - volte para 127. ")

    energia = energia + 3

    escolha = input("\nIr para 330 ou 127?: ")
    match escolha:
        case '330':
            aventura330()
        case '127':
            aventura127()
        case _:
            print("\nOpção Invalida!")
            aventura269()



def aventura270():
    print(stats_final)
    print("\nCAP 270")

    print("\nA tampa da caixa sai facilmente. Dentro, você acha duas Peças de Ouro e um bilhete, escrito num pequeno pedaço de pergaminho, endereçado a você. Depois de colocar o ouro no bolso, você lê a mensagem: Muito bem. Pelo menos você tem o bom senso de parar e tirar proveito da ajuda simbólica que lhe é dada. Agora, posso avisá-lo da necessidade de encontrar e usar diversos itens, se espera sair-se bem no meu Calabouço da Morte. Assinado “Sukumvit.” Guardando de cor o aviso do bilhete, você o rasga em pequenos pedaços e continua para o norte pelo túnel. Volte para 66. ")

    input("\nPressione enter para voltar para 66...")
    aventura66()


def aventura271():
    print(stats_final)
    print("\nCAP 271")
    print("\nQuando você está prestes a soltar o escudo e atirá-lo por cima do poço, ele escorrega de seus dedos e rola pelo chão. Você não consegue apanhá-lo antes que ele ultrapasse a borda, caindo ruidosamente, de lado, no fundo. A perda do escudo reduz-lhe a capacidade - você perde 1 ponto de HABILIDADE. Amaldiçoando sua própria falta de jeito, você dá um passo à frente, salta por sobre o poço e cai em segurança do outro lado. Você não perde tempo e se dirige para o leste. Volte para 237. ")

    input("\nPressione Enter para ir para 237...")
    aventura237()


def aventura272():
    print(stats_final)
    print("\nCAP 272")
    print("\nEmbora a Besta Sangrenta seja pesada e estufada demais para sair da poça, a língua da fera se estica e se enrosca na sua perna. Ainda inconsciente, você é arrastado para a poça de lodo. Depois de decomposto pela ação do lodo abjeto, seu corpo será saboreado pela repugnante Besta Sangrenta. ")

    fim_de_jogo()


def aventura273():
    print(stats_final)
    print("\nCAP 273")
    print("\nA bola de madeira se choca contra o crânio, derrubando-o do pedestal. Para sua surpresa, as bestas não disparam os dardos mortais. Você entra no aposento com cautela e apanha o crânio do chão. Reconhece as jóias amarelas dos olhos como sendo topázios, e rapidamente os arranca das órbitas. Você os coloca na mochila, imaginando se ainda há uma cilada à sua espera no aposento. Você:\n\nFicará de quatro e sairá engatinhando do aposento, segurando o crânio? - Volte para 15\nRecolocará o crânio no pedestal antes de sair do aposento? - Volte para 204 ")

    escolha = input("\nIr para 15 ou 204?: ")
    match escolha:
        case '15':
            aventura15()
        case '204':
            aventura204()
        case _:
            print("\nOpção Invalida!")
            aventura273()



def aventura274():
    print(stats_final)
    print("\nCAP 274")

    print("\nVocê pisa nervosamente na corda, sem se atrever a olhar para baixo. Na metade da travessia, você começa a entrar em pânico e perde o equilíbrio. Jogue dois dados. Se o total for igual ou menor que a sua HABILIDADE, volte para 238. Se o total for maior que sua HABILIDADE, vá para 359. ")

    input("\nPressione Enter para rodar os dados...")
    x = roda_1_dado()
    print(f"\nO dado 1 tirou: {x}.")
    y = roda_1_dado()
    print(f"\nO dado 2 tirou: {y}.")
    soma = x + y

    print(f"\nA soma dos dados deu {soma}, sua habilidade é {habilidade}.")

    if soma <= habilidade:
        input("\n\nPressione Enter para ir para 238 ...")
        aventura238()

    else:
        input("\n\nPressione Enter para ir para 359...")
        aventura359()


def aventura275(sorte):
    print(stats_final)
    print("\nCAP 275")
    print("\nUma fumaça espessa sobe do chão no lugar onde o ácido caiu da moringa quebrada. Você se arrasta desesperadamente, tentando encontrar água potável nas poças rasas do túnel gotejante. Teste sua Sorte. Se você tiver sorte, volte para 231. Se não tiver sorte, vá para 309. ")

    input("\nPressione Enter para rodar os dados...")
    x = roda_1_dado()
    print(f"\nO dado 1 tirou: {x}.")
    y = roda_1_dado()
    print(f"\nO dado 2 tirou: {y}.")
    soma = x + y

    print(f"\nA soma dos dados deu {soma}, sua sorte é {sorte}.")

    if soma <= sorte:
        input("\nVoce deu sorte!\nPressione Enter para ir para 213 ...")
        aventura213()

    else:
        input("\nVocê não teve sorte!\nPressione Enter para ir para 309...")
        aventura309()



def aventura276():

    print(stats_final)
    print("\nCAP 276")
    print("\nAo tentar arrombar a porta com uma pancada de ombro, você ouve as vozes esganiçadas dos Trogloditas que vêm descendo o túnel. Você está encurralado e desembainha a espada. Os Trogloditas se aproximam, os arcos prontos, e uma saraivada de flechas o atinge com impacto fatal. Seu corpo desaba sem vida nas profundezas do Calabouço da Morte. ")

    fim_de_jogo()


def aventura277():
    print(stats_final)
    print("\nCAP 277")
    print("\nO túnel faz uma curva fechada para a direita e depois, uns 100 metros adiante, chega a um cruzamento. Olhando para a esquerda, você vê dois corpos caídos no chão. Resolve chegar perto e investigar. Vá para 338. ")

    input("\nPressione Enter para ir para 338...")

    aventura338()


def aventura278():
    print(stats_final)
    print("\nCAP 278")
    print("\nSua lâmina atinge um dos olhos verdadeiros da Besta Sangrenta. O efeito é devastador. Ela desaba na poça, debatendo-se freneticamente. Você aproveita a oportunidade e corre, contornando a poça, rumo à saída para o túnel. Volte para 134. ")
    input("\nPressione Enter para ir para 134...")
    aventura134()


def aventura279():
    print(stats_final)
    print("\nCAP 279")
    print("\nVocê chega a um cruzamento no túnel. Uma nova ramificação leva para o oeste, mas as pegadas molhadas que você vem seguindo continuam para o norte. Você decide continuar seguindo as pegadas. Volte para 32 ")

    input("\nPressione Enter para retornar para 32...")

    aventura32()


def aventura280():
    print(stats_final)
    print("\nCAP 280")
    print("\nO túnel continua para o leste por uma boa distância antes de chegar a um cruzamento. As paredes, o teto e o chão do túnel que leva para o sul estão cobertos por um limo verde e espesso. Você considera que é mais seguro dirigir-se para o norte. Volte para 218. ")

    input("\nPressione Enter para voltar para 218...")
    aventura218()

def aventura281():
    print(stats_final)
    print("\nCAP 281")
    print("\nCom um golpe da sua espada de fé, você corta a cabeça da Jibóia. Você desenrola o corpo gigantesco, libertando a Mulher-elfo, e tenta ressuscitá-la. Os olhos dela se abrem um pouco, mas não há esperança. Ela olha para você e sorri, depois murmura: “Obrigada. Sei que é tarde demais para mim, mas lhe direi o que já pude aprender. A saída está adiante, mas você precisa de gemas para destrancar a última porta. Uma delas é um diamante, mas não sei quais são as outras. Pena, não encontrei um diamante, mas aconselho-o a procurar um. Boa sorte.” Os olhos dela se fecham, e ela tomba no chão frio. Você a olha entristecido enquanto ela solta o último suspiro. Sabendo que ela não se importaria, retira-lhe os dois punhais e examina a mochila de couro que trazia. Dentro, você acha um pedaço de pão ázimo, um espelho e um amuleto de osso com a forma de um macaco.\n\nSe você quiser comer o pão, vá para 399.\n\nSe preferir pegar apenas o espelho e o amuleto e retornar ao túnel para dirigir-se ao norte, volte para 192. ")

    escolha = input("\nIr para 399 ou 192?")
    match escolha:
        case '399':
            aventura399()
        case '192':
            aventura192()
        case _:
            print("Opção Invalida!")
            aventura281()

def aventura282():
    print(stats_final)
    print("\nCAP 282")
    print("\nO túnel logo termina em uma encruzilhada. Parado lá sozinho e sem saber para que lado ir está um de seus rivais. É um dos Bárbaros. Você o chama, mas ele não responde; apenas olha fria e fixamente para você, segurando a acha com firmeza. Você anda até ele e pergunta para que lado está indo. Ele grunhe sua resposta, dizendo que está indo para o oeste, e, se quiser, você pode ir com ele. Se você quiser seguir para o oeste com o Bárbaro, volte para 22. Se preferir recusar a oferta e seguir para o leste sozinho, vá para 388. ")

    escolha = input("\nIr para 22 ou 388?: ")
    match escolha:
        case '22':
            aventura22()
        case '388':
            aventura388()
        case _:
            print("Opção Invalida.")
            aventura282()




def aventura283():
    print(stats_final)
    print("CAP 283")
    print("\nVocê precisa se espremer e entrar fundo na fenda para se esconder completamente. Dessa posição desajeitada, você não consegue ver o dono dos pés que se arrastam, passando lentamente. Um minuto depois, tudo está quieto de novo, por isso você se esgueira de volta para o túnel e prossegue para o oeste. Volte para 109. ")
    
    input("\nPressione Enter para voltar para 109...")
    aventura109()


def aventura284():
    print(stats_final)
    print("\nCAP 284")
    print("\nVocê bebeu uma poção encontrada em um livro de couro preto? Se você tiver bebido, vá para 398. Se não, volte para 57. ")

    if 'poção do livro preto' in ativos:
        input("\nPressione Enter para ir para 398...")
        aventura398()
    else:
        input("\nPressione Enter para retornar para 57...")
        aventura57()

def aventura285(habilidade, energia):
    print("\nVocê cai pesadamente de costas, mas, felizmente, sua mochila suaviza o impacto. Você perde 1 ponto de HABILIDADE e 2 pontos de ENERGIA. A escuridão é quase total no fundo do poço, e você se arrasta, tateando. Repentinamente, sua mão toca alguma coisa fria, dura e lisa. O objeto é pequeno e redondo, mas você não consegue imaginar o que pode ser. Você o põe na mochila, esperando saber o que é quando sair do poço. Você continua a engatinhar e, adiante, topa com a parede do poço. É lisa demais para ser escalada, e você tem que escavar apoios nela com a espada. Isso toma muito tempo, mas, finalmente, você chega à boca do poço e sai dele pelo lado leste. Imediatamente, verifica a mochila, e descobre que o objeto encontrado é uma esfera de rubi vermelho vivo. Você fica absolutamente deslumbrado e se dirige para o leste com excelente disposição, assobiando suavemente. Volte para 237. ")

    mochila.append('rubi vermelho')

    habilidade = habilidade - 1
    energia = energia - 2

    print(f"\nSua Habilidade agora é {habilidade}\nSua Energia agora é {energia}")

    input("Pressione Enter para voltar para 237...")

    aventura237()


def aventura286():
    print(stats_final)
    print("\nCAP 286")
    print("\nFoi obviamente um erro ter largado suas armas, mas, pelo menos, agora você pode se apossar das do Ninja morto. Você escolhe uma das facas compridas e a longa espada curva. O fio da lâmina de aço é excepcionalmente duro, e você não consegue deixar de admirar-lhe a beleza terrificante. Acrescente 4 pontos de HABILIDADE e vá para 320.")

    habilidade = habilidade + 4

    input("\nPressione Enter para ir para 320...")
    aventura320()



def aventura287():
    print(stats_final)
    print("\nCAP 287")
    print("\nVocê só tem tempo de ouvir o Gnomo dizer: “Uma coroa e dois crânios”, antes que um raio branco de energia parta da fechadura e atinja-lhe o peito, derrubando-o sem sentidos. Jogue um dado, some 1 ao resultado e subtraia o total da sua ENERGIA. Se você ainda estiver vivo, recupera os sentidos e ouve o Gnomo lhe dizer que tente de novo. Você sabe que colocou uma gema na ranhura certa, mas qual delas? Você suspira e tenta uma nova combinação.\n\n   A                B             C\nESMERALDA       DIAMANTE       SAFIRA          VOLTE PARA 16\nDIAMANTE         SAFIRA       ESMERALDA        VOLTE PARA 392\nSAFIRA          ESMERALDA       DIAMANTE       VOLTE PARA 177\nESMERALDA       SAFIRA       DIAMANTE          FIQUE EM 287\nDIAMANTE       ESMERALDA       SAFIRA          VOLTE PARA 132\nSAFIRA          DIAMANTE      ESMERALDA        VOLTE PARA 249 ")
    escolha = input("Você irá para 16, 392, 177, 287, 132 ou 249?: \n")
    match escolha:
        case '16':
            aventura16()
        case '392':
            aventura392()
        case '177':
            aventura177()
        case '287':
            aventura287()
        case '132':
            aventura132()
        case '249':
            aventura249()
        case _:
            print("Opção invalida.")
            aventura287()



def aventura288():
    print(stats_final)
    print("\nCAP 288")
    print("\nVocê olha para a esquerda e vê Throm de pé sobre o Troll da Caverna que ele liquidou. O sangue que escorre do corte profundo que tem no ombro não parece preocupá-lo. Vocês revistam os corpos dos Trolls da Caverna, mas não encontram nada além de um anel de osso em um cordão de couro no pescoço de um deles. O anel tem um símbolo entalhado. Throm o reconhece e explica que deve ter pertencido a druidas do norte; trata-se de um antigo e poderoso talismã, capaz de aumentar-lhe os poderes, se seu corpo puder aceitá-lo. Throm recusa-se a tocar nele, e aconselha que você também não o faça.\n\nSe você quiser pôr o anel, volte para 64.\n\nSe preferir continuar para o leste com Throm, volte para 221. ")

    escolha = input("\nIr para 64 ou 221?: ")
    match escolha:
        case '64':
            aventura64()
        case '221':
            aventura221()
        case _:
            print("\nOpção Invalida!")
            aventura288()


def aventura289(sorte):
    print("\nA cobertura de pano sobe para o topo da gaiola, e nela, para seu horror, você vê o rosto de uma mulher velha, cujo cabelo é uma massa de serpentes que silvam. É a terrível MEDUSA! Teste sua Sorte. Se você tiver sorte, volte para 216. Se não tiver sorte, volte para 19. ")

    input("\nPressione Enter para rodar os dados...")
    x = roda_1_dado()
    print(f"\nO dado 1 tirou: {x}.")
    y = roda_1_dado()
    print(f"\nO dado 2 tirou: {y}.")
    soma = x + y

    print(f"\nA soma dos dados deu {soma}, sua sorte é {sorte}.")

    if soma <= sorte:
        input("\nVoce deu sorte!\nPressione Enter para ir para 216 ...")
        aventura216()

    else:
        input("\nVocê não teve sorte!\nPressione Enter para ir para 19...")
        aventura19()




def aventura290():
    print(stats_final)
    print("\nCAP 290")
    print("\nJogue dois dados. Se o total for oito, volte para 152. Se o total for qualquer número diferente de oito, volte para 121. ")

    input("\nPressione Enter para rodar os dados...")
    x = roda_1_dado()
    print(f"\nO dado 1 tirou: {x}.")
    y = roda_1_dado()
    print(f"\nO dado 2 tirou: {y}.")
    soma = x + y

    print(f"\nA soma dos dados deu {soma}, sua sorte é {sorte}.")

    if soma == 8:
        input("\n8\nPressione Enter para ir para 152 ...")
        aventura152()

    else:
        input("\nVocê não teve sorte!\nPressione Enter para ir para 121...")
        aventura121()


def aventura291():
    print(stats_final)
    print("\nCAP 291")
    print("\nO túnel continua para o norte por uma longa distância, antes de fazer uma curva fechada para a direita. Ao virá-la, você chega a um beco sem saída. Somente a entrada de um escorrega de madeira na parede oferece alguma esperança de continuidade no caminho. Você resolve se arriscar e sobe no escorrega. Desliza suavemente e aterrissa sobre as costas num aposento. Volte para 90.")

    input("\nPressione Enter para ir para 90...")
    aventura90()


def aventura292():
    print(stats_final)
    print("\nCAP 292")
    print("\nUma porta se torna visível na parede do lado esquerdo do túnel. Você escuta cuidadosamente junto à porta, mas não ouve nada. A porta não está trancada, e a maçaneta gira facilmente. Se você quiser abrir a porta, volte para 93. Se preferir prosseguir pelo túnel, volte para 230. ")

    escolha = input("\nIr para 93 ou 230?: ")
    match escolha:
        case '93':
            aventura93()
        case '230':
            aventura230()
        case _:
            print("\nOpção Invalida!")
            aventura292()


def aventura293():
    print(stats_final)
    print("")
    print("CAP 293\n")
    print("\nSeguindo os três pares de pegadas molhadas pela passagem oeste do túnel, você logo chega a uma encruzilhada. Se quiser continuar para o oeste, seguindo dois pares de pegadas, volte para 137. Se quiser se dirigir para o norte, seguindo o terceiro par de pegadas, vá para 387. ")

    escolha = input("Voltar para 137 ou ir para 387?: \n")
    match escolha:
        case '137':
            aventura137()
        case '387':
            aventura387()
        case _:
            print("Opção Invalida.")


def aventura294(sorte, habilidade):
    print("\nVocê puxa o punhal do cinto com a mão livre e golpeia a língua da Besta Sangrenta. A fera urra de dor e rola para a frente, tanto quanto consegue, para tentar abocanhá-lo com as mandíbulas ensanguentadas. Do chão, você tem que lutar contra a fera como punhal. Reduza sua HABILIDADE em 2 pontos durante este combate, pois não está lutando com sua espada. \n\nBESTA SANGRENTA    -    HABILIDADE 12        ENERGIA 10\n\nTão logo você vença sua primeira Série de Ataque, Teste sua Sorte.\nSe você tiver sorte, volte para 97.\nSe não tiver sorte, volte para 21. ")

    habilidade = habilidade - 2

    input("\nPressione Enter para rodar os dados...")
    x = roda_1_dado()
    print(f"\nO dado 1 tirou: {x}.")
    y = roda_1_dado()
    print(f"\nO dado 2 tirou: {y}.")
    soma = x + y

    print(f"\nA soma dos dados deu {soma}, sua sorte é {sorte}.")

    if soma <= sorte:
        input("\nVoce deu sorte!\nPressione Enter para ir para 97 ...")
        aventura97()

    else:
        input("\nVocê não teve sorte!\nPressione Enter para ir para 21...")
        aventura21()



def aventura295(energia):
    print(stats_final)
    print("\nCAP 295")
    print("\nCorrendo na direção da passagem em arco, você tropeça numa pedra e perde o equilíbrio. Você cai estatelado no chão, e, antes que tenha tempo de levantar-se, uma estalactite despenca, rasgando-lhe a perna com a ponta aguçada. Você perde 5 pontos de ENERGIA. Se ainda estiver vivo, volte para 206. ")

    energia = energia - 5
    if energia > 0:
        input("Você sai ferido, mas sobrevive. Pressione Enter para ir para 206...")
        aventura206()


def aventura296():
    print(stats_final)
    print("\nCAP 296")
    print("\nVocê percebe que adiante o túnel faz uma curva e depois continua para o norte. Alertado pelo som de vozes esganiçadas que sussurram e riem baixo, você pára antes da curva.\n\nSe quiser desembainhar a espada e olhar depois da curva - volte para 49.\n\nSe preferir caminhar de volta para a encruzilhada e seguir para o norte - volte para 241. ")

    escolha = input("\nIr para 49 ou 241?: ")
    match escolha:
        case '49':
            aventura49()
        case '241':
            aventura241()
        case _:
            print("\nOpção Invalida!")
            aventura296()


def aventura297():
    print(stats_final)
    print("\nCAP 297")

    print("\nA perda de suas posses, obtidas com tanta dificuldade, está se tornando um problema. Você perde 1 ponto de SORTE. Sem mesmo parar para agradecer, Erva o empurra para fora do quarto por uma porta na parede leste. Ei-lo parado no fim de um outro túnel. Vá para 305. ")

    input("\nPressione Enter para ir para 305...")
    aventura305()


def aventura298():
    print(stats_final)
    print("\nCAP 298")
    print("\nHá uma mochila encostada na parede do túnel. Você se pergunta se ela pertenceria a um de seus rivais. Se você quiser olhar dentro da mochila, vá para 304. Se preferir continuar para o norte, volte para 279. ")
    
    escolha = input("Ir para 304 ou 279?: ")
    match escolha:
        case '304':
            aventura304(energia, habilidade, sorte, stats_final)
        case '279':
            aventura279()
        case _:
            print("Opção Invalida!")


def aventura299():
    print(stats_final)
    print("\nCAP 299")
    print("\nA porta abre para uma grande câmara, onde você se choca ao ver que um de seus rivais obviamente encontrou morte súbita ao ser perfurado. É um dos Bárbaros, e ele está empalado em vários espigões de ferro bem longos, presos a uma tábua projetada de dentro do chão. O piso está coberto de lixo e detritos, escondendo um arame no qual ele deve ter pisado, disparando assim o mecanismo da tábua com espigões. Numa alcova na parede do outro lado, você pode ver uma taça de prata sobre uma pequena mesa de madeira. Você: \n\nIrá até o Bárbaro para revistá-lo? - Volte para 126 \nCaminhará na direção da alcova? - Volte para 41\nFechará a porta e continuará para o oeste? - Volte para 83 ")

    escolha = input("\nIr para 126, 41 ou 83?: ")
    match escolha:
        case '126':
            aventura126()
        case '41':
            aventura41()
        case '83':
            aventura83()
        case _:
            print("\nOpção Invalida!")
            aventura299()



def aventura300():
    print(stats_final)
    print("\nCAP 300")
    print("\nVocê golpeia o espelho com a espada, com toda sua força, mas isso de nada adianta: o espelho não quebra, e o Demônio do Espelho continua a avançar. Se você quiser tentar partir o espelho de novo, volte para 141. Se, em vez disso, preferir atacar o Demônio do Espelho, vá para 327. ")
    escolha = input("\nIr para 141 ou 327?: ")
    match escolha:
        case '141':
            aventura141()
        case '327':
            aventura327()
        case _:
            print("\nOpção Invalida!")
            aventura300()


def aventura301():
    print(stats_final)
    print("\nCAP 301")
    print("\nO cano está úmido e cheio de limo, mas você segue engatinhando na escuridão abafada, escorregando e deslizando no caminho. Subitamente, sua mão toca em algo duro e quadrado; parece ser de madeira. Ao sacudi-la, a coisa chacoalha, e você conclui que deve estar segurando uma caixa.\n\nSe quiser engatinhar de volta e sair do cano para examinar o achado - volte para 162.\n\nSe preferir seguir em frente pelo cano, levando a caixa para examinar mais tarde - volte para 4. ")

    escolha = input("\nIr para 162 ou 4?: ")
    match escolha:
        case '162':
            aventura162()
        case '4':
            aventura4()
        case _:
            print("\nOpção Invalida!")
            aventura301()


def aventura302(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome):
    print(stats_final)
    print("\nCAP 302")
    print("\nDepois de cerca de 20 minutos, o Anão reaparece na sacada. Ele lhe grita: “Bem, eu realmente tenho um problema muito interessante nas mãos. Prepare-se para lutar contra seu próximo adversário.” A porta de madeira se ergue mais uma vez, e você se admira ao ver um rosto conhecido. É Throm! Ele está muito machucado e tem cortes pelo corpo todo, e não parece reconhecê-lo. Está claramente delirante enquanto cambaleia para frente com a acha erguida para atacá-lo. O Anão ri e lhe diz: “A naja o mordeu, mas ele tema força de um touro e conseguiu resistir, ao contrário da maioria dos homens. Agora você deve lutar com ele, para decidir finalmente qual dos dois continuará na Prova dos Campeões.” Você grita com o Anão, revoltado, denunciando a crueldade de um confronto desses. Ele simplesmente ri, e você não tem alternativas e não se defender do ataque do pobre Throm. \n\nTHROM    -    HABILIDADE 10        ENERGIA 12\n\nApesar dos ferimentos, Throm é imensamente forte.\nSe você vencer, vá para 379. ")

    energia_monstro = 12
    habilidade_monstro = 10
    nome = "THROM"

    batalha(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome)

    input(f"Você venceu o {nome}! Pressione Enter para seguir para 379...")

    aventura379()


def aventura303():
    print(stats_final)
    print("\nCAP 159")
    print("\nCom sua mão livre, você busca a moringa na mochila. Desarrolhando-a com os dentes, derrama o ácido sobre a porta, que é na realidade a forma fluida de um IMITADOR. Um jato de fumaça sobe dela, com um alto som sibilante, enquanto o ácido começa a queimar o Imitador. Ela derrete rapidamente, e você consegue afastar-se sem se ferir. Não tendo outra alternativa, você, um tanto apreensivo, gira a maçaneta da outra porta. Volte para 262. ")

    input("\nPressione Enter para ir para 262...")
    aventura262()



def aventura304(energia, habilidade, sorte, stats_final):
    print(stats_final)
    print("\nCAP 304")
    print("\nHá uma única Peça de Ouro no fundo da mochila. Quando você tenta pegá-la, sente um leve movimento que faz cócegas nas costas, da sua mão. Você retira a mão lentamente, tentando controlar o pânico crescente, e fica horrorizado ao ver uma ARANHA VIÚVA NEGRA. Antes que possa afastá-la, ela crava as presas venenosas profundamente no seu pulso. Você perde 6 pontos de ENERGIA. Se ainda estiver vivo, volte para 20. ")


    if energia > 0:
        energia = energia - 6


        print(f"\nO veneno não é o suficiente para te matar, mas agora sua energia é {energia}.")

        input("\nPressione Enter para ir para 20...")

        stats_final = f"\nx---SEU PERSONAGEM--x\n|Habilidade = {habilidade}\n|Energia = {energia}\n|Sorte = {sorte}\nx---------x---------x\n"

        aventura20(energia, habilidade, sorte, stats_final)

    else:
        print("\nVocê nao resiste ao veneno!")
        fim_de_jogo()
    return energia

def aventura305():
    print(stats_final)
    print("\nCAP 305")
    print("\nO túnel termina em um lance de degraus de pedra. Do chão, abaixo, vêm latidos de cães. Você tem um osso velho? Se tiver, volte para 253. Se não tiver, volte para 148.")

    if 'osso velho' in mochila:
        input("\nVocê tem um osso velho na mochila.\n\nPressione Enter para seguir para 253...")
        aventura253()

    else:
        input("\nVocê não tem Osso velho.\n\nPressione Enter para seguir para 148... ")
        aventura148()


def aventura306(sorte):
    print(stats_final)
    print("\nCAP 306")
    print("\nAntes que você possa dar um passo na direção dos Leprechauns, um deles joga uma poeira cintilante em você, que é imediatamente congelado no lugar, incapaz de mover um músculo. Você vê, indefeso, os Leprechauns revirarem sua mochila, fugindo com todas as suas posses e deixando a mochila vazia. Você perde 2 pontos de SORTE. Cerca de uma hora depois, o efeito congelante da poeira se desfaz, e as sensações retornam a seu corpo. Furioso com a perda, você ruma para o norte, determinado a se vingar. Volte para 29. ")

    sorte = sorte - 2

    input("\nPressione Enter para ir para 29...")
    aventura29()




def aventura307():

    print(stats_final)
    print("\nCAP 307")
    print("\nO armário contém uma marreta de madeira e 10 espigões de ferro, os quais você põe na mochila enquanto decide qual porta abrir. Se quiser abrir a porta do oeste, volte para 263. Se preferir abrir a porta do norte, volte para 136. ")

    escolha = input("\nIr para 263 ou 136?: ")
    mochila.append('marreta de madeira')
    mochila.append('espiga de ferro'*10)
    match escolha:
        case '263':
            aventura263()
        case '136':
            aventura322()
        case _:
            print("\nOpção Invalida!")
            aventura307()


def aventura308():

    print(stats_final)
    print("\nCAP 308")

    print("\nA Medusa berra quando você entra na gaiola, mantendo os olhos firmemente fechados e desferindo golpes furiosos de um lado para o outro com a espada. Você sente a lâmina penetrar profundamente na fera e ouve um baque alto quando ela desaba pesadamente no chão. Você abre os olhos de novo e se arrepia com a visão da Medusa prostrada. O manto dela está preso por um grande broche constituído por uma única gema grande; é uma granada. Você a arranca, põe no bolso e sai do aposento, rumo ao norte. Vá para 316. ")

    input("\nPressione Enter para ir para 316...")
    aventura316()


def aventura309(sorte, energia):
    print(stats_final)
    print("\nCAP 309")
    print("\nVocê cambaleia desnorteado em busca de uma poça de água, mas não encontra. O ácido queima com uma dor lancinante bem fundo na sua garganta. Você perde 3 pontos de ENERGIA. Se ainda estiver vivo, Teste sua Sorte. Se você tiver sorte, volte para 231. Se não tiver sorte, volte para 193. ")

    energia = energia - 3
    if energia > 0:
            input("\nPressione Enter para rodar os dados...")
            x = roda_1_dado()
            print(f"\nO dado 1 tirou: {x}.")
            y = roda_1_dado()
            print(f"\nO dado 2 tirou: {y}.")
            soma = x + y

            print(f"\nA soma dos dados deu {soma}, sua sorte é {sorte}.")

            if soma <= sorte:
                input("\nVoce deu sorte!\nPressione Enter para ir para 231 ...")
                aventura231()

            else:
                input("\nVocê não teve sorte!\nPressione Enter para ir para 193...")
                aventura193()
    else:
        fim_de_jogo()




def aventura310():
    print(stats_final)
    print("\nCAP 310")
    print("\nVocê chega à parede do outro lado da câmara e vê duas portas.\n\nSe quiser abrir a portada esquerda - vá para 339.\n\nSe quiser abrir a porta da direita - volte para 262. ")

    escolha = input("\nIr para 339 ou 262?: ")
    match escolha:
        case '339':
            aventura339()
        case '262':
            aventura262()
        case _:
            print("\nOpção Invalida!")
            aventura310()


def aventura311():

    print(stats_final)
    print("\nCAP 311")
    print("\nDepois de muito relutar, o Bárbaro concorda com sua alternativa. Vocês dois tomam distância e saltam por sobre o poço. Aterrissando em segurança do outro lado, você continua descendo pelo túnel. O Bárbaro, que vai na frente, subitamente tropeça em uma pedra, que se inclina para frente e dispara o mecanismo de um rochedo preso precariamente ao teto. O rochedo despenca sobre ele, derrubando-o e esmagando-lhe o crânio. Você terá que continuar sua jornada sozinho. Vá para 325. ")

    input("\nPressione Enter para ir para 325...")
    aventura325()


def aventura312(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome):
    print(stats_final)
    print("\nCAP 312")
    print("\nO disco, afiado como uma navalha, passa assobiando pela sua cabeça e crava-se profundamente em um dos pilares. Você se vira e põe-se em guarda para enfrentar o assassino, que avança com a espada longa desembainhada.\n\nNINJA    -    HABILIDADE 11        ENERGIA 9\n\nSe você vencer, volte para 232. ")

    energia_monstro = 9
    habilidade_monstro = 11
    nome = "NINJA"

    batalha(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome)

    input("Você venceu o NINJA, parabens!\n\nPressione Enter para retornar para 232...")

def aventura313():
    print(stats_final)
    print("\nCAP 313")
    print("\nO túnel termina em uma encruzilhada. As pegadas que você vem seguindo viram para o norte, e você resolve manter-se na trilha delas. Volte para 32. ")

    input("\nPressione Enter para ir para 32...")
    aventura32()



def aventura314():
    print(stats_final)
    print("\nCAP 314")
    print("\nSua espada corta a maçaneta e, separada do corpo de origem, a membrana murcha e cai ao chão. Não tendo outra alternativa, você gira, um tanto apreensivo, a maçaneta da outra porta. Volte para 262 ")

    input("\nPressione Enter para ir para 262...")
    aventura262()



def aventura315():
    print(stats_final)
    print("\nCAP 315")
    print("\nO túnel dá uma guinada brusca para a esquerda e chega ao fim em uma parede alta, na qual há uma porta. Você ouve um rugido feroz vindo do outro lado da porta e tenta imaginar quão gigantesca seria a fera capaz de tamanho ruído. Se você tiver um rolo de corda e um gancho de ferro, volte para 129. Se não tiver esses objetos, volte para 245. ")
    if 'rolo de corda' in mochila and 'gancho de ferro' in mochila:
        input("Você tem os itens para seguir. Pressione Enter para retornar para 129...")
        aventura129()
    else:
        input("Você não tem os itens para seguir. Pressione Enter para retornar para 245...")
        aventura245()

def aventura316():

    print(stats_final)
    print("\nCAP 316")
    print("\nO túnel continua por uma boa distância antes de chegar a um cruzamento.\n\nSe você quiser se dirigir para o oeste pelo novo túnel - volte para 296.\n\nSe preferir continuar para o norte - volte para 241. ")

    escolha = input("\nIr para 296 ou 241?: ")
    match escolha:
        case '296':
            aventura296()
        case '241':
            aventura241()
        case _:
            print("\nOpção Invalida!")
            aventura316()



def aventura317():
    print(stats_final)
    print("\nCAP 317")
    print("\nTateando nos lados do buraco perfurado com sua espada, você abre caminho cegamente pelo lodo viscoso. Você segue as curvas e reviravoltas do orifício por um tempo que parece ser uma eternidade e começa a imaginar onde poderia levar. De repente, você ouve o ruído de alguma coisa se arrastando à frente. Você fica gelado de medo, seus olhos tentando desesperadamente rasgar a escuridão impenetrável. Antes que você se dê conta do que está acontecendo, seu pescoço é abocanhado pelas fortíssimas mandíbulas de outro Verme da Rocha. E o companheiro daquele que você matou, o qual foi atraído pelo cheiro de sangue na sua espada. Ele aperta mais forte. Seu pescoço estala como um ramo seco. Sua aventura termina aqui. ")

    fim_de_jogo()


def aventura318():
    print(stats_final)
    print("\nCAP 318")
    print("\nDepois de cruzar a ponte, você atravessa a caverna correndo. Finalmente, vê um túnel na parede do outro lado, pelo qual você entra a toda. O túnel termina numa pesada porta de madeira, e ela está trancada. Se você tiver uma chave de ferro, volte para 86. Se não tiver uma chave, volte para 276. ")
    if 'chave de ferro' in mochila:
        input("Você tem a chave de ferro. Pressione Enter para seguir para 86...")
        aventura86()
    else:
        input("Você não tem a chave de ferro. Pressione Enter para seguir para 276...")



def aventura319():
    print("\nA armadura e a espada pesam mais do que você pensa. No ar, você toma consciência, com horror, de que não vai conseguir chegar ao outro lado do poço. Você se choca contra o lado do poço, uns dois metros abaixo da borda, e despenca de cabeça para o fundo. Volte para 285.")

    input("\nPressione Enter para voltar 285...")

    aventura285(habilidade, energia)


def aventura320():
    print(stats_final)
    print("\nCAP 320")
    print("\nVocê resolve revistar o Ninja e, em meio às vestes dele, encontra um saco de pano. Dentro, há um frasco de água, um pouco de arroz enrolado em folha de palmeira, um vidro de unguento e um lindo diamante. Você:\n\nComerá o arroz e beberá a água? - Vá para 330\nEsfregará um pouco do unguento nos seus ferimentos? - Volte para 269\nPegará apenas o diamante e sairá do salão? - Volte para 127 ")

    escolha = input("\nIr para 330, 269 ou 127?: ")
    match escolha:
        case '330':
            aventura330()
        case '269':
            aventura269()
        case '127':
            aventura127()
        case _:
            print("\nOpção Invalida!")
            aventura320()

def aventura321():
    print(stats_final)
    print("\nCAP 321")
    print("\nVocê puxa o cordão e o pano sobe pelos lados da gaiola. A voz da mulher insiste para que você seja rápido, dizendo que o aposento está preparado para uma cilada, de forma que o piso desabará em um minuto por causa do seu peso extra. Se você ainda quiser ajudá-la, volte para 289. Se preferir sair do aposento e se dirigir para o norte pelo túnel, Volte para 316. ")

    escolha = input("\nIr para 289 ou 316?: ")
    match escolha:
        case '289':
            aventura289()
        case '316':
            aventura316()
        case _:
            print("\nOpção Invalida!")
            aventura321()



def aventura322():
    print(stats_final)
    print("\nCAP 322")
    print("\nVocê passa pela cadeira de madeira e logo retorna ao cruzamento, virando à direita para o oeste. Volte para 43. ")

    input("\nPressione Enter para ir para 43...")


def aventura323():
    print(stats_final)
    print("\nCAP 323")
    print("\nDepois de amarrar a corda em torno da rocha, você desce devagar para o fundo do poço. Throm recupera a corda dele, soltando-a da rocha com uma sacudidela, e vocês partem juntos pelo novo túnel. Volte para 194. ")

    input("\nPressione Enter para ir para 194...")

    aventura194()



def aventura324():
    print(stats_final)
    print("\nCAP 324")
    print("\nVocê falou com o servo aleijado dos Juízes da Prova? Se falou, volte para 256. Se não, volte para 79. ")

    if 'servo alejado' not in ativos:
        input("Voce não falou com o juiz. Pressione Enter para ir para 79...")
        aventura79()
    else:
        input("Você falou com o juiz. Pressione Enter para ir para 256...")
        aventura256()

def aventura325():
    print(stats_final)
    print("\nCAP 325")
    print("\nVocê se levanta e segue túnel abaixo. De repente, vê a luz do dia no fim do túnel. Enquanto corre na direção da visão mais bela que teve diante de si desde muito tempo, um céu claro e azul, árvores verdes, você sonha com o alegre cenário de pessoas vibrando. Mas não há recepção de herói da parte das pessoas à sua volta. Estão todas mortas. Você está dentro de uma câmara fria repleta de cadáveres e esqueletos com armaduras. A saída para a vitória era apenas uma ilusão. Somente os despojos de aventureiros do passado são reais. Profundamente deprimido, você caminha de volta para o túnel, mas se choca com uma barreira invisível. Você está aprisionado neste sinistro local, fadado a terminar seus dias na câmara dos mortos. ")

    fim_de_jogo()


def aventura326():
    print(stats_final)
    print("\nCAP 326")
    print("\nAdiante, o túnel faz uma curva fechada para a esquerda. Ao □obra-la, você quase bate de frente em dois ORCAS de aspecto feroz, armados de maças com pontas de ferro e usando armaduras de couro. Você está totalmente despreparado, e, enquanto desembainha a espada, um deles desfere-lhe um golpe de maça. Jogue um dado. Se você obtiver 1 ou 2, volte para 91. Se obtiver 3 ou 4, volte para 189. Se obtiver 5 ou 6, vá para 380. ")
    input("\nPressione Enter para rodar o dado...")
    x = roda_1_dado()

    if x == 1 or x == 2:
        input(f"\nO dado resultou em {x}.\nPressione Enter para ir para 91...")
        aventura91()
    elif x == 3 or x == 4:
        input(f"\nO dado resultou em {x}.\nPressione Enter para ir para 189...")
        aventura189()
    elif x == 5 or x == 6:
        input(f"\nO dado resultou em {x}.\nPressione Enter para ir para 380...")
        aventura380()



def aventura327(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome):
    print(stats_final)
    print("\nCAP 327")
    print("\nExclusivamente voltado para agarrar-lhe o braço, o Demônio do Espelho não tenta defender- se.\n\nDEMÔNIO DO ESPELHO    -    HABILIDADE 10        ENERGIA 10\n\nSe, durante uma Série de Ataque, a Força de Ataque do Demônio do Espelho for maior que a sua, volte para 8.\nSe você conseguir derrotar o Demônio do Espelho sem que ele ganhe qualquer Série de Ataque, volte para 92. ")
    energia_monstro = 10
    habilidade_monstro = 10
    nome = "DÊMONIO DO ESPELHO"

    batalha(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome)

    input("Você venceu o DEMONIO DO ESPELHO! Pressione Enter para retornar para 92...")

    aventura92()


def aventura328():
    print(stats_final)
    print("\nCAP 328")
    print("\nVocê olha em torno do quarto de Erva. Ao ver o retrato de um outro Troll pendurado na parede, pergunta a ela se são parentes. Imediatamente, o humor e a expressão dela mudam. Ela afrouxa o aperto sobre você e sorri, dizendo: “Ah, sim. Este é meu amado e querido irmão Barriga Azeda. Ele tem-se saído muito bem lá no sul, em Port Blacksand. Está agora na Guarda Imperial, na tropa de elite de Lord Azzur. Estou muito orgulhosa dele.” Erva fica olhando para a pintura e continua a tecer elogios ao irmão. Se você quiser se esgueirar para fora do quarto, pela porta na parede do leste, volte para 125. Se preferir continuar a conversa, volte para 99. ")


    escolha = input("\nIr para 125 ou 99?: ")
    match escolha:
        case '125':
            aventura125()
        case '99':
            aventura99()
        case _:
            print("\nOpção Invalida!")
            aventura328()


def aventura329():
    print(stats_final)
    print("\nCAP 329")
    print("\nVocê caminha até o espelho e se diverte com a imagem distorcida. Sua cabeça parece tão grande quanto uma abóbora, o rosto, muito estranho... Sem qualquer sinal prévio, uma dor terrível martela-lhe a cabeça; você tenta desviar o olhar do espelho, mas não consegue. Alguma força do mal mantém seus olhos pregados ao próprio reflexo. Você segura a cabeça com as mãos e, horrorizado, se dá conta de que ela está se expandindo. Você não pode mais suportar a dor, e tomba sem sentidos para nunca mais acordar. ")

    fim_de_jogo()



def aventura330():
    print(stats_final)
    print("\nCAP 330")
    print("\nAs rações do Ninja são modestas mas bem-vindas. Acrescente 1 ponto de ENERGIA. Se você ainda não o fez, poderá esfregar um pouco do unguento nos seus ferimentos - volte para 269 - ou sair do salão, levando só o diamante - volte para 127. ")

    escolha = input("\nIr para 269 ou 127?: ")
    match escolha:
        case '269':
            aventura269()
        case '127':
            aventura127()
        case _:
            print("\nOpção Invalida!")
            aventura330()



def aventura331(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome):
    print(stats_final)
    print("\nCAP 331")
    print("\nTocar o pergaminho tem precisamente o efeito que você temia. O esqueleto dá um impulso para frente e, levantando-se da cadeira numa série de movimentos aos arrancos, ergue a espada para golpeá-lo. Esquivando-se para o lado, você desembainha a sua espada para se defender.\n\nGUERREIRO-ESQUELETO    -    HABILIDADE 8        ENERGIA 6\n\nSe você vencer, volte para 71.")


    habilidade_monstro = 8
    energia_monstro = 6
    nome = "GUERREIRO-ESQUELETO"

    batalha(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome)

    input(f"Você venceu o {nome}!\nPressione Enter para ir para 71...")

    aventura71()


def aventura332(sorte):
    print(stats_final)
    print("\nCAP 332")
    print("\nSua gema cai na poça com um 'plop' surdo. Enquanto espera que alguma coisa aconteça, você começa a se sentir fraco. O gás que emana da poça é tóxico, e você tomba inconsciente. Teste sua Sorte. Se você tiver sorte, volte para 53. Se não tiver sorte, volte para 272.")

    x = roda_1_dado()
    print(f"\nO dado 1 tirou: {x}.")
    y = roda_1_dado()
    print(f"\nO dado 2 tirou: {y}.")
    soma = x + y

    print(f"\nA soma dos dados deu {soma}, sua sorte é {sorte}.")

    if soma <= sorte:
        input("\nVoce deu sorte!\nPressione Enter para ir para 53...")
        sorte = sorte - 1
        aventura53()

    else:
        input("\nVocê não teve sorte!\nPressione Enter para ir para 272...")
        sorte = sorte - 1
        aventura272()



def aventura333():
    print(stats_final)
    print("\nCAP 333")
    print("\nVocê ouve passos e, de repente, a porta do alçapão é jogada para trás. Por alguns segundos, você é cegado pela intensa luz que vem do aposento de cima, e não vê o Goblin desferir um golpe de lança, nem ouve o riso sádico quando a ponta rasga seu pescoço. Sua aventura termina aqui, nos degraus de pedra do túnel. ")

    fim_de_jogo()


def aventura334():
    print(stats_final)
    print("\nCAP 334")
    print("\nVocê tenta se livrar da língua com as mãos nuas, mas não consegue. Lentamente, você é arrastado para a poça, onde, depois de decomposto pelo lodo, seu corpo será devorado pela pavorosa Besta Sangrenta. ")

    fim_de_jogo()


def aventura335(sorte):
    print(stats_final)
    print("\nCAP 335")
    print("\nAinda correndo o mais rápido que pode, você mergulha no rio. Teste sua Sorte. Se você tiver sorte, volte para 67. Se não tiver sorte, volte para 101. ")


    x = roda_1_dado()
    print(f"\nO dado 1 tirou: {x}.")
    y = roda_1_dado()
    print(f"\nO dado 2 tirou: {y}.")
    soma = x + y

    print(f"\nA soma dos dados deu {soma}, sua sorte é {sorte}.")

    if soma <= sorte:
        input("\nVoce deu sorte!\nPressione Enter para voltar para 67...")
        sorte = sorte - 1
        aventura67()

    else:
        input("\nVocê não teve sorte!\nPressione Enter para voltar para 101...")
        sorte = sorte - 1
        aventura101()



def aventura336():
    print(stats_final)
    print("\nCAP 336")
    print("\nA munhequeira foi feita e amaldiçoada por uma Bruxa. Ela torna suas reações mais lentas e embota-lhe os sentidos. Reduza sua HABILIDADE em 4 pontos. Furioso, você chuta a parede do túnel e segue para o norte. Volte para 298. ")

    input("\nPressione Enter para voltar para 298...")

    aventura298()


def aventura337():
    print("\nA água fresca é revigorante, mas provém de uma fonte amaldiçoada por uma Bruxa. Some 1 ponto de ENERGIA, mas desconte 2 pontos de SORTE. Se ainda não o fez, você poderá beber da outra fonte - volte para 173 - ou continuar para o norte - vá para 368. ")
    energia = energia + 1
    sorte = sorte - 2

    escolha = input("\nIr para 173 ou 368?: ")
    match escolha:
        case '173':
            aventura173()
        case '368':
            aventura368()
        case _:
            print("Opção Invalida!")
            aventura337()



def aventura338():
    print(stats_final)
    print("\nCAP 338")
    print("\nOs corpos são de dois guardas Orcas. Pelo menos um de seus rivais na Prova dos Campeões ainda deve estar à sua frente. De uma rápida revista aos corpos nada resulta senão um colar de dentes pendurado no pescoço de um dos Orcas. Se você quiser usar o colar, volte para 123. Se preferir partir para o norte sem o colar, volte para 282. ")

    escolha = input("\nIr para 123 ou 282?")
    match escolha:
        case '123':
            aventura123()
        case '282':
            aventura282()
        case _:
            print("Opção Invalida!")
            aventura338()


def aventura339(energia):
    print(stats_final)
    print("\nCAP 339")
    print("\nQuando você toca a maçaneta da porta, ela fica mole na sua mão, e, quando tenta tirar a mão, descobre que ela está grudada na maçaneta. Então, um punho gigantesco se forma no meio da porta e projeta-se na sua direção, atingindo-o no estômago. Você perde 1 ponto de ENERGIA. Se tiver uma moringa de ácido, volte para 303. Se não tiver, volte para 236. ")

    energia = energia - 1
    if 'moringa de acido' in mochila:
        input("Você possui Moringa de acido.\nPressione Enter para seguir para 303...")
        aventura303()
    else:
        input("Você não tem moringa de acido.\nPressione Enter para seguir para 236...")


def aventura340():
    print(stats_final)
    print("\nCAP 340")
    print("\nO medo lhe dá uma nova injeção de energia, e, de alguma forma, suas pernas cansadas conseguem mantê-lo à frente do rochedo. Adiante, à direita, você vê a forma bem-vinda de uma porta. Você mergulha de encontro à porta e, por sorte, ela se abre. O rochedo passa estrondoso, e você fica deitado, exausto, no chão de um aposento grande. Vá para 381. ")

    input("\nPressione Enter para ir para 381...")
    aventura381()


def aventura341():
    print(stats_final)
    print("\nCAP 341")
    print("\nUm homem aleijado, com cadeias nos pés, arrasta-se na sua direção carregando uma bandeja de madeira cheia de pão e água. Ele parece cansado e desalentado, e tenta passar por você sem demonstrar reação à sua presença. Você: \n\nFalará com ele? - Vá para 367 \nPegará pão e água da bandeja dele? - Volte para 38\nOferecerá a ele alguma provisão (se você ainda tiver alguma)? - Volte para 169 ")

    escolha = input("\nIr para 367, 38 ou 169?: ")
    match escolha:
        case '367':
            aventura367()
        case '38':
            aventura38()
        case '169':
            aventura169()
        case _:
            print("\nOpção Invalida!")
            aventura341()



def aventura342():
    print(stats_final)
    print("\nCAP 342")
    print("\nSuas reações são lentas por causa do veneno e, embora você tente pular por cima da língua estendida, suas pernas não conseguem erguê-lo o bastante. A língua pegajosa se enrola na sua perna e começa a puxá-lo na direção da poça. Você é arrastado para o chão e não consegue desembainhar a espada. Se você tiver um punhal, volte para 294. Se não tiver um punhal, volte para 334. ")

    if 'punhal' in mochila:
        input('Você possui um punhal. Pressione Enter para seguir para 294')
        aventura294()
    else:
        input('Você não possui um punhal. Pressione Enter para seguir para 334')
        aventura334()



def aventura343():
    print(stats_final)
    print("\nCAP 343")
    print("\nCom vozes esganiçadas, os Trogloditas explicam as regras da Corrida da Flecha. Eles dispararão uma flecha e você poderá caminhar, sem ser atacado, até o ponto onde ela cair. Porém, você deverá ir descalço, e o chão da caverna, como pode ver, está coberto de pedras pontiagudas. Logo que você chegar à flecha, os Trogloditas começarão a persegui-lo; se o pegarem, você será morto. De repente, um dos Trogloditas dispara uma flecha bem alto no ar. Ela cai a grande distância, e, imediatamente, os Trogloditas forçam-no a caminhar na direção dela. Enquanto você anda devagar na direção da flecha, ouve os gritos excitados dos Trogloditas. Ao chegar à flecha você se volta e vê os Trogloditas agitarem os braços no ar e iniciarem a perseguição. Você corre o mais depressa que pode, os pés sangrando com os cortes sofridos nas pedras pontiagudas. Você perde 1 ponto de ENERGIA. Adiante, um rio subterrâneo, que corre de leste para oeste, cruza a caverna; uma ponte de madeira liga uma margem à outra. Se você quiser atravessar a ponte, volte para 318. Se quiser mergulhar no rio, volte para 47. ")
    energia = energia - 1

    escolha = input("\nIr para 318 ou 47?: ")
    match escolha:
        case '318':
            aventura318()
        case '47':
            aventura47()
        case _:
            print("\nOpção Invalida!")
            aventura343()



def aventura344():
    print(stats_final)
    print("\nCAP 344")
    print("\nO túnel faz curvas e reviravoltas, mas continua sempre para o norte. À sua frente, um facho de luz azul desce do teto para o chão. Ele faísca e cintila, e você pode ver imagens de rostos que riem na luz. Se você quiser passar através da luz, volte para 229. Se preferir contornar o facho, volte para 107. ")

    escolha = input("\nIr para 229 ou 107?: ")
    match escolha:
        case '229':
            aventura229()
        case '107':
            aventura107()
        case _:
            print("\nOpção Invalida!")
            aventura344()



def aventura345():
    print(stats_final)
    print("\nCAP 345")
    print("\nVocê está prestes a entrar no aposento quando a Poção de Detecção de Cilada começa a fazer efeito, e você é dominado por uma terrível premonição. Há uma armadilha mortal neste aposento. Você resolve não entrar e continua para o norte pelo túnel. Volte para 252. ")

    input("\nPressione Enter para ir para 252...")
    aventura252()


def aventura346():
    print(stats_final)
    print("\nCAP 346")
    print("\nVocê tira a bota do pé e se esforça para estendê-la até o sino e travar-lhe a vibração. Aos poucos, o sino vai parando de vibrar, e a dor no seu corpo diminui gradualmente. Você consegue se levantar, mas não afasta a bota do sino até que ele esteja completamente imóvel. Você calça a bota e continua a jornada para o oeste. Vá para 362. ")

    input("\nPressione Enter para ir para 362...")
    aventura362()



def aventura347():
    print(stats_final)
    print("\nCAP 347")
    print("\nO Anão sacode a cabeça, dizendo: “Só músculos, sem inteligência, não bastam para conquistar a Prova dos Campeões. Sinto dizer que você fracassou. Você não terá permissão para ir embora, pois poderá revelar os segredos do calabouço para outros. Todavia, você conseguiu muito chegando tão longe, e eu o indicarei para meu servo pelos anos futuros para preparar o calabouço para os novos competidores”. ")

    fim_de_jogo()


def aventura348():
    print("\nVocê avança sobre a Besta Sangrenta, tentando evitar a língua que se estende para agarrar-lhe a perna. Jogue dois dados. Se o total for igual ou menor que a sua HABILIDADE, volte para 225.\nSe o total for maior que a sua HABILIDADE, volte para 159. ")

    input("\nPressione Enter para rodar os dados...")
    x = roda_1_dado()
    print(f"\nO dado 1 tirou: {x}.")
    y = roda_1_dado()
    print(f"\nO dado 2 tirou: {y}.")
    soma = x + y

    print(f"\nA soma dos dados deu {soma}, sua habilidade é {habilidade}.")

    if soma <= habilidade:
        input("\n\nPressione Enter para ir para 225 ...")
        aventura225()

    else:
        input("\n\nPressione Enter para ir para 159...")
        aventura159()


def aventura349(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome):
    print(stats_final)
    print("\nCAP 349")
    print("\nVocê desce pela corda para o interior do poço, segurando-se com uma das mãos, enquanto a outra leva a espada desembainhada. O Diabo do Poço é uma das feras mais terríveis que você já viu, e você sabe que esta será uma das lutas mais difíceis da sua vida.\n\nDIABO DO POÇO    -    HABILIDADE 12        ENERGIA 15\n\nSe você vencer, volte para 258.")

    energia_monstro = 15
    habilidade_monstro = 12
    nome = "DIABO DO POÇO"
    
    batalha(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome)

    input("Você venceu o DIABO DO POÇO! Pressione Enter para seguir para 258...")

    aventura258()

def aventura350():
    print(stats_final)
    print("\nCAP 350")
    print("\nA Mosca Gigante mergulha na sua direção e agarra-o com quatro patas. Rapidamente ela retorna ao teto da caverna, e você se encontra indefeso pendurado no ar. Súbito, para seu horror, ela o solta. Você despenca de 10 metros de altura, estatelando-se no solo. Jogue um dado e deduza o número de seu índice de ENERGIA. Se ainda estiver vivo, você desembainha a espada; bem a tempo, pois a Mosca Gigante vem descendo para tentar capturá- lo mais uma vez. Volte para 39. ")

    input("\nPressione Enter para ir para 39...")
    aventura39()


def aventura351():
    print(stats_final)
    print("\nCAP 351")
    print("\nO ídolo é muito liso, e a escalada será difícil. Você tem corda? Se tiver, vá para 396. Se não tiver, volte para 186. ")

    if 'corda' in mochila:
        input("\nVocê usa sua corda.\n\nAperte Enter para seguir para 396.")
        aventura396()
    else:
        input("\nVocê não tem uma corda.\n\nPressione Enter para voltar para 186... ")
        aventura186()


def aventura352():
    print(stats_final)
    print("\nCAP 352")
    print("\nVocê ouve o som de rochas sendo trituradas e esmagadas à sua frente. O ruído cresce e, subitamente, você se dá conta de que a parede do seu lado direito começa a desabar. Apavorado, você vê uma enorme e horrorosa criatura, com mandíbulas incrivelmente poderosas, deslizar por um buraco na parede. A enorme boca da criatura mastiga rocha enquanto ela vira a cabeça devagar de um lado para outro, sentindo o ar fresco do túnel. O VERME DA ROCHA parece ser cego, mas dá a impressão de estar ciente de sua presença, talvez sentindo o calor de seu corpo. Ele se arrasta na sua direção com as mandíbulas bem abertas, pronto para o ataque. Se você quiser lutar contra o Verme da Rocha, volte para 254. Se preferir correr de volta pelo túnel para o cruzamento e depois se dirigir para o leste, volte para 68. ")

    escolha = input("\nIr para 254 ou 68?: ")
    match escolha:
        case '254':
            aventura254()
        case '68':
            aventura68()
        case _:
            print("\nOpção Invalida!")
            aventura352()


def aventura353(habilidade, energia):
    print(stats_final)
    print("\nCAP 353")
    print("\nAntes que você possa sair do caminho, o rochedo se choca contra seu ombro. Você perde 1 ponto de HABILIDADE e 4 pontos de ENERGIA. Se ainda estiver vivo, volte para 325. ")

    habilidade = habilidade - 1
    energia = energia - 1
    if energia > 0:
        input("Você sobrevive, mas sai ferido. Pressione Enter para ir para 325...")
        aventura325()
    else:
        fim_de_jogo()


def aventura354():
    print(stats_final)
    print("\nCAP 354")
    print("\nA pílula faz com que você se sinta como se o mundo inteiro estivesse contra você. E perde 2 pontos de SORTE. O Anão lhe diz que agora você pode passar à segunda fase do teste. Ele apanha uma cesta de vime e lhe diz que ela contém uma serpente. Vira a cesta e a serpente cai no chão. É uma naja, e se ergue no ar, pronta para dar o bote. O Anão lhe diz que pretende testar suas reações. Você deverá agarrar a naja com as mãos nuas, pelo pescoço, evitando as presas mortais. Você se agacha, tensionando os músculos para o momento decisivo. Jogue dois dados. Se o total for igual ou menor que a sua HABILIDADE, volte para 55. Se o total for maior que a sua HABILIDADE, volte para 202. ")

    input("\nPressione Enter para rodar os dados...")
    x = roda_1_dado()
    print(f"\nO dado 1 tirou: {x}.")
    y = roda_1_dado()
    print(f"\nO dado 2 tirou: {y}.")
    soma = x + y

    print(f"\nA soma dos dados deu {soma}, sua habilidade é {habilidade}.")

    if soma <= habilidade:
        input("\n\nPressione Enter para ir para 55 ...")
        aventura55()

    else:
        input("\n\nPressione Enter para ir para 202...")
        aventura202()


def aventura355():
    print(stats_final)
    print("\nCAP 355")
    print("\nVocê se aproxima silenciosamente por trás dos Hobglobins que lutam e, saltando das sombras, empurra-os contra a parede e foge correndo. Você olha para trás e os vê esparramados no chão. Rindo, você segue depressa para o norte. Volte para 110. ")

    input("\nPressione Enter para ir para 110...")
    aventura12()


def aventura356():
    print(stats_final)
    print("\nCAP 356")
    print("\nHá uma abertura no lado esquerdo da parede do túnel. Você está de pé na entrada de uma caverna grande, quando ouve uma voz de mulher gritando por socorro. Você distingue apenas a forma de uma figura humana que rola pelo chão no fundo da caverna. Se você quiser entrar na caverna, volte para 170. Se preferir continuar para o norte pelo túnel, volte para 192.")

    escolha = input("\nIr para 170 ou 192?: ")
    match escolha:
        case '170':
            aventura170()
        case '192':
            aventura192()
        case _:
            print("\nOpção Invalida!")
            aventura356()


def aventura357():
    print(stats_final)
    print("\nCAP 357")
    print("\nA Besta Sangrenta chafurda na poça, e o cheiro dos gases venenosos, cujas bolhas sobem à tona e contaminam a atmosfera, provoca ânsias de vômito. Você:\n\nCorrerá contornando a poça da fera, na direção do túnel? - Volte para 255\nJogará uma gema na poça (se você tiver uma)? - Volte para 332 \nAtacará a fera com sua espada? - Volte para 180 ")

    escolha = input("\nIr para 255, 332 ou 180?: ")
    match escolha:
        case '255':
            aventura255()
        case '332':
            aventura332()
        case '180':
            aventura180()
        case _:
            print("\nOpção Invalida!")
            aventura357()


def aventura358(energia):
    print(stats_final)
    print("\nCAP 358")
    print("\nVocê perde o equilíbrio e despenca de cabeça no chão. Perde 2 pontos de ENERGIA. Você desiste de tentar escalar o ídolo e corre para seguir pelo túnel na parede norte. Volte para 239.")


    energia = energia - 2


    input("\nPressione Enter para ir para 239...")
    aventura239()


def aventura359():
    print(stats_final)
    print("\nCAP 359")
    print("\nVocê cai da corda e despenca de cabeça na fenda. Bate com a cabeça em uma saliência rochosa e morre antes de chegar ao fundo da fenda. ")

    fim_de_jogo()


def aventura360():
    print(stats_final)
    print("\nCAP 360")
    print("\nDepois de pagar, você sobe na cesta de vime. O velho grita, jogando a cabeça para trás: 'Puxa, Erva!' A corda se retesa, e a cesta se ergue aos solavancos. Enquanto você está sendo içado cada vez mais alto, o velho lhe grita: “Você vai gostar de Erva, ela é uma ótima garota. Nós a chamamos de Erva Venenosa!” Ele ri descontrolado, e você, um tanto apreensivo, se pergunta quem o está içando. A cesta passa por um buraco no teto, e você se vê em um pequeno quarto, frente a frente com uma mulher TROLL feia e velha. Ela tem o rosto peludo e coberto de verrugas. Com uma enorme mão ela o puxa para fora da cesta, a qual deixa cair lá embaixo. Em seguida, agarra-o pela garganta e lhe diz, numa voz rouca: “Quero pagamento também!” Você:\n\nOferecerá a ela alguma coisa da sua mochila? - Volte para 297\nTentará convencê-la a não cobrar nada de você? - Volte para 328\nAtacará a mulher com sua espada? - Volte para 211")

    escolha = input("\nIr para 297, 328 ou 211?: ")
    match escolha:
        case '297':
            aventura297()
        case '328':
            aventura328()
        case '211':
            aventura211()
        case _:
            print("\nOpção Invalida!")
            aventura68()


def aventura361(sorte):
    print(stats_final)
    print("\nCAP 361")
    print("\nAs mandíbulas do Diabo do Poço dão um bote no amuleto de macaco e o apanham no ar, mas logo se abrem de novo, forçadas pelo amuleto, que se expandiu a ponto de ocupar toda a boca da fera. Enquanto o Diabo do Poço se debate, tentando livrar-se do amuleto, você desce até o fundo para chegar às portas duplas. Desvairado, o Diabo do Poço usa o imenso corpo na tentativa de esmagar você contra a parede. Teste sua Sorte. Se você tiver sorte, volte para 82. Se não tiver sorte, vá para 377. ")

    input("\nPressione Enter para rodar os dados...")
    x = roda_1_dado()
    print(f"\nO dado 1 tirou: {x}.")
    y = roda_1_dado()
    print(f"\nO dado 2 tirou: {y}.")
    soma = x + y

    print(f"\nA soma dos dados deu {soma}, sua sorte é {sorte}.")

    if soma <= sorte:
        input("\nVoce deu sorte!\nPressione Enter para ir para 82 ...")
        aventura82()

    else:
        input("\nVocê não teve sorte!\nPressione Enter para ir para 377...")
        aventura377()



def aventura362():
    print(stats_final)
    print("\nCAP 362")
    print("\nO túnel dá uma guinada acentuada para a direita e continua para o norte até onde a vista alcança. A distância, você ouve uma tremenda comoção: grunhidos, rosnados, uivos. Você desembainha a espada e parte na direção do tumulto. Volte para 264. ")

    input("\nPressione Enter para ir para 264...")
    aventura264()



def aventura363():
    print(stats_final)
    print("\nCAP 363")
    print("\nA comida e a bebida são excelentes, e você se sente muito melhor. Acrescente 2 pontos de ENERGIA. Plenamente satisfeito, você senta e espera a volta do Anão. Volte para 302. ")

    energia = energia + 2

    input("\nPressione Enter para ir para 302...")
    aventura302()

def aventura364():

    print(stats_final)
    print("\nCAP 364")
    print("\nEnquanto remove o sangue do Mantécora de sua espada, você leva um susto ao ver um homenzinho com um nariz grande saltar detrás de um dos pilares de mármore. Ele veste uma túnica justa, verde, e parece inofensivo, embora você fique desconfiado do modo como ele segura uma bola de vidro opaco com uma luz verde cintilante. “Meus cumprimentos!”, ele diz animadamente. “Meu nome é Igbut, o Gnomo, e sou o Juiz da Prova para seu teste final. Não é preciso dizer que meus poderes mágicos são grandes, por isso você não deve tentar me atacar. Talvez você tenha sabido, durante a sua jornada, que as gemas desempenham um papel essencial na Prova dos Campeões. A porta de ferro à sua frente é a saída para a vitória, mas só há uma maneira de abri-la. É preciso pôr três gemas no mecanismo da fechadura, numa ordem específica. Cada gema irradia uma energia que acionará o mecanismo – se você as colocar corretamente, é claro. Eu o ajudarei de certa forma, mas primeiro precisamos das gemas certas. Você tem uma esmeralda?”. Se você tiver uma esmeralda, volte para 31. Se não tiver, volte para 3.")

    if 'esmeralda' in mochila:
        input("Você tem uma esmeralda na sua mochila. Pressione Enter para seguir para 31...")
        aventura31()
    else:
        input("Você não tem uma esmeralda na sua mochila. Pressione Enter para seguir para 3...")
        aventura3()


def aventura365():
    print(stats_final)
    print("\nCAP 365")
    print("\nVocê diz a Throm que matar o Anão não vai adiantar nada, pois vocês jamais acharão a saída da câmara sozinhos. Você argumenta que talvez surja uma chance de enganar o Anão mais tarde, quando tiverem descoberto a saída da câmara, por isso você pretende ir adiante com o teste do Anão. Você diz ao Anão que está pronto, e ele acena para que o siga. Throm deve aguardar a volta dele. Uma porta secreta abre-se na parede da câmara, e você segue o Anão até um pequeno aposento circular. Ele fecha a porta atrás de você e lhe entrega dois dados de osso, mandando que os jogue no chão. Você tira um seis e um dois: total, oito. O Anão pede que você os jogue mais uma vez, mas, agora, deve adivinhar se o total será igual, menor ou maior que oito. Se seu palpite for que será igual, volte para 290. Se achar que será menor que oito, volte para 191. Se optar por maior que oito, volte para 84.")

    escolha = input("\nIr para 290, 191 ou 84?: ")
    match escolha:
        case '290':
            aventura290()
        case '191':
            aventura191()
        case '84':
            aventura84()
        case _:
            print("\nOpção Invalida!")
            aventura365()


def aventura366():
    print(stats_final)
    print("\nCAP 366")
    print("\nA temperatura continua a subir, muito além dos limites de tolerância humanos. Estendido no chão quase derretido do túnel, você não consegue recuperar a consciência. Sua aventura termina aqui.")

    fim_de_jogo()


def aventura367():
    print(stats_final)
    print("\nCAP 367")
    print("\nEle o encara desconfiado quando você diz que é um competidor na Prova dos Campeões. Você pergunta a ele o que faz nos túneis, e ele lhe responde, um tanto relutante, que é servo de um dos Juízes da Prova, os controladores das diferentes partes do calabouço designados pelo Barão Sukumvit. Depois de alguma conversa, ele admite que gostaria de fugir, mas ninguém pode sair do calabouço, pois poderia revelar os segredos da construção. Ele espera conseguir sair dali mediante suborno, e, por uma Peça de Ouro, poderá dizer-lhe onde há um tesouro escondido. Se você quiser pagar pela orientação do velho, volte para 244. Se preferir simplesmente desejar-lhe o melhore continuar para o oeste, volte para 109.")

    escolha = input("\nIr para 244 ou 109?: ")
    match escolha:
        case '244':
            aventura244()
        case '109':
            aventura109()
        case _:
            print("\nOpção Invalida!")
            aventura367()


def aventura368():

    print(stats_final)
    print("\nCAP 368")

    print("\nVocê vê um par de pernas-de-pau junto à parede do lado esquerdo do túnel. Elas estão firmemente acorrentadas, e num aviso preso a um cadeado lê-se: “O preço destas pernas-de- pau é uma Peça de Ouro. Coloque a moeda na ranhura para abrir o cadeado.” Se você quiser comprar as pernas-de-pau, volte para 165. Se preferir prosseguir para o norte, volte para 234.")

    escolha = input("\nIr para 165 ou 234?: ")
    match escolha:
        case '165':
            aventura165()
        case '234':
            aventura234()
        case _:
            print("\nOpção Invalida!")
            aventura368()


def aventura369(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome):
    print(stats_final)
    print("\nCAP 369")
    print("\nO túnel faz uma curva fechada para a direita, continuando para o leste até onde a vista alcança. Throm pára e lhe diz que faça o mesmo. Ele vira a cabeça devagar de um lado para o outro: “Ouço passos descendo pelo túnel na nossa direção”, ele sussurra. “Desembainhe a espada.” Vocês se agacham para se esconder nas sombras, e bem a tempo: duas figuras armadas se aproximam. Throm salta e brada um grito de guerra. Dois TROLLS DA CAVERNA estão diante de vocês. Throm ataca o primeiro com a acha de guerra, e você corre para ajudá-lo, atacando o segundo Troll da Caverna.\n\nTROLL DA CAVERNA    -    HABILIDADE 10        ENERGIA 11\n\nSe você vencer, volte para 288.")

    energia_monstro = 11
    habilidade_monstro = 10
    nome = "TROLL DA CAVERNA"

    batalha(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome)

    input("\n\nParabens! voce venceu o troll da caverna!\n\nPressione Enter para retornar para 288...")


def aventura370(habilidade):
    print(stats_final)
    print("\nCAP 370")
    print("\nQuando você contorna a poça correndo, a Besta Sangrenta estende a língua comprida mais uma vez. Jogue dois dados. Se o total for igual ou menor que o seu índice de HABILIDADE, volte para 104. Se o total for maior que o seu índice de HABILIDADE, volte para 342. ")

    input("\nPressione Enter para rodar os dados...")
    x = roda_1_dado()
    print(f"\nO dado 1 tirou: {x}.")
    y = roda_1_dado()
    print(f"\nO dado 2 tirou: {y}.")
    soma = x + y

    print(f"\nA soma dos dados deu {soma}, sua habilidade é {habilidade}.")

    if soma <= habilidade:
        input("\n\nPressione Enter para ir para 104...")
        aventura104()

    else:
        input("\nnPressione Enter para ir para 342...")
        aventura342()


def aventura371():
    print(stats_final)
    print("\nCAP 371")
    print("\nVocê faz pontaria e joga a bola de madeira no crânio. Jogue dois dados. Se o número obtido for igual ou menor que o seu índice de HABILIDADE, volte para 273. Se o número obtido for maior que o seu índice de HABILIDADE, volte para 113. ")

    input("\nPressione Enter para rodar os dados...")
    x = roda_1_dado()
    print(f"\nO dado 1 tirou: {x}.")
    y = roda_1_dado()
    print(f"\nO dado 2 tirou: {y}.")
    soma = x + y

    print(f"\nA soma dos dados deu {soma}, sua habilidade é {habilidade}.")

    if soma <= habilidade:
        input("\n\nPressione Enter para ir para 273...")
        aventura273()

    else:
        input("\nnPressione Enter para ir para 113...")
        aventura113()


def aventura372():

    print(stats_final)
    print("\nCAP 372")
    print("\nVocê finalmente chega ao corpo do guerreiro, mas, logo que toca na jóia, tanto ela quanto o guerreiro desaparecem como num passe de mágica. A porta bate atrás de você, e segue-se um estrondo agourento acima da sua cabeça. Você olha para o alto e vê o teto baixando. Corre para a porta na tentativa de escapar, mas ela está trancada e não há maçaneta do lado de dentro. O teto vai descendo, e você é obrigado a se deitar no chão, tentando impedir o movimento do teto comas mãos e os pés. Mas o esforço é inútil, e você é esmagado entre os blocos de pedra. ")

    fim_de_jogo()


def aventura373():
    print(stats_final)
    print("\nCAP 373")
    print("\nVocê sobe pelo rochedo macio, temendo ser absorvido por ele a qualquer momento. É difícil passar por cima da coisa, pois seus membros afundam na casca mole, mas, por fim, você consegue chegar ao outro lado. Aliviado por estar de novo em terreno firme, você se dirige para o leste. Volte para 13. ")

    input("\nPressione Enter para ir para 13...")
    aventura13()


def aventura374(sorte):
    print(stats_final)
    print("\nCAP 374")
    print("\nVocê caminha pela caverna, mas não acha nada interessante. Throm o chama lá de trás, dizendo que encontrou um saco de couro sob uma pilha de rochas. Abrindo o saco, Throm ri alto quando um minúsculo camundongo corre entre os dedos dele e foge para uma fresta entre dois rochedos. A súbitas, você ouve o som de rocha rachando: estalactites se desprendem do teto, como resultado da vibração causada pelo riso retumbante de Throm, que ainda ecoa pela caverna. Você berra para que Throm fuja pela passagem em arco, enquanto as estalactites desabam. Teste sua Sorte. Se você tiver sorte, volte para 118. Se não tiver sorte, volte para 295. ")

    input("\nPressione Enter para rodar os dados...")
    x = roda_1_dado()
    print(f"\nO dado 1 tirou: {x}.")
    y = roda_1_dado()
    print(f"\nO dado 2 tirou: {y}.")
    soma = x + y

    print(f"\nA soma dos dados deu {soma}, sua sorte é {sorte}.")

    if soma <= sorte:
        input("\nVoce deu sorte!\nPressione Enter para ir para 118 ...")
        aventura118()

    else:
        input("\nVocê não teve sorte!\nPressione Enter para ir para 295...")
        aventura295()


def aventura375():
    print(stats_final)
    print("\nCAP 375")
    print("\nUma fumaça acre emana da moringa quando você enfia o pano nela. O líquido é indubitavelmente ácido. Você arrolha a moringa de novo e a coloca na mochila, esperando que venha a ter utilidade mais tarde. Você recoloca a espada na bainha e prossegue rumo ao norte. Volte para 110. ")

    mochila.append('moringa de barro')
    input("\nPressione Enter para retornar para 110...")
    aventura110()


def aventura376():
    print(stats_final)
    print("\nCAP 376")
    print("\nO Gnomo, ainda sorrindo, lhe diz, excitado: “Excelente! Só falta uma. Você possui um diamante?” Se você tiver encontrado um diamante, volte para 62. Se não tiver encontrado um diamante, volte para 3. ")

    if 'diamante' in mochila:
        input("Você tem diamante na mochila. Pressione Enter para retornar para 62...")
        aventura62()
    else:
        input("Você não tem diamante na mochila. Pressione Enter para retornar para 3...")
        aventura3()


def aventura377(energia):
    print(stats_final)
    print("\nCAP 377")
    print("\nA imensa fera atira o corpo contra o seu braço, e você solta a corda. Gritando de dor, você despenca no fundo do poço e perde 5 pontos de ENERGIA. Se ainda estiver vivo, volte para 203. ")

    energia = energia - 5
    if energia > 0:
        input("Você sobreviveu, porém sai ferido. Pressione Enter para ir para 203...")
    else:
        fim_de_jogo()


def aventura378(sorte):
    print(stats_final)
    print("\nCAP 378")
    print("\nUm tanto nervoso, você respira fundo e mergulha na poça escura. A parede norte não se projeta muito longe, sob a superfície da água, e você resolve se arriscar e nadar por baixo dela. Logo começa a sentir falta de ar e é obrigado a voltar à tona. Você tenta não pensar que pode estar aprisionado em um velho túnel submerso e fica aliviado quando emerge e encontra ar puro. Você está do outro lado da parede e pode ver o túnel saindo da água e continuando para o norte. Saindo da água, você verifica o conteúdo da mochila molhada. Teste sua Sorte. Se você tiver sorte, volte para 112. Se não tiver sorte, volte para 209. ")

    input("\nPressione Enter para rodar os dados...")
    x = roda_1_dado()
    print(f"\nO dado 1 tirou: {x}.")
    y = roda_1_dado()
    print(f"\nO dado 2 tirou: {y}.")
    soma = x + y

    print(f"\nA soma dos dados deu {soma}, sua sorte é {sorte}.")

    if soma <= sorte:
        input("\nVoce deu sorte!\nPressione Enter para ir para 112 ...")
        aventura112()

    else:
        input("\nVocê não teve sorte!\nPressione Enter para ir para 209...")
        aventura209()



def aventura379():
    print(stats_final)
    print("\nCAP 379")
    print("\nExaurido pelo longo duelo, você cai de joelhos. Ao olhar para o corpo imóvel de Throm, um ódio amargo ao Anão enche-lhe o coração. De alguma forma, você vingará Throm. Envolvido pela raiva, não repara que o Anão entra na arena, até que ele chega diante de você, uma besta carregada apontada para o seu peito. “Sei o que você está pensando”, ele diz calmamente, “mas não se esqueça que só eu sei o modo de sair daqui. Levante-se, está na hora de você ir embora.” O Anão indica que você deve andar à frente dele. De volta à câmara, ele vai até a parede norte e empurra uma das pedras que a compõem. Um pedaço da parede, semelhante a uma porta, gira, abrindo-se para um túnel iluminado por cristais. Com a besta ainda apontada para o seu peito, o Anão sorri, dizendo: “Boa sorte.” Se você quiser caminhar direto para o túnel, volte para 213. Se preferir desferir um soco no Anão, volte para 145. ")

    escolha = input("\nIr para 213 ou 145?: ")
    match escolha:
        case '213':
            aventura213()
        case '145':
            aventura145()
        case _:
            print("\nOpção Invalida!")
            aventura379()


def aventura380(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome):
    print(stats_final)
    print("\nCAP 380")
    print("A maça de ferro do Orca se choca contra o escudo e resvala sem causar dano. O túnel é estreito demais para que os dois o ataquem ao mesmo tempo, por isso você pode lutar com um de cada vez. \n\n\n                        HABILIDADE          ENERGIA\nPrimeiro ORCA     -         5                  5\nSegundo ORCA      -         6                  4\n\nSe você vencer, volte para 257.")

    energia_monstro = 5
    habilidade_monstro = 5
    nome = "Primeiro ORCA"

    batalha(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome)

    input("Você derrotou o primeiro ORCA. Pressione Enter para iniciar a batalha com o Segundo ORCA")

    energia_monstro = 4
    habilidade_monstro = 6
    nome = "Segundo ORCA"

    batalha(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome)

    input("Você derrotou o segundo ORCA. Pressione Enter para ir para 257...")
    aventura257()




def aventura381():
    print(stats_final)
    print("CAP 381")
    print("\nVocê olha em volta no aposento e nada vê de interesse, exceto a alcova na parede do oeste e uma cadeira de pedra no meio do aposento, na qual se encontra sentado o esqueleto de um guerreiro armado, possivelmente um concorrente de anos atrás. Os dedos descamados da mão direita estão fechados em torno de um pedaço de pergaminho. Se você quiser pegar o pergaminho do esqueleto, volte para 331. Se preferir caminhar até a alcova, volte para 128. ")

    escolha = input("\nIr para 331 ou 128?: ")
    match escolha:
        case '331':
            aventura331()
        case '128':
            aventura128()
        case _:
            print("\nOpção Invalida!")
            aventura381()


def aventura382():
    print(stats_final)
    print("\nCAP 382")
    print("\nO velho aponta para uma das estátuas, e você logo a reconhece. É o cavaleiro que iniciou a Prova dos Campeões, um olhar de agonia registrado na pedra para toda a eternidade. O velho sorri, dizendo: “Este homem pesa 50 kg mais a metade do peso dele. Quanto ele pesa?” O que você responderá? \n\n50 quilos? - Volte para 144\n75 quilos? - Volte para 227\n100 quilos? - Vá para 391 ")

    escolha = input("\nIr para 144, 227 ou 391?: ")
    match escolha:
        case '144':
            aventura144()
        case '227':
            aventura227()
        case '391':
            aventura391()
        case _:
            print("\nOpção Invalida!")
            aventura382()



def aventura383():
    print(stats_final)
    print("\nCAP 383")
    print("\nPara sua grande surpresa, nada de extraordinário lhe acontece enquanto está sentado na cadeira. Nada há a fazer senão continuar para o norte pelo túnel. Volte para 188. ")

    input("\nPressione Enter para ir para 188...")
    aventura188()


def aventura384(energia):
    print(stats_final)
    print("\nCAP 384")
    print("\nO quarto degrau cede sob seu peso. Sua perna afunda num buraco e, antes que você tenha tempo de retira-la, sente uma terrível dor no pé quando dentes que não pode ver cravam-se nele. Os guinchos agudos que você ouve lá embaixo são produzidos por ratazanas. Elas estão famintas e arrancam-lhe pedaços do pé, ansiosas pela sua carne. Você perde 2 pontos de ENERGIA. Você recupera o equilíbrio e consegue tirar a perna do buraco. Três ratazanas ainda se penduram pelos dentes no seu pé. Chutando freneticamente, você bate com as cabeças delas contra o corrimão até que se soltem. Você então enrola bandagens improvisadas com sua camisa rasgada em torno do pé que sangra e sobe os degraus para partir para o norte de novo. Volte para 277. ")

    energia = energia - 2

    input("\nPressione Enter para ir para 277...")
    aventura277()


def aventura385():
    print(stats_final)
    print("\nCAP 385")

    print("\nVocê derrama o conteúdo do frasco de vidro na boca e engole o líquido claro. Embora não sinta qualquer mudança imediata, você espera que a poção crie a ilusão de que você é um TROGLODITA igual aos outros diante de você. Respirando fundo, penetra decididamente na caverna. Os Trogloditas continuam com sua dança tribal, acreditando que você é um deles. Você passa por eles andando naturalmente e segue para o norte. Infelizmente, os efeitos da poção são de curta duração, e você ouve um berro atrás de si, quando um dos Trogloditas repara em você, que é forçado a correr, atravessando a caverna. Adiante, você vê um rio subterrâneo que corre de leste para oeste, cruzando a caverna, e uma ponte que liga uma margem à outra. Se você quiser correr pela ponte, volte para 318. Se preferir mergulhar no rio, volte para 47. ")

    escolha = input("\nIr para 318 ou 47?: ")
    match escolha:
        case '318':
            aventura318()
        case '47':
            aventura47()
        case _:
            print("\nOpção Invalida!")
            aventura385()


def aventura386():
    print(stats_final)
    print("\nCAP 386")
    print("\nVocê não chega a percorrer mais de três metros para o oeste antes de se chocar contra uma barreira invisível. Ela estala e solta faíscas, e você é repelido. Você colidiu com uma parede magnética. Você perde 1 ponto de ENERGIA. Não há outra alternativa senão voltar para a encruzilhada e seguir para o norte. Volte para 218. ")

    energia = energia - 1

    input("\nPressione Enter para ir para 218...")
    aventura218()


def aventura387():
    print(stats_final)
    print("CAP 387")
    print("\nDa sua frente vem o baque de passos pesados que se aproximam. Da penumbra surge um ser grande e primitivo, vestido com uma pele de animal e carregando uma clava de madeira. Ao vê-lo, ele grunhe e cospe no chão, em seguida ergue a clava e avança na sua direção, com um ar nada amigável. Você desembainha a espada e se prepara para enfrentar o HOMEM DA CAVERNA.\n\nHOMEM DA CAVERNA    -    HABILIDADE 7        ENERGIA 7\n\nSe você vencer, volte para 114. ")

    habilidade_monstro = 7
    energia_monstro = 7
    nome = "HOMEM DA CAVERNA"




    batalha(habilidade_monstro, energia_monstro, habilidade, sorte, energia, nome)


    input("\nParabens! Você venceu o Homem da Caverna!\n\nPressione Enter para voltar para 114...")
    aventura114()



def aventura388():
    print(stats_final)
    print("\nCAP 388")
    print("\nO túnel logo chega a um beco sem saída. Um pedaço de papel, escurecido e enrugado de tão velho, está pregado na parede do fundo. Se você quiser pegá-lo para ver se contém alguma mensagem, volte para 23. Se preferir apressar-se a voltar pelo túnel para reunir-se ao Bárbaro, volte para 154. ")


    escolha = input("\nIr para 23 ou 154?: ")
    match escolha:
        case '23':
            aventura23()
        case '154':
            aventura154()
        case _:
            print("\nOpção Invalida!")
            aventura388()




def aventura389():
    print(stats_final)
    print("\nCAP 389")
    print("\nSem suas armas você está mais vulnerável, e a perda da espada faz com que se sinta praticamente nu. Você perde 4 pontos de HABILIDADE. Questionando se tomou a decisão correta, você segue pelo túnel para o norte. Volte para 181. ")


    habilidade = habilidade - 4

    input("\nPressione Enter para ir para 181...")
    aventura181()


def aventura390():
    print(stats_final)
    print("\nCAP 390")
    print("\nVocê se agacha ao lado do pedestal, abaixo da linha de fogo das bestas. Estica a mão e puxa o crânio do pedestal, esperando que sua ação faça as bestas dispararem. Para sua grande surpresa, nada acontece. Some 1 ponto de SORTE. Ainda agachado, você arranca as jóias que formam os olhos do crânio. Você identifica as pedras amarelas - topázios - e as coloca na mochila. Olhando para a série de bestas, pergunta-se se ainda há uma armadilha à sua espera no aposento. Você:\n\nEngatinha para fora do aposento, levando o crânio - Volte para 15\nRecoloca o crânio no pedestal antes de engatinhar para fora do aposento? - Volte para 204")

    escolha = input("\nIr para 15 ou 204?: ")
    match escolha:
        case '15':
            aventura15()
        case '204':
            aventura204()
        case _:
            print("\nOpção Invalida!")
            aventura390()



def aventura391(energia, sorte, habilidade):
    print(stats_final)
    print("\nCAP 391")
    print("\nAinda sorrindo, o velho olha para você e diz: “Muito bem, Estranho. Você respondeu corretamente. Desejo-lhe boa sorte durante o resto da Prova dos Campeões, e, com este objetivo, aumentarei seus poderes.” Ele então murmura mais umas poucas palavras ininteligíveis, e você sente um impulso poderoso percorrer-lhe o corpo. Acrescente 1 ponto a cada um dos seus índices de HABILIDADE, ENERGIA e SORTE. Você diz adeus ao velho e sai do aposento para continuar para o norte pela passagem. Volte para 100. ")

    energia = energia + 1
    sorte = sorte + 1
    habilidade = habilidade + 1

    input("\nPressione Enter para ir para 100...")
    aventura100()


def aventura392():
    print("\nVocê só tem tempo de ouvir o Gnomo dizer: “Três crânios”, antes que um raio branco de energia seja disparado da fechadura e atinja-lhe o peito, derrubando-o sem sentidos. Jogue um dado, some 1 ao número obtido e reduza esse total da sua ENERGIA. Se ainda estiver vivo, você recupera os sentidos e ouve o Gnomo ordenar que tente de novo. Você não acertou nenhuma das gemas, por isso não tentará essa combinação de novo. \n\n   A                B             C\nESMERALDA       DIAMANTE       SAFIRA          VOLTE PARA 16\nDIAMANTE         SAFIRA       ESMERALDA        FIQUE EM 392\nSAFIRA          ESMERALDA       DIAMANTE       VOLTE PARA 177\nESMERALDA       SAFIRA       DIAMANTE          VOLTE PARA 287\nDIAMANTE       ESMERALDA       SAFIRA          VOLTE PARA 132\nSAFIRA          DIAMANTE      ESMERALDA        VOLTE PARA 249 ")
    escolha = input("Você irá para 16, 392, 177, 287, 132 ou 249?: \n")
    match escolha:
        case '16':
            aventura16()
        case '392':
            aventura392()
        case '177':
            aventura177()
        case '287':
            aventura287()
        case '132':
            aventura132()
        case '249':
            aventura249()
        case _:
            print("Opção invalida.")
            aventura287()


def aventura393():
    print(stats_final)
    print("\nCAP 393")
    print("\nVocê entra em um aposento frio, dividido por uma fenda profunda. Uma corda retesada estendida de lado a lado atravessa a fenda para o outro lado, onde um magnífico elmo alado repousa sobre um poste. Se você quiser caminhar pela corda bamba para chegar ao elmo, volte para 274. Se preferir retornar pelo túnel para continuar para o norte, volte para 291. ")


    escolha = input("\nIr para 274 ou 291?: ")
    match escolha:
        case '274':
            aventura274()
        case '291':
            aventura291()
        case _:
            print("\nOpção Invalida!")
            aventura393()


def aventura394():
    print(stats_final)
    print("\nCAP 394")
    print("\nVocê arrebenta o vidro com o cabo da espada, fazendo um buraco grande o bastante para que você passe. Imediatamente, os Insetos Gigantes saltam na sua direção. Sem perda de tempo, você entra no aposento, apanhando uma das tochas acesas para se defender. O fogo mantém a maioria dos Insetos a distância, mas, quando você consegue pegar a coroa e retornar ao corredor, certamente foi mordido por alguns deles. Jogue um dado e some 2 ao total. Este é o número de ferroadas que você recebeu, e terá que reduzir sua ENERGIA em 1 ponto para cada uma delas. Os Insetos Gigantes não vêm atrás de você, preferindo a luz brilhante do aposento em que estão. Você examina a coroa, e vê com desgosto que não é nada além de ferro pintado, e o “diamante” é vidro e não vale nada. Você a atira no chão com raiva e fica pensando aonde ir em seguida. Se quiser se dirigir para o oeste, volte para 59. Se preferir retornar ao cruzamento para continuar para o norte, volte para 14. ")

    input("\nPressione Enter para ir para 14...")
    aventura14()



def aventura395(energia):
    print(stats_final)
    print("\nCAP 395")
    print("\nAo ouvir o roído da sua bainha, um dos Trogloditas dá o alarme. Você se levanta e corre o mais rápido que pode pela caverna. Um dos arqueiros dispara uma flecha que lhe rasga o ombro com precisão mortal. Você perde 3 pontos de ENERGIA. Se ainda estiver vivo, volte para 259. ")

    energia = energia - 5
    if energia > 0:
        input("Você sobrevive, mas sai ferido. Pressione Enter para retornar para 259...")
        aventura259()
    else:
        fim_de_jogo()


def aventura396():
    print(stats_final)
    print("\nCAP 396")
    print("\nVocê faz um laço com a corda, gira-o acima de si e o lança na cabeça do ídolo, sorrindo com alegria quando ele cai em torno do pescoço da estátua. Você então aperta o nó e começa a içar-se pela corda. Logo chega ao topo, sentando-se em cima do nariz do ídolo enquanto continua a segurar a corda. Você desembainha a espada e fica pensando de que olho arrancar a jóia primeiro. Se você quiser arrancar primeiro a do olho esquerdo, volte para 151. Se preferir arrancar a do olho direito, volte para 34. ")

    escolha = input("ir para 151 ou 34?")
    match escolha:
        case '151':
            aventura151()
        case '34':
            aventura34()


def aventura397():
    print(stats_final)
    print("\nCAP 397")
    print("\nO líquido é uma poção mágica que lhe permitirá detectar armadilhas ocultas. Some 2 pontos de SORTE. Se ainda não o fez, você pode abrir o livro vermelho – volte para 52. Do contrário, você terá que continuar para o norte com Throm - volte para 369. ")

    escolha = input("\nIr para 52 ou 369?: ")
    match escolha:
        case '52':
            mochila.append("livro vermelho")
            aventura52()
        case '369':
            aventura369()
        case _:
            print("\nOpção Invalida!")
            aventura397()



def aventura398():
    print(stats_final)
    print("\nCAP 398")
    print("\nEmbora não haja qualquer armadilha evidente, você tem a forte sensação de que a arca contém um perigo oculto. A Poção de Detecção de Armadilha está funcionando bem. Você pára de um dos lados da arca e levanta a tampa com a espada, esticando o braço para mantê-la a distância. Quando a tampa se ergue, uma bola de ferro presa a um cordão é atirada para trás e quebra uma cápsula de vidro que está fixada no lado de dentro da tampa, instantaneamente liberando um gás. Felizmente, você tem tempo de pular para trás sem inalar os vapores venenosos. Quando o gás se dissipa, você caminha até a arca e olha dentro dela. Uma corrente com um pingente está jogada no fundo, mas alguém já tirou a jóia que havia nele. Você fica tão aborrecido que joga a corrente no chão e sai do aposento, furioso, para o túnel. Volte para 230. ")

    input("\nPressione Enter para ir para 230...")
    aventura230()


def aventura399():
    print(stats_final)
    print("\nCAP 399")
    print("\nO pão contém ervas curativas secretas dos elfos. Some 3 pontos de ENERGIA. Sentindo-se triste, embora forte, você guarda o espelho e o amuleto, saindo da caverna para seguir para o norte. Volte para 192. ")

    energia = energia + 3

    mochila.append('espelho')
    mochila.append('amuleto')

    
    input("\nPressione Enter para ir para 192...")
    aventura192()

def aventura400():
    print(stats_final)
    print("\nCAP 400")
    print("\nLogo que você aparece na saída do túnel, uma multidão grita e vibra. As pessoas abrem alas para que você siga na direção de um pequeno palanque, no qual, sentado embaixo de um pára- sol de bambu colorido, está o Barão Sukumvit. Ele parece apalermado, como se jamais esperasse que alguém conseguisse sair vivo do Calabouço da Morte. O segredo de Fang foi revelado. Quando o Barão se levanta da cadeira, você sobe os degraus do palanque, inclina-se diante dele e observa aqueles olhos frios fixos em você em completo espanto. Você sorri meio sem graça quando ele lhe oferece a mão estendida. Em meio ao barulho ensurdecedor da ovação do povo de Fang, o Barão Sukumvit abre o cofre que contém seu prêmio de 10.000 Peças de Ouro. Em seguida, ele coloca uma coroa de louros sobre a sua cabeça e o proclama Campeão do Calabouço da Morte. ")

    escolha_final = input("\n\nFim de jogo! Você venceu! \n\nGostaria de jogar de novo? (1. Sim - 2. Não): ").lower()
    if escolha_final == 'sim':
        char_perks()
        inicio()
        aventura1()

    else:
        ("\n\nObrigado por jogar! Até a Próxima!")
        


print("O jogo irá iniciar agora, você deseja fazer o tutorial antes? ('S' ou 'N')")
tut = input().lower()
if tut == "s":
    tutorial()

#INICIO DO JOGO

inicio()

aventura1()