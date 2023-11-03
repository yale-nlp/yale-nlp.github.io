---
title: "Yale NLP Lab - Projects"
layout: gridlay
excerpt: "Yale NLP Lab: Projects"
sitemap: false
permalink: /projects/
---
<style>
  .project-card {
    display: flex;
    flex-direction: column;
    margin: 0 0 30px;
    flex: 1; /* This ensures that the flex item can grow */
  }

  .hover-effect a {
      text-decoration: none;
  }

  .hover-effect:hover {
      transform: translateY(-5px);
      transition: transform 0.3s ease;
  }

  .hover-effect:hover .title {
  color: #007BFF; /* Natural blue color */
  }

  .bg-white {
      background-color: #ffffff;
  }

  .shadow-lg {
      box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
  }

  .rounded-lg {
      border-radius: 0.5rem;
  }

  .overflow-hidden {
      overflow: hidden;
  }

  .bg-cover {
      background-size: cover;
  }

  .bg-center {
      background-position: center;
  }

  .h-56 {
      height: 14rem; /* Assuming base is 4, so 56/4 */
  }

  .p-4 {
      padding: 1rem; /* Assuming base is 4, so 4/4 */
  }

  .title {
    margin-top: 1rem; /* Assuming base is 4, so 2/4 */
    display: block; /* Ensure the title is a block element */
    font-size: 1.5rem; /* Assuming 'text-xl' is roughly 1.25rem */
    font-weight: 700; /* Bold */
    color: #1a202c; /* Assuming 'text-gray-700' */
    text-align: center;
  }

  .text-gray-500 {
      color: #6b7280;
  }

  .text-sm {
      font-size: 1.25rem;
  }
</style>

<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">

<div class="row">
{% assign project_data = site.data.projects.projects %}

{% for project in project_data %}
<!-- Begin card -->
<div class="project-card col-lg-3 col-md-4 col-sm-6 col-xs-12 mb-4">
<!-- Add an 'onclick' event to the outer div that redirects to the project URL -->
<div class="hover-effect" onclick="location.href='{{ project.url }}';" style="cursor: pointer;">
<div class="bg-white shadow-lg rounded-lg overflow-hidden">
<div class="bg-cover bg-center h-56 p-4" style="background-image: url('{{ site.url }}{{ site.baseurl }}/images/teampic/{{ project.photo }}')">
</div>
<div class="p-5 h-20 text-left">
<span class="tracking-wide text-xl font-bold text-gray-700 title">{{ project.project_name }}</span>
</div>
<div class="p-4 h-36 text-left">
<p class="text-gray-500 text-sm">{{ project.tldr }}</p>
</div>
</div>
</div>
</div>
<!-- End card -->
{% endfor %}
</div>

