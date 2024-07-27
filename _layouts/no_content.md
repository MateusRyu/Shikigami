---
layout: null
---
{
    {% for data in page %}
        {%- unless data[0] == "content" %}
            {{ data.first | jsonify }}: {{ data.last | jsonify }}
            {%- unless forloop.last %},{% endunless %}
        {% endunless %}
    {% endfor %}
}