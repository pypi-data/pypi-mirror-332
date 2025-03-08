from typing import Any, Dict, List

from pydantic import BaseModel, ConfigDict, Field

from vector_bridge.schema.ai_knowledge import (BaseAIKnowledge,
                                               BaseAIKnowledgeChunk)
from vector_bridge.schema.helpers.enums import SortOrder


class AIKnowledgeCreate(BaseModel):
    content: str
    other: Dict[str, Any]


class AIKnowledgeChunk(BaseAIKnowledgeChunk):
    pass


class AIKnowledge(BaseAIKnowledge):
    model_config = ConfigDict(from_attributes=True)

    item_id: str
    chunks: List[AIKnowledgeChunk | BaseAIKnowledgeChunk] = Field(default_factory=list)
    other: Dict[str, Any]


class AIKnowledgeContentFilters(BaseModel):
    item_id: str = Field(default=None)
    limit: int = Field(default=100)
    offset: int = Field(default=0)
    sort_by: str = Field(default="timestamp")
    sort_order: SortOrder = Field(default=SortOrder.DESCENDING)

    class Config:
        extra = "allow"

    def to_non_empty_dict(self):
        _dict = self.model_dump()
        return {k: v for k, v in _dict.items() if v is not None and v != ""}

    def to_serializible_non_empty_dict(self):
        _dict = self.model_dump()
        if self.sort_order:
            _dict["sort_order"] = self.sort_order.value
        return {k: v for k, v in _dict.items() if v is not None and v != ""}
