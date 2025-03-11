import click
import subprocess
import glob
import os

from pathlib import Path

from .platforms.platform_manager import PlatformManager
from .problem_info import TestCase, ParsedProblem
from .server import TimedHTTPServer, ProblemHandler

PORT = 10043

GREEN = '\033[0;32m'
RED = '\033[0;31m'
NC = '\033[0m'

def create_test_cases(tests: list[TestCase], problem_id: str, problem_path: Path):
    in_path = problem_path / 'in'
    out_path = problem_path / 'out'
    in_path.mkdir(parents=True, exist_ok=True)
    out_path.mkdir(parents=True, exist_ok=True)

    for i, test in enumerate(tests):
        (in_path / f'{problem_id}{i+1}').write_text(test.input)
        (out_path / f'{problem_id}{i+1}').write_text(test.output)

def create_solution_template(problem: ParsedProblem, template_code: str):
    solution_path = problem.problem_info.get_solution_path()
    if not solution_path.exists():
        solution_path.write_text(template_code)

def create_makefile(problem: ParsedProblem, makefile_code: str):
    makefile_path = problem.problem_info.folder_path / 'makefile'
    makefile_path.write_text(makefile_code)

@click.command()
@click.pass_context
def solve(ctx: click.Context) -> None:
    server = TimedHTTPServer(('localhost', PORT), ProblemHandler)
    config = ctx.obj.get('config')
    if config.get('base_path') is None:
        click.echo("Configuration not found! Run `comp setup` to create one.")
        return

    platform_manager = PlatformManager(ctx.obj['config'].get('base_path'))
    print(f"Waiting for problems on port {PORT}")

    template_path = ctx.obj['config'].get('template_path')
    template_code = Path(template_path).read_text() if template_path is not None else ''

    makefile_path = ctx.obj['config'].get('makefile_path')
    makefile_code = Path(makefile_path).read_text() if makefile_path is not None else None

    code_folder = None
    try:
        batch = server.serve_with_timeout()
        for parsed_problem in batch:
            platform_manager.fill_problem_info(parsed_problem)
            parsed_problem.problem_info.folder_path.mkdir(parents=True, exist_ok=True)
            code_folder = str(parsed_problem.problem_info.folder_path)
            create_solution_template(parsed_problem, template_code)

            if makefile_code is not None:
                create_makefile(parsed_problem, makefile_code)

            if parsed_problem.tests:
                create_test_cases(parsed_problem.tests,
                                  parsed_problem.problem_info.file_name,
                                  parsed_problem.problem_info.folder_path)

        if code_folder is not None:
            print(f"\nOpening VS Code in directory: {code_folder}")
            subprocess.Popen([
                'code',
                code_folder,
            ])
        else:
            print("\nNo contest directory created.")
    except KeyboardInterrupt:
        print("\nShutting down...")
    finally:
        server.server_close()


@click.command()
def test():
    current_dir = os.getcwd()
    cpp_files = glob.glob('*.cpp', root_dir=current_dir)
    if not cpp_files:
        click.echo("Error: No .cpp files found in current directory")
        return 1

    latest_cpp = Path(sorted(cpp_files, key=os.path.getmtime, reverse=True)[0]).stem

    make_process = subprocess.run(['make', '-s', latest_cpp],
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.STDOUT,
                                  text=True,
                                  cwd=current_dir)

    test_input = glob.glob(f"in/{latest_cpp}[0-9]*", root_dir=current_dir)
    test_output = glob.glob(f"out/{latest_cpp}[0-9]*", root_dir=current_dir)

    for i in range(len(test_input)):
        with open(test_input[i], 'r') as infile:
            result = subprocess.run(f'./{latest_cpp}', stdin=infile,
                                    capture_output=True,
                                    text=True,
                                    cwd=current_dir)

        actual_output = result.stdout
        actual_lines = actual_output.strip().split('\n')

        with open(test_output[i], 'r') as f:
            expected_content = f.read().strip()
            expected_lines = expected_content.split('\n')

        while expected_lines and not expected_lines[-1]:
            expected_lines.pop()
        while actual_lines and not actual_lines[-1]:
            actual_lines.pop()

        if expected_lines == actual_lines:
            click.echo(f"{GREEN}Test {i+1}: PASSED{NC}")
        else:
            click.echo(f"{RED}Test {i+1}: FAILED{NC}")
            click.echo("Expected:")
            click.echo(expected_content)
            click.echo("Got:")
            click.echo(actual_output)

    return make_process.returncode