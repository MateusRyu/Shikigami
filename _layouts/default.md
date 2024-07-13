---
layout: web
---
{%- assign filters = "remove_md_extension.liquid" | split: ", " -%}
{% include filtered.liquid %}
