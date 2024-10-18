---
title: Migrando para o Hyprland
tags:
  - v1.1
aliases:
  - 2024/08/09
  - 09/08/2024
  - 2024-08-09
created_at: 2024-08-09T14:46:39-03:00
updated_at: 2024-10-17T17:39:51-03:00
---
## Tarefas

- [x] Configurar gerenciador de ferramentas
- [x] Configurar hyprland
- [x] Configurar syncthing

## Reflexão

[Tiling Window Manager](api/atomos/2024/08/10/Tiling_Window_Manager.md) (TWM) tem uma proposta de fluxo de trabalho que me atrai pois, em geral, eu não precisaria organizar as janelas manualmente. As janelas ocultas deveria significar que eu não quero aquela janela (pelo menos na mesma área de trabalho) onde estou usando o computador. O layout e redimensionamento das janelas deveriam seguir uma certa proporção que pode ser calculado, o que facilita que eu tenha que manualmente dimensionar todas elas e organiza-las. Eu entendo que um TWM pode não ser pra todo mundo pois requer um reaprendizado de como utilizar o computador, mas ao meu ver as suas vantagens e a sua leveza (já que eles desenham menos objetos na tela) é uma grande vantagem.

O [Hyprland](api/entrada/2024/08/10/Hyprland.md) me chamou a atenção por causa da sua performance e beleza (sem precisar de muita configuração). Ele também utiliza o [Wayland](api/entrada/2024/08/17/Wayland.md)  que é um compositor de janelas mais modernos, o que traz ganhos de performance mas pode perder compatibilidades com alguns [Softwares](api/entrada/2024/07/26/Software.md), entretanto atualmente tem ganhado popularidade e o problema de compatibilidade tem se reduzindo.