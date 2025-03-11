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
import glob
import json

from google.cloud import dataform_v1beta1

DATAFORM_CLIENT = dataform_v1beta1.DataformClient()

def get_unit_tests():
    """
    Scans the entire directory the program is running in to identify all
    unit tests with a test_*.json file pattern.

    Args:
        None

    Returns:
        list: A list of JSON objects parsed from each unit test JSON file
    """
    unit_tests = []
    for unit_test in list(glob.iglob(f'**/test_*.json', recursive=True)):
        with open(unit_test) as f:
            contents = f.read()
            to_json = json.loads(contents)
            unit_tests.append(to_json)

    return unit_tests


def get_model_to_test(test, compilation_result):
    """
    Extracts the actual Dataform model that is being tested defined in 
    the unit test.

    Args:
        test (dict): The unit test which is represented as a Python dict.
        compilation_result (string): The Dataform compilation result which contains all the Dataform models developed.

    Returns:
        bool: True if the model to test exists in the Dataform repo; False if not.
        string: The SQL query that is being executed by the Dataform model. None if it doesn't exist.
    """
    model_to_test_schema_table = test["model_to_test"].split(".")
    compilation_result_actions_request = dataform_v1beta1.QueryCompilationResultActionsRequest(name=compilation_result)
    actions = DATAFORM_CLIENT.query_compilation_result_actions(request=compilation_result_actions_request)

    model_exists = False

    for action in actions:
        if action.target.schema == model_to_test_schema_table[0] and action.target.name == model_to_test_schema_table[1]:
            model_exists = True
            return model_exists, action.relation.select_query
        
    return model_exists, None
