# -*- coding: utf-8 -*-
class Simplex:

    def __init__(self):
        self.tabela = []                                            # Declaração da variavel tabela
    
    def set_funcao_objetiva(self, fo):
        self.tabela.append(fo)                                      # Adiciona a linha da função objetivo na tabela

    def add_resticoes(self, sa):   
        self.tabela.append(sa)                                      # Adiciona a linha da restrição na tabela
    
    def get_coluna_entrando(self):
        coluna_pivo = min(self.tabela[0][1:])                       # Calcula o menor valor na função objetivo
        index = self.tabela[0].index(coluna_pivo)                   # Indice do menor valor
        return index                                                # Retorna o indice

    def get_linha_sai(self, coluna_entrando):
        resultado = {}                                              # Cria um dicionario vazio
        for linha in range(len(self.tabela)):                       # Percorre cada linha da tabela
            if linha > 0:                                           # Se o indice linha for maior que 0, ou seja, não ser a linha da função objeivo
                if self.tabela[linha][coluna_entrando] > 0:        # Se o valor dessa posição for maior que 0
                    divisao = self.tabela[linha][-1] / self.tabela[linha][coluna_entrando] #divide o ultimo elemento da linha pelo elemento pivô
                    resultado[linha] = divisao
        index = min(resultado, key=resultado.get)                   # Pega o indice da linha com menor valor positivo na divisao 
        return index                                                # Retorna o indice
        
               
    def calcular_nova_linha_pivo(self, coluna_entrando, linha_saindo):
        linha = self.tabela[linha_saindo]                           # Linha que sai da tabela
        pivo = linha[coluna_entrando]                               # Linha pivô
        nova_linha_pivo = [valor / pivo for valor in linha]         # Para cada valor na linha, divide pelo valor na linha pivô e salva na nova linha pivô
        return nova_linha_pivo                                      # Retorna a nova linha pivô

    def calcular_nova_linha(self, linha, coluna_entrando, linha_pivo):
        pivo = linha[coluna_entrando]  * -1                         # Inverte o sinal do valor pivô da nova linha
        linha_resultante = [valor * pivo for valor in linha_pivo]   # Multiplica cada elemento na linha pelo pivô

        nova_linha = []                                             # Cria uma nova linha vazia
        for i in range(len(linha_resultante)):                      # Para cada valor da linha resultante
            soma = linha_resultante[i] + linha[i]                   # Soma com o valor na linha anterior (Ex:l0=l0anterior-(X)*pivô)
            nova_linha.append(soma)                                 # Adiciona essa soma a nova linha
        return nova_linha                                           # Retorna a nova linha

    def is_negativo(self):                                          # Método para verificar se ha valor negativo
        return any(item < 0 for item in self.tabela[0][1:])

    def calcular(self):
        coluna_entrando = self.get_coluna_entrando()                # Chama o método para calcular a coluna que entra
        primeira_linha_sai = self.get_linha_sai(coluna_entrando)    # Chama o método para calcular a linha que sai

        linha_pivo = self.calcular_nova_linha_pivo(coluna_entrando, primeira_linha_sai) # Chama o método para calcular a linha pivô
        self.tabela[primeira_linha_sai] = linha_pivo                # Adiciona a linha pivô na tabela
        copia_tabela = self.tabela.copy()                           # Cria uma copia da tabela

        index = 0
        while index < len(self.tabela):                             # Laço para percorrer toda a tabela
            if index != primeira_linha_sai:                         # Se a linha não for a pivô
                linha = copia_tabela[index]                         # Linha recebe linha pivô
                nova_linha = self.calcular_nova_linha(linha,coluna_entrando, linha_pivo) # Calcula nova linha
                self.tabela[index] = nova_linha                     # Adiciona a nova linha na tabela
            index += 1

    def imprimir_tabela(self):                                      # Método para mostrar a tabela no console de execução
        print()
        print('--------------------------------------------------')
        for i in range(len(self.tabela)):
            for j in range(len(self.tabela[0])):
                print(f"{self.tabela[i][j]:.2f}\t", end="")
            print()
        print('--------------------------------------------------')

    def resolver(self):                                             # Método que resolve o simplex
        self.calcular()                                             # Faz o primeiro cálculo
        while self.is_negativo():                                   # Se existir elementos negativos na linha 
            self.imprimir_tabela()                                  # Chama o método que mostra a tabela
            self.calcular()                                         # Calcula novamente              
        self.imprimir_tabela()                                      # Chama o método que mostra a tabela                            
    
    def get_coluna_entrando_min(self):
        coluna_pivo = max(self.tabela[0])                           # Calcula o maior valor positivo na função objetivo
        index = self.tabela[0].index(coluna_pivo)                   # Indice do maior valor
        return index
       
    def calcular_min(self):
        coluna_entrando = self.get_coluna_entrando_min()                
        primeira_linha_sai = self.get_linha_sai(coluna_entrando)    

        linha_pivo = self.calcular_nova_linha_pivo(coluna_entrando, primeira_linha_sai) 
        self.tabela[primeira_linha_sai] = linha_pivo                
        copia_tabela = self.tabela.copy()
        
        index = 0
        while index < len(self.tabela):                             
            if index != primeira_linha_sai:                       
                linha = copia_tabela[index]                       
                nova_linha = self.calcular_nova_linha(linha,coluna_entrando, linha_pivo) 
                self.tabela[index] = nova_linha                     
            index += 1
            
    def is_positivo(self):                                          
        return any(item > 0 for item in self.tabela[0])
     
    def resolver_min(self):
        
        self.tabela[0][0] = -1
        self.calcular_min()
        while self.is_positivo():
            self.imprimir_tabela() 
            self.calcular_min()
            
        self.tabela[0][0] = 1
        self.imprimir_tabela()
        
                    
                    
def main():
   
    simplex = Simplex()                                             
    simplex.set_funcao_objetiva([1,2,-1,1,0,0,0,0])
    simplex.add_resticoes([0,3,1,1,1,0,0,60])
    simplex.add_resticoes([0,1,-1,2,0,1,0,10])
    simplex.add_resticoes([0,1,1,-1,0,0,1,20])                     
    simplex.imprimir_tabela()
    simplex.resolver_min()                                              

if __name__ == '__main__':
    main()
