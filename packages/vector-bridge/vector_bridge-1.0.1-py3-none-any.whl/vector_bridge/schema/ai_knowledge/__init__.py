from typing import Dict, List, Optional, Union

from pydantic import BaseModel, ConfigDict, Field


class PresignedUploadUrl(BaseModel):
    url: str
    body: dict


class BaseAIKnowledgeChunk(BaseModel):
    item_id: str
    index: int
    content: str


class BaseAIKnowledge(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    schema_name: str = Field(default="")
    unique_identifier: str = Field(default="")
    content: Optional[str] = None
    timestamp: str

    _chunk_size: int = 384
    _chunk_overlap: int = 76


class AIKnowledgeList(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    items: List[Dict]
    limit: Union[int, None] = Field(default=None)
    offset: Union[int, None] = Field(default=None)
    has_more: bool = Field(default=False)
