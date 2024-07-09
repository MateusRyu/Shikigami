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

### Calculo final
---
Alguns status dependem de outros status, então é necessario um calculo na ordem certa! Por exemplo, [Critical Damage](2024-07-09-Toram_Critical_Damage.md) é calculado baseado no [STR](2024-07-09-Toram_STR.md), então será necessario calcular o [STR](2024-07-09-Toram_STR.md) primeiro par poder usar no calculo do [Critical Damage](2024-07-09-Toram_Critical_Damage.md).  

Para fins didáticos, os jogadores separaram os status em algumas categorias:
1. [Status básico](2024-07-09-Toram_Status_basico.md): Aqueles que podem ser adicionados ao aumentar de level;
2. [Status de equipamento](2024-07-09-Toram_Status_de_equipamento.md): ATK da arma, Equipment DEF, Weapon Stability, Refinement Resistance
3. **Derived Stat:** Those derived from basic stat, such as ATK, HIT, Critical, etc.
4. **Non-Derived Stat:** Those obtained from equipment/skill only, such as Aggro, Evasion, etc.
5. **Special:** AMPR, Motion Speed, Unsheathe Attack

For example, let say we want to calculate ATK value for One-Handed Sword user. This stat is based on _basic stat STR and DEX_, and _Equipment Stat WeaponATK_. So the steps will be as follows:

1. Take original STR and DEX. Apply STR% & DEX% modifier to them.
2. Apply STR+ and DEX+ flat modifier to result of (1), we get final STR and final DEX.
3. Take weaponATK, calculate its refinement bonus.
4. Take weaponATK, Apply weaponATK% and weaponATK+ modifier to it.
5. Adds up (3) and (4), we get final WeaponATK.
6. Calculate ATK from char's level, result of (2) and (5).
7. Apply ATK% and ATK+ to (6), we get final ATK.
## Referencia
---
[Coryn Club](https://coryn.club/guide.php?key=status)


