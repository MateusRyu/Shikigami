---
title: lazy.nvim
tags:
  - v1.1
aliases:
  - lazy.nvim
draft: true
created_at: 2024-07-08T17:33:33-03:00
updated_at: 2024-10-09T15:04:53-03:00
---
## Features

- Manage all your Neovim plugins with a powerful UI
- Fast startup times thanks to automatic caching and bytecode compilation of Lua modules
- Partial clones instead of shallow clones
- Automatic lazy-loading of Lua modules and lazy-loading on events, commands, filetypes, and key mappings
- Automatically install missing plugins before starting up Neovim, allowing you to start using it right away
- Async execution for improved performance
- No need to manually compile plugins
- Correct sequencing of dependencies
- Configurable in multiple files
- Generates helptags of the headings in `README.md` files for plugins that don't have vimdocs
- Dev options and patterns for using local plugins
- Profiling tools to optimize performance
- Lockfile `lazy-lock.json` to keep track of installed plugins
- Automatically check for updates
- Commit, branch, tag, version, and full [Semver](https://devhints.io/semver) support
- [Statusline](../../../../entrada/2024/08/06/Statusline.md) component to see the number of pending updates
- Automatically lazy-loads [[../../../../entrada/2024/08/06/colorschemes|colorschemes]]

## Requirements
---
- [Neovim](../../../../entrada/2024/07/08/Neovim.md) >= **0.8.0** (needs to be built with [LuaJIT](../../../../entrada/2024/07/08/LuaJIT.md))
- [Git](../../../../entrada/2024/07/08/Git.md) >= **2.19.0** (for partial clones support)
-  [Nerd Font](../../../../entrada/2024/07/08/Fonte_Nerd_Font.md) **_(opcional)_**
- [luarocks](../../../../entrada/2024/07/08/luarocks.md) to install [[../../../../entrada/2024/08/06/rockspecs|rockspecs]].
  You can remove `rockspec` from `opts.pkg.sources` to disable this feature.

## Referencias
---
- [Documentação oficial](https://lazy.folke.io/)