import csv
import math
import matplotlib.pyplot as plt


# ==============================================================================
# PARTE B — Leitura e organização dos dados
# ==============================================================================
def carregar_dados(caminho_arquivo, coluna="math score"):
    """
    Lê o arquivo CSV usando csv.DictReader, verifica valores ausentes ou
    inválidos e retorna a lista de notas convertidas para inteiros.
    """
    notas = []
    ausentes_ou_invalidos = 0
    total_linhas = 0

    with open(caminho_arquivo, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            total_linhas += 1
            valor = linha.get(coluna, "").strip()

            if valor == "":
                ausentes_ou_invalidos += 1
                continue

            try:
                nota = int(valor)
                notas.append(nota)
            except ValueError:
                ausentes_ou_invalidos += 1

    return notas, total_linhas, ausentes_ou_invalidos


# ==============================================================================
# PARTE C — Medidas estatísticas (sem bibliotecas estatísticas)
# ==============================================================================
def calcular_media(dados):
    return sum(dados) / len(dados)


def calcular_mediana(dados):
    dados_ordenados = sorted(dados)
    n = len(dados_ordenados)
    meio = n // 2

    if n % 2 == 1:
        return float(dados_ordenados[meio])
    else:
        return (dados_ordenados[meio - 1] + dados_ordenados[meio]) / 2.0


def calcular_modas(dados):
    frequencias = {}
    for valor in dados:
        frequencias[valor] = frequencias.get(valor, 0) + 1

    maior_freq = max(frequencias.values())
    modas = [k for k, v in frequencias.items() if v == maior_freq]
    return sorted(modas), maior_freq


def calcular_variancia_amostral(dados, media):
    n = len(dados)
    soma_quadrados = sum((x - media) ** 2 for x in dados)
    return soma_quadrados / (n - 1)


def calcular_desvio_padrao_amostral(variancia):
    return math.sqrt(variancia)


def calcular_assimetria(dados, media, desvio_padrao):
    """
    Calcula o coeficiente de assimetria amostral (momento de Fisher-Pearson):
    g1 = [n / ((n - 1)(n - 2))] * soma(((x_i - media) / s)^3)
    """
    n = len(dados)
    soma_cubos = sum(((x - media) / desvio_padrao) ** 3 for x in dados)
    return (n / ((n - 1) * (n - 2))) * soma_cubos


# ==============================================================================
# PARTE D — Regra empírica 68–95–99,7
# ==============================================================================
def verificar_regra_empirica(dados, media, desvio_padrao):
    n = len(dados)
    resultados = {}

    for k in (1, 2, 3):
        limite_inf = media - k * desvio_padrao
        limite_sup = media + k * desvio_padrao
        quantidade = sum(1 for x in dados if limite_inf <= x <= limite_sup)
        percentual = (quantidade / n) * 100
        resultados[k] = (limite_inf, limite_sup, quantidade, percentual)

    return resultados


# ==============================================================================
# PARTE E — Escores padronizados (Z-score) e valores atípicos
# ==============================================================================
def calcular_escore_z(x, media, desvio_padrao):
    return (x - media) / desvio_padrao


def identificar_atipicos(dados, media, desvio_padrao):
    """Retorna os valores da base que possuem |z| > 3."""
    atipicos = []
    for x in dados:
        z = calcular_escore_z(x, media, desvio_padrao)
        if abs(z) > 3:
            atipicos.append((x, z))
    return atipicos


# ==============================================================================
# PARTE F — Representação gráfica
# ==============================================================================
def densidade_normal(x, media, desvio_padrao):
    """Função densidade de probabilidade da distribuição normal."""
    coeficiente = 1.0 / (desvio_padrao * math.sqrt(2.0 * math.pi))
    expoente = -((x - media) ** 2) / (2.0 * (desvio_padrao ** 2))
    return coeficiente * math.exp(expoente)


def gerar_graficos(dados, media, desvio_padrao, caminho_saida="histograma_curva_normal.png"):
    fig, (ax_hist, ax_box) = plt.subplots(
        2, 1, figsize=(10, 7), gridspec_kw={"height_ratios": [3, 1]}, sharex=True
    )

    # 1. Histograma das notas (normalizado com density=True para sobrepor a curva)
    ax_hist.hist(
        dados,
        bins=20,
        density=True,
        color="#5B9BD5",
        edgecolor="black",
        alpha=0.7,
        label="Histograma (math score)",
    )

    # 2. Curva normal teórica sobreposta ao histograma
    x_min, x_max = min(dados), max(dados)
    passo = (x_max - x_min) / 300.0
    valores_x = [x_min + i * passo for i in range(301)]
    valores_y = [densidade_normal(x, media, desvio_padrao) for x in valores_x]

    ax_hist.plot(
        valores_x,
        valores_y,
        color="#C00000",
        linewidth=2.2,
        label="Curva Normal Teórica",
    )

    # 3. Linha vertical indicando a média
    ax_hist.axvline(
        media,
        color="#2E75B6",
        linestyle="-",
        linewidth=2,
        label=f"Média ({media:.2f})",
    )

    # 4. Linhas verticais indicando 1 desvio-padrão abaixo e acima da média
    ax_hist.axvline(
        media - desvio_padrao,
        color="#ED7D31",
        linestyle="--",
        linewidth=1.8,
        label=f"-1 Desvio-Padrão ({media - desvio_padrao:.2f})",
    )
    ax_hist.axvline(
        media + desvio_padrao,
        color="#ED7D31",
        linestyle="--",
        linewidth=1.8,
        label=f"+1 Desvio-Padrão ({media + desvio_padrao:.2f})",
    )

    ax_hist.set_title("Distribuição das Notas de Matemática e Curva de Gauss", fontsize=13)
    ax_hist.set_ylabel("Densidade", fontsize=11)
    ax_hist.legend(loc="upper left", fontsize=9)
    ax_hist.grid(axis="y", linestyle=":", alpha=0.6)

    # 5. Gráfico de caixa (Boxplot)
    ax_box.boxplot(
        dados,
        orientation="horizontal",
        patch_artist=True,
        boxprops=dict(facecolor="#5B9BD5", alpha=0.7),
        medianprops=dict(color="#C00000", linewidth=2),
    )
    ax_box.set_xlabel("Nota de Matemática (math score)", fontsize=11)
    ax_box.set_yticks([])
    ax_box.set_title("Gráfico de Caixa (Boxplot)", fontsize=11)
    ax_box.grid(axis="x", linestyle=":", alpha=0.6)

    plt.tight_layout()
    plt.savefig(caminho_saida, dpi=300)
    plt.close()


# ==============================================================================
# EXECUÇÃO PRINCIPAL E EXIBIÇÃO DOS RESULTADOS
# ==============================================================================
def main():
    arquivo_csv = "StudentsPerformance.csv"

    # Parte B
    notas, total_lidos, invalidos = carregar_dados(arquivo_csv, "math score")
    print("=" * 65)
    print("PARTE B — LEITURA E ORGANIZAÇÃO DOS DADOS")
    print("=" * 65)
    print(f"Total de registros lidos no CSV : {total_lidos}")
    print(f"Registros válidos carregados    : {len(notas)}")
    print(f"Valores ausentes ou inválidos   : {invalidos}")

    # Parte C
    qtd = len(notas)
    menor_nota = min(notas)
    maior_nota = max(notas)
    amplitude = maior_nota - menor_nota
    media = calcular_media(notas)
    mediana = calcular_mediana(notas)
    modas, freq_moda = calcular_modas(notas)
    variancia = calcular_variancia_amostral(notas, media)
    desvio_padrao = calcular_desvio_padrao_amostral(variancia)
    assimetria = calcular_assimetria(notas, media, desvio_padrao)
    assimetria_pearson = (3 * (media - mediana)) / desvio_padrao

    print("\n" + "=" * 65)
    print("PARTE C — MEDIDAS ESTATÍSTICAS (math score)")
    print("=" * 65)
    print(f"1. Quantidade de dados          : {qtd}")
    print(f"2. Menor nota                   : {menor_nota}")
    print(f"3. Maior nota                   : {maior_nota}")
    print(f"4. Amplitude total              : {amplitude}")
    print(f"5. Média aritmética (x̄)         : {media:.4f}")
    print(f"6. Mediana                      : {mediana:.2f}")
    print(f"7. Moda(s)                      : {modas} (frequência: {freq_moda})")
    print(f"8. Variância amostral (s²)      : {variancia:.4f}")
    print(f"9. Desvio-padrão amostral (s)   : {desvio_padrao:.4f}")
    print(f"10. Coeficiente de assimetria   : {assimetria:.4f} (Pearson: {assimetria_pearson:.4f})")

    # Parte D
    regra = verificar_regra_empirica(notas, media, desvio_padrao)
    esperados = {1: 68.0, 2: 95.0, 3: 99.7}

    print("\n" + "=" * 65)
    print("PARTE D — REGRA EMPÍRICA 68–95–99,7")
    print("=" * 65)
    for k, (lim_inf, lim_sup, cont, perc) in regra.items():
        print(
            f"Entre x̄ - {k}s e x̄ + {k}s [{lim_inf:6.2f}, {lim_sup:6.2f}]: "
            f"{cont:4d} notas ({perc:6.2f}%) | Esperado: ~{esperados[k]}%"
        )

    # Parte E
    notas_teste = [
        ("Menor nota", menor_nota),
        ("Maior nota", maior_nota),
        ("Nota 50", 50),
        ("Nota 75", 75),
        ("Nota 90", 90),
    ]

    print("\n" + "=" * 65)
    print("PARTE E — ESCORES PADRONIZADOS (Z-SCORE)")
    print("=" * 65)
    for descricao, valor in notas_teste:
        z = calcular_escore_z(valor, media, desvio_padrao)
        status = "ATÍPICO (|z| > 3)" if abs(z) > 3 else "Normal (|z| <= 3)"
        print(f"{descricao:12s} (x = {valor:3d}) -> z = {z:7.4f}  [{status}]")

    atipicos = identificar_atipicos(notas, media, desvio_padrao)
    print("\nValores atípicos encontrados em toda a base (|z| > 3):")
    if atipicos:
        for val, z_val in atipicos:
            print(f"  Nota = {val:3d} | z = {z_val:.4f}")
    else:
        print("  Nenhum valor atípico encontrado.")

    # Parte F
    caminho_grafico = "histograma_curva_normal.png"
    gerar_graficos(notas, media, desvio_padrao, caminho_grafico)
    print("\n" + "=" * 65)
    print("PARTE F — REPRESENTAÇÃO GRÁFICA")
    print("=" * 65)
    print(f"Gráfico gerado e salvo em: '{caminho_grafico}'")
    print("=" * 65)


if __name__ == "__main__":
    main()
