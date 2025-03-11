import jupygrader
from pathlib import Path

TEST_NOTEBOOKS_DIR = Path(__file__).resolve().parent / 'test-notebooks'
TEST_OUTPUT_DIR = Path(__file__).resolve().parent / 'test-output'

def test_notebook_without_test_cases():
    notebook_path = TEST_NOTEBOOKS_DIR / 'no-test-cases' / 'no-test-cases-test.ipynb'

    result = jupygrader.grade_notebook(
        notebook_path=notebook_path,
        output_path=TEST_OUTPUT_DIR
    )

    assert result['learner_autograded_score'] == 0
    assert result['max_total_score'] == 0
    assert result['num_total_test_cases'] == 0

