tabuleiro = [
                ['a','b','c'],
                ['d','e','f'],
                ['g','h','i']
]


#print(tabuleiro[0][0])
#print(tabuleiro[0][1])
#print(tabuleiro[0][2])

#print(tabuleiro[1][0])
#print(tabuleiro[1][1])
#print(tabuleiro[1][2])

#print(tabuleiro[2][0])
#print(tabuleiro[2][1])
#print(tabuleiro[2][2])



jogadas = 0
vez_jogador = 'X'


def apresentaTabuleiro():  # def 'forma de dizer que isso é uma função' (Define uma função)
                           # estrutura necessaria para a criação de uma função
    print(tabuleiro[0])
    print(tabuleiro[1])
    print(tabuleiro[2])
    
def checkVencedor():
    #linha
    for linha in range(3):
        concatLinha = tabuleiro[linha][0] + tabuleiro[linha][1] + tabuleiro[linha][2]
        if concatLinha == "XXX" or concatLinha == '000':
            print('temos um vencedor!')
    #coluna    
    for coluna in range(3):
        concatLinha = tabuleiro[0][coluna] + tabuleiro[1][coluna] + tabuleiro[2][coluna]
        if concatLinha == "XXX" or concatLinha == '000':
            print('temos um vencedor!') 
    
    #diagonal
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] or \
       tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0]:
           print('temos um vencedor!')
        
while jogadas < 9:
    print(f'rodada {jogadas}')
    posicao = input('Inserir a posição desejada:')
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == posicao:
                tabuleiro[linha][coluna] = vez_jogador
                jogadas = jogadas + 1 # jogada realizada
                vez_jogador = '0' if vez_jogador == 'X' else 'X' #altera o jogador
    
    checkVencedor()      
    apresentaTabuleiro()














# posicao = input('Inserir a posição desejada: ')

# if tabuleiro[0][0] == posicao:
#     tabuleiro[0][0] = vez_jogador
# elif tabuleiro[0][1] == posicao:
#      tabuleiro[0][1] = vez_jogador
# elif tabuleiro[0][2] == posicao:
#      tabuleiro[0][2] = vez_jogador
# elif tabuleiro[1][0] == posicao:
#      tabuleiro[1][0] = vez_jogador
# elif tabuleiro[1][1] == posicao:
#      tabuleiro[1][1] = vez_jogador
# elif tabuleiro[1][2] == posicao:
#      tabuleiro[1][2] = vez_jogador
# elif tabuleiro[2][0] == posicao:
#      tabuleiro[2][0] = vez_jogador
# elif tabuleiro[2][1] == posicao:
#      tabuleiro[2][1] = vez_jogador
# elif tabuleiro[2][2] == posicao:
#      tabuleiro[2][2] = vez_jogador
# #array[linha][coluna]

