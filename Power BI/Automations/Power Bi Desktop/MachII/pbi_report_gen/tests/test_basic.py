from pathlib import Path

from pbi_automation.config.paths import ProjectPaths
from pbi_automation.core.report import Report


def test_report_generation(tmp_path: Path):
    """
    This test checks whether a report definition folder is generated successfully.

    NOTE:
    - It expects your base_articrafts template folder to exist inside the repo root.
    - If base_articrafts is missing, this test will fail.
    """

    # Change this path if your repo structure differs
    base_articrafts = Path("base_articrafts")

    assert base_articrafts.exists(), "base_articrafts folder not found in repo root"
    assert base_articrafts.is_dir(), "base_articrafts exists but is not a folder"

    output_definition = tmp_path / "NewReport.Report" / "definition"

    paths = ProjectPaths(
        base_artifacts=base_articrafts,
        output_definition=output_definition,
    )

    report = Report(name="TestReport", paths=paths, width=1280, height=720)
    report.add_page("Homepage", is_home=True)
    report.save_report()

    # Validate basic output files
    assert (output_definition / "version.json").exists()
    assert (output_definition / "report.json").exists()
    assert (output_definition / "pages" / "pages.json").exists()
    assert (output_definition / "pages" / "Homepage" / "page.json").exists()
