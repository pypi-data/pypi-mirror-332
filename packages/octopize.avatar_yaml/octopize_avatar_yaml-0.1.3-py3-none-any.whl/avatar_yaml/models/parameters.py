from dataclasses import dataclass
from typing import Any

from avatar_yaml.models.common import Metadata, ModelKind
from avatar_yaml.yaml_utils import to_yaml


@dataclass(frozen=True)
class AvatarizationParameters:
    k: int
    ncp: int | None = None
    use_categorical_reduction: bool | None = None
    column_weights: dict[str, float] | None = None
    exclude_variables: dict[str, Any] | None = None
    imputation: dict[str, Any] | None = None


@dataclass(frozen=True)
class TimeSeriesParameters:
    projection: dict[str, Any] | None = None
    alignment: dict[str, Any] | None = None


@dataclass(frozen=True)
class SignalMetricsParameters:
    ncp: int | None = None
    use_categorical_reduction: bool | None = None
    imputation: dict[str, Any] | None = None


@dataclass(frozen=True)
class PrivacyMetricsParameters:
    ncp: int | None = None
    use_categorical_reduction: bool | None = None
    known_variables: list[str] | None = None
    target: str | None = None
    closest_rate_percentage_threshold: float | None = None
    closest_rate_ratio_threshold: float | None = None
    categorical_hidden_rate_variables: list[str] | None = None
    imputation: dict[str, Any] | None = None


@dataclass(frozen=True)
class Results:
    volume: str | None = None
    path: str | None = None
    format: str | None = None
    name_template: str | None = None


@dataclass(frozen=True)
class ParametersSpec:
    schema: str
    avatarization: dict[str, AvatarizationParameters | dict[str, Any]] | None = None
    avatarization_ref: str | None = None
    time_series: dict[str, TimeSeriesParameters | dict[str, Any]] | None = None
    time_series_ref: str | None = None
    privacy_metrics: dict[str, PrivacyMetricsParameters | dict[str, Any]] | None = None
    signal_metrics: dict[str, SignalMetricsParameters | dict[str, Any]] | None = None
    results: Results | None = None
    seed: int | None = None


@dataclass(frozen=True)
class Parameters:
    kind: ModelKind
    metadata: Metadata
    spec: ParametersSpec


def get_avatarization_parameters(
    metadata: Metadata,
    avatarization: dict[str, AvatarizationParameters | dict[str, Any]],
    schema_name: str,
    time_series: dict[str, TimeSeriesParameters | dict[str, Any]] | None = None,
    seed: int | None = None,
    results=Results(volume="local-temp-results"),
) -> str:
    spec = ParametersSpec(
        seed=seed,
        schema=schema_name,
        avatarization=avatarization,
        time_series=time_series,
        results=results,
    )

    params = Parameters(
        kind=ModelKind.AVATARIZATION_PARAMETERS,
        metadata=metadata,
        spec=spec,
    )
    return to_yaml(params)


def get_privacy_metrics_parameters(
    metadata: Metadata,
    schema_name: str,
    privacy_metrics: dict[str, PrivacyMetricsParameters | dict[str, Any]] | None = None,
    time_series: dict[str, TimeSeriesParameters | dict[str, Any]] | None = None,
    seed: int | None = None,
    avatarization_ref: str | None = None,
    results: Results | None = None,
) -> str:
    spec = ParametersSpec(
        seed=seed,
        schema=schema_name,
        privacy_metrics=privacy_metrics,
        time_series=time_series,
        avatarization_ref=avatarization_ref,
        results=results,
    )

    params = Parameters(
        kind=ModelKind.PRIVACY_METRICS_PARAMETERS,
        metadata=metadata,
        spec=spec,
    )
    return to_yaml(params)


def get_signal_metrics_parameters(
    metadata: Metadata,
    schema_name: str,
    signal_metrics: dict[str, SignalMetricsParameters | dict[str, Any]] | None = None,
    seed: int | None = None,
    avatarization_ref: str | None = None,
    results: Results | None = None,
) -> str:
    spec = ParametersSpec(
        seed=seed,
        schema=schema_name,
        signal_metrics=signal_metrics,
        avatarization_ref=avatarization_ref,
        results=results,
    )

    params = Parameters(
        kind=ModelKind.SIGNAL_METRICS_PARAMETERS,
        metadata=metadata,
        spec=spec,
    )
    return to_yaml(params)
