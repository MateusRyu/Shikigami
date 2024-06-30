# Shikigami
---
Shikigami is a project to keep my knowledge at one unique place and serve as API to be consumed to anyone.
## Features
---
- [ ] Template to each type of knowledge for easy consume;
- [x] Private folder to sensitive data (Folder will not be store remotely);
- [ ] End-point to consume data;
- [x] Each data is writing with [Markdown](_draft/Markdown.md) with an [atomic](_insight/atomic.md) way to easily recover the information.

## Structure
---
-  All folder that start with `__` DO NOT will be committed, so do you can save sensitive data at that folder (like at `__daily` default personal folder).
-  All folders that start with `_` DO NOT will be served as end-point of the API.
-  `src`: contain all knowledge files and is organized by folders of year, month and day. Also, each filename start with the date of creation and the name with camel case,  as `YYYY-MM-DD-Name_of_file.md`.
-  `_draft` folder is destined to docs under creation.
-  `_insight` folder is destined to possible ideas that can be more elaborate at future and I want to maintain a way to links to existent docs.
-  `_templates` folders is destined to save [Obsidian](src/2024/06/30/2024-06-30-Obsidian.md)'s templates and end-point templates.
-  `assets` folder is to media files and others types of files.
- `index` folder is to docs that aggregate and index the `src` files. 

## Templates
___
- [Anime.tpl](Anime.tpl.md);