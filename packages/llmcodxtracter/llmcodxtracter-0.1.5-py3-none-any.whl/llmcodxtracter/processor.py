from .validator import LLMOutputValidator
from .extractor import LLMCodeExtractor
from .exceptions import LLMOutputException
from collections import namedtuple
import yaml

CodeBlock = namedtuple("CodeBlock", ["filename", "extension", "code"])

# Mapping programming languages to standard file extensions
LANGUAGE_TO_EXTENSION = {
    "python": "py",
    "javascript": "js",
    "typescript": "ts",
    "java": "java",
    "c": "c",
    "cpp": "cpp",
    "cs": "cs",  # C#
    "go": "go",
    "rust": "rs",
    "swift": "swift",
    "ruby": "rb",
    "php": "php",
    "html": "html",
    "css": "css",
    "json": "json",
    "yaml": "yaml",
}

class LLMOutputProcessor:
    """Processor for validating, extracting, and formatting LLM-generated code output."""

    def __init__(self, validator: LLMOutputValidator, extractor: LLMCodeExtractor):
        self.validator = validator
        self.extractor = extractor

    def process(self, text: str, rules_path: str = None):
        """Validates, extracts, and applies formatting rules to LLM output."""
        match = self.validator.validate(text)
        code_block = self.extractor.extract(match)

        # Standardize extension based on language name
        standardized_extension = LANGUAGE_TO_EXTENSION.get(code_block.extension, code_block.extension)

        # Ensure filename and extension match
        filename = code_block.filename
        if not filename.endswith(f".{standardized_extension}"):
            filename = f"{filename.split('.')[0]}.{standardized_extension}"

        final_code = code_block.code
        if rules_path:
            final_code = self.apply_formatting_rules(final_code, rules_path)

        return CodeBlock(filename, standardized_extension, final_code)

    def apply_formatting_rules(self, code: str, rules_path: str) -> str:
        """Applies formatting rules defined in a YAML file to the code."""
        with open(rules_path, 'r') as file:
            rules = yaml.safe_load(file)

        # Example rule handling logic (simple placeholders)
        for rule in rules.get('formatting_rules', []):
            if rule.get('action') == 'replace':
                code = code.replace(rule['find'], rule['replace'])
            elif rule.get('action') == 'prepend':
                code = rule['content'] + "\n" + code
            elif rule.get('action') == 'append':
                code += "\n" + rule['content']

        return code

# Instantiate components
validator = LLMOutputValidator()
extractor = LLMCodeExtractor()
processor = LLMOutputProcessor(validator, extractor)
