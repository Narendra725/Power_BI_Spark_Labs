"""
Tests for Power BI utilities package.
"""

import pytest
from pathlib import Path
import json
import tempfile

from powerbi_utils import SchemaGenerator, ReportValidator, ReportTransformer


class TestSchemaGenerator:
    """Test schema generation functionality."""

    def test_initialization(self):
        """Test SchemaGenerator initialization."""
        generator = SchemaGenerator()
        assert generator.cache_dir.name == "schemas_cache"
        assert generator.cache_dir.exists()

    def test_smart_string_values(self):
        """Test smart string value generation."""
        generator = SchemaGenerator()

        # Test name field
        assert generator._smart_string_value({}, "reportName") == "Sample Name"

        # Test URL field
        assert generator._smart_string_value({}, "apiUrl") == "https://example.com"

        # Test ID field
        assert generator._smart_string_value({}, "userId") == "sample-id-123"

    def test_smart_numeric_values(self):
        """Test smart numeric value generation."""
        generator = SchemaGenerator()

        # Test width
        assert generator._smart_int_value("width") == 1280

        # Test height
        assert generator._smart_int_value("height") == 720

        # Test opacity
        assert generator._smart_number_value("opacity") == 1.0


class TestReportValidator:
    """Test report validation functionality."""

    def test_initialization(self):
        """Test ReportValidator initialization."""
        validator = ReportValidator()
        assert validator.schema_gen is not None

    def test_validate_valid_report(self):
        """Test validation of a valid report structure."""
        validator = ReportValidator()

        valid_report = {
            "$schema": "https://example.com/schema.json",
            "themeCollection": {
                "baseTheme": {
                    "name": "Default Theme",
                    "reportVersionAtImport": {
                        "visual": "1.0",
                        "page": "1.0",
                        "report": "1.0"
                    }
                }
            }
        }

        errors = validator.validate_report_data(valid_report)
        assert len(errors) == 0

    def test_validate_invalid_report(self):
        """Test validation of an invalid report structure."""
        validator = ReportValidator()

        invalid_report = {
            "themeCollection": "not an object"
        }

        errors = validator.validate_report_data(invalid_report)
        assert len(errors) > 0


class TestReportTransformer:
    """Test report transformation functionality."""

    def test_initialization(self):
        """Test ReportTransformer initialization."""
        transformer = ReportTransformer()
        assert len(transformer._transformers) == 0

    def test_rename_report(self):
        """Test report renaming."""
        transformer = ReportTransformer()

        report = {
            "name": "Old Name",
            "displayName": "Old Display Name"
        }

        renamed = transformer.rename_report(report, "New Name")

        assert renamed["name"] == "New Name"
        assert renamed["displayName"] == "New Name"

    def test_add_metadata(self):
        """Test metadata addition."""
        transformer = ReportTransformer()

        report = {}
        metadata = {"author": "Test User", "version": "1.0"}

        with_metadata = transformer.add_metadata(report, metadata)

        assert with_metadata["metadata"]["author"] == "Test User"
        assert with_metadata["metadata"]["version"] == "1.0"

    def test_merge_reports(self):
        """Test report merging."""
        transformer = ReportTransformer()

        base = {"name": "Base", "config": {"width": 100}}
        overlay = {"config": {"height": 200}, "newField": "value"}

        merged = transformer.merge_reports(base, overlay)

        assert merged["name"] == "Base"
        assert merged["config"]["width"] == 100
        assert merged["config"]["height"] == 200
        assert merged["newField"] == "value"


class TestIntegration:
    """Integration tests for the package."""

    def test_full_workflow(self):
        """Test a complete workflow from generation to validation."""
        # Generate sample data
        generator = SchemaGenerator()
        sample_data = generator.generate_sample_data()

        # Validate the generated data
        validator = ReportValidator()
        errors = validator.validate_report_data(sample_data)

        # Should have no critical errors (may have some warnings)
        critical_errors = [e for e in errors if "Missing required field" in e.message]
        assert len(critical_errors) == 0

        # Transform the data
        transformer = ReportTransformer()
        transformed = transformer.add_metadata(sample_data, {"generated": True})

        assert transformed["metadata"]["generated"] is True