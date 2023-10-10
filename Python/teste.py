habilidade = 25


def alterar_habilidade(habilidade, valor):
    habilidade += valor
    return habilidade

def aventura72(habilidade):
    print("CAP 72\n")
    print("\nO Espelho se quebra, lançando fragmentos de vidro por toda parte. As quatro faces do Demônio do Espelho gritam de agonia, e aparecem rachaduras em todas elas. Em seguida, elas também se partem e caem ao chão numa pilha de cacos de vidro. Infelizmente ao quebrar o espelho, você cortou seriamente o braço com que segura a espada. Embora sua força não tenha sido afetada, sua habilidade com as armas foi prejudicada. Você perde 2 pontos de HABILIDADE antes de continuar na sua jornada para o norte. Vá para 122 ")


    nova_habilidade = alterar_habilidade(habilidade, -2)

    print(habilidade)
    print(nova_habilidade)


aventura72(habilidade)