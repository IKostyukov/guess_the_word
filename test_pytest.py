<<<<<<< HEAD
import pytest

import app
import conftest



app.words = ["iii", "iii", "iii"]
app.word = "iii"
count = 1
used_lit = "u"
ok_lit = "i"

def test_hello():
    result_task = app.hello()
    assert result_task == "iii"    


def test_make_frame():
    result = app.make_frame(app.word)
    assert result == ["_", "_", "_"]

def test_get_new_literal(monkeypatch):   
    monkeypatch.setattr('builtins.input', lambda x: ok_lit)
    i = input('Введите букву на английском: ')    
    assert i == "i"


def test_veryficaition_lit_more_one(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "abc")
    i = input('Введите букву на английском: ')    
    assert i == "abc"
    # result = app.veryficaition("abc")
    # type(result) == type(app.get_new_literal())

def test_veryficaition_lit_no_english(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "щ")
    i = input('Введите букву на английском: ')    
    assert i == "щ"
    # result = app.veryficaition("щ")
    # assert type(result) == type(app.get_new_literal())
    
def test_veryficaition_lit_used(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: used_lit)
    i = input('Введите букву на английском: ')    
    assert i == "u"
    # result = app.veryficaition(used_lit)
    # assert type(result) == type(app.get_new_literal())

def test_veryficaition_lit_ok(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: ok_lit)
    i = input('Введите букву на английском: ')    
    assert i == "i"
    # result = app.veryficaition(ok_lit)
    # assert type(result) == type(app.get_new_literal())

def test_make_count_less_big_count(big_count):
    result = app.make_count_less(app.count, app.word)
    assert result == 2

def test_make_count_less_yes(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "yes")  
    result = app.make_count_less(count, app.word)
    assert result == 4


def test_make_count_less_not(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "not")  
    result = app.make_count_less(count, app.word)
    assert result == False    



def test_opening_lit_ok_1(ok_1):   
    result = app.opening_lit()
    assert result == ["_", "i", "_"]

def test_opening_lit_ok_3(ok_3):   
    result = app.opening_lit()
    assert result == ["i", "i", "i"]    




 

=======
import pytest

import app
import conftest



app.words = ["iii", "iii", "iii"]
app.word = "iii"
count = 1
used_lit = "u"
ok_lit = "i"

def test_hello():
    result_task = app.hello()
    assert result_task == "iii"    


def test_make_frame():
    result = app.make_frame(app.word)
    assert result == ["_", "_", "_"]

def test_get_new_literal(monkeypatch):   
    monkeypatch.setattr('builtins.input', lambda x: ok_lit)
    i = input('Введите букву на английском: ')    
    assert i == "i"


def test_veryficaition_lit_more_one(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "abc")
    i = input('Введите букву на английском: ')    
    assert i == "abc"
    # result = app.veryficaition("abc")
    # type(result) == type(app.get_new_literal())

def test_veryficaition_lit_no_english(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "щ")
    i = input('Введите букву на английском: ')    
    assert i == "щ"
    # result = app.veryficaition("щ")
    # assert type(result) == type(app.get_new_literal())
    
def test_veryficaition_lit_used(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: used_lit)
    i = input('Введите букву на английском: ')    
    assert i == "u"
    # result = app.veryficaition(used_lit)
    # assert type(result) == type(app.get_new_literal())

def test_veryficaition_lit_ok(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: ok_lit)
    i = input('Введите букву на английском: ')    
    assert i == "i"
    # result = app.veryficaition(ok_lit)
    # assert type(result) == type(app.get_new_literal())

def test_make_count_less_big_count(big_count):
    result = app.make_count_less(app.count, app.word)
    assert result == 2

def test_make_count_less_yes(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "yes")  
    result = app.make_count_less(count, app.word)
    assert result == 4


def test_make_count_less_not(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "not")  
    result = app.make_count_less(count, app.word)
    assert result == False    



def test_opening_lit_ok_1(ok_1):   
    result = app.opening_lit()
    assert result == ["_", "i", "_"]

def test_opening_lit_ok_3(ok_3):   
    result = app.opening_lit()
    assert result == ["i", "i", "i"]    




 

>>>>>>> 766ac694a4f32a9e29c0f43b17c21edef7140a13
