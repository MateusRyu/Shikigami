---
title: SyntaxHighlighting
tags:
  - plugin/transformer
created_at: 2025-01-24T00:59:11-03:00
updated_at: 2025-01-24T01:04:05-03:00
---

This plugin is used to add syntax highlighting to code blocks in Quartz. See [[syntax highlighting|Syntax Highlighting]] for more information.

> [!note]
> For information on how to add, remove or configure plugins, see the [[configuration#Plugins|Configuration]] page.

This plugin accepts the following configuration options:

- `theme`: a separate id of one of the [themes bundled with Shikiji](https://shikiji.netlify.app/themes). One for light mode and one for dark mode. Defaults to `theme: { light: "github-light", dark: "github-dark" }`.
- `keepBackground`: If set to `true`, the background of the Shikiji theme will be used. With `false` (default) the Quartz theme color for background will be used instead.

In addition, you can further override the colours in the `quartz/styles/syntax.scss` file.

## API

- Category: Transformer
- Function name: `Plugin.SyntaxHighlighting()`.
- Source: [`quartz/plugins/transformers/syntax.ts`](https://github.com/jackyzha0/quartz/blob/v4/quartz/plugins/transformers/syntax.ts).