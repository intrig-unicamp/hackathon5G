# 🏋️‍♂️ Desafios
> Nessa pasta contém os desafios propostos para a _Hackathon SMARTNESS / 5G Dataset Challenge_

Como parte da Hackathon, os participantes deverão resolver o maior número possível dos desafios fornecidos a seguir.

- 📊 Visualização usando o PathsViewer
**A ferramenta**: PathsViewer é uma interface para visualização de dados espaço-temporais em tempo real ou pós-eventos. Essa ferramenta busca suprir a demanda por ferramentas de visualização de trajetórias de objetos, em vista do grande interesse em pesquisas nesse tipo de dado.

É possível utilizar conjuntos de dados variados, com estruturas diversas, tais como traces de 5G georeferenciados e trajetórias de veículos.

**O desafio**: Esse desafio tem como objetivo usar a ferramenta PathViewer para apresentar os conjuntos de dados fornecidos (não é necessário utilizar todos eles).

A equipe deve explorar as funcionalidades do PathViewer, como ajuste de escala, visualização em mapa 2D ou satélite, envio de múltiplos conjuntos de dados, entre outras. Com isso, é possível gerar visualizações claras e informativas que ajudem os usuários a visualizar as informações contidas nos dados de trajetórias de objetos.

**A entrega**: De modo que esse desafio em específico não envolve a aplicação de técnicas de aprendizado de máquina (tal como os demais a seguir), não é solicitado a entrega de um Jupyter Notebook/Colab. Em vez disso, espera-se que a solução desse desafio seja composta de uma descrição do que foi realizado pela equipe, os insights obtidos, eventuais códigos produzidos para o tratamento de dados, acompanhado de um vídeo ou capturas de tela que mostrem a interface do PathsViewer com os conjuntos de dados fornecidos. É importante que a entrega mostre as funcionalidades utilizadas da ferramenta.

- 🤝 Análise da tendências de construção e de características dos ERBs no Brasil. 
*Conjunto de dados: `mosaico`

*O desafio: Avaliar as features do dataset do mosaico e avaliar características relevantes dos ERBs no Brasil. Algumas possíveis analíses incluem, avaliar qual tem sido o plano de construção de antenas de uma dada operadora como a Claro. Quais as principais diferenças entre as antenas em operação dessas operadoras, ou quem sabe entre as regiões. Qual empresa tem prevalecido na construção de antenas 5G. 

*A entrega: As análises são em grande parte de carater exploratório, por isso a elaboração de gráficos e de mapas que apoiem uma tomada de decisão acerca do tema abordado é o principal objetivo.

- 🔮 Predição de qualidade de sinal
*Conjunto de dados: `g-nettrack-pro`

*O desafio: Avaliar métricas de qualidade de streaming de vídeo como CQI, SNNR, entre outros.

*A entrega: Avaliar o erro entre o valor real e o valor previsto pelos métodos propostos.

- 🔮 Predição do tipo de mobilidade
*Conjunto de dados: `g-nettrack-pro`

*O desafio: Predizer o tipo de mobilidade do usuário Ex: parado, caminhando, correndo, em veículo... Isso pode ser feito avaliando as coordenadas do usuário no dataset de transmissão do video e avaliar como isso impacta na qualidade de transmissão de vídeo.

*A entrega: Espera-se o uso de mapas que ilustrem o deslocamento do usuário, e que a qualidade de vídeo seja avaliada e comparada para os diferentes cenários de deslocamento.

- 🤝 Correlação de atributos
*Conjunto de dados: Qualquer

*O desafio: Avaliar variáveis correlacionadas que possam ser úteis para a solução de algum problema. A decisão de quais atributos e de qual o problema a ser abordado é de livre escolha.

*A entrega: Por ser um problema com escopo amplo, espera-se que a solução tenha algum impacto relevante, e que tal impacto seja avaliado e mensurado. O storytelling nesse caso é fundamental. 

- 🔮🗂️ Predição da qualidade do sinal dadas as coordenadas do celular
*Conjunto de dados: `g-nettrack-pro` + `mosaico`

*O desafio:  Avaliar o valor de Quality of Experience (QoE) dado os datasets com informações sobre a qualidade de transmissão do video e da lista de ERBs. Espera-se que para essa tarefa sejam usados diferentes modelos de regressão.

*A entrega:  O objetivo é reduzir ao máximo as métricas de avaliação do modelo utilizado, explicar todas as decisões tomadas ao longo da elaboração do modelo e do processamento de dados.

- 🔮🗂️ Predição da qualidade do stream de vídeo de acordo com as coordenadas do celular
*Conjunto de dados: `youtube-qoe-pcap` + `g-nettrack-pro` + `mosaico`

*O desafio:  Avaliar o valor de Quality of Experience (QoE) dado os datasets com informações sobre o trafego de rede, qualidade de transmissão do video e da lista de ERBs. Espera-se que para essa tarefa sejam usados diferentes modelos de regressão.

*A entrega:  O objetivo é reduzir ao máximo as métricas de avaliação do modelo utilizado, explicar todas as decisões tomadas ao longo da elaboração do modelo e do processamento de dados.

- 🔮🗂️ Predição da qualidade do stream de vídeo dada a qualidade do sinal
*Conjunto de dados: `youtube-qoe-pcap` + `g-nettrack-pro`

*O desafio: Avaliar o valor de Quality of Experience (QoE) dado os datasets com informações sobre o trafego de rede e da qualidade de transmissão do video. Espera-se que para essa tarefa sejam usados diferentes modelos de regressão.

*A entrega: O objetivo é reduzir ao máximo as métricas de avaliação do modelo utilizado, explicar todas as decisões tomadas ao longo da elaboração do modelo e do processamento de dados.

- 🔮🗂️ Inferir a qual ERB (estação rádio base) o celular está conectado
*Conjunto de dados: `g-nettrack-pro` + `mosaico`

*O desafio: A partir do dataset de transmissão de video com a posição do usuario, inferir qual a ERB mais próxima do usuário. Assim pode-se avaliar melhor em que ponto o usuário pode ter mudado entre ERBs e como isso impactou a qualidade do vídeo.

*A entrega: Espera-se a manipulação dos dois datasets para relacionar a posição do usuário com a posição da antena mais próxima. Pode-se também fazer visualições com a posição das antenas e do usuário. Ou mesmo uma função que automaticamente adicione uma coluna de antena selecionada no dataset do g-nettrack-pro.

# 🤔 Critérios de avaliação
- Pré-processamento dos dados
- Representação dos dados e estratégia de composição de atributos
- Estratégia de seleção do modelo escolhido
- Estratégia de validação
- Qualidade do modelo em relação as métricas de qualidade (acurácia, precisão, revocação, F1-score, etc)
- Interpretabilidade do modelo sugerido
- Storytelling dos dados, incluindo conclusões
- Potencial impacto e viabilidade da solução apresentada
- Criatividade da solução e apresentação
