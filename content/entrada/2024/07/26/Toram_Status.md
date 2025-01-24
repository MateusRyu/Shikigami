---
title: Status
tags:
  - v1.1
aliases:
  - Status
created_at: 2024-07-26T13:21:33-03:00
updated_at: 2025-01-24T00:31:16-03:00
---

No [Toram](content/entrada/2024/07/26/Toram.md), o status é a base matemática para o jogo calcular todas as interações de batalha no jogo, que inclui danos, velocidade de ataque, velocidade de conjuração e entre outros. Os status são os dados que o jogador pode distribuir para cada vez que ele aumentar de nível ou através de recompensas no jogo.

> [!note] Observação
> As informações são baseados no que os jogadores descobriram e alguma informação pode não estar certo!

---

## Calculo do status total
### Regra geral

 - Para todos os casos, o calculo básico sempre segue a ordem: 
	1. Calcula a soma dos modificadores percentual;
	2. Aplica os modificadores percentual;
	3. Arredonda o valor para baixo;
	4. Aplica os modificadores puros.

Por exemplo:
 - Personagem tem 255 de [STR](content/entrada/2024/07/26/Toram_STR.md);
 - Armadura tem 8% de [STR](content/entrada/2024/07/26/Toram_STR.md);
 - Arma tem -1% de [STR](content/entrada/2024/07/26/Toram_STR.md);
 - Buff de comida [STR](content/entrada/2024/07/26/Toram_STR.md)+18;

1. Soma dos modificadores percentual = 8% - 1% = 7%
2. Valor com modificadores percentual = 255 * 107% = 272.85
3. Valor arredondado para baixo = 272
4. Valor com modificador puro = 272 + 18 = 290

==STR = 290==

### Status percentual

Alguns status já são valores percentuais (exemplo: [Guard Rate](content/entrada/2024/07/09/Toram_Guard_Rate.md), [Guard Power](content/entrada/2024/07/09/Toram_Guard_Power.md), [Evasion Rate](content/entrada/2024/07/09/Toram_Evasion_Rate.md)). Nesses casos, basta somar todos os valores!

### Calculo final

Alguns status dependem de outros status, então é necessário um calculo na ordem certa! Por exemplo, [Critical Damage](content/entrada/2024/07/09/Toram_Critical_Damage.md) é calculado baseado no [STR](content/entrada/2024/07/26/Toram_STR.md), então será necessário calcular o [STR](content/entrada/2024/07/26/Toram_STR.md) primeiro par poder usar no calculo do [Critical Damage](content/entrada/2024/07/09/Toram_Critical_Damage.md).  

Para fins didáticos, os jogadores separaram os status em algumas categorias:
1. [Status básico](content/entrada/2024/07/26/Toram_Status_basico.md): Aqueles que podem ser adicionados ao aumentar de level;
2. [Status de equipamento](content/entrada/2024/07/09/Toram_Status_de_equipamento.md): ATK da arma, Equipment DEF, Weapon Stability, Refinement Resistance
3. [Status derivados](content/entrada/2024/07/09/Toram_Status_derivados.md): Status que se derivam dos [Status básicos](content/entrada/2024/07/26/Toram_Status_basico.md).
4. [Status não-derivados](content/entrada/2024/07/09/Toram_Status%20não-derivados.md): Aqueles obtidos exclusivamente de equipamentos ou habilidade.
5. [Status Especial](content/entrada/2024/07/09/Toram_Status_Especial.md): Status que não se encaixam nas classificações anteriores.

Por exemplo, digamos que queremos calcular o valor de [ATK](content/entrada/2024/07/09/Toram_ATK.md) para o usuário da [Espada de uma mão](content/entrada/2024/07/12/Toram_One_Handed_Sword.md). Este status é baseada em ([Status básicos](content/entrada/2024/07/26/Toram_Status_basico.md)) [STR](content/entrada/2024/07/26/Toram_STR.md) e [DEX](content/entrada/2024/07/09/Toram_DEX.md) e ([Status de equipamento](content/entrada/2024/07/09/Toram_Status_de_equipamento.md)) [ATK](content/entrada/2024/07/09/Toram_ATK.md). Portanto os passos serão os seguintes:
1. Pegue [STR](content/entrada/2024/07/26/Toram_STR.md) e [DEX](content/entrada/2024/07/09/Toram_DEX.md) originais. Aplique o modificador [STR](content/entrada/2024/07/26/Toram_STR.md)% e [DEX](content/entrada/2024/07/09/Toram_DEX.md)% a eles.
2. Aplique o modificador plano [STR](content/entrada/2024/07/26/Toram_STR.md)+ e [DEX](content/entrada/2024/07/09/Toram_DEX.md)+ ao resultado de (1), obtemos [STR](content/entrada/2024/07/26/Toram_STR.md) final e [DEX](content/entrada/2024/07/09/Toram_DEX.md) final.
3. Pegue o [ATK](content/entrada/2024/07/09/Toram_ATK.md) da arma e calcule seu bônus de refinamento.
4. Pegue o [ATK](content/entrada/2024/07/09/Toram_ATK.md) da arma, aplique o [ATK](content/entrada/2024/07/09/Toram_ATK.md)% da arma e o modificador do [ATK](content/entrada/2024/07/09/Toram_ATK.md)+ da arma a ele.
5. Somando (3) e (4), obtemos o [ATK](content/entrada/2024/07/09/Toram_ATK.md) final da arma.
6. Calcule o [ATK](content/entrada/2024/07/09/Toram_ATK.md) a partir do nível do personagem, resultado de (2) e (5).
7. Aplique [ATK](content/entrada/2024/07/09/Toram_ATK.md)% e [ATK](content/entrada/2024/07/09/Toram_ATK.md)+ em (6), obtemos o [ATK](content/entrada/2024/07/09/Toram_ATK.md) final.

![Toram_status.excalidraw](../../../../../_excalidraw/Toram_status.excalidraw.md)

## Referencia
---
[Coryn Club](https://coryn.club/guide.php?key=status)


