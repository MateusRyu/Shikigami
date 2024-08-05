---
title: Estilo visual
chapter: 1
group: Aparência
variations:
    default: 
        class: 
        name: padrão
    primary: 
        class: primary
        name: primário
    secondary: 
        class: secondary
        name: secundário
    accent: 
        class: accent
        name: realce
    info: 
        class: info
        name: informação
    success: 
        class: success
        name: sucesso
    warning: 
        class: warning
        name: aviso
    error: 
        class: error
        name: erro
---
{% capture text_tags %}
    Normal, <a href="#">Link normal</a>, <a href="#">Link já visitado</a>, <a>Link vazio</a>, 
    <b>Negrito</b> ({{ "<b></b>" | escape }} - não-semantico), 
    <strong>Importante</strong> ({{ "<strong></strong>" | escape }} - semantico e com estilo), 
    <i>Italico</i> ({{ "<i></i>" | escape }} - não-semantico), 
    <em>Enfase</em> ({{ "<em></em>" | escape }} - semantico e sem estilo), 
    <mark>Marcado</mark> ({{ "<mark></mark>" | escape }} - semantico e com estilo), 
    <small>Pequeno</small> ({{ "<small></small>" | escape }} - semantico e com estilo), 
    <del>Deletado</del>, 
    <ins>Inserido</ins>, 
    Texto<sub>Subscrito</sub>, 
    Texto<sup>Superscrito</sup>.
{% endcapture %}
{% capture typography %}
{% for variation in page.variations %}
    {% assign class = variation[1].class %}
    {% case class %}
        {% when null %}
            <details>
                <summary>Texto: Padrão</summary>
                <p>{{ text_tags }}</p>
            </details>
        {% when "primary", "secondary", "accent" %}
            {% for intensity in (1..9) %}
                <details class="text-{{ class }}-{{ intensity }}">
                    <summary>Texto: {{ variation[1].name }}-{{ intensity }}</summary>
                    <p>
                        {{ text_tags }}
                    </p>
                </details>
            {% endfor %}
        {% else %}
            <details class="text-{{ variation[1].class }}">
                <summary>Texto: {{ variation[1].name }}</summary>
                <p>
                    {{ text_tags }}
                </p>
            </details>
    {% endcase %}
{% endfor %}
{% endcapture %}
<div>
    <h2>Cores</h2>
    {% for variation in page.variations %}
        {% assign class = variation[1].class %}
        {% case class %}
            {% when null %}
                <details>
                    <summary>Padrão</summary>
                    <div class="card">
                        {{ typography }}
                    </div>
                </details>
            {% when "primary", "secondary", "accent" %}
                {% for intensity in (1..9) %}
                    <details>
                        <summary class="bg-{{ class }}-{{ intensity }}" >Variante: {{ class }} {{ intensity }}</summary>
                        <div class="card bg-{{ class }}-{{ intensity }}">
                            {{ typography }}
                        </div>
                    </details>
                {% endfor %}
            {% else %}
                <details>
                    <summary>Variante: {{ class }}</summary>
                    <div class="card bg-{{ class }}">
                        {{ typography }}
                    </div>
                </details>
        {% endcase %}
    {% endfor %}
</div>
<div>
    <h2>Botões</h2>
    {% for variation in page.variations %}
        <button class="btn-{{ variation[1].class }}">{{ variation[1].name | capitalize }}</button>
    {% endfor %}
    <details open>
        <summary>Código-fonte</summary>
        {% highlight html linenos %}
            {%- for variation in page.variations %}
<button class="btn{{ variation[1].class }}">{{ variation[1].name | capitalize }}</button>
            {%- endfor -%}
        {% endhighlight %}
    </details>
</div>
<div>
    <h2>Badge</h2>
    {% for variation in page.variations %}
        <span class="badge{{ variation[1].class }}">{{ variation[1].name | capitalize }}</span>
    {% endfor %}
    <details open>
        <summary>Código-fonte</summary>
        {% highlight html linenos %}
        {%- for variation in page.variations %}
<span class="badge{{ variation[1].class }}">{{ variation[1].name | capitalize }}</span>
        {%- endfor -%}
        {% endhighlight %}
    </details>
</div>
<div>
    <h2>Navegação</h2>
    <div class="tabs tabs-lifted">
        <button class="tab">Tab</button>
        <button class="tab tab-active">Tab</button>
        <button class="tab">Tab</button>
    </div>
</div>
<div class="flex flex-col">
    <h2>Links</h2>
    {% for variation in page.variations %}
        <span class="link{{ variation[1].class }}">{{ variation[1].name | capitalize }}</span>
    {% endfor %}
</div>
<div>
    <h2>Progresso</h2>
    {% assign values = "20, 25, 30, 40, 45, 55, 70, 90" | split: ", " %}
    {% for variation in page.variations %}
        <progress value="{{ values[forloop.index0] }}" max="100" class="progress{{ variation[1].class }}">{{ variation[1].name | capitalize }}</progress>
    {% endfor %}
</div>
<form>
    <h2>Formulario</h2>
    <div>
        <h3>Checkbox</h3>
        <div>
            <h4>Checado</h4>
            {% for variation in page.variations %}
                <label for="checked{{variation[1].class}}">{{ variation[1].name | capitalize }}:</label>
                <input id="checked{{variation[1].class}}" type="checkbox" class="checkbox{{ variation[1].class }}" checked="checked">
            {% endfor %}
        </div>
        <div>
            <h4>Não checado</h4>
            {% for variation in page.variations %}
                <label for="unchecked{{variation[1].class}}">{{ variation[1].name | capitalize }}:</label>
                <input id="unchecked{{variation[1].class}}" type="checkbox" class="checkbox{{ variation[1].class }}">
            {% endfor %}
        </div>
    </div>
    <div>
        <h3>Radio</h3>
        {% for variation in page.variations %}
            <label for="radio{{variation[1].class}}">{{ variation[1].name | capitalize }}:</label>
            <input id="radio{{variation[1].class}}" type="radio" name="radio" class="radio{{ variation[1].class }}" {% if forloop.index == 2 %}checked="checked"{% endif %}>
        {% endfor %}
    </div>
    <div>
        <h3>Range</h3>
        {% for variation in page.variations %}
            <label for="range{{variation[1].class}}">{{ variation[1].name | capitalize }}:</label>
            <input id="range{{variation[1].class}}" min="0" max="100" value="{{values[forloop.index0]}}" type="range" class="range{{ variation[1].class }}" >
        {% endfor %}
    </div>
    <div>
        <h3>Input</h3>
        {% for variation in page.variations %}
            <input type="text" placeholder="{{ variation[1].name |  capitalize }}" class="range{{ variation[1].class }}" >
        {% endfor %}
    </div>
</form>
<div class="flex gap-3">
    <h2>Tipografia</h2>
    <div>
        <h3>Cabeçalho</h3>
        {% for size in (1..6) %}
            <h{{ size }}>Titulo {{ size }} (H{{ size }})</h{{ size }}>
        {% endfor %}
    </div>
    {% assign font_size = "4xl, 3xl, 2xl, xl, lg, sm, xs" |  split: ", " %}
    <div>
        <h3>Tamanho da fonte</h3>
        {% for size in font_size %}
            <p class="text-{{ size }}">Tamanho da fonte: {{ font_size.size |  minus: forloop.index0 }} ({{ size }})</p>
        {% endfor %}
    </div>
</div>
<div>
    <h2>Listas</h2>
    <div>
        <h3>Ordenda</h3>
        <ol class="steps steps-vertical">
        {% for size in (1..4) %}
            <li>Item {{ size }}</li>
        {% endfor %}
        </ol>
    </div>
    <div>
        <h3>Não-ordenda</h3>
        <ul class="steps steps-vertical">
        {% for size in (1..4) %}
            <li>Item {{ size }}</li>
        {% endfor %}
        </ul>
    </div>
    <div>
        <h3>Passos</h3>
        <ul class="steps steps-vertical">
            <li class="step step-primary">Passo 1</li>
            <li class="step step-primary">Passo 2</li>
            <li class="step">Passo 3</li>
            <li class="step">Passo 4</li>
        </ul>
    </div>
</div>
<div>
    <h2>Alertas</h2>
    <div class="alert">
        <span>12 unread messages. Tap to see.</span>
    </div> 
    <div class="alert alert-info">
        <span>New software update available.</span>
    </div> 
    <div class="alert alert-success">
        <span>Your purchase has been confirmed!</span>
    </div> 
    <div class="alert alert-warning">
        <span>Warning: Invalid email address!</span>
    </div> 
    <div class="alert alert-error">
        <span>Error! Task failed successfully.</span>
    </div>
</div>