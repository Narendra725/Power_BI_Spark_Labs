# Power BI Utilities

A comprehensive Python package for Power BI automation, schema generation, validation, and report manipulation.

## Features

- **Schema Generation**: Download and generate sample data from Power BI JSON schemas
- **Validation**: Validate Power BI report structures and catch common issues
- **Transformation**: Modify and transform report data programmatically
- **CLI Tools**: Command-line utilities for common operations

## Installation

### From source
```bash
cd powerbi_utils
pip install -e .
```

### With development dependencies
```bash
pip install -e ".[dev]"
```

## Usage

### As a Python package

```python
from powerbi_utils import SchemaGenerator, ReportValidator, ReportTransformer

# Generate sample data
generator = SchemaGenerator()
sample_data = generator.generate_sample_data()

# Validate a report
validator = ReportValidator()
errors = validator.validate_report_file("path/to/report.json")

# Transform report data
transformer = ReportTransformer()
renamed = transformer.rename_report(report_data, "New Report Name")
```

### Command Line

```bash
# Generate sample report
pb-schema-gen generate --output sample_report.json

# Validate a report
pb-schema-gen validate report.json

# Transform a report
pb-schema-gen transform input.json output.json --operation rename --name "New Name"
```

## Package Structure

```
powerbi_utils/
├── __init__.py          # Package initialization and exports
├── schema.py            # SchemaGenerator class for downloading/generating schemas
├── validators.py        # ReportValidator class for validation
├── transformers.py      # ReportTransformer class for data manipulation
└── cli.py              # Command-line interface
```

## Development

### Adding new functionality

1. **Create a new module**: Add your class/function to an appropriate module or create a new one
2. **Update __init__.py**: Export your new functionality
3. **Add CLI commands**: Extend the CLI in `cli.py` if needed
4. **Write tests**: Add tests in the `tests/` directory
5. **Update documentation**: Keep README and docstrings current

### Example: Adding a new transformer

```python
# In transformers.py
class ReportTransformer:
    def new_transformation(self, report_data: dict, param: str) -> dict:
        """Transform report data in some way."""
        # Your implementation here
        return transformed_data

# In __init__.py
from .transformers import ReportTransformer

# In cli.py
# Add new subcommand and handler
```

## Testing

```bash
pytest tests/
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

MIT License - see LICENSE file for details.