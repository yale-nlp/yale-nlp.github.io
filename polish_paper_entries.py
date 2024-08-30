import difflib
import os

import requests
import yaml
from langchain.prompts import ChatPromptTemplate
from langchain.utilities import ArxivAPIWrapper
from langchain_openai import ChatOpenAI
from requests.sessions import Session
from tqdm import tqdm

S2_API_KEY = os.environ.get("S2_API_KEY")


def get_paper(
    session: Session, paper_id: str, fields: str = "paperId,title,abstract", **kwargs
) -> dict:
    params = {
        "fields": fields,
        **kwargs,
    }
    headers = {
        "X-API-KEY": S2_API_KEY,
    }

    with session.get(
        f"https://api.semanticscholar.org/graph/v1/paper/{paper_id}",
        params=params,
        headers=headers,
    ) as response:
        response.raise_for_status()
        return response.json()


def search_paper_by_title(session: Session, title: str, limit: int = 1) -> dict:
    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    query_params = {"query": title, "limit": limit, "fields": "paperId,title,abstract"}
    headers = {
        "X-API-KEY": S2_API_KEY,
    }

    with session.get(url, params=query_params, headers=headers) as response:
        response.raise_for_status()
        results = response.json()
        if results["data"]:
            return results["data"][0]  # Return the first result
    return None


def search_arxiv(title):
    arxiv = ArxivAPIWrapper()
    try:
        results = arxiv.run(title)
        if results:
            return results.split("\n")[1].split(": ")[1]
    except Exception as e:
        print(f"Error searching for '{title}': {e}")
    return None


def get_paper_info(session, s2_id, title):
    try:
        if s2_id:
            try:
                paper = get_paper(session, s2_id)
                return paper
            except requests.exceptions.RequestException:
                # If s2_id fails, fall through to search by title
                pass

        # Search by title
        paper = search_paper_by_title(session, title)
        if (
            paper
            and difflib.SequenceMatcher(
                None, paper["title"].lower(), title.lower()
            ).ratio()
            >= 0.95
        ):
            return paper

        # If no match found
        print(f"No matching paper found for title: {title}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching paper info for {s2_id or title}: {e}")
        return None


def get_categories(title, abstract):
    chat = ChatOpenAI(model="gpt-4o-mini-2024-07-18")
    prompt = ChatPromptTemplate.from_template(
        "Given the following paper title and abstract, select up to 3 most relevant categories from this list: "
        "[ foundation models, evaluation, training methods, interpretability, code generation, document understanding, specialized domains, LM agents ]\n"
        "Do not explain. One category per line. Just output the categories.\n\n"
        "Title: {title}\n\n"
        "Abstract: {abstract}\n\n"
        "Categories:"
    )
    response = chat.invoke(prompt.format(title=title, abstract=abstract))
    categories = [cat.strip() for cat in response.content.split("\n")]
    return categories[:3]


def process_file(file_path):
    with open(file_path, "r") as file:
        data = yaml.safe_load(file)

    updated_data = []
    with requests.Session() as session:
        for entry in tqdm(data, desc=f"Processing {os.path.basename(file_path)}"):
            # Fetch paper info from Semantic Scholar
            s2_id = entry["url"].split("/")[-1] if entry["url"] is not None else None
            paper_info = get_paper_info(session, s2_id, entry["title"])

            if paper_info:
                # Get categories
                categories = get_categories(paper_info["title"], paper_info["abstract"])

                # Update entry
                updated_entry = {
                    "url": entry["url"]
                    or (
                        f"https://www.semanticscholar.org/paper/{paper_info['paperId']}"
                        if paper_info.get("paperId")
                        else None
                    ),
                    "title": f'"{paper_info["title"]}"',
                    "venue": entry["venue"],
                    "year": entry["year"],
                    "authors": (
                        entry["authors"].split(", ")
                        if isinstance(entry["authors"], str)
                        else entry["authors"]
                    ),
                    "project": entry["project"],
                    "display": entry["display"],
                }
                # Add categories if not present in the original entry
                if "category" not in entry:
                    updated_entry["category"] = categories
                else:
                    updated_entry["category"] = entry["category"]

                # Add paper_link if it exists in the original entry
                if "paper_link" in entry:
                    updated_entry["paper_link"] = entry["paper_link"]

                # Add arXiv URL if not present
                if entry["url"] is not None and "arxiv.org" not in entry["url"]:
                    arxiv_url = search_arxiv(paper_info["title"])
                    if arxiv_url:
                        updated_entry["arxiv_url"] = arxiv_url

                updated_data.append(updated_entry)
            else:
                # If paper_info is None, keep the original entry
                updated_data.append(entry)
                print(f"Skipping entry with URL: {entry['url']}")

    new_file_path = file_path.replace(".yml", "_updated.yml")
    with open(new_file_path, "w") as file:
        yaml.dump(
            updated_data,
            file,
            sort_keys=False,
            default_flow_style=False,
            indent=2,
            width=float("inf"),
        )
    print(f"Updated file saved as: {new_file_path}")


def main():
    directory = "_data/publications"
    files = [f for f in os.listdir(directory) if f.endswith("_publist.yml")]
    sorted_files = sorted(files, reverse=True)
    print(sorted_files)
    for filename in sorted_files:
        file_path = os.path.join(directory, filename)
        process_file(file_path)


if __name__ == "__main__":
    main()
