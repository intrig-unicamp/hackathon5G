# 🏋️‍♂️ Desafios
> Nessa pasta contém os desafios propostos para a _Hackathon SMARTNESS / 5G Dataset Challenge_

A edição mais recente do [Relatório de Mobilidade Ericsson](https://www.ericsson.com/en/reports-and-papers/mobility-report/dataforecasts/traffic-by-application) apontou que no ano de 2022 71% do tráfego da rede móvel mundial foi constituído por transmissão de vídeo e que até 2028 esta demanda deve aumentar em 9%. Deste modo, o gerenciamento de redes celulares se mostra um elemento fundamental para promover a experiência de uso deste tipo de serviço, fator este que tende a proporcionar novas oportunidades de negócio e pesquisa à medida em que o uso da rede 5G se expande.

Em vista disso, a Hackathon SMARTNESS apresenta os seguintes desafios que podem contribuir para o desenvolvimento de novas soluções de gerenciamento de redes móveis, visando atender a crescente demanda de tráfego de vídeo e a otimização da qualidade de experiência do usuário.

- 📊 **Visualização usando o PathsViewer**

  **A ferramenta**: PathsViewer é uma interface para visualização de dados espaço-temporais em tempo real ou pós-eventos. Essa ferramenta busca suprir a demanda por ferramentas de visualização de trajetórias de objetos, em vista do grande interesse em pesquisas nesse tipo de dado.

  É possível utilizar conjuntos de dados variados, com estruturas diversas, tais como traces de 5G georeferenciados e trajetórias de veículos.

  **O desafio**: Esse desafio tem como objetivo usar a ferramenta PathViewer para apresentar os conjuntos de dados fornecidos (não é necessário utilizar todos eles).

  A equipe deve explorar as funcionalidades do PathViewer, como ajuste de escala, visualização em mapa 2D ou satélite, envio de múltiplos conjuntos de dados, entre outras. Com isso, é possível gerar visualizações claras e informativas que ajudem os usuários a visualizar as informações contidas nos dados de trajetórias de objetos.

  **A entrega**: De modo que esse desafio em específico não envolve a aplicação de técnicas de aprendizado de máquina (tal como os demais a seguir), não é solicitado a entrega de um Jupyter Notebook/Colab. Em vez disso, espera-se que a solução desse desafio seja composta de uma descrição do que foi realizado pela equipe, os insights obtidos, eventuais códigos produzidos para o tratamento de dados, acompanhado de um vídeo ou capturas de tela que mostrem a interface do PathsViewer com os conjuntos de dados fornecidos. É importante que a entrega mostre as funcionalidades utilizadas da ferramenta.

---
- 📊 **Análise da tendências de construção e de características das ERBs no Brasil**

  O desafio envolve avaliar os atributos do conjunto de dados `mosaico` e avaliar características relevantes das ERBs no Brasil. Algumas possíveis analises incluem avaliar entre operadoras, ou até mesmo entre as regiões, qual tem sido o plano de construção de antenas, quais as principais diferenças entre as antenas em operação de diferentes operadoras/regiões, qual empresa tem prevalecido na construção de antenas 5G, entre outros.

  As análises são em grande parte de carater exploratório, por isso a elaboração de gráficos e de mapas que apoiem uma tomada de decisão acerca do tema abordado é o principal objetivo.

---
- 🔮 **Predição de qualidade de sinal**

  Com o objetivo de prever a qualidade de sinal, para resolver esse desafio a equipe deve empregar técnicas de aprendizado de máquina nos conjuntos de dados fornecidos pela comissão organizadora da Hackathon SMARTNESS, compostos por dados de uso de serviços de streaming de vídeo adaptativo (YouTube) e redes 5G no Brasil, entre outras bases que a equipe julgue pertinente. Uma estratégia pode ser a combinação de diferentes bases de dados para enriquecimento de dados, como, por exemplo, usar o conjunto de dados `g-nettrack-pro` enriquecido com o `mosaico` para prover informações das antenas na proximidade, como a localização, densidade de antenas, frequência e tecnologia.

  As equipes deverão utilizar técnicas de aprendizado de máquina, como predição mono-variada e multi-variada, para prever os valores de um ou mais indicadores de qualidade de sinal, tal como QUAL, CQI e SNNR.

---
- 🔮 **Predição do tipo de mobilidade**

  Esse desafio consiste em utilizar técnicas de aprendizado de máquina para prever o tipo de mobilidade (pedestre, veículo, metrô/trem) de um dispositivo móvel com base nos dados de localização fornecidos pelo conjunto de dados `g-nettrack-pro`. Essa tarefa pode ser abordada como um problema de classificação, onde o modelo de aprendizado de máquina deve classificar cada registro do conjunto de dados em uma das classes de mobilidade possíveis.

---
- 🔮🗂️ **Predição da qualidade de transmissão de vídeo**

  O desafio de predição da qualidade de transmissão de vídeo adaptativo (YouTube) consiste em utilizar técnicas de aprendizado de máquina para prever a qualidade da transmissão de vídeo em dispositivos móveis. O objetivo é criar um modelo de predição que leve em conta informações como as coordenadas do celular, as características da rede, a tecnologia utilizada, entre outras variáveis, para estimar a qualidade de transmissão de vídeo. Com isso, é possível melhorar a experiência do usuário, garantindo que a transmissão de vídeo seja realizada com a melhor qualidade possível, considerando as condições da rede e do ambiente em que o usuário está localizado.

  As equipes deverão utilizar técnicas de aprendizado de máquina para prever a qualidade de transmissão de vídeo usando, separadamente, os dados de localização correlacionado com as antenas na proximidade e métricas da rede (como qualidade do sinal, tecnologia, frequência).

---
- 🔮🗂️ **Inferir a qual Estação Rádio Base o celular está conectado**

  O desafio proposto é inferir a qual Estação Rádio Base (ERB) o dispositivo móvel está conectado, com base nas coordenadas do celular correlacionado com as antenas na proximidade. Isso envolve o uso de técnicas de processamento de dados e aprendizado de máquina para analisar os dados de localização e dados das antenas próximas e identificar a ERB mais provável. As equipes podem utilizar diferentes técnicas, como regressão logística, classificação por árvores de decisão, redes neurais e outras técnicas de aprendizado de máquina para resolver esse desafio. A precisão da inferência pode ser medida utilizando métricas como a acurácia e a taxa de falsos positivos.

# 🤔 Critérios de avaliação
- Os participantes deverão resolver o maior número possível dos desafios fornecidos
- Pré-processamento dos dados
- Representação dos dados e estratégia de composição de atributos
- Estratégia de seleção do modelo escolhido
- Estratégia de validação
- Qualidade do modelo em relação as métricas de qualidade (acurácia, precisão, revocação, F1-score, etc)
- Interpretabilidade do modelo sugerido
- Storytelling dos dados, incluindo conclusões
- Potencial impacto e viabilidade da solução apresentada
- Criatividade da solução e apresentação
