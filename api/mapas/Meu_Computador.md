---
title: Meu Computador
tags:
  - v1
aliases:
  - Meu Computador
created_at: 2024-07-26T13:21:33-03:00
updated_at: 2024-08-10T01:57:12-03:00
---

Dual boot com a [Pasta home](../ideias/2024/07/14/Pasta_home.md) compartilhada para ter um [Sistema Operacional](../sementes/2024/07/07/2024-06-30-Sistema_Operacional.md) de backup pra caso algo dê errado no [sistema](../sementes/2024/07/07/2024-06-30-Sistema_Operacional.md) principal.

---

## Particionamento
- `sda1`: `/boot/efi`
- `sda2`: `/` ([Crystal](Crystal%20Linux))
- `sda3`: `/` ([Arco Linux](../sementes/2024/07/07/2024-07-07-Arco_Linux.md))
- `sda4`: [SWAP](../ideias/2024/07/14/SWAP.md)
-  `sda6`: `/home` 

## Crystal
- [Gnome](../../Gnome.md)
- [Hyprland](Hyprland)
	- Barra de status: [[Waybar]]
	- Notificação: [[SwayNotificationCenter]]
	- Wallpapers: [[hyprpaper]]
	- App launchers: [[tofi]]
	- Color pickers: [[Hyprpicker]]
	- Pipewire: [[pipewire]] e [[wireplumber]]
	- Hyprland Desktop Portal: 
		- [[xdg-desktop-portal-wlr]]
		- [[xdg-desktop-portal-hyprland]]
		- [[xdg-desktop-portal-gtk]]
	- Authentication Agent: [[polkit-kde-agent]]
	- Qt Wayland Support: [[qt5-wayland]] e [[qt6-wayland]]