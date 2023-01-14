class Simplex:

    def __init__(self):
        self.tabela = []
    
    def set_funcao_objetiva(self, fo):
        self.tabela.append(fo)

    def add_resticoes(self, sa):   
        self.tabela.append(sa)
    
    def get_coluna_entrando(self):
        coluna_pivo = min(self.tabela[0]) #Retorna o menor valor da linha da função objetiva
        index = self.tabela[0].index(coluna_pivo) # indice do menor valor
        return index

    def get_linha_sai(self, coluna_entrando):
        resultado = {}
        for linha in range(len(self.tabela)):
            if linha > 0:
                if self.tabela[linha][coluna_entrando] > 0:
                    divisao = self.tabela[linha][-1] / self.tabela[linha][coluna_entrando] #divide o ultimo elemento da linha pelo elemento pivô
                    resultado[linha] = divisao
        index = min(resultado, key=resultado.get)#Pega a linha com menor valor na divisao 
        return index

    def calcular_nova_linha_pivo(self, coluna_entrando, linha_saindo):
        linha = self.tabela[linha_saindo]
        pivo = linha[coluna_entrando]
        nova_linha_pivo = [valor / pivo for valor in linha]
        return nova_linha_pivo

    def calcular_nova_linha(self, linha, coluna_entrando, linha_pivo):
        pivo = linha[coluna_entrando] * -1
        linha_resultante = [valor * pivo for valor in linha_pivo]

        nova_linha = []
        for i in range(len(linha_resultante)):
            soma = linha_resultante[i] + linha[i]
            nova_linha.append(soma)
        return nova_linha

    def is_negativo(self):
        negativo = list(filter(lambda x: x < 0, self.tabela[0]))
        return True if len(negativo) > 0 else False

    def calcular(self):
        coluna_entrando = self.get_coluna_entrando()
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

    def imprimir_tabela(self):
        print()
        for i in range(len(self.tabela)):
            for j in range(len(self.tabela[0])):
                print(f"{self.tabela[i][j]}\t", end="")
            print()

    def resolver(self):
        self.calcular()
        while self.is_negativo():
            self.imprimir_tabela()
            self.calcular()

        self.imprimir_tabela()

def main():
    """ Um sapateiro faz 6 sapatos por hora, se fizer somente sapatos, e 5 cintos por hora, se fizer somente
        cintos. Ele gasta 2 unidades de couro para fabricar 1 unidade de sapato e 1 unidade de couro para fabricar
        uma unidade de cinto. Sabendo-se que o total disponível de couro é de 6 unidades e que o lucro unitário
        por sapato é de $5.00 e o do cinto é de $2.00, pede-se: o modelo do sistema de produção do sapateiro, se
        o objetivo é maximizar seu lucro por hora. """
    """ Max Z = 5x1 + 2x2
        Sujeito a:
            2x1 + x2 <= 6
            10x1 + 12x2 <= 60
            x1, x2 >= 0 
        
        Forma padrão
        Max Z - 5x1 - 2x2 + 0x3 + 0x4 = 0
        Sujeito a:
            2x1 + x2 + x3 = 6
            10x1 + 12x2 + x4 = 60
            x1, x2, x3, x4 >= 0
            """
    simplex = Simplex()
    simplex.set_funcao_objetiva([1,-5,-2,0,0,0])
    simplex.add_resticoes([0,2,1,1,0,6])
    simplex.add_resticoes([0,10,12,0,1,60])
    simplex.resolver()

if __name__ == '__main__':
    main()
