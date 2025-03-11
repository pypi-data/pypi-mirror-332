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
from . import sql_unit_test_builder
from . import unit_test_extractor
from . import unit_test_parser
from tabulate import tabulate

def run_tests(compilation_result, gcp_project_id):
    """
    Main program logic, finds and executes all defined unit tests

    Args:
        compilation_result (string): The Dataform compilation result the program should search the model for
        gcp_project_id (string): The GCP project ID the program should execute BQ queries in

    Returns:
        list: A list of failed test names
    """
    failed_tests = []
    for test in unit_test_extractor.get_unit_tests(): #after getting all tests, build and submit a test to BQ
        try:
            test_name = test.get("name", "undefined")

            if unit_test_parser.validate_schema(test):
                model_exists, model_to_test = unit_test_extractor.get_model_to_test(test, compilation_result)
                if model_exists:
                    if validate_mocked_tables(test_name, test, model_to_test):
                        results = execute_test(gcp_project_id, test, model_to_test)

                        if not is_passed_test(results, test_name):
                            failed_tests.append(test_name)
                    else:
                        failed_tests.append(test_name)
                else:
                    print(f"\u001b[33mUnit test `{test_name}`: {test['model_to_test']} no longer exists in your Dataform repo, please double check this is correct, otherwise delete this unit test")
            else:
                print(f"\u001b[31mUnit test `{test_name}` has an invalid format")
                failed_tests.append(test_name)
        except Exception as e:
            print(f"\u001b[31mUnit test `{test_name}`: {e.message}")
            failed_tests.append(test_name)
    
    return failed_tests


def execute_test(gcp_project_id, test, model_to_test):
    """
    Executes a valid unit test

    Args:
        gcp_project_id (string): The GCP project ID the program should execute BQ queries in
        test (dict): The unit test to execute
        model_to_test (string): The Dataform model to test

    Returns:
        dataframe: A Pandas dataframe containing the results of the executed query in BigQuery
    """
    unit_test_parser.scaffold_tables(gcp_project_id, test["input_data"], model_to_test)
    unit_test_parser.scaffold_tables(gcp_project_id, test["expected_output"], model_to_test)    
    test_to_submit = sql_unit_test_builder.build_test_to_submit(test, model_to_test)
    return submit_test_to_bq(test_to_submit)


def validate_mocked_tables(test_name, test, model_to_test):
    """
    Takes a test and validates the mocked tables are valid through different checks

    Args:
        test_name (string): The name of the test to check
        test (dict): The unit test to evaluate
        model_to_test (string): The Dataform model to test

    Returns:
        dataframe: A Pandas dataframe containing the results of the executed query in BigQuery
    """
    if not unit_test_parser.check_input_tables_exist(test, model_to_test):
        print(f"\u001b[31mUnit test `{test_name}` contains input tables that don't exist in the Dataform model, please double check.")
        return False
    if not unit_test_parser.check_input_table_cols_match(test["input_data"]):
        print(f"\u001b[31mUnit test `{test_name}` contains input tables with inconsistent columns provided, please double check.")
        return False
    if not unit_test_parser.check_expected_output_cols_match(test["expected_output"]):
        print(f"\u001b[31mUnit test `{test_name}` contains inconsistent columns provided for the expected output, please double check.")
        return False

    return True


def is_passed_test(unit_test_results, test_name):
    """
    Takes a test's results and evaluates if it has passed or failed'

    Args:
        uni_test_results (dataframe): The dataframe containing the test results
        test_name (string): The name of the unit test

    Returns:
        bool: True if passed; False if not
    """
    if unit_test_results.empty:
        print(f"\u001b[32mUnit test `{test_name}` passed")
        return True
    else:
        print(f"""\u001b[31mUnit test `{test_name}` failed
        
        {tabulate(unit_test_results, headers='keys', tablefmt='github')}""")
        return False


def submit_test_to_bq(test_to_submit):
    """
    Takes a SQL string which reperesents a unit test and submits to BigQuery
    for processing

    Args:
        test_to_submit (string): A SQL string which represents the unit test to execute

    Returns:
        dataframe: A Pandas dataframe containing the results of the executed query in BigQuery
    """
    return unit_test_parser.BQ_CLIENT.query(test_to_submit).to_dataframe()
