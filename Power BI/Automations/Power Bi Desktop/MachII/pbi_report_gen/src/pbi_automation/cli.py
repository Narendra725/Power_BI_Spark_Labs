# src/pbi_automation/cli.py

import argparse
from pathlib import Path

from pbi_automation.config.paths import ProjectPaths
from pbi_automation.core.report import Report


def build_report(base_artifacts: Path, output_definition: Path, report_name: str, width: int, height: int):
    paths = ProjectPaths(
        base_artifacts=base_artifacts,
        output_definition=output_definition,
    )

    report = Report(name=report_name, paths=paths, width=width, height=height)

    # Default starter page
    report.add_page("Homepage", is_home=True)

    report.save_report()
    return report


def main():
    parser = argparse.ArgumentParser(
        prog="pbi_automation",
        description="Generate Power BI report definition folders using base JSON artifacts.",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    build_parser = subparsers.add_parser("build", help="Build a new report definition output")
    build_parser.add_argument(
        "--base",
        required=True,
        type=str,
        help="Path to base_artifacts folder (template JSONs)",
    )
    build_parser.add_argument(
        "--out",
        required=True,
        type=str,
        help="Output folder for report definition (example: output/NewReport.Report/definition)",
    )
    build_parser.add_argument(
        "--name",
        default="DemoReport",
        type=str,
        help="Report name (default: DemoReport)",
    )
    build_parser.add_argument(
        "--width",
        default=1280,
        type=int,
        help="Report page width (default: 1280)",
    )
    build_parser.add_argument(
        "--height",
        default=720,
        type=int,
        help="Report page height (default: 720)",
    )

    args = parser.parse_args()

    if args.command == "build":
        build_report(
            base_artifacts=Path(args.base),
            output_definition=Path(args.out),
            report_name=args.name,
            width=args.width,
            height=args.height,
        )
        print(f"Report generated successfully at: {args.out}")


if __name__ == "__main__":
    main()
