import requests
from typing import List, Optional, Dict, Any

class JobSearchRequest:
    def __init__(self, title: str, size: int, company_name: Optional[str] = None, city: Optional[str] = None,
                 state: Optional[str] = None, country: Optional[str] = None, is_remote: Optional[bool] = None):
        self.title = title
        self.company_name = company_name
        self.city = city
        self.state = state
        self.country = country
        self.is_remote = is_remote
        self.size = size

    def to_dict(self) -> Dict[str, Any]:
        return {
            "title": self.title,
            "companyName": self.company_name,
            "city": self.city,
            "state": self.state,
            "country": self.country,
            "isRemote": self.is_remote,
            "size": self.size,
        }

class GeographicLocation:
    def __init__(self, lat: float, lon: float):
        self.lat = lat
        self.lon = lon

class JobLocation:
    def __init__(self, city: str, country: str, state: str, loc: GeographicLocation):
        self.city = city
        self.country = country
        self.state = state
        self.loc = loc

class Job:
    def __init__(self, name: str, company_name: str, location: JobLocation, feed: str, job_id: str, created: str):
        self.name = name
        self.company_name = company_name
        self.location = location
        self.feed = feed
        self.id = job_id
        self.created = created

class JobSearchResult:
    def __init__(self, jobs: List[Job]):
        self.jobs = jobs

class JobSearchService:
    BASE_URL = "https://api.jopilot.net"

    @staticmethod
    def search_jobs(request: JobSearchRequest) -> Dict[str, Any]:  # Return dictionary instead of JobSearchResult
        try:
            response = requests.post(f"{JobSearchService.BASE_URL}/api/v1/search", json=request.to_dict())
            response.raise_for_status()
            return response.json()  # Return raw JSON response
        except requests.RequestException as e:
            print(f"Error searching jobs: {e}")
            raise Exception("There was an error connecting to the job search service.")
