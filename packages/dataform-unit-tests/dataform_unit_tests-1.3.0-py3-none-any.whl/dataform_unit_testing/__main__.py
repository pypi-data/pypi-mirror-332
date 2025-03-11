"""
Copyright 2025 Neeraj Morar

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import os
import sys

from . import unit_test_runner

COMPILATION_RESULT = os.getenv("COMPILATION_RESULT")
GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")

def main():
    evaluate_all_results(unit_test_runner.run_tests(COMPILATION_RESULT, GCP_PROJECT_ID))


def evaluate_all_results(failed_tests):
    if failed_tests:
        print("\n")
        print(f"\u001b[31m{len(failed_tests)} unit tests failed!")
        for failed in failed_tests:
            print(f"\u001b[31m\t- {failed}")
        sys.exit(1)
    else:
        print("\u001b[32mAll unit tests passed!")
        sys.exit(0)


if __name__ == '__main__':
    main()
