from typing import Dict, List, Optional, Union
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field

from vector_bridge.schema.ai_knowledge import BaseAIKnowledge
from vector_bridge.schema.helpers.enums import FileSystemType, SortOrder

# CREATES ---


class AIKnowledgeFileSystemItemCreate(BaseAIKnowledge):
    model_config = ConfigDict(from_attributes=True)

    name: str = Field(default=None)
    parent_id: Optional[str] = Field(default=None)
    source_documents_ids: Optional[List[str]] = Field(default_factory=list)
    type: FileSystemType = Field(default=FileSystemType.FILE)
    file_size_bytes: int = Field(default=0)
    starred: bool = Field(default=False)
    tags: List[str] = Field(default_factory=list)
    private: bool = Field(default=False)
    users_with_read_access: List[str] = Field(default_factory=list)
    users_with_write_access: List[str] = Field(default_factory=list)
    groups_with_read_access: List[str] = Field(default_factory=list)
    groups_with_write_access: List[str] = Field(default_factory=list)
    created_by: str
    cloud_stored: bool = Field(default=False)
    vectorized: bool = Field(default=True)


# OUTPUTS ---


class AIKnowledgeFileSystemItemChunk(BaseModel):
    item_id: str = Field(default_factory=lambda: str(uuid4()))
    index: int
    content: str


class AIKnowledgeFileSystemItem(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    item_id: str
    name: str
    chunks: List[AIKnowledgeFileSystemItemChunk] = Field(default_factory=list)
    parent: Optional["AIKnowledgeFileSystemItem"] = Field(default=None)
    source_documents: List["AIKnowledgeFileSystemItem"] = Field(default_factory=list)
    derived_documents: List["AIKnowledgeFileSystemItem"] = Field(default_factory=list)
    parent_id: Optional[str]
    parent_ids_hierarchy: List[str]
    type: FileSystemType
    file_size_bytes: int
    starred: bool
    tags: List[str]
    private: bool
    users_with_read_access: List[str]
    users_with_write_access: List[str]
    groups_with_read_access: List[str]
    groups_with_write_access: List[str]
    unique_identifier: str
    timestamp: str
    created_by: str
    cloud_stored: bool
    vectorized: bool = Field(default=True)
    archived: bool = Field(default=False)


AIKnowledgeFileSystemItem.model_rebuild()


class AIKnowledgeFileSystemItemsList(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    items: List[AIKnowledgeFileSystemItem]
    limit: Union[int, None] = Field(default=None)
    offset: Union[int, None] = Field(default=None)
    has_more: bool = Field(default=False)


class AIKnowledgeFileSystemFilters(BaseModel):
    file_name_like: str = Field(default=None)
    file_name_equal: str = Field(default=None)
    item_id: str = Field(default=None)
    parent_id: str = Field(default=None)
    parent_id_is_null: bool = Field(default=None)
    parent_ids_hierarchy_contains_any: List[str] = Field(default=None)
    source_documents_ids_contains_any: List[str] = Field(default=None)
    source_documents_ids_contains_all: List[str] = Field(default=None)
    type: FileSystemType = Field(default=None)
    is_starred: bool = Field(default=None)
    tags_contains_any: List[str] = Field(default=None)
    tags_contains_all: List[str] = Field(default=None)
    is_private: bool = Field(default=None)
    users_with_read_access_contains_any: List[str] = Field(default=None)
    users_with_read_access_contains_all: List[str] = Field(default=None)
    users_with_write_access_contains_any: List[str] = Field(default=None)
    users_with_write_access_contains_all: List[str] = Field(default=None)
    groups_with_read_access_contains_any: List[str] = Field(default=None)
    groups_with_read_access_contains_all: List[str] = Field(default=None)
    groups_with_write_access_contains_any: List[str] = Field(default=None)
    groups_with_write_access_contains_all: List[str] = Field(default=None)
    unique_identifier: str = Field(default="")
    file_size_bytes_min: int = Field(default=None)
    file_size_bytes_max: int = Field(default=None)
    timestamp_after: str = Field(default="")
    timestamp_before: str = Field(default="")
    is_cloud_stored: bool = Field(default=None)
    is_vectorized: bool = Field(default=None)
    is_archived: bool = Field(default=None)
    limit: int = Field(default=100)
    offset: int = Field(default=None)
    sort_by: str = Field(default="timestamp")
    sort_order: SortOrder = Field(default=SortOrder.DESCENDING)

    def to_non_empty_dict(self):
        _dict = self.model_dump()
        return {k: v for k, v in _dict.items() if v is not None and v != ""}

    def to_serializible_non_empty_dict(self):
        _dict = self.model_dump()
        if self.sort_order:
            _dict["sort_order"] = self.sort_order.value
        if self.type:
            _dict["type"] = self.type.value
        return {k: v for k, v in _dict.items() if v is not None and v != ""}


class FileSystemItemArchivedCount(BaseModel):
    files: int
    archived_files: int


class FileSystemItemCount(BaseModel):
    files: int
    folders: int


class FileSystemItemAggregatedCount(BaseModel):
    items: Dict[str, FileSystemItemCount]
