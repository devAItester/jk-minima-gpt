---
layout: page
title: Все записи
permalink: /posts/
---

Список всех опубликованных записей.

<ul class="post-list">
  {%- for post in site.posts -%}
  <li>
    <article>
      <p class="post-meta">
        <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: site.minima.date_format }}</time>
      </p>
      <h2>
        <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title | escape }}</a>
      </h2>
    </article>
  </li>
  {%- endfor -%}
</ul>
