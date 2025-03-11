from avatar_yaml.models.common import Metadata
import pytest

from avatar_yaml.models.schema import (
    TableDataInfo,
    TableInfo,
    get_standard_schema,
    Schema,
    ModelKind,
    SchemaSpec,
    get_standard_schema,
    _get_standard_schema,
)
from tests.conftest import from_pretty_yaml


def test_get_standard_schema_private():
    expected = Schema(
        kind=ModelKind.SCHEMA,
        metadata=Metadata(name="test"),
        spec=SchemaSpec(
            tables=[
                TableInfo(
                    name="table",
                    data=TableDataInfo(volume="volume", file="file.csv"),
                )
            ],
        ),
    )

    schema = _get_standard_schema(
        name="test", table_name="table", volume="volume", file="file.csv"
    )

    assert schema == expected


def test_get_standard_schema():
    schema = get_standard_schema(name="test", table_name="table", volume="volume", file="file.csv")
    expected = from_pretty_yaml("""kind: AvatarSchema
metadata:
  name: test
spec:
  tables:
  - name: table
    data:
      volume: volume
      file: file.csv
""")
    assert schema == expected
