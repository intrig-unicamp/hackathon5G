# _Scripts_ auxiliares
> Essa pasta contém _scripts_ auxiliares diversos utilizados para produzir os conjuntos de dados disponibilizados

- [extract_youtube_qoe_urls](./extract_youtube_qoe_urls.py): Remove informações adicionais sensíveis de arquivos pcap, pcapng e har. As requisições são filtradas pelo URL do `youtube.com/api/stats/qoe`. Apenas a URL e _timestamp_ da requisição são mantidos.
- [youtube_qoe_urls_preprocessing](./youtube_qoe_urls_preprocessing.py): Trata os URLs do YouTube QoE em um formato mais fácil de manipular.

## Preparação do ambiente de execução
Os _scripts_ dessa pasta possuem requisitos de bibliotecas diferentes do repositório geral. Dessa forma, use o `environment.yml` dessa pasta para criar o ambiente.

1. Crie o ambiente a partir do arquivo `environment.yml`
    ```
    # se usar o Micromamba:
    micromamba env create -f environment.yml -y

    # se usar o Conda:
    conda env create -f environment.yml
    ```

2. Ative o ambiente
    ```
    # se usar o Micromamba:
    micromamba activate hackathon5G-scripts

    # se usar o Conda:
    conda activate hackathon5G-scripts
    ```
