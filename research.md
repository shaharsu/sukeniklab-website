---
title: Research
subtitle: We are interested in how the cellular environment affects biomolecular function
permalink: /research/
---

<div class="section">
  <p>The cellular environment displays extreme spatial and temporal heterogeneity even in a
  single cell. For example, as a cell enters mitosis water uptake increases cellular volume
  by up to 30%, the cytoskeleton disassembles and reforms causing the cell to round up, and
  the nuclear membrane breaks down releasing sequestered molecules into the cytoplasm within
  seconds. The way proteins react to routine (or pathological) changes in the cellular
  environment remains poorly understood. Our research is currently funded by the NIH (grant
  <a href="https://reporter.nih.gov/project-details/10224270">R35GM137926</a>) and the NSF
  (award <a href="https://www.nsf.gov/awardsearch/showAward?AWD_ID=2128067&amp;HistoricalAwards=false">2128067</a>).</p>

  <div class="research-cards">
    {%- for card in site.data.research_cards %}
    <div class="research-card">
      <h3>{{ card.title }}</h3>
      <p>{{ card.text }}</p>
    </div>
    {%- endfor %}
  </div>
</div>

{% assign themes = site.research | sort: "order" %}
{%- for theme in themes %}
<article class="research-theme">
  <div class="theme-body">
    <h2>{{ theme.title }}</h2>
    {{ theme.content | markdownify }}
  </div>
  <div class="theme-figure">
    <img src="{{ theme.image | relative_url }}" alt="{{ theme.image_alt }}" loading="lazy">
  </div>
</article>
{%- endfor %}
