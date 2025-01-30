def somatorio_hash(chave):
    return sum(ord(c) for c in chave)

def hash_polinomial(chave, p=31):
    valor_hash = 0
    for i, c in enumerate(chave):
        valor_hash += ord(c) * (p ** i)
    return valor_hash

def deslocamento_critico(chave):
    valor_hash = 0
    for c in chave:
        valor_hash ^= ord(c)
        valor_hash = (valor_hash << 5) | (valor_hash >> 27)
    return valor_hash


def compressao_divisao(valor_hash, tamanho=32):
    return valor_hash % tamanho

def compressao_dobra(valor_hash, tamanho=32):
    str_hash = str(abs(valor_hash))
    partes = [int(str_hash[i:i+2]) for i in range(0, len(str_hash), 2)]
    return sum(partes) % tamanho

def compressao_mad(valor_hash, tamanho=32, a=31, b=7, p=100003):
    return ((a * valor_hash + b) % p) % tamanho


def testar_hash(strings, funcao_hash, funcao_compressao, tamanho=32):
    tabela = [None] * tamanho
    colisões = 0

    for s in strings:
        valor_hash = funcao_hash(s)
        indice = funcao_compressao(valor_hash, tamanho)
        
        if tabela[indice] is not None:
            colisões += 1
        tabela[indice] = s
    
    return colisões, tabela


strings_teste = ["apple", "voadora", "banjo", "banana", "cherry", "date",
                 "elderberry", "fig", "grape", "honeydew", "kiwi", "xuru", "runin", "xamã",
                 "mirtilho", "lemon", "mango", "nectarine", "orange", "papaya", "quince",
                 "raspberry", "strawberry", "tangerine", "ugli", "voavanga", "maravilha",
                 "IFCE", "maracanaú", "ceará", "manga", "rendemption", "bobo", "maluco"]

metodos_distribuicao = {
    "Somatório": somatorio_hash,
    "Polinomial": hash_polinomial,
    "Deslocamento Crítico": deslocamento_critico
}

metodos_compressao = {
    "Divisão": compressao_divisao,
    "Dobra": compressao_dobra,
    "MAD": compressao_mad
}


resultados = {}
for nome_disp, funcao_disp in metodos_distribuicao.items():
    for nome_comp, funcao_comp in metodos_compressao.items():
        colisões, tabela = testar_hash(strings_teste, funcao_disp, funcao_comp)
        resultados[(nome_disp, nome_comp)] = colisões
        print(f"{nome_disp} + {nome_comp}: {colisões} colisões")
        print("Tabela Hash Resultante:")
        for i, valor in enumerate(tabela):
            print(f"{i}: {valor}")
        print("-" * 50)

melhor_metodo = min(resultados, key=resultados.get)
print(f"O melhor método foi: {melhor_metodo[0]} + {melhor_metodo[1]} com {resultados[melhor_metodo]} colisões")
