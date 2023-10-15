---
title: "Yale NLP Lab - Publications"
layout: gridlay
excerpt: "Yale NLP Lab -- Publications."
sitemap: false
permalink: /publications/
---
<style>
  .line-through-title {
      position: relative;
      text-align: center;
      margin-bottom: 15px;
  }

  .line-through-title span {
      background-color: #fff; /* Assuming your background is white. If not, change this. */
      padding: 0 10px; /* Adjust as needed to give space around the text. */
      z-index: 1;
      position: relative;
      font-size: xx-large;
  }

  .line-through-title::before {
      content: "";
      position: absolute;
      top: 50%;
      left: 0;
      right: 0;
      height: 1px;
      background: black; /* Adjust the color as needed. */
      z-index: 0;
  }

  .justified-content {
      text-align: justify;
  }
  .justified-content ul {
      padding-left: 20px;
  }
</style>


<div class="line-through-title">
  <span>2023</span>
</div>

<div class="justified-content">
<ul>
{% for publi in site.data.publications.2023_publist %}
    {% if publi.display != 0 %}
        <li>{{ publi.authors }} <a href="{{ publi.url }}">{{ publi.title }}.</a> <i>{{ publi.venue }}</i></li>
    {% endif %}
{% endfor %}
</ul>
</div>

<div class="line-through-title">
  <span>2022</span>
</div>

<div class="justified-content">
<ul>
{% for publi in site.data.publications.2022_publist %}
    {% if publi.display != 0 %}
        <li>{{ publi.authors }} <a href="{{ publi.url }}">{{ publi.title }}.</a> <i>{{ publi.venue }}</i></li>
    {% endif %}
{% endfor %}
</ul>
</div>
