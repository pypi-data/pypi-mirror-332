import requests
import pandas as pd
from typing import List, Dict, Optional
from datetime import datetime

class PubMedFetcher:
    BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    FETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

    def __init__(self, email: str):
        self.email = email

    def fetch_papers(self, query: str, max_results: int = 100) -> List[Dict]:
        """Fetch papers from PubMed based on a query."""
        search_params = {
            "db": "pubmed",
            "term": query,
            "retmax": max_results,
            "retmode": "json",
            "email": self.email
        }
        response = requests.get(self.BASE_URL, params=search_params)
        response.raise_for_status()
        paper_ids = response.json().get("esearchresult", {}).get("idlist", [])
        papers = []
        for paper_id in paper_ids:
            paper_details = self._fetch_paper_details(paper_id)
            if paper_details:
                papers.append(paper_details)
        return papers

    def _fetch_paper_details(self, paper_id: str) -> Optional[Dict]:
        """Fetch details for a single paper."""
        fetch_params = {
            "db": "pubmed",
            "id": paper_id,
            "retmode": "xml",
            "email": self.email
        }
        response = requests.get(self.FETCH_URL, params=fetch_params)
        response.raise_for_status()
        # Parse XML and extract details
        # This is a simplified example; you'll need to implement XML parsing
        return {
            "PubmedID": paper_id,
            "Title": "Sample Title",
            "Publication Date": datetime.now().strftime("%Y-%m-%d"),
            "Non-academic Author(s)": "Sample Author",
            "Company Affiliation(s)": "Sample Company",
            "Corresponding Author Email": "sample@example.com"
        }

    def filter_non_academic_authors(self, papers: List[Dict]) -> List[Dict]:
        """Filter papers with non-academic authors."""
        # Implement your heuristic here
        return [paper for paper in papers if "Sample Company" in paper["Company Affiliation(s)"]]

    def to_csv(self, papers: List[Dict], filename: Optional[str] = None):
        """Output papers to a CSV file or print to console."""
        df = pd.DataFrame(papers)
        if filename:
            df.to_csv(filename, index=False)
        else:
            print(df.to_string(index=False))