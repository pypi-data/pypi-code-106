import sys
import subprocess
import random
import tempfile
from a7d import Archive
from pathlib import Path

def test_using_tester_dir(tester_dir, context=None):
    if not isinstance(tester_dir, Archive):
        tester_dir = Archive(tester_dir)
    with tempfile.TemporaryDirectory() as test_dir:
        test_dir = Path(test_dir)
        if context is not None:
            context.to_directory(test_dir)
        tester_dir.to_directory(test_dir)
        result = subprocess.run(test_dir/'test', cwd=test_dir).returncode
    return result

def check_all_tests(tests_dir, context=None, log=lambda x: print(x)):
    tests = [(Archive(p), p.name) for p in Path(tests_dir).iterdir()]
    results = [0, 0]
    if context is not None and not isinstance(context, Archive):
        context = Archive(context)
    for i, (test, name) in enumerate(tests):
        n = i + 1
        log(f'[{n}/{len(tests)}] {name}')
        result = test_using_tester_dir(test, context)
        results[result != 0] += 1
        result = 'ok' if result == 0 else f'FAIL({result})'
        log(f'[{n}/{len(tests)}] -> {result}')
    return tuple(results)

def main():
    tests = sys.argv[1] if len(sys.argv) > 1 else 'tests'
    ok, fails = check_all_tests(tests, '.')
    print(f'ok: {ok}')
    print(f'fails: {fails}')
    print(f'{100*ok/(fails + ok):0.4}% passed')

if __name__ == '__main__':
    main()
