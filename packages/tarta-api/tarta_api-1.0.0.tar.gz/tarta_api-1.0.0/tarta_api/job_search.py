import requests
from typing import List, Optional, Dict, Any

class JobSearchRequest:
    def __init__(
        self, title: str, size: int, company_name: Optional[str] = None,
        city: Optional[str] = None, state: Optional[str] = None,
        country: Optional[str] = None, is_remote: Optional[bool] = None
    ):
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
    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude

class JobLocation:
    def __init__(self, city: str, country: str, state: str, coordinates: GeographicLocation):
        self.city = city
        self.country = country
        self.state = state
        self.coordinates = coordinates

class Job:
    def __init__(self, title: str, company: str, location: JobLocation, source: str, job_id: str, posted_date: str):
        self.title = title
        self.company = company
        self.location = location
        self.source = source
        self.id = job_id
        self.posted_date = posted_date

class JobSearchResult:
    def __init__(self, jobs: List[Job]):
        self.jobs = jobs

class JobSearchService:
    BASE_URL = "https://api.tarta.ai"

    @staticmethod
    def search_jobs(request: JobSearchRequest) -> Dict[str, Any]:
        url = f"{JobSearchService.BASE_URL}/api/v1/search"
        try:
            response = requests.post(url, json=request.to_dict())
            response.raise_for_status()
            return response.json()
        except requests.RequestException as error:
            print(f"Error searching jobs: {error}")
            raise RuntimeError("Failed to connect to the job search service.")
