---
title: Meu Computador
tags:
  - v1
aliases:
  - Meu Computador
created_at: 2024-07-26T13:21:33-03:00
updated_at: 2024-08-11T00:45:55-03:00
---

Dual boot com a [Pasta home](../ideias/2024/07/14/Pasta_home.md) compartilhada para ter um [Sistema Operacional](../sementes/2024/07/07/2024-06-30-Sistema_Operacional.md) de backup pra caso algo dê errado no [sistema](../sementes/2024/07/07/2024-06-30-Sistema_Operacional.md) principal.

---

## Particionamento
- `sda1`: `/boot/efi`
- `sda2`: `/` ([Crystal](../rascunhos/2024/08/10/Crystal%20Linux.md))
- `sda3`: `/` ([Arco Linux](../sementes/2024/07/07/2024-07-07-Arco_Linux.md))
- `sda4`: [SWAP](../ideias/2024/07/14/SWAP.md)
-  `sda6`: `/home` 

## Crystal
- [Gnome](../ideias/2024/08/10/Gnome.md)
- [Hyprland](../ideias/2024/08/10/Hyprland.md)
	- Barra de status: [Waybar](../ideias/2024/08/11/Waybar.md)
	- Notificação: [SwayNotificationCenter](../ideias/2024/08/10/SwayNotificationCenter.md)
	- Wallpapers: [hyprpaper](../ideias/2024/08/11/hyprpaper.md)
	- App launchers: [tofi](../ideias/2024/08/11/tofi.md)
	- Color pickers: [Hyprpicker](../ideias/2024/08/11/Hyprpicker.md)
	- Pipewire: [pipewire](pipewire) e [wireplumber](wireplumber)
	- Hyprland Desktop Portal: 
		- [xdg-desktop-portal-wlr](xdg-desktop-portal-wlr)
		- [xdg-desktop-portal-hyprland](xdg-desktop-portal-hyprland)
		- [xdg-desktop-portal-gtk](xdg-desktop-portal-gtk)
	- Authentication Agent: [polkit-kde-agent](polkit-kde-agent)
	- Qt Wayland Support: [qt5-wayland](qt5-wayland) e [qt6-wayland](qt6-wayland)