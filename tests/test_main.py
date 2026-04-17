import pytest

def create_student_info(names, scores):
    return [f"{name}: {score}" for name, score in zip(names, scores)]

def test_create_student_info():
    names = ["John", "Alice", "Bob"]
    scores = [90, 85, 95]
    expected_output = ["John: 90", "Alice: 85", "Bob: 95"]
    assert create_student_info(names, scores) == expected_output

def test_create_student_info_empty_lists():
    names = []
    scores = []
    expected_output = []
    assert create_student_info(names, scores) == expected_output

def test_create_student_info_unequal_list_lengths():
    names = ["John", "Alice", "Bob"]
    scores = [90, 85]
    expected_output = ["John: 90", "Alice: 85"]
    assert create_student_info(names, scores) == expected_output
