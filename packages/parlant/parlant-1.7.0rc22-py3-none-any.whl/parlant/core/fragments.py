# Copyright 2024 Emcie Co Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import NewType, Optional, Sequence, cast
from typing_extensions import override, TypedDict, Self

from parlant.core.async_utils import ReaderWriterLock
from parlant.core.persistence.document_database_helper import DocumentStoreMigrationHelper
from parlant.core.tags import TagId
from parlant.core.common import ItemNotFoundError, UniqueId, Version, generate_id
from parlant.core.persistence.common import ObjectId
from parlant.core.persistence.document_database import (
    BaseDocument,
    DocumentDatabase,
    DocumentCollection,
)

FragmentId = NewType("FragmentId", str)


@dataclass(frozen=True)
class FragmentField:
    name: str
    description: str
    examples: list[str]


@dataclass(frozen=True)
class Fragment:
    TRANSIENT_ID = FragmentId("<transient>")
    INVALID_ID = FragmentId("<invalid>")

    id: FragmentId
    creation_utc: datetime
    value: str
    fields: Sequence[FragmentField]
    tags: Sequence[TagId]


class FragmentUpdateParams(TypedDict, total=True):
    value: str
    fields: Sequence[FragmentField]


class FragmentStore(ABC):
    @abstractmethod
    async def create_fragment(
        self,
        value: str,
        fields: Sequence[FragmentField],
        creation_utc: Optional[datetime] = None,
    ) -> Fragment: ...

    @abstractmethod
    async def read_fragment(
        self,
        fragment_id: FragmentId,
    ) -> Fragment: ...

    @abstractmethod
    async def update_fragment(
        self,
        fragment_id: FragmentId,
        params: FragmentUpdateParams,
    ) -> Fragment: ...

    @abstractmethod
    async def delete_fragment(
        self,
        fragment_id: FragmentId,
    ) -> None: ...

    @abstractmethod
    async def list_fragments(
        self,
    ) -> Sequence[Fragment]: ...

    @abstractmethod
    async def add_tag(
        self,
        fragment_id: FragmentId,
        tag_id: TagId,
        creation_utc: Optional[datetime] = None,
    ) -> Fragment: ...

    @abstractmethod
    async def remove_tag(
        self,
        fragment_id: FragmentId,
        tag_id: TagId,
    ) -> Fragment: ...


class _FragmentFieldDocument(TypedDict):
    name: str
    description: str
    examples: list[str]


class _FragmentDocument(TypedDict, total=False):
    id: ObjectId
    version: Version.String
    creation_utc: str
    value: str
    fields: Sequence[_FragmentFieldDocument]


class _FragmentTagAssociationDocument(TypedDict, total=False):
    id: ObjectId
    version: Version.String
    creation_utc: str
    fragment_id: FragmentId
    tag_id: TagId


class FragmentDocumentStore(FragmentStore):
    VERSION = Version.from_string("0.1.0")

    def __init__(self, database: DocumentDatabase, allow_migration: bool = False) -> None:
        self._database = database
        self._fragments_collection: DocumentCollection[_FragmentDocument]
        self._fragment_tag_association_collection: DocumentCollection[
            _FragmentTagAssociationDocument
        ]
        self._allow_migration = allow_migration
        self._lock = ReaderWriterLock()

    async def _document_loader(self, doc: BaseDocument) -> Optional[_FragmentDocument]:
        if doc["version"] == "0.1.0":
            return cast(_FragmentDocument, doc)

        return None

    async def _association_document_loader(
        self, doc: BaseDocument
    ) -> Optional[_FragmentTagAssociationDocument]:
        if doc["version"] == "0.1.0":
            return cast(_FragmentTagAssociationDocument, doc)
        return None

    async def __aenter__(self) -> Self:
        async with DocumentStoreMigrationHelper(
            store=self,
            database=self._database,
            allow_migration=self._allow_migration,
        ):
            self._fragments_collection = await self._database.get_or_create_collection(
                name="fragments",
                schema=_FragmentDocument,
                document_loader=self._document_loader,
            )

            self._fragment_tag_association_collection = (
                await self._database.get_or_create_collection(
                    name="fragment_tag_associations",
                    schema=_FragmentTagAssociationDocument,
                    document_loader=self._association_document_loader,
                )
            )

        return self

    async def __aexit__(
        self,
        exc_type: Optional[type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[object],
    ) -> bool:
        return False

    def _serialize_fragment(self, fragment: Fragment) -> _FragmentDocument:
        return _FragmentDocument(
            id=ObjectId(fragment.id),
            version=self.VERSION.to_string(),
            creation_utc=fragment.creation_utc.isoformat(),
            value=fragment.value,
            fields=[
                {"name": s.name, "description": s.description, "examples": s.examples}
                for s in fragment.fields
            ],
        )

    async def _deserialize_fragment(self, fragment_document: _FragmentDocument) -> Fragment:
        tags = [
            doc["tag_id"]
            for doc in await self._fragment_tag_association_collection.find(
                {"fragment_id": {"$eq": fragment_document["id"]}}
            )
        ]

        return Fragment(
            id=FragmentId(fragment_document["id"]),
            creation_utc=datetime.fromisoformat(fragment_document["creation_utc"]),
            value=fragment_document["value"],
            fields=[
                FragmentField(name=d["name"], description=d["description"], examples=d["examples"])
                for d in fragment_document["fields"]
            ],
            tags=tags,
        )

    @override
    async def create_fragment(
        self,
        value: str,
        fields: Sequence[FragmentField],
        creation_utc: Optional[datetime] = None,
    ) -> Fragment:
        async with self._lock.writer_lock:
            creation_utc = creation_utc or datetime.now(timezone.utc)

            fragment = Fragment(
                id=FragmentId(generate_id()),
                value=value,
                fields=fields,
                creation_utc=creation_utc,
                tags=[],
            )

            await self._fragments_collection.insert_one(
                document=self._serialize_fragment(fragment=fragment)
            )

        return fragment

    @override
    async def read_fragment(
        self,
        fragment_id: FragmentId,
    ) -> Fragment:
        async with self._lock.reader_lock:
            fragment_document = await self._fragments_collection.find_one(
                filters={"id": {"$eq": fragment_id}}
            )

        if not fragment_document:
            raise ItemNotFoundError(item_id=UniqueId(fragment_id))

        return await self._deserialize_fragment(fragment_document)

    @override
    async def update_fragment(
        self,
        fragment_id: FragmentId,
        params: FragmentUpdateParams,
    ) -> Fragment:
        async with self._lock.writer_lock:
            fragment_document = await self._fragments_collection.find_one(
                filters={"id": {"$eq": fragment_id}}
            )

            if not fragment_document:
                raise ItemNotFoundError(item_id=UniqueId(fragment_id))

            result = await self._fragments_collection.update_one(
                filters={"id": {"$eq": fragment_id}},
                params={
                    "value": params["value"],
                    "fields": [
                        {"name": s.name, "description": s.description, "examples": s.examples}
                        for s in params["fields"]
                    ],
                },
            )

        assert result.updated_document

        return await self._deserialize_fragment(fragment_document=result.updated_document)

    async def list_fragments(
        self,
    ) -> Sequence[Fragment]:
        async with self._lock.reader_lock:
            return [
                await self._deserialize_fragment(e)
                for e in await self._fragments_collection.find({})
            ]

    @override
    async def delete_fragment(
        self,
        fragment_id: FragmentId,
    ) -> None:
        async with self._lock.writer_lock:
            result = await self._fragments_collection.delete_one({"id": {"$eq": fragment_id}})

        if result.deleted_count == 0:
            raise ItemNotFoundError(item_id=UniqueId(fragment_id))

    @override
    async def add_tag(
        self,
        fragment_id: FragmentId,
        tag_id: TagId,
        creation_utc: Optional[datetime] = None,
    ) -> Fragment:
        async with self._lock.writer_lock:
            fragment = await self.read_fragment(fragment_id)

            if tag_id in fragment.tags:
                return fragment

            creation_utc = creation_utc or datetime.now(timezone.utc)

            association_document: _FragmentTagAssociationDocument = {
                "id": ObjectId(generate_id()),
                "version": self.VERSION.to_string(),
                "creation_utc": creation_utc.isoformat(),
                "fragment_id": fragment_id,
                "tag_id": tag_id,
            }

            _ = await self._fragment_tag_association_collection.insert_one(
                document=association_document
            )

            fragment_document = await self._fragments_collection.find_one(
                {"id": {"$eq": fragment_id}}
            )

        if not fragment_document:
            raise ItemNotFoundError(item_id=UniqueId(fragment_id))

        return await self._deserialize_fragment(fragment_document=fragment_document)

    @override
    async def remove_tag(
        self,
        fragment_id: FragmentId,
        tag_id: TagId,
    ) -> Fragment:
        async with self._lock.writer_lock:
            delete_result = await self._fragment_tag_association_collection.delete_one(
                {
                    "fragment_id": {"$eq": fragment_id},
                    "tag_id": {"$eq": tag_id},
                }
            )

            if delete_result.deleted_count == 0:
                raise ItemNotFoundError(item_id=UniqueId(tag_id))

            fragment_document = await self._fragments_collection.find_one(
                {"id": {"$eq": fragment_id}}
            )

        if not fragment_document:
            raise ItemNotFoundError(item_id=UniqueId(fragment_id))

        return await self._deserialize_fragment(fragment_document=fragment_document)
