from pydantic import BaseModel, ConfigDict

class page(BaseModel):
    model_config = ConfigDict(extra="ignore")

class PageMetadata(BaseModel):
    """Model for page metadata."""
    schema: str | None = None
    pageOrder: list[str] | None = None
    activePageName: str | None = None


class bookmarkMetadata(BaseModel):
    model_config = ConfigDict(extra="ignore")

class versionMetadata(BaseModel):
    model_config = ConfigDict(extra="ignore")

class visualContainer(BaseModel):
    model_config = ConfigDict(extra="ignore")
    
class BaseSchema(BaseModel):
    model_config = ConfigDict(extra="ignore")

class bookmark(BaseModel):
    model_config = ConfigDict(extra="ignore")
