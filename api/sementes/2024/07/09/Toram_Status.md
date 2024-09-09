---
title: Status
tags:
  - v1
aliases:
  - Status
  - status
created_at: 2024-07-26T13:21:33-03:00
updated_at: 2024-09-09T10:41:51-03:00
---

No [Toram](../../../../atomos/2024/07/26/Toram.md), o status é a base matemática para o jogo calcular todas as interações de batalha no jogo, que inclui danos, velocidade de ataque, velocidade de conjuração e entre outros. Os status são os dados que o jogador pode distribuir para cada vez que ele aumentar de nível ou através de recompensas no jogo.

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
 - Personagem tem 255 de [STR](Toram_STR.md);
 - Armadura tem 8% de [STR](Toram_STR.md);
 - Arma tem -1% de [STR](Toram_STR.md);
 - Buff de comida [STR](Toram_STR.md)+18;

1. Soma dos modificadores percentual = 8% - 1% = 7%
2. Valor com modificadores percentual = 255 * 107% = 272.85
3. Valor arredondado para baixo = 272
4. Valor com modificador puro = 272 + 18 = 290

==STR = 290==

### Status percentual

Alguns status já são valores percentuais (exemplo: [Guard Rate](../../../../ideias/2024/07/09/Toram_Guard_Rate.md), [Guard Power](../../../../ideias/2024/07/09/Toram_Guard_Power.md), [Evasion Rate](../../../../ideias/2024/07/09/Toram_Evasion_Rate.md)). Nesses casos, basta somar todos os valores!

### Calculo final

Alguns status dependem de outros status, então é necessário um calculo na ordem certa! Por exemplo, [Critical Damage](../../../../ideias/2024/07/09/Toram_Critical_Damage.md) é calculado baseado no [STR](Toram_STR.md), então será necessário calcular o [STR](Toram_STR.md) primeiro par poder usar no calculo do [Critical Damage](../../../../ideias/2024/07/09/Toram_Critical_Damage.md).  

Para fins didáticos, os jogadores separaram os status em algumas categorias:
1. [Status básico](../26/Toram_Status_basico.md): Aqueles que podem ser adicionados ao aumentar de level;
2. [Status de equipamento](../../../../ideias/2024/07/09/Toram_Status_de_equipamento.md): ATK da arma, Equipment DEF, Weapon Stability, Refinement Resistance
3. [Status derivados](../../../../ideias/2024/07/09/Toram_Status_derivados.md): Status que se derivam dos [Status básicos](../26/Toram_Status_basico.md).
4. [Status não-derivados](../../../../ideias/2024/07/09/Toram_Status%20não-derivados.md): Aqueles obtidos exclusivamente de equipamentos ou habilidade.
5. [Status Especial](../../../../ideias/2024/07/09/Toram_Status_Especial.md): Status que não se encaixam nas classificações anteriores.

Por exemplo, digamos que queremos calcular o valor de [ATK](../../../../ideias/2024/07/09/Toram_ATK.md) para o usuário da [Espada de uma mão](../../../../ideias/2024/07/12/Toram_One_Handed_Sword.md). Este status é baseada em ([Status básicos](../26/Toram_Status_basico.md)) [STR](Toram_STR.md) e [DEX](../../../../ideias/2024/07/09/Toram_DEX.md) e ([Status de equipamento](../../../../ideias/2024/07/09/Toram_Status_de_equipamento.md)) [ATK](../../../../ideias/2024/07/09/Toram_ATK.md). Portanto os passos serão os seguintes:
1. Pegue [STR](Toram_STR.md) e [DEX](../../../../ideias/2024/07/09/Toram_DEX.md) originais. Aplique o modificador [STR](Toram_STR.md)% e [DEX](../../../../ideias/2024/07/09/Toram_DEX.md)% a eles.
2. Aplique o modificador plano [STR](Toram_STR.md)+ e [DEX](../../../../ideias/2024/07/09/Toram_DEX.md)+ ao resultado de (1), obtemos [STR](Toram_STR.md) final e [DEX](../../../../ideias/2024/07/09/Toram_DEX.md) final.
3. Pegue o [ATK](../../../../ideias/2024/07/09/Toram_ATK.md) da arma e calcule seu bônus de refinamento.
4. Pegue o [ATK](../../../../ideias/2024/07/09/Toram_ATK.md) da arma, aplique o [ATK](../../../../ideias/2024/07/09/Toram_ATK.md)% da arma e o modificador do [ATK](../../../../ideias/2024/07/09/Toram_ATK.md)+ da arma a ele.
5. Somando (3) e (4), obtemos o [ATK](../../../../ideias/2024/07/09/Toram_ATK.md) final da arma.
6. Calcule o [ATK](../../../../ideias/2024/07/09/Toram_ATK.md) a partir do nível do personagem, resultado de (2) e (5).
7. Aplique [ATK](../../../../ideias/2024/07/09/Toram_ATK.md)% e [ATK](../../../../ideias/2024/07/09/Toram_ATK.md)+ em (6), obtemos o [ATK](../../../../ideias/2024/07/09/Toram_ATK.md) final.

![Toram_status.excalidraw](../../../../../_excalidraw/Toram_status.excalidraw.md)

## Referencia
---
[Coryn Club](https://coryn.club/guide.php?key=status)


