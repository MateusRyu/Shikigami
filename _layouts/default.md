---
layout: web
---

<h1>{{ page.title }}</h1>
{%- assign filters = "remove_md_extension.liquid" | split: ", " -%}
{% include filtered.liquid %}
