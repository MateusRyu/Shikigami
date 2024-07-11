# Shikigami
---
Shikigami is a project to keep my knowledge at one unique place and serve as API to be consumed to anyone.

Translated versions:
- [ ] [Brazilian Portuguese](_docs/README-pt_br.md)

## Table of contents
---
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage) 
- [License](#license) 
- [Contact](#contact)
## Features
---
- [ ] Template to each type of knowledge for easy consume;
- [x] Private folder to sensitive data (Folder will not be store remotely);
- [ ] End-point to consume data;
- [x] Each data is writing with [2024-07-08-Markdown](_draft/2024/07/2024-07-08-Markdown.md) with an [atomic](_insight/2024/07/2024-07-08-atomico.md)] way to easily recover the information.
- [ ] [[Jekyll]] to publish at web

## Installation
---
### Requirements
- [Ruby](https://www.ruby-lang.org/en/downloads/) version **2.5.0** or higher, including all development headers (check your Ruby version using `ruby -v`)
- [RubyGems](https://rubygems.org/pages/download) (check your Gems version using `gem -v`)
- [GCC](https://gcc.gnu.org/install/) and [Make](https://www.gnu.org/software/make/) (check versions using `gcc -v`,`g++ -v`, and `make -v`)

## Usage
### Structure
---
-  All folder that start with `__` DO NOT will be committed, so do you can save sensitive data at that folder (like at `__daily` default personal folder).
-  All folders that start with `_` DO NOT will be served as end-point of the API.
-  `src`: contain all knowledge files and is organized by folders of year, month and day. Also, each filename start with the date of creation and the name with camel case,  as `YYYY-MM-DD-Name_of_file.md`.
-  `_draft` folder is destined to docs under creation.
-  `_insight` folder is destined to possible ideas that can be more elaborate at future and I want to maintain a way to links to existent docs.
-  `_templates` folder is destined to save [Obsidian](api/2024/06/2024-06-30-Obsidian.md)'s templates and end-point templates.
- `docs` folder contain the translated versions of this `README`.
-  `assets` folder is to media files and others types of files.
- `index` folder is to docs that aggregate and index the `src` files. 

### Templates
___
- [Insight](_templates/Insight.md)
- [Post](_templates/Post.md)
- [Update](_templates/Update.md)
- [Daily](_templates/Daily.md)
- [Anime](_templates/Anime.md)

## License
---
#to-do 

## Contact
---
You can see all my updated contact forms at this [link](https://link.ryu.dev.br/)!