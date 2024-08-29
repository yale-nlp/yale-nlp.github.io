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
  display: inline-block;
  padding: 2px 8px;
  margin: 2px 4px 2px 0;
  text-decoration: none;
  border-radius: 3px;
  font-size: 12px;
  background-color: #f0f0f0;
  color: #333;
}

.publication-category-dataset {
  background-color: #e3f2fd;
  color: #1565c0;
}

.publication-category-reasoning {
  background-color: #e8f5e9;
  color: #2e7d32;
}

.publication-category-evaluation {
  background-color: #fff3e0;
  color: #e65100;
}

.publication-category-document-understanding {
  background-color: #f3e5f5;
  color: #6a1b9a;
}

.publication-category-specialized-domains {
  background-color: #e1f5fe;
  color: #0277bd;
}

.publication-item {
  margin-bottom: 20px;
}
.publication-title {
  font-weight: bold;
  color: #4e5d99;
  text-decoration: none;
  transition: all 0.5s ease;
  margin-right: 10px;
}

.publication-title-container {
  display: flex;
  align-items: baseline;
  margin-bottom: 5px;
}

.publication-award {
  color: #ff0000;
  margin-left: 10px;
  font-weight: bold;
  font-style: italic;
}

.publication-authors {
  display: block;
  margin-bottom: 5px;
}

.publication-venue {
  font-style: italic;
  padding: 2px 6px;
  border-radius: 4px;
  margin-right: 5px;
}

.publication-venue-preprint {
  background-color: #e3f2fd;
  color: #1565c0;
}

.publication-venue-journal {
  background-color: #e8f5e9;
  color: #2e7d32;
}

.publication-venue-conference {
  background-color: #f3e5f5;
  color: #6a1b9a;  
}

.publication-venue-workshop {
  background-color: #f5ead5;
  color: #ad8539;
}

.publication-venue-categories {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
}

.publication-categories {
  display: inline;
  margin-left: 5px;
}

.publication-category {
  display: inline-block;
  padding: 2px 8px;
  margin: 2px 4px 2px 0;
  text-decoration: none;
  border-radius: 3px;
  font-size: 12px;
  background-color: #f0f0f0;
  color: #333;
}

.separator {
  margin: 0 5px;
  color: #999;
}

/* New styles for filter section */
#category-filter {
  /* margin-bottom: 20px; */
  display: flex;
  flex-wrap: wrap;
  align-items: center;
}

#category-filter h5 {
  margin-right: 15px;
  margin-bottom: 10px;
}

.category-label {
  display: inline-block;
  padding: 2px 10px;
  margin-right: 15px;
  /* margin-bottom: 10px; */
  border-radius: 4px;
  margin-top: 5px;
  cursor: pointer;
  font-size: small;
  background-color: #f0f0f0;
  color: #333;
  opacity: 0.4;
}

.category-checkbox {
  display: none;
}

.category-checkbox:checked + .category-label {
  opacity: 1;
  box-shadow: 0 0 6px rgba(0, 0, 0, 0.5);
}

#publication-type-filter {
  /* margin-bottom: 20px; */
  display: flex;
  flex-wrap: wrap;
  align-items: center;
}

#publication-type-filter h5 {
  margin-right: 15px;
  display: block;
  width: 100%;  
  /* margin-bottom: 10px; */
}

.publication-type-checkbox {
  display: none;
}

.publication-type-label {
  display: inline-block;
  padding: 2px 10px;
  margin-right: 15px;
  /* margin-bottom: 10px; */
  border-radius: 4px;
  cursor: pointer;
  font-size: small;
  font-style: italic;
  opacity: 0.4; 
}

.publication-type-checkbox:checked + .publication-type-label {
  opacity: 1;
  box-shadow: 0 0 6px rgba(0, 0, 0, 0.5);
}

.publication-type-label-preprint {
  background-color: #e3f2fd;
  color: #1565c0;
}

.publication-type-label-journal {
  background-color: #e8f5e9;
  color: #2e7d32;
}

.publication-type-label-conference {
  background-color: #f3e5f5;
  color: #6a1b9a;  
}

.publication-type-label-workshop {
  background-color: #f5ead5;
  color: #ad8539;
}
</style>

<div id="category-filter">
  <h5>Filter by category:</h5>
  <input type="checkbox" id="filter-default" class="category-checkbox" value="default" checked>
  <label for="filter-default" class="category-label">Default</label>

  <input type="checkbox" id="filter-dataset" class="category-checkbox" value="training methods" checked>
  <label for="filter-dataset" class="category-label">Training methods</label>

  <input type="checkbox" id="filter-foundation-models" class="category-checkbox" value="foundation models" checked>
  <label for="filter-foundation-models" class="category-label">Foundation models</label>

  <input type="checkbox" id="filter-reasoning" class="category-checkbox" value="reasoning" checked>
  <label for="filter-reasoning" class="category-label">Reasoning</label>

  <input type="checkbox" id="filter-evaluation" class="category-checkbox" value="evaluation" checked>
  <label for="filter-evaluation" class="category-label">Evaluation</label>

  <input type="checkbox" id="filter-specialized-domains" class="category-checkbox" value="specialized-domains" checked>
  <label for="filter-specialized-domains" class="category-label">Specialized Domains</label>
</div>
<div id="publication-type-filter">
  <h5>Filter by publication type:</h5>
  <input type="checkbox" id="filter-preprint" class="publication-type-checkbox" checked>
  <label for="filter-preprint" class="publication-type-label publication-type-label-preprint">Preprint</label>

  <input type="checkbox" id="filter-journal" class="publication-type-checkbox" checked>
  <label for="filter-journal" class="publication-type-label publication-type-label-journal">Journal</label>

  <input type="checkbox" id="filter-conference" class="publication-type-checkbox" checked>
  <label for="filter-conference" class="publication-type-label publication-type-label-conference">Conference</label>

  <input type="checkbox" id="filter-workshop" class="publication-type-checkbox" checked>
  <label for="filter-workshop" class="publication-type-label publication-type-label-workshop">Workshop</label>
</div>

<div id="publication-list" class="justified-content">

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

<ul>
{% for publi in publication_data %}
    {% if publi.display != 0 %}
        {% assign pub_type = "conference" %}
        {% if publi.venue == "Preprint" %}
            {% assign pub_type = "preprint" %}
        {% elsif publi.venue contains "workshop" %}
            {% assign pub_type = "workshop" %}
        {% elsif publi.publication-type == "journal" %}
            {% assign pub_type = "journal" %}
        {% endif %}
        <li class="publication-item" data-pub-type="{{ pub_type }}" 
          data-category="{% if publi.category %}{{ publi.category | join: ',' | downcase }}{% else %}default{% endif %}">
            <div class="publication-title-container">
                <a class="publication-title" href="{% if publi.paper_link %}{{ publi.paper_link }}{% else %}{{ publi.url }}{% endif %}" target="_blank">{{ publi.title }}</a>
                {% if publi.award %}
                    <span class="publication-award">🏆&nbsp;&nbsp;{{ publi.award }}</span>
                {% endif %}
            </div>
            <span class="publication-authors">{{ publi.authors | join: ', ' }}</span>
            <div class="publication-venue-categories">
                <span class="publication-venue publication-venue-{{ pub_type }}">{{ publi.venue }}</span>
                {% if publi.category %}
                    <span class="separator">|</span>
                    <div class="publication-categories">
                    {% for cat in publi.category %}
                        <span class="publication-category publication-category-{{ cat | slugify }}" data-category="{{ cat }}">{{ cat }}</span>
                    {% endfor %}
                    </div>
                {% else %}
                    <span class="publication-category publication-category-default" data-category="default">Default</span>
                {% endif %}
            </div>
        </li>
    {% endif %}
{% endfor %}
{% endfor %}
</ul>

</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const categoryCheckboxes = document.querySelectorAll('.category-checkbox');
  const typeCheckboxes = document.querySelectorAll('.publication-type-checkbox');
  const publications = document.querySelectorAll('.publication-item');

  function filterPublications() { // Combined filtering function
    const selectedCategories = Array.from(categoryCheckboxes)
      .filter(cb => cb.checked)
      .map(cb => cb.value);

    const selectedTypes = Array.from(typeCheckboxes)
      .filter(cb => cb.checked)
      .map(cb => cb.id.replace('filter-', ''));

    publications.forEach(pub => {
      const pubCategories = Array.from(pub.querySelectorAll('.publication-category'))
        .map(cat => cat.dataset.category);
      const pubType = pub.dataset.pubType;

      const matchesCategory = selectedCategories.length === 0 || 
                              selectedCategories.some(cat => pubCategories.includes(cat)) ||
                              (pubCategories.length === 0 && selectedCategories.includes('default'));
      const matchesType = selectedTypes.length === 0 || selectedTypes.includes(pubType);

      if (matchesCategory && matchesType) {
        pub.style.display = '';
      } else {
        pub.style.display = 'none';
      }
    });
  }

  categoryCheckboxes.forEach(checkbox => {
    checkbox.addEventListener('change', filterPublications); 
  });

  typeCheckboxes.forEach(checkbox => {
    checkbox.addEventListener('change', filterPublications); 
  });

  // Initial filter application
  filterPublications(); 
});
</script>