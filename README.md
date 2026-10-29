# Análise da Distribuição Normal e Curva de Gauss

Projeto desenvolvido para a disciplina de **Probabilidade e Estatística Aplicada**, com o objetivo de carregar dados reais a partir de um arquivo CSV, calcular medidas estatísticas manualmente em Python (sem uso de bibliotecas estatísticas prontas), verificar a Regra Empírica 68–95–99,7, calcular escores padronizados ($z$) e avaliar visualmente e analiticamente se as notas seguem uma Distribuição Normal (Curva de Gauss).

---

## Autores

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/Ramos902">
        <img src="https://github.com/Ramos902.png" width="100px;" alt="Foto de João Pedro Ramos"/><br />
        <sub><b>João Pedro Ramos</b></sub>
      </a><br />
      <sub><a href="https://github.com/Ramos902">@Ramos902</a></sub>
    </td>
    <td align="center">
      <img src="https://ui-avatars.com/api/?name=Gabriel+Leme&size=100&background=2E75B6&color=fff&bold=true" width="100px;" alt="Avatar de Gabriel Leme"/><br />
      <sub><b>Gabriel Leme</b></sub><br />
      <sub>Coautor</sub>
    </td>
  </tr>
</table>

---

## 1. Sobre o Projeto e Base de Dados

A análise utiliza o conjunto de dados público [**Students Performance in Exams**](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams) (`StudentsPerformance.csv`), composto por **1.000 registros** e **8 colunas** com informações demográficas e notas escolares em três disciplinas:
- `math score` *(variável quantitativa principal analisada neste estudo)*
- `reading score`
- `writing score`

### Restrições Técnicas Respeitadas
Todos os algoritmos de cálculo estatístico foram implementados manualmente em Python puro, **sem** utilizar funções prontas de bibliotecas como `statistics`, `scipy.stats`, `numpy` ou `pandas`. Foram utilizados apenas os módulos permitidos:
- `csv` (leitura estruturada com `csv.DictReader`)
- `math` (operações matemáticas elementares como `sqrt`, `exp` e `pi`)
- `matplotlib` (construção do histograma, curva normal teórica e *boxplot*)

---

## 2. Estrutura de Arquivos

```text
Avaliacao_DistribuicaoNormalCurvaDeGauss/
├── analise_distribuicao_normal.py   # Script principal com todos os cálculos e geração do gráfico
├── StudentsPerformance.csv          # Base de dados bruta (1.000 estudantes)
├── histograma_curva_normal.png      # Gráfico gerado (Histograma + Curva de Gauss + Boxplot)
├── relatorio.md                     # Relatório completo em formato Markdown
├── relatorio.pdf                    # Relatório final diagramado em PDF para entrega
└── README.md                        # Documentação geral do projeto
```

---

## 3. Fundamentação Teórica e Fórmulas Utilizadas

A **Distribuição Normal** (ou **Curva de Gauss**) é uma distribuição de probabilidade contínua, unimodal e simétrica em formato de sino, inteiramente caracterizada por dois parâmetros: a **média** ($\mu$ ou $\bar{x}$), que centraliza a curva, e o **desvio-padrão** ($\sigma$ ou $s$), que define sua dispersão.

1. **Função Densidade de Probabilidade da Normal:**
   $$f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}$$

2. **Desvio-Padrão Amostral ($s$):**
   $$s = \sqrt{\frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n - 1}}$$

3. **Escore Padronizado ($z$-score):**
   $$z = \frac{x - \bar{x}}{s}$$
   Mede quantos desvios-padrão uma observação $x$ se afasta da média $\bar{x}$. Valores com $|z| > 3$ são classificados como possíveis valores atípicos (*outliers*).

---

## 4. Resultados Obtidos (`math score`)

### Parte B — Leitura e Validação dos Dados
- **Registros lidos no CSV:** `1000`
- **Registros válidos convertidos para `int`:** `1000`
- **Valores ausentes ou inválidos:** `0`

### Parte C — Medidas Estatísticas Descritivas

| Medida Estatística | Valor Calculado |
| :--- | :--- |
| **1. Quantidade de dados ($n$)** | `1000` |
| **2. Menor nota** | `0` |
| **3. Maior nota** | `100` |
| **4. Amplitude total** | `100` |
| **5. Média aritmética ($\bar{x}$)** | `66.0890` |
| **6. Mediana** | `66.00` |
| **7. Moda** | `65` (frequência: `36` alunos) |
| **8. Variância amostral ($s^2$)** | `229.9190` |
| **9. Desvio-padrão amostral ($s$)** | `15.1631` |
| **10. Coeficiente de assimetria** | `-0.2789` (leve assimetria à esquerda) |

### Parte D — Regra Empírica 68–95–99,7

| Intervalo | Limites Calculados | Quantidade de Notas | Percentual Observado | Esperado (Teórico) |
| :--- | :--- | :--- | :--- | :--- |
| $\bar{x} \pm 1s$ | $[50,93;\; 81,25]$ | `696` | **69,60%** | $\approx 68,0\%$ |
| $\bar{x} \pm 2s$ | $[35,76;\; 96,42]$ | `954` | **95,40%** | $\approx 95,0\%$ |
| $\bar{x} \pm 3s$ | $[20,60;\; 111,58]$ | `996` | **99,60%** | $\approx 99,7\%$ |

### Parte E — Escores Padronizados ($z$) e Valores Atípicos

| Nota Analisada | Valor ($x$) | Escore $z$ | Classificação ($\|z\| > 3$) |
| :--- | :--- | :--- | :--- |
| **Menor nota** | `0` | `-4.3585` | **Atípico** ($\|z\| > 3$) |
| **Maior nota** | `100` | `+2.2364` | Normal ($\|z\| \le 3$) |
| **Nota 50** | `50` | `-1.0611` | Normal ($\|z\| \le 3$) |
| **Nota 75** | `75` | `+0.5877` | Normal ($\|z\| \le 3$) |
| **Nota 90** | `90` | `+1.5769` | Normal ($\|z\| \le 3$) |

Em toda a base de `1.000` estudantes, foram identificadas **4 notas atípicas** ($|z| > 3$), todas na extremidade inferior:
- Nota `0` ($z = -4,3585$)
- Nota `8` ($z = -3,8309$)
- Nota `18` ($z = -3,1715$)
- Nota `19` ($z = -3,1055$)

---

## 5. Representação Gráfica (Parte F)

![Histograma e Curva de Gauss](./histograma_curva_normal.png)

O gráfico acima combina:
1. **Histograma de densidade** das notas de matemática;
2. **Curva Normal Teórica (Curva de Gauss)** parametrizada com $\bar{x} = 66,09$ e $s = 15,16$;
3. **Linha vertical contínua** indicando a média ($\bar{x}$);
4. **Linhas verticais tracejadas** indicando um desvio-padrão abaixo ($\bar{x} - s$) e acima ($\bar{x} + s$) da média;
5. **Gráfico de Caixa (*Boxplot*)** na base, evidenciando a mediana centralizada e os valores atípicos à esquerda.

---

## 6. Conclusão (Parte G)

- **Formato e Centralidade:** O histograma apresenta formato próximo ao de um sino, com média ($66,09$), mediana ($66,00$) e moda ($65$) praticamente idênticas.
- **Aderência à Regra 68–95–99,7:** Os percentuais empíricos encontrados ($69,60\%$, $95,40\%$ e $99,60\%$) são extremamente próximos aos valores teóricos da distribuição normal.
- **Assimetria e Atípicos:** A distribuição possui leve assimetria negativa ($-0,2789$) devido à presença de $4$ notas muito baixas ($|z| > 3$) e ao limite superior natural da prova em $100$ pontos ($z = +2,24$).
- **Síntese:** Embora os dados não sigam uma distribuição normal *perfeita* (pois são valores inteiros limitados ao intervalo $[0, 100]$ e com leve cauda à esquerda), eles apresentam comportamento **aproximadamente normal**, tornando a Curva de Gauss um excelente modelo prático para descrever o desempenho dos estudantes.

---

## 7. Como Executar o Programa

1. Certifique-se de ter o **Python 3** e a biblioteca `matplotlib` instalados:
   ```bash
   pip install matplotlib
   ```
2. Execute o script principal na raiz do projeto:
   ```bash
   python3 analise_distribuicao_normal.py
   ```
3. Os resultados das **Partes B, C, D e E** serão exibidos no terminal e o gráfico atualizado será salvo automaticamente em `histograma_curva_normal.png`.

