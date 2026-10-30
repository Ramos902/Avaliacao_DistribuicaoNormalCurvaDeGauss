# Relatório: Distribuição Normal e Curva de Gauss

**Disciplina:** Probabilidade e Estatística Aplicada  
**Alunos:** João Pedro Ramos e Gabriel Leme  
**Base de dados:** `StudentsPerformance.csv`  
**Coluna analisada:** `math score` (notas de matemática)

---

## Parte A - Pesquisa Teórica

### 1. O conceito de distribuição normal
A distribuição normal é um modelo estatístico usado para variáveis contínuas onde a maioria dos dados fica concentrada perto da média e poucos valores ficam nas pontas (muito altos ou muito baixos).

### 2. Características da Curva de Gauss
O gráfico da distribuição normal é chamado de Curva de Gauss. As principais características dele são:
- Tem formato de sino, com um único pico no meio;
- É simétrico em relação ao centro (a metade da esquerda é igual à da direita);
- Na curva normal exata, a média, a mediana e a moda têm o mesmo valor;
- As pontas da curva vão diminuindo até quase encostar no eixo horizontal, sem nunca tocar nele;
- A área total embaixo da curva vale 1 (ou 100%).

A fórmula da curva é:

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}$$

### 3. Função da média na distribuição
A média ($\mu$ ou $\bar{x}$) define onde fica o centro da curva no eixo horizontal. Se a média muda, a curva inteira anda para a esquerda ou para a direita, mas não muda de formato.

### 4. Função do desvio-padrão
O desvio-padrão ($\sigma$ ou $s$) mostra o quanto os dados estão espalhados em torno da média. Quando o desvio-padrão é pequeno, as notas são parecidas e o sino fica alto e estreito. Quando é grande, os dados são mais espalhados e a curva fica baixa e larga.

Fórmula do desvio-padrão amostral:

$$s = \sqrt{\frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n - 1}}$$

### 5. Significado da regra 68-95-99,7
Em dados que seguem uma distribuição normal, a porcentagem de valores perto da média segue um padrão conhecido:
- Cerca de 68% dos dados ficam entre $\bar{x} - s$ e $\bar{x} + s$ (até 1 desvio-padrão da média);
- Cerca de 95% ficam entre $\bar{x} - 2s$ e $\bar{x} + 2s$ (até 2 desvios-padrão);
- Cerca de 99,7% ficam entre $\bar{x} - 3s$ e $\bar{x} + 3s$ (até 3 desvios-padrão).

### 6. Conceito de escore padronizado z
O escore $z$ serve para mostrar quantos desvios-padrão um valor específico está longe da média. Se $z$ for positivo, a nota está acima da média; se for negativo, está abaixo. Quando $|z| > 3$, o valor está muito longe do centro e pode ser considerado um valor atípico (fora do padrão).

Fórmula do escore $z$:

$$z = \frac{x - \bar{x}}{s}$$

---

## Parte B - Leitura e Organização dos Dados

O arquivo `StudentsPerformance.csv` foi lido em Python usando o módulo `csv` e o `csv.DictReader`:
- Quantidade de linhas lidas: 1000
- Quantidade de notas válidas convertidas para inteiro: 1000
- Valores vazios ou inválidos: 0

---

## Parte C - Medidas Estatísticas

Resultados calculados pelo código para a coluna `math score`:

| Medida | Resultado |
| :--- | :--- |
| 1. Quantidade de dados ($n$) | 1000 |
| 2. Menor nota | 0 |
| 3. Maior nota | 100 |
| 4. Amplitude total | 100 |
| 5. Média aritmética ($\bar{x}$) | 66,0890 |
| 6. Mediana | 66,00 |
| 7. Moda | 65 (aparece 36 vezes) |
| 8. Variância amostral ($s^2$) | 229,9190 |
| 9. Desvio-padrão amostral ($s$) | 15,1631 |
| 10. Coeficiente de assimetria | -0,2789 |

---

## Parte D - Regra 68-95-99,7

Contagem de notas dentro de cada faixa de desvio-padrão (usando $\bar{x} = 66,09$ e $s = 15,16$):

| Faixa | Intervalo de notas | Quantidade | Percentual encontrado | Esperado pela regra |
| :--- | :--- | :--- | :--- | :--- |
| $\bar{x} - s$ até $\bar{x} + s$ | 50,93 até 81,25 | 696 | 69,60% | 68% |
| $\bar{x} - 2s$ até $\bar{x} + 2s$ | 35,76 até 96,42 | 954 | 95,40% | 95% |
| $\bar{x} - 3s$ até $\bar{x} + 3s$ | 20,60 até 111,58 | 996 | 99,60% | 99,7% |

---

## Parte E - Escores Padronizados

Cálculo do escore $z$ para as notas pedidas na atividade:

| Caso | Nota ($x$) | Escore $z$ | Classificação ($\|z\| > 3$) |
| :--- | :--- | :--- | :--- |
| Menor nota | 0 | -4,3585 | Atípico ($\|z\| > 3$) |
| Maior nota | 100 | 2,2364 | Normal |
| Nota 50 | 50 | -1,0611 | Normal |
| Nota 75 | 75 | 0,5877 | Normal |
| Nota 90 | 90 | 1,5769 | Normal |

Olhando as 1000 notas da base, apenas 4 notas tiveram $|z| > 3$ (todas notas muito baixas):
- Nota 0 ($z = -4,3585$)
- Nota 8 ($z = -3,8309$)
- Nota 18 ($z = -3,1715$)
- Nota 19 ($z = -3,1055$)

---

## Parte F - Representação Gráfica

O gráfico foi gerado pelo script no arquivo `histograma_curva_normal.png`, contendo o histograma das notas, a curva normal teórica por cima, as linhas da média e de 1 desvio-padrão e o boxplot embaixo.

---

## Parte G - Conclusão

**1. O histograma apresenta aproximadamente o formato de sino?**  
Sim. A maior parte das notas fica concentrada no meio (entre 55 e 80) e as barras vão diminuindo nas pontas, acompanhando bem o desenho do sino.

**2. Média e mediana apresentam valores próximos?**  
Sim, são quase iguais: a média deu 66,09 e a mediana deu 66,00 (e a moda também ficou perto, em 65).

**3. Os percentuais observados são próximos da regra 68-95-99,7?**  
Sim, bateram muito perto: deu 69,60% (para 68%), 95,40% (para 95%) e 99,60% (para 99,7%).

**4. A distribuição apresenta assimetria?**  
Tem uma leve assimetria negativa (-0,2789), ou seja, uma cauda um pouco maior para a esquerda. Isso acontece porque existem notas muito baixas chegando até zero, enquanto do lado direito a nota trava no limite máximo de 100.

**5. Existem valores atípicos?**  
Sim. Usando a regra $|z| > 3$, existem 4 notas atípicas na ponta de baixo: 0, 8, 18 e 19. Elas também aparecem como bolinhas soltas na esquerda do boxplot.

**6. É adequado afirmar que os dados seguem perfeitamente uma distribuição normal?**  
Não perfeitamente, porque uma distribuição normal teórica vai para o infinito dos dois lados e aceita qualquer número com vírgula, enquanto as notas da prova são números inteiros travados entre 0 e 100 e têm uma leve assimetria para a esquerda.

**7. Qual seria uma conclusão mais cuidadosa sobre a distribuição das notas?**  
O mais correto é dizer que as notas de matemática não têm uma distribuição normal perfeita, mas seguem um comportamento aproximadamente normal. Como a média e a mediana são praticamente iguais e as porcentagens batem quase cravado na regra 68-95-99,7, a Curva de Gauss funciona muito bem para representar esses dados na prática.
