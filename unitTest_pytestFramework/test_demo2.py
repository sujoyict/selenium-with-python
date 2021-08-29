import pytest

@pytest.mark.smoke
@pytest.mark.skip # to skip any method from run command
def test_firstProgram():
    msg = "hello"
    assert msg == "hi" , "Test failed because strings do not match"

def test_SecondProgram():
    a=4
    b=6
    assert a+2 == 6, "Addition do not match"

def test_CreditCard():  #run matched method name
    a=4
    b=6
    assert a+2 == 6, "Addition do not match"

# py.test -k CreditCard -v -s //will run the specific method name file