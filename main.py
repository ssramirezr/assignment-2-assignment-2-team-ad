def cky(gramatica, terminales, cadena):
    
    n = len(cadena)
    tabla = [[set() for j in range(n + 1)] for i in range(n)]

    for i in range(n):
        for produccion, no_terminales in gramatica.items():
            if cadena[i] in produccion:
                tabla[i][i+1].update(no_terminales)

    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l
            for k in range(i + 1, j):
                for B in tabla[i][k]:
                    for C in tabla[k][j]:
                        BC = B + C
                        if BC in gramatica:
                            tabla[i][j].update(gramatica[BC])

    return 'S' in tabla[0][n]  

def main():
    
    numCasos = int(input())  
    resultados = []

    for _ in range(numCasos):
        k, m = map(int, input().split())  
        gramatica = {}  
        terminales = []

        for _ in range(k):
            entrada = input().split()
            no_terminal = entrada[0]
            producciones = entrada[1:]

            for produccion in producciones:
                if produccion not in gramatica:
                    gramatica[produccion] = []
                gramatica[produccion].append(no_terminal)

                if produccion.islower(): 
                    terminales.append(produccion)

       
        cadenas = [input() for _ in range(m)]  

        for cadena in cadenas:
            resultado = cky(gramatica, terminales, cadena)
            resultados.append(resultado)

    for resultado in resultados:
        if resultado:
            print('yes')
        else:
            print('no')

#----[MAIN]----
if __name__ == '__main__':
    main()
