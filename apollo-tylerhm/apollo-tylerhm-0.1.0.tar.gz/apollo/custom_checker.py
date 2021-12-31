import subprocess
from .verdict import Response, Correct, WrongAnswer

# Checker path, file paths to standard checker input
def check(checker: str, judge_input, user_output, judge_output):
    command_args = [checker, judge_input, user_output, judge_output]
    if (checker.split('.').pop() == 'py'):
        command_args.insert(0, 'python3')
        
    verdict = subprocess.run(command_args, capture_output=True)

    err = verdict.stderr.decode('utf-8')
    out = verdict.stdout.decode('utf-8')

    if (err != ''):
        return Response(WrongAnswer, f"Checker output: {err}");

    if (out != ''):
        return Response(WrongAnswer, f"Checker output: {out}");

    return Response(Correct)
