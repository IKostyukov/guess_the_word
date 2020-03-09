<<<<<<< HEAD
import pytest
import app


app.lit = "i"


@pytest.fixture
def big_count():
    app.count = 3
 

@pytest.fixture
def ok_1():
    app.word = "pip"

@pytest.fixture
def ok_3():
    app.word = "iii"

# @pytest.fixture
# def lit_no_english():
#     app.lit = "щ"
    
# @pytest.fixture
# def lit_used():
#     app.lit = "u"
#     app.used_lit = USED_LIT

# @pytest.fixture
# def lit_ok():
=======
import pytest
import app


app.lit = "i"


@pytest.fixture
def big_count():
    app.count = 3
 

@pytest.fixture
def ok_1():
    app.word = "pip"

@pytest.fixture
def ok_3():
    app.word = "iii"

# @pytest.fixture
# def lit_no_english():
#     app.lit = "щ"
    
# @pytest.fixture
# def lit_used():
#     app.lit = "u"
#     app.used_lit = USED_LIT

# @pytest.fixture
# def lit_ok():
>>>>>>> 766ac694a4f32a9e29c0f43b17c21edef7140a13
#     app.lit = lit