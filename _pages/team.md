---
title: "Yale NLP Lab - Team"
layout: gridlay
excerpt: "Yale NLP Lab: Team members"
sitemap: false
permalink: /team/
---
<style>
  .card {
      position: relative;
      width: 100%;
      height: 210pt;
      padding: 5px;
      border-radius: 8px;
      text-align: center;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      margin-bottom: 20px;
  }

  .details-container {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-color: rgba(114, 114, 114, 0.89);
      z-index: 10;
      color: white;
      padding: 10px;
      opacity: 0;
      transition: all 0.3s cubic-bezier(0.68, -0.55, 0.27, 1.55);
      display: flex;
      flex-direction: column;
      transform: translateY(-100%); 
      max-height: 0;
      overflow: hidden;
      font-size: xlarge;
  }

  .details-container.active {
      opacity: 1;
      transform: translateY(0);
      max-height: 210pt;
  }

  .details-container h2, .card-body h2 {
      text-align: center;
      font-size: large;
      font-weight: 600;
  }

  .details-container p, .card-body p {
      text-align: center;
      font-size: small;
  }

  .avatar {
      width: 150px;
      height: 150px;
      margin: 0 auto;
      overflow: hidden;
      border-radius: 50%;
      display: flex;
      align-items: center;   /* Vertically centers the content */
      justify-content: center;   /* Horizontally centers the content */
      overflow: hidden;
  }
  
  .avatar img {
    width: 100%;
    height: 100%;
    object-fit: cover;   /* This ensures the image will cover its parent without being stretched */
    border-radius: 50%;
    object-fit: cover;   /* Ensures the image covers its parent without being stretched */
    object-position: center;
  }

  .card-body {
      color: black;
  }

  .icons {
      display: flex;
      justify-content: center;
  }

  .icon {
      width: 24px;
      height: 24px;
      fill: white;
  }

  ul.no-indent {
    margin-left: 0;
    padding-left: 1em;
    text-align: left;
  }
  ul.no-indent li {
    margin: 0;
    style="text-align:left"
  }
</style>

<script>
  document.addEventListener("DOMContentLoaded", function() {
    const cards = document.querySelectorAll(".card");
    
    cards.forEach(card => {
      card.addEventListener("mouseenter", function() {
        const details = this.querySelector(".details-container");
        if (details) {
          details.classList.add("active");
        }
      });

      card.addEventListener("mouseleave", function() {
        const details = this.querySelector(".details-container");
        if (details) {
          details.classList.remove("active");
        }
      });
    });
  });
</script>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/jpswalsh/academicons@1/css/academicons.min.css">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">


<div class="row">
{% assign member_types = "Faculty,PhD,Master,Undergraduate" | split: ',' %}

{% for type_name in member_types %}

{% assign student_data = "" %}
{% case type_name %}
  {% when 'Faculty' %}
    {% assign student_data = site.data.members.faculty %}
    {% assign student_data.type = type_name %}
  {% when 'PhD' %}
    {% assign student_data = site.data.members.phd_students %}
  {% when 'Master' %}
    {% assign student_data = site.data.members.ms_students %}
  {% when 'Undergraduate' %}
    {% assign student_data = site.data.members.ug_students %}
{% endcase %}

{% for member in student_data %}
<div class="col-lg-3 col-md-4 col-sm-6 col-xs-12 mb-4">
<div class="card">
<div class="details-container">
  <h2>{{ member.name }}</h2>
  <div class="icons">
  {% if member.homepage %}
  <a href="{{ member.homepage }}" target="_blank"><i class="fas fa-home pr-1 icon" style="color: white;"></i></a>
  {% endif %}
  {% if member.github %}
  <a href="{{ member.github }}" target="_blank"><i class="fab fa-github icon" style="color: white;"></i></a>
  {% endif %}
  {% if member.google_scholar %}
  <a href="{{ member.google_scholar }}" target="_blank"><i class="ai ai-google-scholar ai-lg icon" style="color: white;"></i></a>
  {% endif %}
  {% if member.twitter %}
  <a href="{{ member.twitter }}" target="_blank"><i class="fab fa-twitter icon" style="color: white;"></i></a>
  {% endif %}
  </div>

  <ul style="overflow: hidden" class="no-indent">
  {% if member.interests %}  
      {% for interest in (member.interests) %}
            <li> {{ interest }} </li>
      {% endfor %}
  {% endif %}  
  </ul>
  {% if member.type %} 
  {{member.type }}
  {% endif %}
</div>

  <figure class="flex-col bg-base-100">
  <div class="avatar inline-flex place-content-center place-items-start rounded-full bg-gradient-to-r from-cyan-500 to-blue-500">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" alt="{{ member.name }} profile image" class="w-full h-auto rounded-full" />
  </div>
  </figure>
  <div class="card-body">
  <h2>{{ member.name }}</h2>
  <p>{{ member.info }}</p>
  </div>
</div>
</div>
{% endfor %}
{% endfor %}
</div>


<div class="row" style="margin-bottom: 50px; margin-left: 40px; margin-right: 10px">

<h2 class="fancy-h2"> Alumni </h2>

<h4 style="text-align: left;">PhD Students</h4>
<div class="row">
{% assign student_data = site.data.alumni.phd_students %}
{% for member in student_data %}
<div class="col-lg-3 col-md-4 col-sm-6 col-xs-12 mb-4">
<div class="card">
<div class="details-container">
  <h2>{{ member.name }}</h2>
  <div class="icons">
  {% if member.homepage %}
  <a href="{{ member.homepage }}" target="_blank"><i class="fas fa-home pr-1 icon" style="color: white;"></i></a>
  {% endif %}
  {% if member.github %}
  <a href="{{ member.github }}" target="_blank"><i class="fab fa-github icon" style="color: white;"></i></a>
  {% endif %}
  {% if member.google_scholar %}
  <a href="{{ member.google_scholar }}" target="_blank"><i class="ai ai-google-scholar ai-lg icon" style="color: white;"></i></a>
  {% endif %}
  {% if member.twitter %}
  <a href="{{ member.twitter }}" target="_blank"><i class="fab fa-twitter icon" style="color: white;"></i></a>
  {% endif %}
  </div>

  <ul style="overflow: hidden" class="no-indent">
  {% if member.interests %}  
      {% for interest in (member.interests) %}
            <li> {{ interest }} </li>
      {% endfor %}
  {% endif %}  
  </ul>
</div>
<figure class="flex-col bg-base-100">
  <div class="avatar inline-flex place-content-center place-items-start rounded-full bg-gradient-to-r from-cyan-500 to-blue-500">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" alt="{{ member.name }} profile image" class="w-full h-auto rounded-full" />
  </div>
  </figure>
  <div class="card-body">
  <h2>{{ member.name }}</h2>
  <p>{{ member.year }}</p>
  <p>{{ member.info }}</p>
  </div>
</div>
</div>
{% endfor %}
</div>

<div class="col-sm-6 clearfix">
<h4 style="text-align: left; margin-bottom: 25px;">Undergraduate and Master Students</h4>
{% for member in site.data.alumni.yale_students %}
<p style="text-align: left;">
{{ member.name }}
</p>
{% endfor %}
</div>

<div class="col-sm-6 clearfix">
<h4 style="text-align: left; margin-bottom: 25px;">Visiting Students</h4>
{% for member in site.data.alumni.visiting_students %}
<p style="text-align: left;">
{{ member.name }}
</p>
{% endfor %}
</div>

<!-- </div> -->

<style>
  .fancy-h2 {
    text-align: left;
    margin-top: 20px;
    font-family: 'Roboto', sans-serif;
    font-size: 2.5em;
    color: #1A90E2;
    border-bottom: 2px solid rgba(26, 144, 226, 0.5);
    padding-bottom: 10px;
  }
</style>