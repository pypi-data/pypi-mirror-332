# IFC2IDA

[![PyPI Version](https://img.shields.io/pypi/v/ifc2ida.svg)](https://pypi.org/project/ifc2ida/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python package for converting **IFC (Industry Foundation Classes)** files to **IDA (Indoor Database ASCII)** compatible formats, designed for BIM (Building Information Modeling) data analysis workflows.

## Features

- **IFC Parsing**: Extract geometric and semantic data from IFC files using `ifcopenshell`.
- **Data Transformation**: Convert IFC entities into structured formats (e.g., CSV, JSON, Parquet) for analysis.
- **Customizable Pipelines**: Define rules to map IFC properties to IDA-compatible schemas.
- **CLI Support**: Command-line interface for batch processing.

## Installation

```bash
pip install ifc2ida
```

For development dependencies:
```bash
pip install ifc2ida[dev]
```

## Usage

### Basic Conversion

```python
from ifc2ida import convert

# Convert IFC to CSV
convert.ifc_to_csv("input.ifc", "output.csv")

# Convert IFC to Parquet
convert.ifc_to_parquet("input.ifc", "output.parquet")
```

### Command Line Interface

```bash
ifc2ida --input model.ifc --output data.csv --format csv
```

### Custom Schema Mapping

Create a JSON configuration file (`schema_config.json`):
```json
{
  "Walls": {
    "attributes": ["Name", "Volume", "Material"],
    "filters": {"ClassName": "IfcWall"}
  }
}
```

Then run:
```python
from ifc2ida import CustomConverter

converter = CustomConverter("schema_config.json")
converter.convert("input.ifc", "output.parquet")
```

## Documentation

Full documentation available at [GitHub Wiki](https://github.com/yourusername/ifc2ida/wiki).

## Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

## License

MIT License. See [LICENSE](LICENSE) for details.