import argparse
import ast
import sys
from pathlib import Path

from aporiapy.compilers.compiler_01_sc import CompilerSc
from aporiapy.compilers.compiler_02_flat import CompilerFlat
from aporiapy.compilers.compiler_03_cfi import CompilerCfi

compilers = [CompilerSc(), CompilerFlat(), CompilerCfi()]


def compile_source(input_path):
    with open(input_path, "r") as file:
        original_source = file.read()
    program_ast = ast.parse(original_source)
    for compiler in compilers:
        program_ast = compiler.compile(program_ast)
        if isinstance(program_ast, ast.Module):
            ast.fix_missing_locations(program_ast)
    return program_ast


def cli():
    parser = argparse.ArgumentParser(description="Compiles Python code to Aporia code")

    parser.add_argument(
        "input_file", type=str, help="Path to the input Python file to compile."
    )

    parser.add_argument(
        "-o", "--output", type=str, help="Path to the output file to write the compiled code."
    )

    parser.add_argument(
        "--stdout", action="store_true", help="Output the compiled code to stdout instead of a file."
    )

    parser.add_argument(
        "--ast", action="store_true", help="Print the ast of the compiled code."
    )

    args = parser.parse_args()

    input_path = Path(args.input_file)

    if not input_path.exists():
        sys.stderr.write(f"Error: Input file '{input_path}' does not exist.\n")
        sys.exit(1)

    compiled_ast = compile_source(input_path)
    compiled_source = str(compiled_ast)


    if args.ast:
        print(f"{"*" * 8} AST BEGIN {"*" * 8}")
        print(compiled_ast.pretty())
        print(f"{"*" * 8} AST END {"*" * 8}")
    if args.stdout:
        print(compiled_source)
    else:
        output_path = Path(args.output) if args.output else input_path.with_suffix(".spp")
        with open(output_path, "w") as output_file:
            output_file.write(compiled_source)
        print(f"Compiled file written to: {output_path}")

if __name__ == "__main__":
    cli()


