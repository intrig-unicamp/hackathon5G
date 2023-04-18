# Datasets
> Nessa pasta contém os conjuntos de dados disponibilizados para a _Hackathon SMARTNESS / 5G Dataset Challenge_

Para a Hackathon, foi feita a coleta de dados de utilização da rede 5G no Brasil. A metodologia de coleta de dados foi com base em testes de campo. Os experimentos foram conduzidos em um _Samsung S21 5G_.

Abaixo enumeramos os dois conjuntos de dados produzidos e um auxiliar. Cada conjunto de dados possui um Jupyter Notebook demonstrando uma exploração de dados inicial para os usuários conhecerem a estrutura dos dados.

# 🎬 Monitoramento do tráfego
O YouTube tem integrado nos seus diversos clientes (Web, Web Mobile, IFrame, e aplicativos iOS e Android) um instrumento de coleta de métricas de experiência do usuário. Analisamos o código do YouTube Web e identificamos as métricas monitoradas, as quais são iguais nos demais clientes. Os [dados iniciais](./youtube-qoe-har) desse experimento foram coletados pelo Chrome DevTools no formato HAR.

Para gerar os dados de tráfego no _Samsung S21 5G_, tocamos uma playlist com alta resolução no YouTube Web Mobile, e a interceptação das métricas de tráfego foi feita pelo [`PCAPdroid`](https://github.com/emanuele-f/PCAPdroid) e o plugin [`PCAPdroid-mitm`](https://github.com/emanuele-f/PCAPdroid-mitm) para descriptografar os pacotes SSL.

> 🛠️ Futuramente, será utilizado o aplicativo do YouTube para representar uma situação mais próxima da realidade dos clientes móveis. Por enquanto, isso ainda não foi feito porque o aplicativo do YouTube utiliza o protocolo QUIC, que não é suportado pela versão atual do plugin, mas será suportado na [próxima versão](https://github.com/mitmproxy/mitmproxy/blob/main/CHANGELOG.md).

- [Dados `youtube-qoe-pcap`](./youtube-qoe-pcap) (coletado pelo PCAPdroid)
- [Dados `youtube-qoe-har`](./youtube-qoe-har) (coletado pelo Chrome DevTools)
- [Exploração de dados / Jupyter Notebook](./youtube-qoe.ipynb)

# 📶 Monitoramento da rede móvel
As métricas de rede foram coletadas pela ferramenta [G-NetTrack Pro](https://gyokovsolutions.com/manual-g-nettrack/) em um trajeto com cobertura 5G da operadora Claro, como por exemplo, pelo centro de São Paulo, Av. Paulista, Butantã, e arredores.

- [Dados `g-nettrack-pro`](./g-nettrack-pro)
- [Exploração de dados / Jupyter Notebook](./g-nettrack-pro.ipynb)

# 📡 ERBs Mosaico/Anatel (auxiliar)
Em conjunto com os dados de tráfego e rede móvel, também podemos fazer o **enriquecimento de dados** com outros datasets, como por exemplo, o Mosaico da Anatel, que contém informações sobre todas as estações de telecomunicações (ERBs) registradas no Brasil. Entre os dados armazenados no Mosaico estão informações sobre os proprietários das estações, as tecnologias e equipamentos utilizados, as frequências de transmissão e recepção, a localização geográfica das estações e as datas de licenciamento e validade.

- [Dados `mosaico`](./mosaico)
- [Exploração de dados / Jupyter Notebook](./mosaico.ipynb)
