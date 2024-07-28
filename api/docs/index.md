---
layout: post
---
{% assign docs = site.pages | sort: "chapter" %}
{%- for doc in docs %}
    {%- assign dir = doc.dir | split: "/" -%}
    {%- unless dir[1] == "api" and dir[2] == "docs" -%}
        {%- continue -%}
    {%- endunless -%}
    {%- if doc.url == page.url -%}
        {%- continue -%}
    {%- endif -%}
    - [pagina {{ doc.chapter}}]({{ doc.url }})
{% endfor -%}