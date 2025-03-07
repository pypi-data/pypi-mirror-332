from pydantic import BaseModel, Field
from typing import List, Optional


class WebpageMetadata(BaseModel):
    """Model representing metadata extracted from a webpage."""
    browser_title: Optional[str] = Field(None, description="Title from the browser tab")
    section_number: Optional[str] = Field(None, description="Section number if available")
    subject: Optional[str] = Field(None, description="Subject of the webpage")
    language: Optional[str] = Field(None, description="Language of the webpage")
    meta_tags: dict[str, str] = Field(default_factory=dict, description="Additional metadata from meta tags")


class WebpageContent(BaseModel):
    """Model representing the complete webpage content and metadata."""
    url: str = Field(..., description="URL of the webpage")
    status_code: int = Field(..., description="HTTP status code of the request")
    metadata: WebpageMetadata = Field(..., description="Extracted metadata from the webpage")
    content_lines: List[str] = Field(default_factory=list, description="Extracted text content lines")
    error_message: Optional[str] = Field(None, description="Error message if request fails") 