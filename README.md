# HACKATHON SMARTNESS / 5G DATASET CHALLENGE
> _Desenvolvendo soluções e insights usando aprendizado de máquina nos dados de redes 5G no Brasil_

[![Launch Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/intrig-unicamp/hackathon5G/main)
[![nbviewer](https://raw.githubusercontent.com/jupyter/design/main/logos/Badges/nbviewer_badge.svg)](https://nbviewer.org/github/intrig-unicamp/hackathon5G/tree/main/)

O avanço do 5G é uma das transformações mais significativas no mundo da tecnologia nos últimos anos, e o Brasil não está ficando para trás nessa corrida. Com uma latência e velocidade de transmissão de dados sem precedentes, o 5G promete revolucionar a conectividade e comunicação humana, além de possibilitar infinitas novas oportunidades para a inovação e empreendedorismo em diversas áreas como a saúde, a agricultura, a indústria e muito mais.

Nesse sentido, a _Hackathon SMARTNESS / 5G Dataset Challenge_ tem como objetivo instigar o desenvolvimento de soluções inovadoras e elaboração de _insights_ utilizando bases (fornecidas pela comissão organizadora da Hackathon SMARTNESS) compostas por dados de uso de serviços de _streaming_ de vídeo adaptativo (YouTube) e redes 5G no Brasil. Para suportar a resolução dos problemas, as equipes poderão usar bases auxiliares para enriquecimento de dados.

As equipes poderão desenvolver seus projetos em diversas linhas, como, por exemplo, análise exploratória de dados, desenvolvimento de _insights_ inovadores usando 5G e os conjuntos de dados disponibilizados, modelos de Aprendizado de Máquina para predição, classificação, agrupamento, suporte à decisão, desenvolvimento de modelos de desempenho de aplicações no contexto de 5G e muito mais.

# Requisitos
Para desenvolver soluções para a Hackathon, é necessário ter um computador para realizar o processamento de dados e Aprendizado de Máquina no _Jupyter Notebook_.

Além disso, é desejável que os participantes tenham conhecimentos nos seguintes assuntos:
- Processamento e análise de dados;
- Métodos de Aprendizado de Máquina, tais como regressão, clusterização, árvores de decisão, florestas aleatórias (_Random Forest_), k-vizinhos mais próximos (kNN), análise de discriminante linear;
- Programação em _Python_; e
- _Jupyter Notebook_.

# 1º Passo: Preparação do ambiente de execução

> ⚠️ Esse projeto não possui suporte oficial ao Google Colab

- **Binder**

  É possível utilizar esse repositório de forma online, sem configurações adicionais. Basta clicar na _badge_ do Binder que o repositório inteiro será carregado

  [![Launch Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/intrig-unicamp/hackathon5G/main)

- **Localmente (testado em Linux e Windows)**

  Esse repositório pode ser executado localmente utilizando o ambiente [Mamba](https://mamba.readthedocs.io/en/latest/installation.html) ou [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html), e baixando os conjuntos de dados adicionais.

  1. Clone o repositório em sua máquina dentro da pasta desejada:
      ```
      git clone --depth=1 https://github.com/intrig-unicamp/hackathon5G.git
      cd hackathon5G
      ```

  2. Crie o ambiente a partir do arquivo `environment.yml`:
      ```
      # se usar o Micromamba:
      micromamba env create -f environment.yml -y

      # se usar o Conda:
      conda env create -f environment.yml
      ```

  3. Ative o ambiente:
      ```
      # se usar o Micromamba:
      micromamba activate hackathon5G

      # se usar o Conda:
      conda activate hackathon5G
      ```

  4. Inicie o Jupyter Lab. Se uma janela do navegador não for aberta com o Jupyter Lab, basta clicar em um dos links de acesso disponíveis no terminal:
      ```
      jupyter lab
      ```

# 2º passo: Datasets
Consulte [aqui](datasets) a pasta com as bases de dados disponibilizadas e a sua respectiva documentação no [README](datasets/README.md) desta pasta.

# 3º passo: Desafios
Consulte [aqui](challenges) a pasta com os desafios propostos. O [README](challenges/README.md) dessa pasta fornece as instruções necessárias sobre cada desafio. Também são fornecidos Notebooks auxiliares para as equipes iniciarem mais rapidamente o desenvolvimento dos desafios.

# 4º passo: Entrega
> **[Google Forms](https://forms.gle/mZd3qTaYuCifXgLW7) para submissão das soluções**

As equipes devem submeter os arquivos do Jupyter Notebook produzidos em cada solução, que devem conter um storytelling dos dados cobrindo a descrição do que foi realizado pela equipe, os insights obtidos, o pré-processamento, os modelos de Aprendizado de Máquina desenvolvidos, a avaliação de desempenho dos modelos, a escolha do modelo de Aprendizado de Máquina, entre outros tópicos que as equipes julguem pertinente.

Atente-se ao roteiro dos desafios, aos critérios de avaliação e a entrega diferenciada de alguns desafios. Garanta que os avaliadores da comissão organizadora da Hackathon SMARTNESS tenham acesso a todos os arquivos da sua submissão. As equipes devem se assegurar de fornecer todos os demais conjuntos de dados que utilizaram. Dê preferência para baixar os dados necessários tal como as seguintes alternativas:

```python
# ✅ Recomendável
# > clonar um repositório do GitHub. Exemplo:
!git clone --depth=1 https://github.com/intrig-unicamp/hackathon5G.git

# ✅ Recomendável
# > baixar um arquivo usando o wget. Exemplo:
!wget https://github.com/intrig-unicamp/hackathon5G/raw/main/datasets/mosaico/mosaico-erbs-são-paulo.zip

# ✅ Recomendável
# > baixar um arquivo do Google Drive (o arquivo deve estar acessível publicamente via link)
!wget https://docs.google.com/uc?export=download&confirm=t&id=<ID DO ARQUIVO>

# exemplo de link de arquivo: https://drive.google.com/file/d/1kqOgkzK-QTViGlVjyfMT7Dzr/view
# o <ID DO ARQUIVO> seria: 1kqOgkzK-QTViGlVjyfMT7Dzr
!wget https://docs.google.com/uc?export=download&confirm=t&id=1kqOgkzK-QTViGlVjyfMT7Dzr
```
