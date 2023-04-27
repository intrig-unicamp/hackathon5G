# HACKATHON SMARTNESS / 5G DATASET CHALLENGE
> _Desenvolvendo soluções e insights usando aprendizado de máquina nos dados de redes 5G no Brasil_

O avanço do 5G tem sido uma das transformações mais significativas no mundo da tecnologia nos últimos anos, e o Brasil não está ficando para trás nessa corrida. Com uma latência e velocidade de transmissão de dados sem precedentes, o 5G promete revolucionar a maneira como nos conectamos e nos comunicamos uns com os outros, além de possibilitar infinitas novas oportunidades para a inovação e empreendedorismo em diversas áreas como a saúde, a agricultura, a indústria e muito mais.

Nesse sentido, a _Hackathon SMARTNESS / 5G Dataset Challenge_ tem como objetivo instigar o desenvolvimento de soluções inovadoras e elaboração de _insights_ com base nas bases de dados (fornecidas pela comissão organizadora da Hackathon SMARTNESS) compostas por dados de uso de serviços de _streaming_ de vídeo adaptativo (YouTube) e redes 5G e no Brasil, entre outras bases que a equipe julgue pertinente.

As equipes poderão desenvolver seus projetos em diversas linhas, como, por exemplo, análise exploratória de dados, desenvolvimento de _insights_ inovadores usando 5G e os conjuntos de dados disponibilizados, modelos de Aprendizado de Máquina para predição, classificação, agrupamento, suporte à decisão, desenvolvimento de modelos de desempenho de aplicações no contexto de 5G e muito mais.

# Requisitos
Para desenvolver soluções para a hackathon, é necessário ter um computador (i.) capaz de realizar o processamento de dados e AM no _Jupyter Notebook_ ou (ii.) ter acesso aos recursos em nuvem através do _Google Colab_.

Além disso, é desejável que os participantes tenha conhecimentos nos seguintes assuntos:
- Processamento e análise de dados
- Métodos de Aprendizado de Máquina (tais como regressão, clusterização, árvores de decisão, florestas aleatórias (_Random Forest_), k-vizinhos mais próximos (kNN), análise de discriminante linear)
- Programação em _Python_
- _Jupyter Notebook_/_Google Colab_

# 1º passo: Datasets
Consulte [aqui](datasets) a pasta com os conjuntos de dados disponibilizados. Os dados estão documentados no [README](datasets/README.md) dessa pasta.

# 2º passo: Desafios
Consulte [aqui](challenges) a pasta com os desafios propostos. O [README](challenges/README.md) dessa pasta fornece instruções adicionais.

# 3º passo: Entrega
> **[Google Forms](https://example.com/link-do-forms) para submissão das soluções**

A equipe deve submeter o Jupyter Notebook/Colab produzido em cada solução, que deve conter um storytelling dos dados cobrindo a descrição do que foi realizado pela equipe, os insights obtidos, o pré-processamento, os modelos de aprendizado de máquina desenvolvidos, a avaliação de desempenho dos modelos, a escolha do modelo de aprendizado de máquina, entre outros tópicos que a equipe julgue pertinente.

Atente-se ao roteiro dos desafios, aos critérios de avaliação e a entrega diferenciada de alguns desafios. Garanta que os avaliadores da comissão organizadora da Hackathon SMARTNESS tenham acesso a todos os arquivos da sua submissão. A equipe deve se assegurar de fornecer todos os demais conjuntos de dados que escolha utilizar. Não acesse arquivos do Google Drive do usuário atual, tal como:

```python
# ❌ NÃO FAÇA ISSO!
# > montar o Google Drive do usuário atual
from google.colab import drive
drive.mount('/content/drive')
```

Isso é problemático porque depende de arquivos armazenados no Drive do usuário atual que está executando o Colab, e não há garantia de que os arquivos estejam presentes. Em vez disso, dê preferência para baixar os dados necessários em tempo de execução, como as seguintes alternativas:

```python
# ✅ Recomendável
# > clonar um repositório do GitHub
!git clone --depth=1 https://github.com/intrig-unicamp/hackathon5G.git hackathon5G

# ✅ Recomendável
# > baixar um arquivo usando o wget
!wget https://github.com/intrig-unicamp/hackathon5G/raw/main/datasets/mosaico/mosaico-erbs-s%C3%A3o-paulo.zip

# ⚠️ Use com moderação
# > baixar um arquivo do Google Drive (garanta que o arquivo esteja acessível publicamente para todos com o link)
!wget https://docs.google.com/uc?export=download&confirm=t&id=<ID DO ARQUIVO>

# exemplo de link de arquivo: https://drive.google.com/file/d/1kqOgkzK-QTViGlVjyfMT7DzrfaN7naP3/view?usp=sharing
# o <ID DO ARQUIVO> seria: 1kqOgkzK-QTViGlVjyfMT7DzrfaN7naP3
!wget https://docs.google.com/uc?export=download&confirm=t&id=1kqOgkzK-QTViGlVjyfMT7DzrfaN7naP3
```
