from pydantic import BaseModel


class InfoApi(BaseModel):
    title: str
    description: str
    version: str

    class Config:
        json_schema_extra = {
            "example": {
                  "title": "Stable Protocol API v2",
                  "description": "Stable Protocol API v2",
                  "version": "1.0.4"
            }

        }
