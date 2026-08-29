---
title: Contact us
permalink: /contact/
---

<div class="contact">
  <div>
    <p>If you have any questions about our research, please don't hesitate to reach out!</p>
    <p>The lab is recruiting at all levels for Fall 2024.</p>

    <address>
      {%- for line in site.address_lines %}
      {{ line }}{% unless forloop.last %}<br>{% endunless %}
      {%- endfor %}
    </address>

    <p>PI email: <a href="mailto:{{ site.email }}">{{ site.email }}</a></p>
  </div>

  <div>
    <img src="{{ '/assets/images/contact/lab-photo.png' | relative_url }}"
         alt="The Sukenik Lab out to dinner" loading="lazy">
  </div>
</div>
