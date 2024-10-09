---
title: Meu Computador
tags:
  - v1.1
aliases:
  - Meu Computador
created_at: 2024-07-26T13:21:33-03:00
updated_at: 2024-10-09T16:57:28-03:00
---

Dual boot com a [Pasta home](../atomos/2024/07/14/Pasta_home.md) compartilhada para ter um [Sistema Operacional](../entrada/2024/08/04/Sistema_Operacional.md) de backup pra caso algo dê errado no [sistema](../entrada/2024/08/04/Sistema_Operacional.md) principal.

---

## Particionamento
- `sda1`: `/boot/efi`
- `sda2`: `/` ([Crystal](../atomos/2024/08/10/Crystal%20Linux.md))
- `sda3`: `/` ([Arco Linux](../entrada/2024/07/26/Arco_Linux.md))
- `sda4`: [SWAP](../atomos/2024/07/14/SWAP.md)
-  `sda6`: `/home` 

## Crystal
- [Gnome](../entrada/2024/08/10/Gnome.md)
- [Hyprland](../entrada/2024/08/10/Hyprland.md)
	- Barra de status: [Waybar](../entrada/2024/08/11/Waybar.md)
	- Notificação: [SwayNotificationCenter](../entrada/2024/08/10/SwayNotificationCenter.md)
	- Wallpapers: [sww](../entrada/2024/08/12/sww.md)
	- App launchers: [tofi](../entrada/2024/08/11/tofi.md)
	- Color pickers: [Hyprpicker](../entrada/2024/08/11/Hyprpicker.md)
	- Pipewire: [pipewire](../entrada/2024/08/11/pipewire.md) e [wireplumber](../entrada/2024/08/11/wireplumber.md)
	- Hyprland Desktop Portal: 
		- [xdg_desktop_portal_wlr](../entrada/2024/08/11/xdg_desktop_portal_wlr.md)
		- [xdg_desktop_portal_hyprland](../entrada/2024/08/11/xdg_desktop_portal_hyprland.md)
		- [xdg_desktop_portal_gtk](../entrada/2024/08/11/xdg_desktop_portal_gtk.md)
	- Authentication Agent: [polkit_kde_agent](../entrada/2024/08/11/polkit_kde_agent.md)
	- Qt Wayland Support: [qt5_wayland](../entrada/2024/08/11/qt5_wayland.md) e [qt6_wayland](../entrada/2024/08/11/qt6_wayland.md)