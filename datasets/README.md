# Datasets
> Essa pasta contém os conjuntos de dados disponibilizados para a _Hackathon SMARTNESS / 5G Dataset Challenge_

Para a Hackathon, foi feita a coleta de dados de utilização da rede 5G no Brasil. A metodologia de coleta de dados foi com base em testes de campo. Os experimentos foram conduzidos em um _Samsung S21 5G_.

Abaixo, enumeramos os dois conjuntos de dados produzidos e um auxiliar. Cada conjunto de dados possui um Jupyter Notebook demonstrando uma exploração de dados inicial para os participantes conhecerem a estrutura dos dados.

# 🎬 Monitoramento do tráfego
O YouTube tem integrado nos seus diversos clientes (Web, Web Mobile, IFrame, e aplicativos iOS e Android) um instrumento de coleta de métricas de experiência do usuário. Para identificar as métricas monitoradas (as quais são iguais nos demais clientes), analisamos o código do YouTube Web e as coletas de requisições em HAR pelo Chrome DevTools.

Para gerar os dados de tráfego no _Samsung S21 5G_, reproduzimos uma playlist com vídeos de alta resolução no YouTube Web Mobile, e a interceptação das métricas de tráfego foi feita pelo [`PCAPdroid`](https://github.com/emanuele-f/PCAPdroid) e o plugin [`PCAPdroid-mitm`](https://github.com/emanuele-f/PCAPdroid-mitm) para descriptografar os pacotes TLS.

> 🛠️ Futuramente, o experimento vai utilizar o aplicativo do YouTube para representar uma situação mais próxima da realidade dos clientes móveis. Por enquanto, isso ainda não foi feito porque o aplicativo do YouTube utiliza o protocolo QUIC, que não é suportado pela versão atual do plugin, mas será suportado na [próxima versão](https://github.com/mitmproxy/mitmproxy/blob/main/CHANGELOG.md#unreleased-mitmproxy-next).

- [Dados `youtube-qoe`](./youtube-qoe) (coletas do PCAPdroid)
- [Exploração de dados / Jupyter Notebook](./youtube-qoe.ipynb)

<details>
<summary><b>Como coletar os dados usando o PCAPdroid</b></summary>

## Configurar a descriptografia TLS
- Na seção *Traffic inspection* nas configurações do PCAPdroid (ícone ⚙️ no canto superior direito), habilite *TLS decryption*
- Na primeira vez que a descriptografia for habilitada, será aberto o menu para configuração do plugin. Os passos incluem:
    1. Baixar e instalar o addon `PCAPdroid-mitm`
    2. Autorizar o PCAPdroid a controlar o addon
    3. Instalar o certificado de autoridade (CA) do PCAPdroid

## Configuração inicial
- Na seção _Traffic inspection_ nas configurações do PCAPdroid (ícone ⚙️ no canto superior direito), desabilite a opção _Full payload_
- Na seção _Capture_ nas configurações do PCAPdroid, habilite a opção _PCAPdroid trailer_
- Defina o formato da captura de tráfego (_traffic dump format_) como _PCAP file_
- Selecione o aplicativo que vai capturar o tráfego (nesse caso, o navegador que vai abrir o YouTube Web Mobile. Exemplo: Google Chrome, Firefox, Samsung Internet)

## Capturar e exportar
- Entre no aplicativo PCAPdroid
- Selecione _Ready_
- Inicie a geração de tráfego. Nesse momento, é possível sair do aplicativo
- ...
- Para finalizar a captura de tráfego, entre novamente no PCAPdroid
- Pressione o botão de parar (ícone ⬜ no canto superior direito)
- Pressione _OK_ no diálogo informando que o tráfego foi salvo
- Se for gerado um arquivo com chaves SSL `sslkeylogfile.txt`, um diálogo será aberto para salvá-lo:
    - Vá para a pasta na qual o arquivo derá ser salvo, como em `~/Download/PCAPdroid` (o mesmo local que as capturas PCAP são salvas)
    - Selecione o arquivo de captura PCAP mais recente para copiar seu nome (para facilitar a identificação posterior)
    - Edite a extensão `.pcap` para `.txt` do arquivo a ser salvo
    - Salve

## Juntar `sslkeylogfile.txt` e `.pcap` em um único arquivo `.pcapng`

Para juntar os dois arquivos `sslkeylogfile.txt` e `.pcap` em um único arquivo `.pcapng`, podemos utilizar o programa de linha de comando `editcap` (que pode ser obtido ao instalar o `tshark`).

Se o arquivo de chaves SSL e PCAP possuem o mesmo nome, basta usar uma variável com o nome da captura:
```bash
filename=PCAPdroid_17_Feb_02_19_56
editcap --inject-secrets tls,${filename}.txt ${filename}.pcap ${filename}.pcapng
```

Alternativamente, podemos informar os diferentes nomes individualmente:
```bash
editcap --inject-secrets tls,sslkeylogfile_abc.txt captura_abc.pcap captura_e_sslkeys_abc.pcapng
```

Ao obter os arquivos `.pcapng`, fazemos o pré-processamento para um formato mais fácil de utilizar. Para isso, executamos os [_scripts_](../scripts/) abaixo:
```bash
# transforma arquivos .pcapng para .json
./scripts/extract_youtube_qoe_urls.py -g '*.pcapng'

# transforma arquivos .json para Dataframes pandas no formato .pickle
./scripts/youtube_qoe_urls_preprocessing.py -g '*.json'
```

</details>

# 📶 Monitoramento da rede móvel
As métricas de rede foram coletadas pela ferramenta G-NetTrack Pro ([manual](https://gyokovsolutions.com/manual-g-nettrack/#:~:text=Here%20is%20description%20of%20logfile%20columns)) em um trajeto com cobertura 5G da operadora Claro, como por exemplo, pelo centro de São Paulo, Av. Paulista, Butantã, e arredores.

- [Dados `g-nettrack`](./g-nettrack-pro)
- [Exploração de dados / Jupyter Notebook](./g-nettrack-pro.ipynb)

# 📡 ERBs Mosaico/Anatel (auxiliar)
Em conjunto com os dados de tráfego e rede móvel, também podemos fazer o **enriquecimento de dados** com outros datasets, como por exemplo, usando o Mosaico da Anatel, que contém informações sobre todas as estações de telecomunicações (ERBs) registradas no Brasil. Dentre os dados disponibilizados pelo Mosaico, incluem: as tecnologias e equipamentos utilizados, as frequências de transmissão e recepção, a localização geográfica das estações, as datas de licenciamento e validade, informações sobre os proprietários das estações, entre outras.

- [Dados `mosaico`](./mosaico)
- [Exploração de dados / Jupyter Notebook](./mosaico.ipynb)
