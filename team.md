---
title: The team
permalink: /team/
---

<div class="section">
  <div class="people">
    {%- for person in site.people %}
    <div class="person">
      <img class="person-photo" src="{{ person.photo | relative_url }}"
           alt="{{ person.name }}" width="120" height="123" loading="lazy">
      <h3>{{ person.name }}</h3>
      <p class="role">{{ person.role }}</p>
      <div class="blurb">{{ person.content | markdownify }}</div>
      <p class="person-links">
        {%- for e in person.emails %}
        <a href="mailto:{{ e }}">{{ e }}</a>{% unless forloop.last %}<br>{% endunless %}
        {%- endfor %}
        {%- if person.links %}<br>
        {%- for l in person.links %}<a href="{{ l.url }}">{{ l.label }}</a>{% unless forloop.last %} | {% endunless %}{% endfor %}
        {%- endif %}
      </p>
    </div>
    {%- endfor %}
  </div>
</div>

<div class="section">
  <h2>Lab alumni</h2>
  <ul class="alumni">
    {%- for a in site.data.alumni %}
    <li>{{ a }}</li>
    {%- endfor %}
  </ul>
</div>

<div class="section join" id="join-us">
  <img src="{{ '/assets/images/team/join-us.jpg' | relative_url }}" alt="" loading="lazy">
  <div>
    <h2>Join us!</h2>
    <p>The lab is always looking for motivated, talented individuals!</p>
    <p>Projects in the lab tend to be interdisciplinary, and can involve live-cell
    microscopy, protein biophysics, and/or programming, depending on your interests.
    If you like what you see, <a href="mailto:shaharsu@gmail.com">drop Shahar a line</a>.
    Please indicate why you're interested in joining.</p>
  </div>
</div>
