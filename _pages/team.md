---
title: "Yale NLP Lab - Team"
layout: gridlay
excerpt: "Yale NLP Lab: Team members"
sitemap: false
permalink: /team/
---
<style>
  ul.no-indent {
    margin-left: 0;
    padding-left: 1em;
  }
  ul.no-indent li {
    margin: 0;
  }
</style>

<!-- # Group Members -->
<!-- **We are  looking for new PhD students, Postdocs, and Master students to join the team** [(see openings)]({{ site.url }}{{ site.baseurl }}/vacancies) **!** -->
<!-- Jump to [staff](#staff), [master and bachelor students](#master-and-bachelor-students), [alumni](#alumni), [administrative support](#administrative-support), [lab visitors](#lab-visitors). -->

### Faculty
{% assign number_printed = 0 %}
{% for member in site.data.members.faculty %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="12.5%" style="float: left" />
  {% if member.homepage %}
  <h4><a href="{{ member.homepage }}" target="_blank" style="color: inherit; text-decoration: none;">{{ member.name }}</a></h4>
  {% else %}
  <h4>{{ member.name }}</h4>
  {% endif %}
  <i>{{ member.info }} <!--<br>email: <{{ member.email }}></i> -->
  <ul style="overflow: hidden" class="no-indent">
    {% for i in (1..member.number_interests) %}
      {% case i %}
        {% when 1 %}
          <li> {{ member.interest1 }} </li>
        {% when 2 %}
          <li> {{ member.interest2 }} </li>
        {% when 3 %}
          <li> {{ member.interest3 }} </li>
        {% when 4 %}
          <li> {{ member.interest4 }} </li>
        {% when 5 %}
          <li> {{ member.interest5 }} </li>
      {% endcase %}
    {% endfor %}
  </ul>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

### PhD Students
{% assign number_printed = 0 %}
{% for member in site.data.members.phd_students %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  {% if member.homepage %}
  <h4><a href="{{ member.homepage }}" target="_blank" style="color: inherit; text-decoration: none;">{{ member.name }}</a></h4>
  {% else %}
  <h4>{{ member.name }}</h4>
  {% endif %}
  <i>{{ member.info }}

  <ul style="overflow: hidden" class="no-indent">
  {% if member.interests %}  
      {% for interest in (member.interests) %}
            <li> {{ interest }} </li>
      {% endfor %}
  {% endif %}  
  </ul>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}




{% assign student_types = "Master,Undergraduate" | split: ',' %}

{% for student_name in student_types %}
  
### {{ student_name }} Students
{% assign number_printed = 0 %}

{% assign student_data = "" %}
{% case student_name %}
  {% when 'Master' %}
    {% assign student_data = site.data.members.ms_students %}
  {% when 'Undergraduate' %}
    {% assign student_data = site.data.members.bs_students %}
{% endcase %}

{% for member in student_data %}

{% assign even_odd = number_printed | modulo: 6 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-2 clearfix" style="text-align: center;">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="70%" style="margin: 0 auto; display: block;" />
  {% if member.homepage %}
  <h4><a href="{{ member.homepage }}" target="_blank" style="color: inherit; text-decoration: none;">{{ member.name }}</a></h4>
  {% else %}
  <h4>{{ member.name }}</h4>
  {% endif %}
  <i>{{ member.info }}</i>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 5 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 6 %}
{% if even_odd > 0 %}
</div>
{% endif %}

{% endfor %}




<!-- ### Alumni

{% assign number_printed = 0 %}
{% for member in site.data.alumni_members %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  <h4>{{ member.name }}</h4>
  <i>{{ member.duration }} <br> Role: {{ member.info }}</i>
  <ul style="overflow: hidden">

  </ul>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %} -->

### Former visitors, BSc/ MSc students
<div class="row">

<div class="col-sm-4 clearfix">
<h4>Visiting Students</h4>
{% for member in site.data.alumni.visiting_students %}
{{ member.name }}
{% endfor %}
</div>

<div class="col-sm-4 clearfix">
<h4>Master students</h4>
{% for member in site.data.alumni.ms_students %}
{{ member.name }}
{% endfor %}
</div>

<div class="col-sm-4 clearfix">
<h4>Bachelor Students</h4>
{% for member in site.data.alumni.bs_students %}
{{ member.name }}
{% endfor %}
</div>

</div>


<!-- ### Administrative Support
<a href="mailto:Rijsewijk@Physics.LeidenUniv.nl">Ellie van Rijsewijk</a> is helping us (and other groups) with administration. -->
