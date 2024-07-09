---
layout: post
title: Status
created_at: 2024-07-09T00:20:55-03:00
tags:
  - v0
aliases:
  - Status
  - status
---
# Status
---

> [!note] Observação
> As informações são baseados no que os jogadores descobriram e alguma informação pode não estar certo!

Status é a base matemática para o jogo calcular todas as interações de batalha no jogo, que inclui danos, velocidade de ataque, velocidade de conjuração e entre outros. Os status são os dados que o jogador pode distribuir para cada vez que ele aumentar de nível ou através de recompensas no jogo.
## Calculo do status total
---

### Regra geral
---
 - Para todos os casos, o calculo básico sempre segue a ordem: 
	1. Calcula a soma dos modificadores percentual;
	2. Aplica os modificadores percentual;
	3. Arredonda o valor para baixo;
	4. Aplica os modificadores puros.

#### Exemplo
 - Personagem tem 255 de [STR](2024-07-09-Toram_STR.md);
 - Armadura tem 8% de [STR](2024-07-09-Toram_STR.md);
 - Arma tem -1% de [STR](2024-07-09-Toram_STR.md);
 - Buff de comida [STR](2024-07-09-Toram_STR.md)+18;

1. Soma dos modificadores percentual = 8% - 1% = 7%
2. Valor com modificadores percentual = 255 * 107% = 272.85
3. Valor arredondado para baixo = 272
4. Valor com modificador puro = 272 + 18 = 290

==STR = 290==

### Status percentual
---
Alguns status já são valores percentuais (exemplo: [Guard Rate](2024-07-09-Toram_Guard_Rate.md), [Guard Power](2024-07-09-Toram_Guard_Power.md), [Evasion Rate](2024-07-09-Toram_Evasion_Rate.md)). Nesses casos, basta somar todos os valores!

## Referencia
---
[Coryn Club](https://coryn.club/guide.php?key=status)


