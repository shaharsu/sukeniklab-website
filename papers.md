---
title: Papers
permalink: /papers/
---

<p class="subtitle">Selected publications from recent years. A complete publication list can
be found on <a href="{{ site.scholar_url }}">Google Scholar</a>.</p>

{% assign pubs = site.publications | sort: "order" %}
{% assign years = pubs | group_by: "year" | sort: "name" | reverse %}

{%- for group in years %}
<h2 class="pub-year" id="y{{ group.name }}">{{ group.name }}</h2>

{%- for pub in group.items %}
<article class="pub">
  <div class="pub-figure">
    {%- if pub.image %}
    <img src="{{ pub.image | relative_url }}" alt="Figure from {{ pub.title }}" loading="lazy">
    {%- endif %}
  </div>
  <div>
    <h3 class="pub-title">{{ pub.title }}</h3>
    <p class="pub-authors">{{ pub.authors }}</p>
    {%- if pub.venue %}<p class="pub-venue">{{ pub.venue }}</p>{% endif %}
    <a class="pub-link" href="{{ pub.link }}">{{ pub.link_label }}</a>
  </div>
</article>
{%- endfor %}

{%- assign figs = site.data.paper_figures[group.name] %}
{%- if figs and figs.size > 0 %}
<div class="news-figures year-figures">
  {%- for f in figs %}
  <figure><img src="{{ f | relative_url }}" alt="" loading="lazy"></figure>
  {%- endfor %}
</div>
{%- endif %}
{%- endfor %}

<p style="margin-top:32px"><a href="{{ site.scholar_url }}">Google Scholar — older papers</a></p>
