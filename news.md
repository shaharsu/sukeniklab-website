---
title: Lab news
permalink: /news/
---

{% assign items = site.news | sort: "date" | reverse %}
{%- for item in items %}
<article class="news-item{% if item.images %} has-figures{% endif %}">
  {%- if item.images %}
  <div class="news-figures">
    {%- for img in item.images %}
    <figure>
      <img src="{{ img.src | relative_url }}" alt="{{ img.caption }}" loading="lazy">
      {%- if img.caption %}<figcaption>{{ img.caption }}</figcaption>{% endif %}
    </figure>
    {%- endfor %}
  </div>
  {%- endif %}
  <div class="news-body">
    <p class="news-date">{{ item.date_display }}</p>
    {{ item.content | markdownify }}
  </div>
</article>
{%- endfor %}
