import pytest
import functionality.todo
from functionality.todo import *


def test_check_pos_should_raise_exception_if_len_equal_0(mocker):
    mocker.patch.object(functionality.todo, 'todos', [])
    with pytest.raises(Exception) as e_info:
        check_pos(0)
    assert str(e_info.value) == "No more todos!"


@pytest.fixture
def initialise_todos(mocker):
    mocker.patch.object(functionality.todo, 'todos', ['aaa', 'bbb'])


@pytest.mark.parametrize("pos", [2, 3, 15])
def test_check_pos_should_raise_exception_if_pos_ge_len(initialise_todos, pos):
    with pytest.raises(Exception) as e_info:
        check_pos(pos)
    assert str(e_info.value) == "No such item number!"


@pytest.mark.parametrize("pos", [-1, -3, -5])
def test_check_pos_should_raise_exception_if_pos_negative(initialise_todos, pos):
    with pytest.raises(Exception) as e_info:
        check_pos(pos)
    assert str(e_info.value) == "No such item number!"


@pytest.mark.parametrize("content", ['ccc', ''])
def test_check_pos_should_add_content_correctly(mocker, content):
    todo_object = mocker.patch.object(functionality.todo, 'todos', ['aaa', 'bbb'])
    add_todo(content)
    assert todo_object == ['aaa', 'bbb', content]


@pytest.mark.parametrize("content", [51, -14.5])
def test_check_pos_should_add_non_string_content_correctly(mocker, content):
    todo_object = mocker.patch.object(functionality.todo, 'todos', ['aaa', 'bbb'])
    add_todo(content)
    assert todo_object == ['aaa', 'bbb', content]


@pytest.mark.parametrize("parameters", [(['aaa', 'bbb'], 0, ['bbb']), (['aaa', 'bbb'], 1, ['aaa'])])
def test_check_pos_should_remove_content_correctly(mocker, parameters):
    todo_object = mocker.patch.object(functionality.todo, 'todos', parameters[0])
    remove_todo(parameters[1])
    assert todo_object == parameters[2]


@pytest.mark.parametrize("pos", [2, 3, -1])
def test_should_check_pos_raise_exception_if_removing_wrong_pos(mocker, pos):
    mocker.patch.object(functionality.todo, 'todos', ['aaa', 'bbb'])
    with pytest.raises(Exception):
        remove_todo(pos)


def test_check_pos_should_raise_exception_if_removing_from_empty(mocker):
    mocker.patch.object(functionality.todo, 'todos', [])
    with pytest.raises(Exception):
        remove_todo(0)


def test_check_pos_should_clear_todos_correctly(mocker):
    todo_object = mocker.patch.object(functionality.todo, 'todos', ['aaa', 'bbb'])
    remove_all()
    assert todo_object == []


def test_check_pos_should_clear_todos_without_errors_from_empty_todos(mocker):
    todo_object = mocker.patch.object(functionality.todo, 'todos', [])
    remove_all()
    assert todo_object == []
