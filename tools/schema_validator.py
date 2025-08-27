import json
import jsonschema
import sys


def validate(schema_path: str, data_path: str) -> None:
    with open(schema_path) as sf, open(data_path) as df:
        schema = json.load(sf)
        data = json.load(df)
    jsonschema.validate(instance=data, schema=schema)
    print("Valid")


if __name__ == "__main__":
    validate(sys.argv[1], sys.argv[2]) 