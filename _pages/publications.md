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

/* Add some basic styling to the button */
.publication-button {
  padding: 0px 16px;
  margin-left: 0px;
  margin-right: 10px;
  background-color: #209bff;
  color: white;
  text-decoration: none;
  border-radius: 5px;
  font-size: 14px;
  cursor: pointer;
}

.publication-category {
  padding: 0px 16px;
  margin-left: 0px;
  margin-right: 10px;
  background-color: #902bff;
  color: white;
  text-decoration: none;
  border-radius: 5px;
  font-size: 14px;
  cursor: pointer;
}



/* Style the list to look better */
.publication-item {
  list-style-type: none;
  padding-bottom: 15px;
}

.publication-authors,
.publication-venue {
  display: block; /* makes it a block to form its own line */
  margin-top: 5px;
  color: #135
}

/* Change the color of the venue to distinguish it */
.publication-venue {
  color: #555;
}

</style>

{% assign years = "2024,2023,2022,2021,2020" | split: ',' %}

{% for year in years %}

{% assign publication_data = "" %}
{% case year %}
  {% when '2024' %}
    {% assign publication_data = site.data.publications.2024_publist %}
  {% when '2023' %}
    {% assign publication_data = site.data.publications.2023_publist %}
  {% when '2022' %}
    {% assign publication_data = site.data.publications.2022_publist %}
  {% when '2021' %}
    {% assign publication_data = site.data.publications.2021_publist %}    
  {% when '2020' %}
    {% assign publication_data = site.data.publications.2020_publist %}    
{% endcase %}

<div class="line-through-title">
  <span>{{year}}</span>
</div>

<!-- <div class="justified-content">
<ul>
{% for publi in publication_data %}
    {% if publi.display != 0 %}
        <li>{{ publi.authors }} <a href="{{ publi.url }}" target="_blank">{{ publi.title }}.</a> <i>{{ publi.venue }}</i></li>
    {% endif %}
{% endfor %}
</ul>
</div> -->

<div class="justified-content">
<ul>
{% for publi in publication_data %}
    {% if publi.display != 0 %}
        <li class="publication-item">
            <span>{{ publi.title }}</span>
            <span class="publication-authors">
            {{ publi.authors | join: ', ' }}</span>
            <i class="publication-venue">{{ publi.venue }}</i>
            {% if publi.paper_link %}
              <a class="publication-button" href="{{ publi.paper_link }}" target="_blank">pdf</a>
            {% else %}
              <a class="publication-button" href="{{ publi.url }}" target="_blank">pdf</a>
            {% endif %}
            <!-- {% if publi.category %}
              <span class="publication-category" target="_blank">{{ publi.category }}</span>
            {% endif %} -->
        </li>
    {% endif %}
{% endfor %}
</ul>
</div>

{% endfor %}
