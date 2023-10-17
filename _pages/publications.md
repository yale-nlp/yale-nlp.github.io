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

{% assign years = "2023,2022" | split: ',' %}

{% for year in years %}

{% assign publication_data = "" %}
{% case year %}
  {% when '2023' %}
    {% assign publication_data = site.data.publications.2023_publist %}
  {% when '2022' %}
    {% assign publication_data = site.data.publications.2022_publist %}
{% endcase %}

<div class="line-through-title">
  <span>{{year}}</span>
</div>

<div class="justified-content">
<ul>
{% for publi in publication_data %}
    {% if publi.display != 0 %}
        <li>{{ publi.authors }} <a href="{{ publi.url }}" target="_blank">{{ publi.title }}.</a> <i>{{ publi.venue }}</i></li>
    {% endif %}
{% endfor %}
</ul>
</div>
{% endfor %}
