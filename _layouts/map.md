---
layout: null
---
{
    {%- assign link_list = page.content | jsonify | split: '\n' -%}
    "size": {{ link_list.size | jsonify }},
    "list": [
        {%- for link in link_list -%}
            {%- if link contains "[" and link contains "]" -%}
                {%- assign alias = link | split: "[" | last | split: "]" | first -%}
                {%- assign url = link | split: "(" | last | split: ")" | first -%}
                {%- if alias == "" -%}
                    {% assign alias = forloop.index0 %}
                {%- endif -%}
                {"{{ alias }}": "{{ url |  replace: ".html", "" }}"}
                {%- unless forloop.last %},{% endunless -%}
            {%- endif -%}
            
        {%- endfor -%}
    ]
}