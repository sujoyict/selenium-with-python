# pytest method names should start with test_ or end with _test
# pytest methid names should start with test
# Anycode should be wrapped in method only
# -k for method names execution, -s for logs in output, -v for more info like metadata //this run method is mostly used
# u can run specific file with py.test <filename>
# you can mark (tag) tests @pytest.mark.smoke (smoke is mark name) and then run with -m
import pytest


@pytest.mark.smoke
def test_firstProgram():
    print("hello")
# methodname will not be the same

def test_gret():
    print("Good Morning")

def test_CreditCard():
    print("Good Morning")

# ---run selected file test---
# py.test -v -s //will run all the files
# py.test test_demo2.py -v -s //will run the specific file
# py.test -k CreditCard -v -s //will run the specific method name file
# py.test -m smoke -v -s //will run the specific tagged/marked file



