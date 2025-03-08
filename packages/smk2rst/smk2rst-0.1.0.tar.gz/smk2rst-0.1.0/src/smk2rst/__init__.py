try:
    from importlib.metadata import version as get_version

    version = get_version(__name__)
except ImportError:
    from pkg_resources import get_distribution

    version = get_distribution(__name__).version

import re
import os
import fnmatch
from rstcloth import RstCloth
from pathlib import Path


def list_snakemake_files(path, patterns):
    files = []
    for dirpath, dirnames, filenames in os.walk(path):

        if not filenames:
            continue
        matching_files = sum(
            [fnmatch.filter(filenames, pattern) for pattern in patterns], []
        )
        if matching_files:
            for file in matching_files:
                files.append(Path(f"{dirpath}/{file}"))

    return files


def codebase_parser(path, patterns=["*.smk", "Snakefile"]):

    files = list_snakemake_files(path, patterns)
    source_files = []
    for fin in files:

        fout = infer_output_name(fin)
        source_file = SourceFile(fin, fout)

        print(f"{fin}\n\t-> {fout}")

        if fin == fout:
            raise Exception(
                "Output file is the same than input file ! Should not happen"
            )

        source_files.append(source_file)
        source_file.to_rst()
    return source_files


def infer_output_name(input_name: Path):
    if input_name.suffix == ".smk":
        output_name = input_name.with_suffix(".rst")
        return output_name

    elif input_name.name == "Snakefile":
        output_name = input_name.parent / input_name.parent.name
        output_name = output_name.with_suffix(".rst")
        return output_name


def check_has_title(text):
    pattern = re.compile(r"(?:^|\n)([^\n\r]+)\r?\n(=+)(?:\r?\n|$)", re.MULTILINE)
    match = pattern.search(text)
    if match:
        return len(match.group(1).strip()) == len(match.group(2).strip())

    return False


class SourceFile:
    HEADER_PATTERN = re.compile(r'^"""(\n|.)*?^"""', re.MULTILINE)

    def __init__(self, source_path, rst_path=None):
        self.path = source_path
        with open(self.path, "r") as inputfile:
            self.text = inputfile.read()
        self.rst = rst_path
        self.parse()

    def parse(self):
        self.get_header_from_docstring()
        self.find_code_content()
        self.find_includes()

    def get_header_from_docstring(self):
        r = self.HEADER_PATTERN.search(self.text)
        if r is None:
            self.header = None
        else:
            self.header = self.text[r.start() + 3 : r.end() - 3]

    def find_code_content(self):
        splitter = re.compile("^[a-zA-Z].*$", re.MULTILINE)
        objects = []

        boundaries = [r.start() for r in splitter.finditer(self.text)]
        boundaries.append(len(self.text))
        for i in range(len(boundaries) - 1):
            objects.append(self.text[boundaries[i] : boundaries[i + 1]].strip())

        check_rule = re.compile(
            r"(?P<function>(rule|checkpoint)\s+(?P<name>\w+):)", re.MULTILINE
        )
        check_rule_overloaded = re.compile(
            r"use (?P<function>(rule|checkpoint))\s+(?P<parent_name>\w+)\s+as\s+(?P<name>\w+)\s+with",
            re.MULTILINE,
        )
        check_function = re.compile(
            r"^def\s+((?P<name>\w+)\((?P<args>.*)\)):", re.MULTILINE
        )

        self.rules = []
        self.functions = []
        for obj, line_nb in zip(objects, boundaries[:-1]):
            rule_match = check_rule.match(obj)
            rule_overloaded_match = check_rule_overloaded.match(obj)
            func_match = check_function.match(obj)
            if rule_match:
                rule = Rule(rule_match.group("name"), obj, line_nb)
                self.rules.append(rule)
            elif rule_overloaded_match:
                rule = RuleOverloaded(
                    rule_overloaded_match.group("name"),
                    rule_overloaded_match.group("parent_name"),
                    obj,
                    line_nb,
                )
                self.rules.append(rule)
            elif func_match:
                func = Function(func_match.group("name"), obj, line_nb)
                self.functions.append(func)

    def find_includes(self):
        self.includes = []
        pattern = re.compile(r'^include\s*:\s*"(?P<file>.*)"', re.MULTILINE)
        for r in pattern.finditer(self.text):
            self.includes.append(Path(r.group("file")))

    def to_rst(self, rst_path=None):
        if self.rst is None and rst_path is None:
            raise Exception("rst_path should be provided at least once")

        if rst_path:
            self.rst = rst_path

        with open(self.rst, "w") as fout:
            doc = RstCloth(fout)
            doc.directive("toctree", fields=[("hidden", "")])  # ("maxdepth","3"),

            doc.newline()
            readme = self.rst.parent / "README.rst"

            # Check for title
            has_title = False
            if readme.exists() and self.path.name == "Snakefile":
                with open(readme, "r") as freadme:
                    has_title = check_has_title(freadme.read())
            if self.header:
                has_title = check_has_title(self.header)

            # If no title, add one based on file name
            if not has_title:
                doc.h1(self.rst.with_suffix("").name.replace("_", " ").title())

            # If Snakefile, import README in the same dir per default
            if readme.exists() and self.path.name == "Snakefile":
                doc.directive("include", arg=str(readme.name))
                doc.newline()

            if self.header:  # Import docstring from current file
                fout.write(self.header)
                doc.newline()

            if self.includes:  # If includes, propagate toc
                content = [
                    str(infer_output_name(p))
                    for p in self.includes
                    if not p.parts[0].startswith("..")
                ]
                doc.directive(
                    "toctree",
                    fields=[("maxdepth", "1"), ("caption", "Section content")],
                    content=content,
                )
                doc.newline()

            if self.rules:  # Add rules
                doc.h2("Rules")
                for rule in self.rules:
                    rule.to_rst(fout)

            if self.functions:  # Add rules
                doc.h2("Functions")
                for function in self.functions:
                    function.to_rst(fout)

    def __str__(self):
        return f"<SourceFile> {self.path}"


class Rule:
    INFO_PARSER = re.compile(
        r'(?P<type>rule|checkpoint)\s+(?P<name>\w+).\n\s*(?P<docstring>"""(\n|.)*?""")',
        re.MULTILINE,
    )

    def __init__(self, name, text, line_nb=0):
        self.name = name
        self.text = text
        self.line_nb = 0
        self.docstring = None

        r = self.INFO_PARSER.match(text)
        if r is not None:
            self.docstring = r.group("docstring")[3:-3]

    def to_rst(self, fout: Path):
        doc = RstCloth(fout)

        fout.write(f".. _{self.name}:\n\n")
        doc.h3(self.name)
        doc.newline()

        if self.docstring:
            fout.write(self.docstring)
            doc.newline()

        doc.codeblock(self.code, language="python")
        doc.newline()

    @property
    def code(self):
        if self.docstring is None:
            return self.text
        else:
            return self.text.replace(self.docstring, "[...]")

    def __str__(self):
        return f"<Rule> {self.name}"


class RuleOverloaded(Rule):
    def __init__(self, name, parent_name, text, line_nb=0):
        super().__init__(name, text, line_nb=line_nb)
        self.parent = parent_name
        self.docstring = f"Redefinition of :ref:`{self.parent}`\n"

    def __str__(self):
        return f"<RuleOverloaded> {self.name} from {self.parent}"


class Function(Rule):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)

    def __str__(self):
        return f"<Function> {self.name}"


def print_stats(source_files, show_details=False, basepath=Path("./")):

    stats = {"source_file": [], "path": [], "rules": [], "functions": []}

    for source_file in source_files:
        stats["source_file"].append(source_file)
        stats["path"].append(source_file.path.relative_to(basepath))
        stats["rules"].append(len(source_file.rules))
        stats["functions"].append(len(source_file.functions))

    def row_formater(path, rules, functions):
        if len(path) > 60:
            path = f"..{path[-58:]}"
        return f"| {path:60s} | {rules if rules != 0 else '':12} | {functions if functions != 0 else '':12} |"

    def separator_formater(line):
        sep = []
        for c in line:
            if c == "|":
                sep.append("+")
            else:
                sep.append("-")

        return "".join(sep)

    labels = row_formater("Path", "# rules", "# functions")
    print(labels)
    print(separator_formater(labels))
    if show_details:
        for i in range(len(stats["source_file"])):
            print(
                row_formater(
                    str(stats["path"][i]), stats["rules"][i], stats["functions"][i]
                )
            )
        print(separator_formater(labels))
    print(row_formater("Total", sum(stats["rules"]), sum(stats["functions"])))
