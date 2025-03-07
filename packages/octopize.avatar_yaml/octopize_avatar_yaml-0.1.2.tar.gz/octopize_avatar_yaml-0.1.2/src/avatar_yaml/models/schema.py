from dataclasses import dataclass
from enum import StrEnum

from avatar_yaml.models.common import Metadata, ModelKind
from avatar_yaml.yaml_utils import to_yaml


class ColumnType(StrEnum):
    INT = "int"
    BOOL = "bool"
    CATEGORY = "category"
    NUMERIC = "float"
    DATETIME = "datetime"


@dataclass(frozen=True)
class TableDataInfo:
    volume: str
    file: str


@dataclass(frozen=True)
class ColumnInfo:
    field: str
    type: ColumnType
    value_type: str | None
    identifier: bool = False
    primary_key: bool = False
    time_series_time: bool = False


@dataclass(frozen=True)
class TableInfo:
    name: str
    data: TableDataInfo


@dataclass(frozen=True)
class SchemaSpec:
    tables: list[TableInfo]


@dataclass(frozen=True)
class Schema:
    kind: ModelKind
    metadata: Metadata
    spec: SchemaSpec


def get_table_data(volume: str, file: str) -> TableDataInfo:
    return TableDataInfo(volume=volume, file=file)


def get_original_table(table_name: str, volume: str, file: str) -> TableInfo:
    return TableInfo(
        name=table_name,
        data=get_table_data(volume=volume, file=file),
    )


def _get_standard_schema(name: str, table_name: str, volume: str, file: str) -> Schema:
    return Schema(
        kind=ModelKind.SCHEMA,
        metadata=Metadata(name=name),
        spec=SchemaSpec(
            tables=[get_original_table(table_name=table_name, volume=volume, file=file)],
        ),
    )


def get_standard_schema(name: str, table_name: str, volume: str, file: str) -> str:
    return to_yaml(_get_standard_schema(name, table_name, volume, file))
