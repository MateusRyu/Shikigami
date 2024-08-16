---
title: Meu Computador
tags:
  - v1
aliases:
  - Meu Computador
created_at: 2024-07-26T13:21:33-03:00
updated_at: 2024-08-16T14:07:17-03:00
---

Dual boot com a [Pasta home](../ideias/2024/07/14/Pasta_home.md) compartilhada para ter um [Sistema Operacional](../sementes/2024/07/07/Sistema_Operacional.md) de backup pra caso algo dê errado no [sistema](../sementes/2024/07/07/Sistema_Operacional.md) principal.

---

## Particionamento
- `sda1`: `/boot/efi`
- `sda2`: `/` ([Crystal](../rascunhos/2024/08/10/Crystal%20Linux.md))
- `sda3`: `/` ([Arco Linux](../sementes/2024/07/07/Arco_Linux.md))
- `sda4`: [SWAP](../ideias/2024/07/14/SWAP.md)
-  `sda6`: `/home` 

## Crystal
- [Gnome](../ideias/2024/08/10/Gnome.md)
- [Hyprland](../ideias/2024/08/10/Hyprland.md)
	- Barra de status: [Waybar](../ideias/2024/08/11/Waybar.md)
	- Notificação: [SwayNotificationCenter](../ideias/2024/08/10/SwayNotificationCenter.md)
	- Wallpapers: [sww](sww)
	- App launchers: [tofi](../ideias/2024/08/11/tofi.md)
	- Color pickers: [Hyprpicker](../ideias/2024/08/11/Hyprpicker.md)
	- Pipewire: [pipewire](../ideias/2024/08/11/pipewire.md) e [wireplumber](../ideias/2024/08/11/wireplumber.md)
	- Hyprland Desktop Portal: 
		- [xdg-desktop-portal-wlr](../ideias/2024/08/11/xdg-desktop-portal-wlr.md)
		- [xdg-desktop-portal-hyprland](../ideias/2024/08/11/xdg-desktop-portal-hyprland.md)
		- [xdg-desktop-portal-gtk](../ideias/2024/08/11/xdg-desktop-portal-gtk.md)
	- Authentication Agent: [polkit-kde-agent](../ideias/2024/08/11/polkit-kde-agent.md)
	- Qt Wayland Support: [qt5-wayland](../ideias/2024/08/11/qt5-wayland.md) e [qt6-wayland](../ideias/2024/08/11/qt6-wayland.md)