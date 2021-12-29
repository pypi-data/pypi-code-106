import sys
import shutil
import subprocess
import random
from a7d import Archive
from pathlib import Path

def test_using_tester_dir(tester_dir):
    if not isinstance(tester_dir, Archive):
        tester_dir = Archive(tester_dir)
    test_dir = Path('test-' + str(random.randint(10**58, 10**59 - 1)))
    tester_dir.to_directory(test_dir)
    result = subprocess.run(test_dir/'test').returncode
    shutil.rmtree(test_dir)
    return result

def check_all_tests(tests_dir, log=lambda x: print(x)):
    tests = [(Archive(p), p.name) for p in Path(tests_dir).iterdir()]
    results = [0, 0]
    for i, (test, name) in enumerate(tests):
        n = i + 1
        log(f'[{n}/{len(tests)}] {name}')
        result = test_using_tester_dir(test)
        results[result != 0] += 1
        result = 'ok' if result == 0 else f'FAIL({result})'
        log(f'[{n}/{len(tests)}] -> {result}')
    return tuple(results)

def main():
    ok, fails = check_all_tests(sys.argv[1] if len(sys.argv) > 1 else 'tests')
    print(f'ok: {ok}')
    print(f'fails: {fails}')
    print(f'{100*ok/(fails + ok):0.4}% passed')

if __name__ == '__main__':
    main()
