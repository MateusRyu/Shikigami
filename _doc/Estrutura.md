---
title: Estrutura dos arquivos
chapter: 0
group: Filosofia
created_at: 2024-09-04T22:50:26-03:00
updated_at: 2024-10-08T15:31:35-03:00
---

A estrutura de arquivos não precisa ser fixo e padronizado para todo mundo. O importante é entender qual a ideia geral para se criar uma estrutura de pastas que faça sentido para permitir que você gaste menos tempo pensando em qual pasta cada documento deveria ir, além de entender o minimo das questões técnicas associados para a gestão dos arquivos (para que o [Software](../api/entrada/2024/07/26/Software.md) continue eficiente e não te atrapalhe). E está tudo bem se não souber qual a estrutura ideal para você, a estrutura ideal é aquela que te permite capturar e conectar ideias de forma eficiente e intuitiva, mas você vai precisar experimentar e avaliar o que te serve melhor para tornar o seu [Shikigami](../api/sementes/2024/07/07/Shikigami.md) no seu verdadeiramente familiar. Aqui, irei descrever uma sugestão de estrutura de arquivos desenvolvida pensando na filosofia do [Shikigami](../api/sementes/2024/07/07/Shikigami.md), a estrutura de pastas do [Zettelkasten](../api/atomos/2024/07/12/Zettelkasten.md) e a estrutura de pastas do [Método PARA](../Metodo_PARA.md) para que você possa ter como referencia e adaptar ao seu contexto.


## Estruturas
### Shikigami

Esta estrutura prioriza que os arquivos sejam mais fixos em suas pastas de criação para evitar problemas na quebra de links entre os arquivos. Por mais que algumas ferramentes, como o [Obsidian](../api/sementes/2024/07/08/Obsidian.md), tenham algum meio para auxiliar a manutenção dos links ao mover arquivos, falhas podem ocorrer eventualmente e essa funcionalidade pode fazer com que você dependa de ferramentas especificas. Desta forma, uma estrutura de pastas em que os documentos sejam fixos auxiliam na manutenção do documento. 

Entretanto, como ponto negativo, essa fixação dos documentos vai criar a necessidade de contornar a sua falta de rastreabilidade e de controle de publicação por meio de [metadados](../Metadados) e arquivos auxiliares. Isso é um contra a ser considerado para a sua preferencia pessoal, apesar que não é realmente um grande problema, visto que essa estrutura permite que cada nota seja mais independente e a manutenção dos documentos se concentre mais nos metadados, que tem uma estrutura previsível e de rápida visualização, o que facilita a criação de algoritmos para auxiliar nessa manutenção. O contrapartida, a manutenção de links é mais trabalhosa pois é mais difícil de prever a movimentação dos arquivos e aumenta a chance de existir arquivos duplicados, que por sua vez dificulta ainda mais a manutenção.

- **Entrada:** Serve como um repositório para informações externas, como artigos, citações, pessoas ou qualquer obra externa. Essa separação inicial permite que você centralize todas as suas referências em um único local.
- **Retorno:** É um espaço dedicado à reflexão e análise crítica das informações coletadas na pasta "Entrada". Essa separação incentiva a internalização do conhecimento e a formação de suas próprias ideias, permitindo a diversidade ideológica sem que você precise concordar com todas.
- **Átomos:** Pasta para armazenar notas curtas e independentes. É um lugar para registrar ideias, observações e definições de termos de forma concisa.
- **Mapas:** Pasta para armazenar os [MOC's](../MOC.md) (sigla para "Maps Of Contents", que significa "Mapas de conteúdo"). Cada [MOC](../MOC.md) serve para mapear documentos que você gostaria de rastrear para que tenha um rápido acesso para consulta.
- **Diário:** Um espaço pessoal para registrar experiências, pensamentos e sentimentos. Essa separação mantém suas notas mais íntimas separadas das informações mais objetivas.
- **Segredos:** Uma pasta dedicada para informações que você quer anotar para si mesmo mas definitivamente não quer que seja exposto. Essa pasta já é uma contra-medida para aumentar a segurança das suas notas sem te restringir. Pode ser marcado no seu sistema de backup/publicação para ser ignorado.

### Sub estrutura
Opcionalmente, você pode adotar, em cada pasta, uma estrutura de pastas de `./ano/mês/dia/` para reduzir a quantidade de arquivos soltos, em que o `ano`, `mês` e `dia` são referentes à data de criação do arquivo, visto que esta é uma informação inata de cada documento e essa divisão temporal ajuda a diminuir o sobrecarregamento das pasta e é uma estrutura bem previsível. Reduzir a quantidade de arquivos soltos, apesar de aumentar a complexidade da estrutura, pode melhorar o desempenho dos [softwares](../api/entrada/2024/07/26/Software.md) que vão utilizar e manipular o projeto.

## Dicas
- **Comece simples:** Não se preocupe em criar uma estrutura perfeita desde o início. Adapte-a conforme suas necessidades evoluem.
- **Seja consistente:** Mantenha uma nomenclatura clara e consistente para facilitar a organização e a pesquisa.
- **Experimente:** Não tenha medo de experimentar diferentes estruturas até encontrar aquela que funciona melhor para você.