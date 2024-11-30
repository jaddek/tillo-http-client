from dataclasses import asdict


def filter_none_values(instance):
    return {k: v for k, v in asdict(instance).items() if v is not None}


def transform_to_dict(instance) -> dict:
    return asdict(instance)

