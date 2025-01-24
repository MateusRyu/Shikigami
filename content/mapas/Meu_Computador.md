---
title: Meu Computador
tags:
  - v1.1
aliases:
  - Meu Computador
created_at: 2024-07-26T13:21:33-03:00
updated_at: 2025-01-24T00:42:20-03:00
---

Dual boot com a [Pasta home](content/atomos/2024/07/14/Pasta_home.md) compartilhada para ter um [Sistema Operacional](content/entrada/2024/08/04/Sistema_Operacional.md) de backup pra caso algo dê errado no [sistema](content/entrada/2024/08/04/Sistema_Operacional.md) principal.

---

## Particionamento
- `sda1`: `/boot/efi`
- `sda2`: `/` ([Crystal](content/atomos/2024/08/10/Crystal%20Linux.md))
- `sda3`: `/` ([NixOS]
- `sda4`: [SWAP](content/atomos/2024/07/14/SWAP.md)
-  `sda6`: `/home` 

## Crystal
- [Gnome](content/entrada/2024/08/10/Gnome.md)
- [Hyprland](content/entrada/2024/08/10/Hyprland.md)
	- Barra de status: [Waybar](content/entrada/2024/08/11/Waybar.md)
	- Notificação: [SwayNotificationCenter](content/entrada/2024/08/10/SwayNotificationCenter.md)
	- Wallpapers: [sww](content/entrada/2024/08/12/sww.md)
	- App launchers: [tofi](content/entrada/2024/08/11/tofi.md)
	- Color pickers: [Hyprpicker](content/entrada/2024/08/11/Hyprpicker.md)
	- Pipewire: [pipewire](content/entrada/2024/08/11/pipewire.md) e [wireplumber](content/entrada/2024/08/11/wireplumber.md)
	- Hyprland Desktop Portal: 
		- [xdg_desktop_portal_wlr](content/entrada/2024/08/11/xdg_desktop_portal_wlr.md)
		- [xdg_desktop_portal_hyprland](content/entrada/2024/08/11/xdg_desktop_portal_hyprland.md)
		- [xdg_desktop_portal_gtk](content/entrada/2024/08/11/xdg_desktop_portal_gtk.md)
	- Authentication Agent: [polkit_kde_agent](content/entrada/2024/08/11/polkit_kde_agent.md)
	- Qt Wayland Support: [qt5_wayland](content/entrada/2024/08/11/qt5_wayland.md) e [qt6_wayland](content/entrada/2024/08/11/qt6_wayland.md)