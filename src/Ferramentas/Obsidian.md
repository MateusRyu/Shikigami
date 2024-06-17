É um [Software](Software) para anotação e organização de ideias baseado em [Grafos](Grafos). As anotações são escritos com [Markdown](Markdown.md). Apesar de herdar varias [Sintaxe](Sintaxe) do [Markdown](Markdown.md), o Obsidian tem algumas usadas para criar conexões (_links_) entre os documentos para poder criar os grafos.

## Sintaxe

![Cabeçalho](Markdown#Cabeçalho)

![Lista](Markdown#Lista)
### Link
#### Link interno
##### Wikilink
```md
[[Nome do documento]]
[[Nome do documento#Cabeçalho da seção]]
[[Nome do documento#^ID_do_Bloco]]
```
##### Markdown
```md
[Nome do documento](Nome%20do%20documento.md)
[Nome do documento](Nome%20do%20documento.md#Cabeçalho%20da%20seção)
[Nome do documento](Nome%20do%20documento.md#^ID_do_bloco)
```

> Observação: É preciso seguir a [codificação URL](Codificação%20URL) para o caminho de onde está localizado o arquivo que o link se refere!
#### Apelido
```md
[[Nome do documento|apelido usado para exibição do texto]]
[[Nome do documento#Cabeçalho da seção|apelido usado para exibição do texto]]
```

#### Embed
![Explicação do que é Embed](Embed.md#^9a9d4c)

# Daily notes

## Plugins 

- calendário
- obsidian git
- excalidraw