---
title: Static
tags:
  - plugin/emitter
created_at: 2025-01-24T00:59:11-03:00
updated_at: 2025-01-24T01:04:05-03:00
---

This plugin emits all static resources needed by Quartz. This is used, for example, for fonts and images that need a stable position, such as banners and icons. The plugin respects the `ignorePatterns` in the global [[configuration|Configuration]].

> [!important]
> This is different from [[Assets]]. The resources from the [[Static]] plugin are located under `quartz/static`, whereas [[Assets]] renders all static resources under `content` and is used for images, videos, audio, etc. that are directly referenced by your markdown content.

> [!note]
> For information on how to add, remove or configure plugins, see the [[configuration#Plugins|Configuration]] page.

This plugin has no configuration options.

## API

- Category: Emitter
- Function name: `Plugin.Static()`.
- Source: [`quartz/plugins/emitters/static.ts`](https://github.com/jackyzha0/quartz/blob/v4/quartz/plugins/emitters/static.ts).