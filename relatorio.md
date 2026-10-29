# Relatório: Análise da Distribuição Normal e Curva de Gauss

**Disciplina:** Probabilidade e Estatística Aplicada  
**Base de dados:** *Students Performance in Exams* (`StudentsPerformance.csv`)  
**Variável analisada:** `math score` (Nota de Matemática)

---

## Parte A — Pesquisa Teórica

### 1. Conceito de Distribuição Normal
A distribuição normal (ou distribuição gaussiana) é uma das distribuições de probabilidade contínuas mais importantes da estatística. Ela modela fenômenos naturais, físicos, sociais e educacionais nos quais a grande maioria das observações se concentra em torno de um valor central, enquanto valores extremos (muito baixos ou muito altos) ocorrem com frequência cada vez menor à medida que se afastam do centro.

### 2. Características da Curva de Gauss
O gráfico da função densidade de probabilidade da distribuição normal é conhecido como **Curva de Gauss** e apresenta as seguintes propriedades fundamentais:
- **Formato de sino (unimodal):** possui um único pico central onde a densidade de probabilidade é máxima.
- **Simetria perfeita:** a curva é perfeitamente simétrica em relação ao seu centro. Em uma distribuição normal exata, a **média**, a **mediana** e a **moda** coincidem no mesmo ponto ($\mu = \text{mediana} = \text{moda}$).
- **Comportamento assintótico:** as caudas da curva se estendem indefinidamente para $-\infty$ e $+\infty$, aproximando-se do eixo horizontal sem nunca tocá-lo.
- **Área total unitária:** a área total sob a curva é igual a $1$ (ou $100\%$).

A função densidade de probabilidade é dada por:

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}$$

### 3. Função da Média na Distribuição ($\mu$ ou $\bar{x}$)
A média atua como o **parâmetro de posição (ou localização)**. Ela define o centro de gravidade da distribuição e o eixo de simetria da Curva de Gauss. Alterar o valor da média desloca a curva horizontalmente para a esquerda ou para a direita, sem alterar a sua forma ou abertura.

### 4. Função do Desvio-Padrão ($\sigma$ ou $s$)
O desvio-padrão atua como o **parâmetro de escala (ou dispersão)**. Ele mede o grau de espalhamento dos dados em relação à média:
- Um **desvio-padrão pequeno** indica dados concentrados próximos à média, resultando em uma curva mais estreita e alta.
- Um **desvio-padrão grande** indica dados mais espalhados, resultando em uma curva mais larga e achatada.

Na análise de uma amostra de tamanho $n$, utiliza-se o desvio-padrão amostral ($s$):

$$s = \sqrt{\frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n - 1}}$$

### 5. Significado da Regra Empírica 68–95–99,7
Para conjuntos de dados que seguem aproximadamente uma distribuição normal, a proporção de observações contidas em intervalos simétricos ao redor da média obedece à chamada **Regra Empírica**:
- Cerca de **$68\%$** dos dados estão a até $1$ desvio-padrão da média: $[\mu - \sigma,\; \mu + \sigma]$.
- Cerca de **$95\%$** dos dados estão a até $2$ desvios-padrão da média: $[\mu - 2\sigma,\; \mu + 2\sigma]$.
- Cerca de **$99{,}7\%$** dos dados estão a até $3$ desvios-padrão da média: $[\mu - 3\sigma,\; \mu + 3\sigma]$.

### 6. Conceito de Escore Padronizado $z$
O escore padronizado $z$ (*z-score*) indica quantos desvios-padrão uma determinada observação $x$ está acima ($z > 0$) ou abaixo ($z < 0$) da média amostral $\bar{x}$. Ele permite comparar posições relativas e identificar valores atípicos (*outliers*). Sua fórmula é:

$$z = \frac{x - \bar{x}}{s}$$

Observações com $|z| > 3$ situam-se além de três desvios-padrão da média (onde se espera apenas $0{,}3\%$ dos dados em uma curva normal) e são classificadas como possíveis valores atípicos.

---

## Parte B — Leitura e Organização dos Dados

O arquivo `StudentsPerformance.csv` foi processado em Python utilizando exclusivamente o módulo nativo `csv` e a classe `csv.DictReader`:
- **Total de registros lidos:** $1.000$
- **Registros válidos convertidos para `int` (`math score`):** $1.000$
- **Valores ausentes ou inválidos:** $0$

---

## Parte C — Medidas Estatísticas (`math score`)

Todos os cálculos foram implementados manualmente em Python (sem uso de bibliotecas estatísticas):

| Medida Estatística | Valor Encontrado |
| :--- | :--- |
| **1. Quantidade de dados ($n$)** | $1.000$ |
| **2. Menor nota** | $0$ |
| **3. Maior nota** | $100$ |
| **4. Amplitude total** | $100$ |
| **5. Média aritmética ($\bar{x}$)** | $66{,}0890$ |
| **6. Mediana** | $66{,}00$ |
| **7. Moda** | $65$ (36 ocorrências) |
| **8. Variância amostral ($s^2$)** | $229{,}9190$ |
| **9. Desvio-padrão amostral ($s$)** | $15{,}1631$ |
| **10. Coeficiente de assimetria** | $-0{,}2789$ |

---

## Parte D — Verificação da Regra 68–95–99,7

Utilizando $\bar{x} = 66{,}0890$ e $s = 15{,}1631$, obteve-se a seguinte distribuição das $1.000$ notas nos intervalos:

| Intervalo | Limites Numéricos | Quantidade de Notas | Percentual Observado | Percentual Teórico Esperado |
| :--- | :--- | :--- | :--- | :--- |
| $\bar{x} \pm 1s$ | $[50{,}93;\; 81{,}25]$ | $696$ | **$69{,}60\%$** | $\approx 68{,}0\%$ |
| $\bar{x} \pm 2s$ | $[35{,}76;\; 96{,}42]$ | $954$ | **$95{,}40\%$** | $\approx 95{,}0\%$ |
| $\bar{x} \pm 3s$ | $[20{,}60;\; 111{,}58]$ | $996$ | **$99{,}60\%$** | $\approx 99{,}7\%$ |

---

## Parte E — Escores Padronizados ($z$) e Valores Atípicos

Aplicando $z = \frac{x - 66{,}0890}{15{,}1631}$ para os valores solicitados:

| Referência | Nota ($x$) | Escore Padronizado ($z$) | Classificação ($\|z\| > 3$) |
| :--- | :--- | :--- | :--- |
| **Menor nota** | $0$ | $-4{,}3585$ | **Atípico** ($\|z\| > 3$) |
| **Maior nota** | $100$ | $+2{,}2364$ | Normal ($\|z\| \le 3$) |
| **Nota igual a 50** | $50$ | $-1{,}0611$ | Normal ($\|z\| \le 3$) |
| **Nota igual a 75** | $75$ | $+0{,}5877$ | Normal ($\|z\| \le 3$) |
| **Nota igual a 90** | $90$ | $+1{,}5769$ | Normal ($\|z\| \le 3$) |

Varrendo todas as $1.000$ notas do arquivo, foram identificados **4 valores atípicos** com $|z| > 3$, todos na cauda inferior:
- $x = 0 \implies z = -4{,}3585$
- $x = 8 \implies z = -3{,}8309$
- $x = 18 \implies z = -3{,}1715$
- $x = 19 \implies z = -3{,}1055$

---

## Parte F — Representação Gráfica

O gráfico gerado (`histograma_curva_normal.png`) sobrepõe a Curva de Gauss teórica ao histograma de densidade das notas de matemática, destacando a média ($\bar{x} = 66{,}09$) e os limites de $\pm 1$ desvio-padrão ($50{,}93$ e $81{,}25$), acompanhado do gráfico de caixa (*boxplot*) na parte inferior.

---

## Parte G — Conclusão (Respostas às Questões)

1. **O histograma apresenta aproximadamente o formato de sino?**  
   Sim. O histograma exibe concentração clara de notas na região central (entre $55$ e $80$) e redução gradual das frequências em direção às extremidades, acompanhando de perto o contorno em sino da curva normal teórica.

2. **Média e mediana apresentam valores próximos?**  
   Sim, são praticamente idênticas: a média é $66{,}09$ e a mediana é $66{,}00$ (e a moda é $65$), evidenciando forte centralidade dos dados.

3. **Os percentuais observados são próximos da regra 68–95–99,7?**  
   Sim, muito próximos. Os valores empíricos encontrados foram **$69{,}60\%$**, **$95{,}40\%$** e **$99{,}60\%$**, apresentando desvios inferiores a $1{,}6$ ponto percentual em relação aos valores teóricos ($68\%$, $95\%$ e $99{,}7\%$).

4. **A distribuição apresenta assimetria?**  
   Apresenta uma **leve assimetria negativa (à esquerda)**, indicada pelo coeficiente de assimetria de $-0{,}2789$. Isso ocorre porque o limite superior das notas é truncado em $100$ (a cerca de $+2{,}24$ desvios-padrão da média), enquanto a cauda esquerda se estende até a nota $0$ ($-4{,}36$ desvios-padrão).

5. **Existem valores atípicos?**  
   Sim. Pelo critério $|z| > 3$, existem $4$ notas atípicas na cauda inferior: $0$, $8$, $18$ e $19$. O gráfico de caixa (*boxplot*) também evidencia esses pontos extremos à esquerda.

6. **É adequado afirmar que os dados seguem perfeitamente uma distribuição normal?**  
   Não. Além de as notas serem valores discretos e limitados ao intervalo fechado $[0, 100]$ (enquanto a distribuição normal teórica é contínua e ilimitada em $(-\infty, +\infty)$), há uma leve assimetria à esquerda e cauda superior cortada na nota máxima $100$.

7. **Qual seria uma conclusão mais cuidadosa sobre a distribuição das notas?**  
   Conclui-se que as notas de matemática **não seguem uma distribuição normal perfeita, mas são muito bem aproximadas por um modelo normal** ($\bar{x} \approx 66{,}09$ e $s \approx 15{,}16$) para fins práticos. A forte proximidade entre média, mediana e moda e a excelente aderência à regra empírica $68\text{–}95\text{–}99{,}7$ validam o uso da distribuição normal como boa aproximação descritiva para o desempenho dos estudantes, ressalvando-se apenas a presença de $4$ notas muito baixas (atípicas) e a limitação natural do teto de $100$ pontos.

