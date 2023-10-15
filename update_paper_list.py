import argparse
import yaml
import os

import requests

def save_to_yaml(data, file_path):
    with open(file_path, 'w') as file:
        for item in data:
            yaml.dump([item], file, default_flow_style=False, sort_keys=False)
            file.write('\n')  # separator for better readability

def load_yaml_file(file_path):
    with open(file_path, 'r') as file:
        # Load all documents in the YAML file
        docs = list(yaml.safe_load_all(file))

    # Flattening the list of lists into a single list
    return [item for sublist in docs for item in sublist]

def get_author_papers(author_id):
    rsp = requests.get(f'https://api.semanticscholar.org/graph/v1/author/{author_id}/papers',
                       params={'fields': 'title,url,year,authors,venue,abstract', 'limit': 1000})
    rsp.raise_for_status()
    return rsp.json()['data']


def find_authored_papers(author_id):
    papers = get_author_papers(author_id)

    return sorted(papers, key=lambda p: (-p['year'], p['title']))

venue_dict = {
    "Annual Meeting of the Association for Computational Linguistics": "ACL",
    "Conference of the European Chapter of the Association for Computational Linguistics": "EACL",
    "arXiv.org": "ArXiv",
    "Conference on Empirical Methods in Natural Language Processing": "EMNLP",
    "International Conference on Computational Linguistics": "COLING",
    "North American Chapter of the Association for Computational Linguistics": "NAACL",
    "Neural Information Processing Systems": "NeurIPS",
    "International Conference on Machine Learning": "ICML",
    "International Conference on Learning Representations": "ICLR",
}

paper_order = ["Preprint", "other", "EACL", "ICLR", "ACL", "NAACL", "ICML", "NeurIPS", "EMNLP", "COLING"][::-1]

def paper_order_index(venue):
    try:
        return paper_order.index(venue.split(" ")[0])
    except ValueError:
        return paper_order.index("other")  # Place it at the end if not in paper_order
    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--author_id', default='2527954')
    parser.add_argument('--start_year', default='2022')
    args = parser.parse_args()

    # paper might change the title, so we need to remove the previous record
    existing_papers_dict = {}
    for filename in os.listdir('_data/publications'):
        filepath = f'_data/publications/{filename}'
        paper_list = load_yaml_file(filepath)
        if not paper_list:
            continue
        for paper in paper_list:
            existing_papers_dict[paper["url"]] = paper

    authored_papers = find_authored_papers(args.author_id)
    for paper in authored_papers:
        if int(paper["year"]) < int(args.start_year):
            continue
        
        year = paper["year"]
        paper["authors"] = ", ".join([author["name"] for author in paper["authors"]]) + "."
        del paper["paperId"]
        del paper["abstract"]
        paper["project"] = "other"
        
        paper["title"] = paper["title"].strip(".")

        if not paper["venue"]:
            paper["venue"] = "Preprint"
        else:
            if paper["venue"] in venue_dict:
                paper["venue"] = venue_dict[paper["venue"]]
            paper["venue"] = f"{paper['venue']} {year}"
            if paper["venue"].startswith("ArXiv"):
                paper["venue"] = "Preprint"
        
        paper["display"] = 1
        filepath = f'_data/publications/{year}_publist.yml'
        paper_list = load_yaml_file(filepath)
        if not paper_list:
            paper_list = []

        if paper["url"] not in existing_papers_dict:
            paper_list.append(paper)
        
        # update the paper record if the venue is changed from Preprint to others
        if paper["url"] in existing_papers_dict \
            and existing_papers_dict[paper["url"]]["venue"].startswith("Preprint") \
            and paper["venue"] != "Preprint":
            paper_list = [p for p in paper_list if p["url"] != paper["url"]]
            paper_list.append(paper)
        
        # sorted paper list by venue and make the venue order (starts with) as above
        paper_list = sorted(paper_list, key=lambda p: (paper_order_index(p["venue"]), p["venue"]))
        save_to_yaml(paper_list, filepath)
            

if __name__ == '__main__':
    main()