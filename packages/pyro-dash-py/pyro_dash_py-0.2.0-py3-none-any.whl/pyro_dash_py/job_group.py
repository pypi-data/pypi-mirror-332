from __future__ import annotations
from typing import Optional
from dataclasses import dataclass

from .core import GET, POST, require_resource
from .job import PyroJob, PyroJobResource
from .client import PyroApiClient


class PyroJobGroupResource:
    def __init__(self, client: PyroApiClient):
        self.client = client
        self._endpoint = "job_groups"

    @classmethod
    def from_client(cls, client: PyroApiClient) -> "PyroJobGroupResource":
        return PyroJobGroupResource(client)

    def create(self, name: str = "Untitled Group") -> PyroJobGroup:
        """
        # Create a job group

        ## Example
        ```python
        pyro = PyroDash(...)
        group = pyro.job_groups.create("PY999")
        ```
        """
        resp = self.client.request(POST, self._endpoint, {"name": name})
        _dict = {**resp, "_resource": self}
        return PyroJobGroup.from_dict(_dict)

    def list_jobs(self, id: str) -> list[PyroJob]:
        """
        # Retrieve jobs in a job group

        ## Example
        ```python
        pyro = PyroDash(...)
        job_group_id = "jg_2VF7h.."
        jobs = pyro.job_groups.list_jobs(job_group_id)
        ```
        """
        url = f"{self._endpoint}/{id}"
        resp = self.client.request(GET, url)
        jobs = []
        for job in resp["jobs"]:
            job_url = f"jobs/{job['id']}"
            full_job_raw = self.client.request(GET, job_url)
            as_dict = {**full_job_raw, "_resource": PyroJobResource(self.client)}
            jobs.append(PyroJob.from_dict(as_dict))

        return jobs

    def add_job(self, id: str, job_id: str) -> PyroJob:
        """
        # Add a job to a job group

        ## Example
        ```python
        pyro = PyroDash(...)
        group = pyro.job_groups.create()
        job_id = "j_r62X.."
        job = group.add_job(job_id)
        ```
        """
        url = f"{self._endpoint}/{id}/add_job"
        resp = self.client.request(POST, url, {"job_id": job_id})
        _dict = {**resp, "_resource": PyroJobResource(self.client)}
        return PyroJob.from_dict(_dict)


@dataclass
class PyroJobGroup:
    id: str
    name: str
    created_at: str
    is_active: str
    _resource: Optional[PyroJobGroupResource] = None

    @classmethod
    def default(cls, **kwargs) -> PyroJobGroup:
        return PyroJobGroup(**kwargs)

    @classmethod
    def from_dict(cls, _dict: dict) -> PyroJobGroup:
        return PyroJobGroup(
            _dict["id"],
            _dict["name"],
            _dict["created_at"],
            _dict["is_active"],
            _dict["_resource"],
        )

    @require_resource
    def list_jobs(self) -> list[PyroJob]:
        """
        # Retrieve jobs in this job group

        ## Example
        ```python
        job_group = PyroJobGroup(...)
        job = job_group.list_jobs()
        ```
        """
        assert self._resource is not None
        return self._resource.list_jobs(self.id)

    @require_resource
    def add_job(self, job_id: str) -> PyroJob:
        """
        # Add a job to this job group

        ## Example
        ```python
        job_group = PyroJobGroup(...)
        job_id = "j_r62X"
        job = job_group.add_job(job_id)
        ```
        """
        assert self._resource is not None
        return self._resource.add_job(self.id, job_id)
