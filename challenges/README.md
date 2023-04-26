# 🏋️‍♂️ Desafios
> Nessa pasta contém os desafios propostos para a _Hackathon SMARTNESS / 5G Dataset Challenge_

Como parte da Hackathon, os participantes deverão resolver o maior número possível dos desafios fornecidos a seguir.

> **Legenda**
> - 🤝: O desafio envolve correlação de atributos
> - 🔮: O desafio envolve predição
> - 📊: O foco do desafio está na visualização de dados
> - 🗂️: O uso de múltiplos conjuntos de dados é recomendados

- 📊 Visualização usando o paths-viewer

- 🔮 Predição de qualidade de sinal mono-variada
    Conjuntos de dados recomendados: `g-nettrack-pro`

- 🔮 Predição de qualidade de sinal multi-variada
    Conjuntos de dados recomendados: `g-nettrack-pro`
    (CQI, SNNR, xxx)

- 🔮 Predição do tipo de mobilidade
    Conjuntos de dados recomendados: `g-nettrack-pro`

- 🤝 Correlação de atributos

- 🔮🗂️ Inferir a qual ERB (estação rádio base) o celular está conectado

    Conjuntos de dados recomendados: `g-nettrack-pro` + `mosaico`

- 🔮🗂️ Predição da qualidade do sinal dadas as coordenadas do celular

    Conjuntos de dados recomendados: `g-nettrack-pro` + `mosaico`

- 🔮🗂️ Predição da qualidade do stream de vídeo de acordo com as coordenadas do celular

    Conjuntos de dados recomendados: `youtube-qoe-pcap` + `g-nettrack-pro` + `mosaico`

- 🔮🗂️ Predição da qualidade do stream de vídeo dada a qualidade do sinal

    Conjuntos de dados recomendados: `youtube-qoe-pcap` + `g-nettrack-pro`

- 🤝 Análise da tendências de construção e de características dos ERBs no Brasil. 

    Conjuntos de dados recomendados: `mosaico`


# 🤔 Critérios de avaliação

- Pré-processamento dos dados
- Representação dos dados e estratégia de composição de atributos
- Estratégia de seleção do modelo escolhido
- Estratégia de validação
- Qualidade do modelo em relação as métricas de qualidade (acurácia, precisão, revocação, F1-score, etc)
- Interpretabilidade do modelo sugerido
- Storytelling dos dados, incluindo conclusões
- Potencial impacto e viabilidade da solução apresentada.
