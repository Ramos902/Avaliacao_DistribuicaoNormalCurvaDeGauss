import csv
import math
import matplotlib.pyplot as plt


# Parte B - Leitura dos dados do CSV
def carregar_dados(caminho_arquivo, coluna="math score"):
    notas = []
    invalidos = 0
    total_linhas = 0

    with open(caminho_arquivo, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            total_linhas += 1
            valor = linha.get(coluna, "").strip()

            if valor == "":
                invalidos += 1
                continue

            try:
                notas.append(int(valor))
            except ValueError:
                invalidos += 1

    return notas, total_linhas, invalidos


# Parte C - Calculo das medidas estatisticas na mao
def calcular_media(dados):
    return sum(dados) / len(dados)


def calcular_mediana(dados):
    ordenados = sorted(dados)
    n = len(ordenados)
    meio = n // 2

    if n % 2 == 1:
        return float(ordenados[meio])
    return (ordenados[meio - 1] + ordenados[meio]) / 2.0


def calcular_modas(dados):
    contagem = {}
    for x in dados:
        contagem[x] = contagem.get(x, 0) + 1

    maior_freq = max(contagem.values())
    modas = [k for k, v in contagem.items() if v == maior_freq]
    return sorted(modas), maior_freq


def calcular_variancia_amostral(dados, media):
    n = len(dados)
    soma_quadrados = sum((x - media) ** 2 for x in dados)
    return soma_quadrados / (n - 1)


def calcular_desvio_padrao_amostral(variancia):
    return math.sqrt(variancia)


def calcular_assimetria(dados, media, desvio_padrao):
    n = len(dados)
    soma_cubos = sum(((x - media) / desvio_padrao) ** 3 for x in dados)
    return (n / ((n - 1) * (n - 2))) * soma_cubos


# Parte D - Regra 68-95-99,7
def verificar_regra_empirica(dados, media, desvio_padrao):
    n = len(dados)
    resultados = {}

    for k in (1, 2, 3):
        lim_inf = media - k * desvio_padrao
        lim_sup = media + k * desvio_padrao
        qtd = sum(1 for x in dados if lim_inf <= x <= lim_sup)
        perc = (qtd / n) * 100
        resultados[k] = (lim_inf, lim_sup, qtd, perc)

    return resultados


# Parte E - Escore z e busca por valores atipicos (|z| > 3)
def calcular_escore_z(x, media, desvio_padrao):
    return (x - media) / desvio_padrao


def buscar_atipicos(dados, media, desvio_padrao):
    atipicos = []
    for x in dados:
        z = calcular_escore_z(x, media, desvio_padrao)
        if abs(z) > 3:
            atipicos.append((x, z))
    return atipicos


# Parte F - Grafico com histograma, curva normal e boxplot
def densidade_normal(x, media, desvio_padrao):
    parte1 = 1.0 / (desvio_padrao * math.sqrt(2.0 * math.pi))
    expoente = -((x - media) ** 2) / (2.0 * (desvio_padrao ** 2))
    return parte1 * math.exp(expoente)


def gerar_graficos(dados, media, desvio_padrao, caminho_saida="histograma_curva_normal.png"):
    fig, (ax_hist, ax_box) = plt.subplots(
        2, 1, figsize=(10, 7), gridspec_kw={"height_ratios": [3, 1]}, sharex=True
    )

    # Histograma das notas
    ax_hist.hist(
        dados,
        bins=20,
        density=True,
        color="#5B9BD5",
        edgecolor="black",
        alpha=0.7,
        label="Histograma (math score)",
    )

    # Curva normal teorica
    x_min, x_max = min(dados), max(dados)
    passo = (x_max - x_min) / 300.0
    eixo_x = [x_min + i * passo for i in range(301)]
    eixo_y = [densidade_normal(x, media, desvio_padrao) for x in eixo_x]

    ax_hist.plot(eixo_x, eixo_y, color="#C00000", linewidth=2, label="Curva Normal Teorica")

    # Linhas da media e de 1 desvio-padrao
    ax_hist.axvline(media, color="#2E75B6", linestyle="-", linewidth=2, label=f"Media ({media:.2f})")
    ax_hist.axvline(
        media - desvio_padrao,
        color="#ED7D31",
        linestyle="--",
        linewidth=1.8,
        label=f"-1 Desvio-Padrao ({media - desvio_padrao:.2f})",
    )
    ax_hist.axvline(
        media + desvio_padrao,
        color="#ED7D31",
        linestyle="--",
        linewidth=1.8,
        label=f"+1 Desvio-Padrao ({media + desvio_padrao:.2f})",
    )

    ax_hist.set_title("Distribuicao das Notas de Matematica e Curva de Gauss")
    ax_hist.set_ylabel("Densidade")
    ax_hist.legend(loc="upper left")
    ax_hist.grid(axis="y", linestyle=":", alpha=0.6)

    # Boxplot na parte de baixo
    ax_box.boxplot(
        dados,
        orientation="horizontal",
        patch_artist=True,
        boxprops=dict(facecolor="#5B9BD5", alpha=0.7),
        medianprops=dict(color="#C00000", linewidth=2),
    )
    ax_box.set_xlabel("Nota de Matematica (math score)")
    ax_box.set_yticks([])
    ax_box.set_title("Grafico de Caixa (Boxplot)")
    ax_box.grid(axis="x", linestyle=":", alpha=0.6)

    plt.tight_layout()
    plt.savefig(caminho_saida, dpi=300)
    plt.close()


def main():
    arquivo_csv = "StudentsPerformance.csv"

    # Parte B
    notas, total_lidos, invalidos = carregar_dados(arquivo_csv, "math score")
    print("--- PARTE B: Leitura dos dados ---")
    print(f"Total de linhas no CSV: {total_lidos}")
    print(f"Notas validas carregadas: {len(notas)}")
    print(f"Valores ausentes ou invalidos: {invalidos}\n")

    # Parte C
    qtd = len(notas)
    menor = min(notas)
    maior = max(notas)
    amplitude = maior - menor
    media = calcular_media(notas)
    mediana = calcular_mediana(notas)
    modas, freq_moda = calcular_modas(notas)
    variancia = calcular_variancia_amostral(notas, media)
    desvio = calcular_desvio_padrao_amostral(variancia)
    assimetria = calcular_assimetria(notas, media, desvio)

    print("--- PARTE C: Medidas estatisticas ---")
    print(f"Quantidade de dados: {qtd}")
    print(f"Menor nota: {menor}")
    print(f"Maior nota: {maior}")
    print(f"Amplitude total: {amplitude}")
    print(f"Media: {media:.4f}")
    print(f"Mediana: {mediana:.2f}")
    print(f"Moda: {modas} (aparece {freq_moda} vezes)")
    print(f"Variancia amostral: {variancia:.4f}")
    print(f"Desvio-padrao amostral: {desvio:.4f}")
    print(f"Coeficiente de assimetria: {assimetria:.4f}\n")

    # Parte D
    regra = verificar_regra_empirica(notas, media, desvio)
    esperados = {1: 68.0, 2: 95.0, 3: 99.7}

    print("--- PARTE D: Regra 68-95-99,7 ---")
    for k, (lim_inf, lim_sup, cont, perc) in regra.items():
        print(
            f"Intervalo de {k} desvio(s) [{lim_inf:.2f} a {lim_sup:.2f}]: "
            f"{cont} notas ({perc:.2f}%) - esperado: ~{esperados[k]}%"
        )
    print()

    # Parte E
    notas_teste = [
        ("Menor nota", menor),
        ("Maior nota", maior),
        ("Nota 50", 50),
        ("Nota 75", 75),
        ("Nota 90", 90),
    ]

    print("--- PARTE E: Escores z ---")
    for nome, valor in notas_teste:
        z = calcular_escore_z(valor, media, desvio)
        tipo = "Atipico" if abs(z) > 3 else "Normal"
        print(f"{nome} ({valor}): z = {z:.4f} ({tipo})")

    atipicos = buscar_atipicos(notas, media, desvio)
    print("\nNotas com |z| > 3 em toda a base:")
    for val, z_val in atipicos:
        print(f"  Nota {val} -> z = {z_val:.4f}")

    # Parte F
    gerar_graficos(notas, media, desvio, "histograma_curva_normal.png")
    print("\n--- PARTE F: Grafico ---")
    print("Arquivo salvo como: histograma_curva_normal.png")


if __name__ == "__main__":
    main()
