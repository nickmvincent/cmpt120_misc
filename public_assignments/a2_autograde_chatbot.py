"""
Autograder for Character Chatbots (Single or All, Item-Count Scoring)
---------------------------------------------------------------------
Default:
    python autograde_chatbot.py
        -> runs checks on chatbot.py

Special:
    python autograde_chatbot.py --all
        -> runs checks on all chatbot*.py files in this directory
"""

import ast
import io
import os
import re
import runpy
import sys
import textwrap
import traceback
from pathlib import Path
from contextlib import redirect_stdout
from unittest import mock

# -------------------------
# Utility & scoring helpers
# -------------------------

class CheckResult:
    def __init__(self, name, passed, message=""):
        self.name = name
        self.passed = passed
        self.message = message

def green(text): return f"\033[92m{text}\033[0m"
def red(text): return f"\033[91m{text}\033[0m"
def yellow(text): return f"\033[93m{text}\033[0m"

def print_check(result: CheckResult):
    mark = green("✅") if result.passed else red("❌")
    if result.passed:
        print(f"{mark} {result.name}")
    else:
        print(f"{mark} {result.name} — {result.message}")

def safe_read(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return None

def count_elif_chain(if_node: ast.If) -> int:
    """Return how many `elif` occur in a chain starting at this If node."""
    count = 0
    node = if_node
    while node.orelse and len(node.orelse) == 1 and isinstance(node.orelse[0], ast.If):
        count += 1
        node = node.orelse[0]
    return count

def parse_tree(src: str):
    if not src:
        return None, "Could not read file."
    try:
        return ast.parse(src), None
    except SyntaxError as e:
        return None, f"SyntaxError: {e}"

# -------------------------
# Core checks (filename-param)
# -------------------------

def check_file_exists(filename):
    exists = os.path.exists(filename)
    return CheckResult(
        f"File named {filename} exists",
        exists,
        f"Create {filename} (exact name, no spaces)."
    )

def check_header_comment(filename: str):
    """
    Expect a header comment with Program/Title, Name, Date near the top.
    """
    src = safe_read(filename)
    if not src:
        return CheckResult("Header includes title, name, date", False, "Could not read the file.")
    first_40_lines = "\n".join(src.splitlines()[:40])
    has_title = re.search(r"(program|title)\s*:", first_40_lines, re.I) or \
                re.search(r"#\s*.*", first_40_lines)  # any comment line
    has_name = re.search(r"(name)\s*:", first_40_lines, re.I)
    has_date = re.search(r"(date)\s*:", first_40_lines, re.I)

    passed = all([has_title, has_name, has_date])
    msg = "Include header comments with Program/Title, Name, and Date near the top."
    return CheckResult("Header includes title, name, date", passed, msg)

def check_line_length(filename: str, limit=100):
    src = safe_read(filename)
    if not src:
        return CheckResult(f"Line length ≤ {limit} chars", False, "Could not read the file.")
    long_lines = [i+1 for i, line in enumerate(src.splitlines()) if len(line) > limit]
    if long_lines:
        return CheckResult(
            f"Line length ≤ {limit} chars",
            False,
            f"Lines over {limit} chars: {long_lines[:5]}{'...' if len(long_lines)>5 else ''}"
        )
    return CheckResult(f"Line length ≤ {limit} chars", True)

def check_ast_structures(filename: str):
    """
    - Has standalone if
    - Has if/else
    - Has if/elif/else with at least two elifs (anywhere)
    - Has an `or` in a condition (ast.BoolOp Or)
    """
    src = safe_read(filename)
    if not src:
        return CheckResult("Uses required if/elif/else patterns and `or`", False, "Could not read the file.")

    tree, err = parse_tree(src)
    if err:
        return CheckResult("Python parses successfully", False, err)

    has_if = False
    has_if_else = False
    has_if_elif_else_with_two_elifs = False
    has_or_condition = False

    for node in ast.walk(tree):
        if isinstance(node, ast.If):
            has_if = True or has_if

            if node.orelse:
                has_if_else = True

            elif_count = count_elif_chain(node)
            end = node
            while end.orelse and len(end.orelse) == 1 and isinstance(end.orelse[0], ast.If):
                end = end.orelse[0]
            has_final_else = bool(end.orelse) and not isinstance(end.orelse[0], ast.If)

            if elif_count >= 2 and has_final_else:
                has_if_elif_else_with_two_elifs = True

        if isinstance(node, ast.BoolOp) and isinstance(node.op, ast.Or):
            has_or_condition = True

    missing = []
    if not has_if: missing.append("a standalone if")
    if not has_if_else: missing.append("an if/else")
    if not has_if_elif_else_with_two_elifs: missing.append("an if/elif/else with ≥2 elifs")
    if not has_or_condition: missing.append("a condition using `or`")

    if missing:
        return CheckResult(
            "Uses required if/elif/else patterns and `or`",
            False,
            "Missing: " + ", ".join(missing)
        )
    return CheckResult("Uses required if/elif/else patterns and `or`", True)

def run_program_with_inputs(filename, inputs, pad_extra=20, pad_value=None):
    """
    Execute <filename> as __main__ with mocked input/print capture.
    Returns (stdout_text, error or None, input_calls_count)
    """
    buf = io.StringIO()
    error = None
    modname = Path(filename).stem  # filename without .py

    if "" not in sys.path:
        sys.path.insert(0, "")
    # Allow programs that request more than the provided number of inputs by
    # padding additional values (repeating the last provided or empty string).
    if inputs:
        filler = inputs[-1] if pad_value is None else pad_value
    else:
        filler = "" if pad_value is None else pad_value
    side_effect_values = list(inputs) + [filler] * max(0, int(pad_extra))

    with mock.patch("builtins.input", side_effect=side_effect_values) as mocked_input:
        with redirect_stdout(buf):
            try:
                runpy.run_module(modname, run_name="__main__")
            except SystemExit:
                pass
            except Exception:
                error = traceback.format_exc()

    return buf.getvalue(), error, mocked_input.call_count

def check_runtime_behavior(filename: str):
    """
    - Program runs without crashing (with provided inputs).
    - Asks at least 3 questions (approximate by count of '?').
    - Uses input in a response (echo detection).
    """
    sample_inputs = ["yes", "blue", "pizza", "goodbye"]

    out, err, input_calls = run_program_with_inputs(filename, sample_inputs)

    if err:
        msg = "Program crashed.\n" + textwrap.indent(err, "  ")
        return [
            CheckResult("Program executes without crashing", False, msg),
            CheckResult("Asks at least 3 questions", False, "Program did not complete execution."),
            CheckResult("Uses the user's input in a response", False, "Program did not complete execution."),
        ]

    qmarks = out.count("?")
    asks_three = qmarks >= 3 or input_calls >= 3
    used_input = any(val.lower() in out.lower() for val in ["yes", "blue", "pizza", "goodbye"])

    return [
        CheckResult("Program executes without crashing", True),
        CheckResult("Asks at least 3 questions", asks_three,
                    "Make sure you prompt the user 3+ times (use '?')."),
        CheckResult("Uses the user's input in a response", used_input,
                    "Include the user's answer in a printed line."),
    ]

# -------------------------
# Week 1–3 analysis helpers (with fixes)
# -------------------------

def _contains_input_call(node: ast.AST) -> bool:
    """True if any descendant is a Call to builtin input()."""
    for sub in ast.walk(node):
        if isinstance(sub, ast.Call) and isinstance(sub.func, ast.Name) and sub.func.id == "input":
            return True
    return False

def _is_booleanish(expr: ast.AST) -> bool:
    """True if expr is something that evaluates to a bool (Compare/BoolOp/Unary not)."""
    if isinstance(expr, ast.Compare): return True
    if isinstance(expr, ast.BoolOp): return True
    if isinstance(expr, ast.UnaryOp) and isinstance(expr.op, ast.Not): return True
    return False

def build_analysis(filename: str):
    src = safe_read(filename)
    if not src:
        return None, "Could not read the file."
    tree, err = parse_tree(src)
    if err:
        return None, err

    info = {
        "calls_input": [],
        "assigned_input_nodes": set(),
        "str_vars": set(),
        "list_of_strings_exists": False,
        "import_random": False,
        "importfrom_random_choice": False,
        "uses_random_choice": False,
        "uses_in_operator": False,
        "uses_string_method": False,
        "has_for_loop": False,
        "has_nested_if": False,
        "uses_boolop_and": False,
        "uses_boolop_or": False,
        "has_comparison": False,
        "prints_boolean_literal_or_expr": False,
        "prints_string_var": False,
        "concatenates_strings": False,
    }

    # Collect data
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            # string methods
            if isinstance(node.func, ast.Attribute) and node.func.attr in {"strip", "lower", "upper"}:
                info["uses_string_method"] = True
            # random.choice detection
            if isinstance(node.func, ast.Attribute) and node.func.attr == "choice":
                if isinstance(node.func.value, ast.Name) and node.func.value.id == "random":
                    info["uses_random_choice"] = True
            if isinstance(node.func, ast.Name) and node.func.id == "choice":
                info["uses_random_choice"] = True
            # print(Boolean or booleanish expr)
            if isinstance(node.func, ast.Name) and node.func.id == "print":
                for arg in node.args:
                    if (isinstance(arg, ast.Constant) and isinstance(arg.value, bool)) or _is_booleanish(arg):
                        info["prints_boolean_literal_or_expr"] = True
            # record input() calls
            if isinstance(node.func, ast.Name) and node.func.id == "input":
                info["calls_input"].append(node)

        elif isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name == "random":
                    info["import_random"] = True

        elif isinstance(node, ast.ImportFrom):
            if node.module == "random":
                for alias in node.names:
                    if alias.name in {"choice", "*"}:
                        info["importfrom_random_choice"] = True

        elif isinstance(node, ast.List):
            if node.elts and all(isinstance(e, ast.Constant) and isinstance(e.value, str) for e in node.elts):
                info["list_of_strings_exists"] = True

        elif isinstance(node, ast.For):
            info["has_for_loop"] = True

        elif isinstance(node, ast.If):
            if any(isinstance(sub, ast.If) for sub in node.body):
                info["has_nested_if"] = True

        elif isinstance(node, ast.BoolOp):
            if isinstance(node.op, ast.And):
                info["uses_boolop_and"] = True
            if isinstance(node.op, ast.Or):
                info["uses_boolop_or"] = True

        elif isinstance(node, ast.Compare):
            info["has_comparison"] = True
            if any(isinstance(op, (ast.In, ast.NotIn)) for op in node.ops):
                info["uses_in_operator"] = True

        elif isinstance(node, ast.Assign):
            # track string variable assignments
            if isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
                for t in node.targets:
                    if isinstance(t, ast.Name):
                        info["str_vars"].add(t.id)

    # Mark input() calls that are assigned even if wrapped: find input() inside Assign/AAnnAssign values
    for node in ast.walk(tree):
        if isinstance(node, (ast.Assign, ast.AnnAssign)) and getattr(node, "value", None) is not None:
            for sub in ast.walk(node.value):
                if isinstance(sub, ast.Call) and isinstance(sub.func, ast.Name) and sub.func.id == "input":
                    info["assigned_input_nodes"].add(sub)

    # Saved vs unsaved input usage
    total_input_calls = len(info["calls_input"])
    assigned_input_calls = sum(1 for c in info["calls_input"] if c in info["assigned_input_nodes"])
    unassigned_input_calls = total_input_calls - assigned_input_calls
    info["has_input_saved"] = assigned_input_calls >= 1
    info["has_input_unsaved"] = unassigned_input_calls >= 1

    # Detect "print a string variable" and "concatenate strings"
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "print":
            for arg in node.args:
                if isinstance(arg, ast.Name) and arg.id in info["str_vars"]:
                    info["prints_string_var"] = True
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
            left, right = node.left, node.right
            def is_stry(n):
                return (isinstance(n, ast.Constant) and isinstance(n.value, str)) or \
                       (isinstance(n, ast.Name) and n.id in info["str_vars"])
            if is_stry(left) or is_stry(right):
                info["concatenates_strings"] = True

    info["random_choice_ok"] = info["uses_random_choice"] and (info["import_random"] or info["importfrom_random_choice"])
    return info, None

# Week 1–3 checks (filename-param)

def check_comments_present(filename: str):
    src = safe_read(filename)
    if not src:
        return CheckResult("Comments / pseudocode present (Week 1–2)", False, "Could not read the file.")
    has_hash_comment = any(line.strip().startswith("#") and len(line.strip()) > 1 for line in src.splitlines())
    has_top_string = bool(re.search(r'^\s*("""|\'\'\')(?:.|\n)+?\1', src, re.M))
    ok = has_hash_comment or has_top_string
    return CheckResult("Comments / pseudocode present (Week 1–2)", ok, "Add at least one comment or pseudocode block.")

def check_input_both_ways(filename: str):
    info, err = build_analysis(filename)
    if err:
        return [CheckResult("Input saved to a variable (Week 2)", False, err),
                CheckResult("Input also used without saving (Week 2)", False, err)]
    return [
        CheckResult("Input saved to a variable (Week 2)", info["has_input_saved"],
                    "Do something like: answer = input('...')"),
        CheckResult("Input also used without saving (Week 2)", info["has_input_unsaved"],
                    "Also call input(...) directly (e.g., print(input('...'))) in a different place."),
    ]

def check_variables_and_strings(filename: str):
    info, err = build_analysis(filename)
    if err:
        msg = err
        return [
            CheckResult("Assign a string to a variable (Week 2)", False, msg),
            CheckResult("Print a string variable (Week 2)", False, msg),
            CheckResult("Concatenate strings (Week 2)", False, msg),
        ]
    return [
        CheckResult("Assign a string to a variable (Week 2)", len(info["str_vars"]) > 0,
                    "Example: greeting = 'Hello'"),
        CheckResult("Print a string variable (Week 2)", info["prints_string_var"],
                    "Example: print(greeting)"),
        CheckResult("Concatenate strings (Week 2)", info["concatenates_strings"],
                    "Use '+' with strings or string vars, e.g., greeting + ', world'"),
    ]

def check_lists_and_randomness(filename: str):
    info, err = build_analysis(filename)
    if err:
        return [
            CheckResult("Create a list of strings (Week 2)", False, err),
            CheckResult("Use random.choice() (with import) (Week 2)", False, err),
        ]
    return [
        CheckResult("Create a list of strings (Week 2)", info["list_of_strings_exists"],
                    "Example: foods = ['pizza','taco','salad']"),
        CheckResult("Use random.choice() (with import) (Week 2)", info["random_choice_ok"],
                    "Import random or from random import choice, then call random.choice(list) or choice(list)."),
    ]

def check_in_operator(filename: str):
    info, err = build_analysis(filename)
    if err:
        return CheckResult("Use 'in' on strings/lists (Week 3)", False, err)
    return CheckResult("Use 'in' on strings/lists (Week 3)", info["uses_in_operator"],
                       "Use 'in' or 'not in' in a condition.")

def check_string_methods(filename: str):
    info, err = build_analysis(filename)
    if err:
        return CheckResult("Use .strip() / .lower() / .upper() (Week 3)", False, err)
    return CheckResult("Use .strip() / .lower() / .upper() (Week 3)", info["uses_string_method"],
                       "Call one of these on a string, e.g., name.strip().lower().")

def check_for_loop(filename: str):
    info, err = build_analysis(filename)
    if err:
        return CheckResult("Use a for loop (Week 3)", False, err)
    return CheckResult("Use a for loop (Week 3)", info["has_for_loop"],
                       "Add a for loop over a list or range(...).")

def check_nested_conditionals(filename: str):
    info, err = build_analysis(filename)
    if err:
        return CheckResult("Nested conditionals (Week 3)", False, err)
    return CheckResult("Nested conditionals (Week 3)", info["has_nested_if"],
                       "Place an if-statement inside another if-statement's body.")

def check_boolean_logic_and_comparisons(filename: str):
    info, err = build_analysis(filename)
    if err:
        return [
            CheckResult("Use 'and' or 'or' (Week 2–3)", False, err),
            CheckResult("Use a comparison like '==' (Week 2–3)", False, err),
            CheckResult("Print a Boolean (literal or expression) (Week 2–3)", False, err),
        ]
    return [
        CheckResult("Use 'and' or 'or' (Week 2–3)", info["uses_boolop_and"] or info["uses_boolop_or"],
                    "Include boolean logic in a condition."),
        CheckResult("Use a comparison like '==' (Week 2–3)", info["has_comparison"],
                    "Compare values, e.g., color == 'blue'."),
        CheckResult("Print a Boolean (literal or expression) (Week 2–3)", info["prints_boolean_literal_or_expr"],
                    "Do: print(True) / print(False) or print(name == 'alex')."),
    ]

# -------------------------
# Scoring rubric (Item-count)
# -------------------------

def check_runtime_wrapper(filename):  # shim for consistent signature
    return check_runtime_behavior(filename)

RUBRIC = [
    # Core file/style/AST basics
    ("exists", lambda fn: check_file_exists(fn)),
    ("header", lambda fn: check_header_comment(fn)),
    ("linelen", lambda fn: check_line_length(fn)),
    ("ast", lambda fn: check_ast_structures(fn)),
    ("runtime", lambda fn: check_runtime_wrapper(fn)),  # returns list of 3 items

    # Week 1–3 additions
    ("comments", lambda fn: check_comments_present(fn)),
    ("input_both", lambda fn: check_input_both_ways(fn)),          # 2 items
    ("vars_strings", lambda fn: check_variables_and_strings(fn)),   # 3 items
    ("lists_random", lambda fn: check_lists_and_randomness(fn)),    # 2 items
    ("in_op", lambda fn: check_in_operator(fn)),
    ("str_methods", lambda fn: check_string_methods(fn)),
    ("for_loop", lambda fn: check_for_loop(fn)),
    ("nested_if", lambda fn: check_nested_conditionals(fn)),
    ("bool_logic_cmp_print", lambda fn: check_boolean_logic_and_comparisons(fn)),  # 3 items
]

# -------------------------
# Grading & driver (item-count scoring)
# -------------------------

def grade_file(filename):
    print("\n" + "="*66)
    print(f" Grading {filename}")
    print("="*66 + "\n")

    total_items, passed_items = 0, 0
    all_results = []

    for key, func in RUBRIC:
        results = func(filename)
        if isinstance(results, list):
            for res in results:
                total_items += 1
                print_check(res)
                if res.passed:
                    passed_items += 1
                all_results.append(res)
        else:
            res = results
            total_items += 1
            print_check(res)
            if res.passed:
                passed_items += 1
            all_results.append(res)

    print("\n" + "-"*66)
    score_line = f"Score: {passed_items}/{total_items} items"
    print(green(score_line) if passed_items == total_items else yellow(score_line))
    print("-"*66 + "\n")

    # Hints
    failed = [r for r in all_results if not r.passed and r.message]
    if failed:
        print("Hints:")
        for res in failed:
            print(" • " + res.message)
        print()

def main():
    args = sys.argv[1:]
    thisfile = Path(__file__).name

    if "--all" in args:
        files = sorted(
            f for f in os.listdir(".")
            if f.startswith("chatbot") and f.endswith(".py") and f != thisfile
        )
        if not files:
            print("No chatbot*.py files found.")
            return
    else:
        files = ["chatbot.py"]

    for f in files:
        grade_file(f)

if __name__ == "__main__":
    main()
