"""Markdown code analyser module."""
from pathlib import Path
from pymarkdown.api import PyMarkdownApi, PyMarkdownApiException

from .code import Code
from ..report import Report


import logging
logging.getLogger('pymarkdown').setLevel(logging.CRITICAL)


class CodeMarkdown(Code):
    """Markdown code analyser class."""

    @classmethod
    def get_language(cls) -> str:
        """Returns language supported by the analyser."""
        return 'markdown'


    @classmethod
    def includes(cls, path: Path) -> list[str]:
        """Returns file and directory patterns to be included in the analysis.

        For a potential list of extensions see:
        https://superuser.com/questions/249436/

        Args:
            path (Path): Path of the code base.

        Returns:
            List of file and directory patterns.
        """
        return [
            '*.markdown',
            '*.md',
            '*.mdown',
            '*.mdtext',
            '*.mdtxt',
            '*.mdwn',
            '*.mkd',
        ]


    @classmethod
    def analyse_code(cls, content: str, report: Report, path: Path=None, disable_rules: list[str]=None) -> dict:
        """Analyses Markdown code.

        Args:
            content (str): Markdown code.
            report (Report): Analysis report.
            path (Path): Path of the file (optional).

        Returns:
            Dictionary of the analysis results.
        """
        markdown = PyMarkdownApi()
        for rule in disable_rules if disable_rules else []:
            markdown.disable_rule_by_identifier(rule.lower())

        try:
            result = markdown.scan_string(content)

        except Exception as err:
            report.add_warning(cls, str(err), path)
            return

        return {
            'scan_failures': result.scan_failures,
            'pragma_errors': result.pragma_errors,
        }


    @classmethod
    def output_result(cls, report: Report, result: dict) -> str:
        out = ''

        for item in result.get('scan_failures', []):
            out += "* {}{} (Line {}).\n".format(
                item.rule_description,
                (" " + item.extra_error_information)
                if item.extra_error_information
                else
                '',
                item.line_number
            )

        for item in result.get('pragma_errors', []):
            out += "* {} (Line {}".format(
                item.pragma_error,
                item.line_number
            )

        return out


    @classmethod
    def output(cls, report: Report, results: dict) -> str:
        """Generates output from the analysis report and results.

        Args:
            report (Report): Analysis report.
            results (dict): Analysis results.

        Returns:
            Analysis output.
        """
        out = ''

        for path, result in results.items():

            if not result:
                continue

            part = cls.output_result(report, result)

            if part:
                out += report.output_heading(str(path.relative_to(report.path)), 3)
                out += part + "\n"

        if out:
            out = report.output_heading("Markdown Files", 2) + out + "\n"

        return out
