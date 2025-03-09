# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["ListConnectionConfigsResponse"]


class ListConnectionConfigsResponse(BaseModel):
    id: str

    connector_name: str

    org_id: str
