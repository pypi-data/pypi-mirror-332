import os

import tree_sitter_languages

from graph_construction.languages.base_parser import BaseParser
from graph_construction.utils.interfaces.GlobalGraphInfo import GlobalGraphInfo


class DartParser(BaseParser):
    def __init__(self, global_graph_info: GlobalGraphInfo):
        super().__init__("dart", "*", ".dart", ".", global_graph_info)

    @property
    def self_syntax(self):
        # In Dart, instance attributes are accessed with "this."
        return "this."

    @property
    def decompose_call_query(self):
        # This query attempts to break down member accesses and standalone expressions.
        # Adjust the query based on your Dart tree-sitter grammar details.
        return """
            (property_access
                object: (identifier) @_
                property: (identifier) @_
            )
            (expression_statement
                (identifier) @_
            )
            """

    @property
    def assignment_query(self):
        # Dart typically represents assignments with an assignment_expression node.
        return "(assignment_expression left: (identifier) @variable right: _ @expression)"

    @property
    def function_call_query(self):
        # In Dart, method calls are often captured as method_invocation nodes.
        return "(method_invocation function: (identifier) @function_call)"

    @property
    def inheritances_query(self):
        # This query captures both "extends" and "implements" clauses from a class declaration.
        return """
            (class_declaration
                (extends_clause
                    (type_identifier) @inheritance
                )
            )
            (class_declaration
                (implements_clause
                    (type_identifier) @inheritance
                )
            )
            """

    @property
    def scopes_names(self):
        # Dart functions can be declared as function_declaration or method_declaration.
        return {
            "function": ["function_declaration", "method_declaration"],
            "class": ["class_declaration"],
            "plain_code_block": [],
        }

    @property
    def relation_types_map(self):
        # Map node types to relationship types.
        return {
            "function_declaration": "FUNCTION_DEFINITION",
            "method_declaration": "FUNCTION_DEFINITION",
            "class_declaration": "CLASS_DEFINITION",
        }

    def _get_imports(self, path: str, file_node_id: str, root_path: str) -> dict:
        parser = tree_sitter_languages.get_parser(self.language)
        with open(path, "r") as file:
            code = file.read()
        tree = parser.parse(bytes(code, "utf-8"))

        # For Dart, we look for import directives.
        imports = {file_node_id: {}}
        for node in tree.root_node.children:
            if node.type == "import_directive":
                # Look for the string literal containing the import path.
                for child in node.children:
                    if child.type == "string_literal":
                        # Remove quotes from the string literal.
                        import_path = child.text.decode().strip("'\"")
                        imports[file_node_id][import_path] = {
                            "path": self.resolve_import_path(import_path, path, root_path),
                            "alias": "",  # Dart imports can use an alias with the "as" keyword.
                            "type": "import_directive",
                        }
        return imports

    def parse_file(self, file_path: str, root_path: str, global_graph_info: GlobalGraphInfo, level: int):
        # Dart does not have an equivalent to __init__.py.
        return self.parse(file_path, root_path, global_graph_info, level)

    def parse_init(self, file_path: str, root_path: str):
        # No special init parsing is needed for Dart.
        return {}
