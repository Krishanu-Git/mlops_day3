import os, sys
import pytest

def test_model_files_exist():
    expected = ['models/knn.joblib', 'models/nb.joblib']
    missing = [p for p in expected if not os.path.exists(p)]
    assert not missing, f'MISSING FILES: {missing}'
