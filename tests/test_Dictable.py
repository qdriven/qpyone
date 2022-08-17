#!/usr/bin/env python
# -*- coding:utf-8 -*-
from collections import OrderedDict

from pytest import fixture, raises

from fluentqpy.builtins.dicts.dictable import classproperty, Dictable, DatabaseDictable, \
    DictTable


def test_classproperty():
    class Test:
        _foo = "bar"

        @classproperty
        def foo(cls):
            return cls._foo

    assert Test.foo == "bar"


def test_classproperty_vs_attribute_conflicts():
    class Foo(Dictable):
        _foo = "bar"

        @classproperty
        def foo(cls):
            return cls._foo

    assert Foo.foo == "bar"

    foo = Foo()
    assert foo.foo is None

    foo._silent = False
    with raises(AttributeError):
        foo.foo

    foo = Foo(foo="baz")
    assert foo._foo == "bar"
    assert foo.foo == "baz"


def test_property_vs_attribute_conflicts():
    class Foo(Dictable):
        _foo = "bar"

        @property
        def foo(self):
            return self._foo

    foo = Foo()
    assert foo.foo == "bar"

    with raises(AttributeError) as excinfo:
        foo = Foo(foo="baz")
    assert str(excinfo.value) == "can't set attribute"

    foo = Foo({"foo": "baz"})
    assert foo._foo == "bar"
    assert foo.foo == "bar"
    assert foo.__dict__["foo"] == "baz"


def test_dictable_return_type():
    view = Dictable()
    assert view(None) == {}
    view = Dictable(ordered=True)
    assert view(None) == OrderedDict()


@fixture
def TestDictable():
    class TestDictable(Dictable):
        @property
        def foobaz(self):
            return self.foo + self.baz

    return TestDictable


@fixture
def TestDatabaseDictable():
    class TestDatabaseDictable(DatabaseDictable):
        pass

    return TestDatabaseDictable

def test_init_with_dict():
    Dictable = DictTable({"foo": "bar", "baz": "qux"})
    assert Dictable.foo == "bar"
    assert Dictable.baz == "qux"


def test_init_with_args():
    Dictable = DictTable(foo="bar", baz="qux")
    assert Dictable.foo == "bar"
    assert Dictable.baz == "qux"

def test_init_mixed():
    Dictable = DictTable({"foo": "bar"}, baz="qux")
    assert Dictable.foo == "bar"
    assert Dictable.baz == "qux"


def test_repr():
    Dictable = eval(repr(DictTable(bar="baz")))
    assert isinstance(Dictable, DictTable)
    assert Dictable.bar == "baz"


def test_update_with_dict():
    Dictable = DictTable(foo="bar", baz="qux")
    Dictable.update({"foo": "BAR"})
    assert Dictable.foo == "BAR"
    assert Dictable.baz == "qux"


def test_default_view():
    Dictable = DictTable(foo="bar", baz="qux")
    assert Dictable.view() == {"foo": "bar", "baz": "qux"}

def test_missing_view():
    Dictable = DictTable(foo="bar", baz="qux")
    with raises(KeyError):
        Dictable.view("nop")


def test_property_exceptions():
    class ScreamingDictable(DictTable):
        @property
        def foo(self):
            raise AttributeError("Foo!")

    Dictable = ScreamingDictable()
    with raises(AttributeError) as excinfo:
        Dictable.foo
    assert str(excinfo.value) == "Foo!"

    class ScreamingDictableChild(ScreamingDictable):
        pass

    Dictable = ScreamingDictableChild()
    with raises(AttributeError) as excinfo:
        Dictable.foo
    assert str(excinfo.value) == "Foo!"


def test_silence():
    Dictable = ScreamingDictable()
    assert Dictable.foo is None

    class ScreamingDictable(Dictable):
        _silent = False

    Dictable = ScreamingDictable()
    with raises(AttributeError):
        Dictable.foo


def test_add_view(TestDictable):
    TestDictable.add_view("test")
    Dictable = TestDictable(foo="bar", baz="qux")
    assert Dictable.view() == {"foo": "bar", "baz": "qux"}
    assert Dictable.view("test") == {}


def test_add_view_override(TestDictable):
    TestDictable.add_view("defaults", defaults=False)
    Dictable = TestDictable(foo="bar", baz="qux")
    assert not Dictable.view()


def test_add_view_defaults(TestDictable):
    TestDictable.add_view("test", defaults=True)
    Dictable = TestDictable(foo="bar", baz="qux")
    assert Dictable.view("test") == {"foo": "bar", "baz": "qux"}


def test_add_view_include(TestDictable):
    TestDictable.add_view("test", include="foo")
    Dictable = TestDictable(foo="bar", baz="qux")
    assert Dictable.view("test") == {"foo": "bar"}


def test_add_view_include_list(TestDictable):
    TestDictable.add_view("test", include=["foo", "baz"])
    Dictable = TestDictable(foo="bar", baz="qux")
    assert Dictable.view("test") == {"foo": "bar", "baz": "qux"}


def test_add_view_exclude(TestDictable):
    TestDictable.add_view("test", defaults=True, exclude="foo")
    Dictable = TestDictable(foo="bar", baz="qux")
    assert Dictable.view("test") == {"baz": "qux"}


def test_add_view_exclude_list(TestDictable):
    TestDictable.add_view("test", defaults=True, exclude=["foo", "baz"])
    Dictable = TestDictable(foo="bar", baz="qux")
    assert Dictable.view("test") == {}


def test_tuple_aliases(TestDictable):
    TestDictable.add_view("test", include=[("foo", "FOO")])
    Dictable = TestDictable(foo="bar", baz="qux")
    assert Dictable.view("test") == {"FOO": "bar"}


def test_names():
    class FooBar(NamesMixin):
        pass

    assert FooBar.names == ["foo", "bar"]

    class FooBar(NamesMixin, Dictable):
        pass

    assert FooBar.names == ["foo", "bar"]


def test_names_with_abbreviation():
    class FOOBarQux(NamesMixin):
        pass

    assert FOOBarQux.names == ["foo", "bar", "qux"]

    class BarFOOQux(NamesMixin):
        pass

    assert BarFOOQux.names == ["bar", "foo", "qux"]

    class BarQuxFOO(NamesMixin):
        pass

    assert BarQuxFOO.names == ["bar", "qux", "foo"]


def test_database_names():
    assert DatabaseDictable.names == ["database", "Dictable"]


def test_database_name_from_class():
    class DatabaseTable(DatabaseDictable):
        pass

    assert DatabaseTable.database_name == "database"


def test_database_name_from_database():
    class DatabaseTable(DatabaseDictable):
        _database = True

    assert DatabaseTable.database_name is None


def test_database_name_from_attribute():
    class DatabaseTable(DatabaseDictable):
        _database_name = "foo"

    assert DatabaseTable.database_name == "foo"


def test_database_name_priority():
    class DatabaseTable(DatabaseDictable):
        _database = True
        _database_name = "foo"

    assert DatabaseTable.database_name is None


def test_table_name_from_class():
    class DatabaseTable(DatabaseDictable):
        pass

    assert DatabaseTable.table_name == "table"


def test_table_name_from_class_with_database():
    class DatabaseTable(DatabaseDictable):
        _database = True

    assert DatabaseTable.table_name == "database_table"


def test_table_name_from_class_with_database_name():
    class DatabaseTable(DatabaseDictable):
        _database_name = "foo"

    assert DatabaseTable.table_name == "database_table"


def test_table_name_from_table():
    class DatabaseTable(DatabaseDictable):
        _table = True

    assert DatabaseTable.table_name is None


def test_table_name_from_attribute():
    class DatabaseTable(DatabaseDictable):
        _table_name = "foo"

    assert DatabaseTable.table_name == "foo"


def test_table_name_priority():
    class DatabaseTable(DatabaseDictable):
        _table = True
        _table_name = "foo"

    assert DatabaseTable.table_name is None


def test_undefined_database():
    class Table(DatabaseDictable):
        pass

    assert Table.database_name is None

    with raises(AttributeError):
        Table.database

    class Table(DatabaseDictable):
        _table = True

    with raises(AttributeError):
        Table.database

    class DatabaseTable(DatabaseDictable):
        pass

    with raises(AttributeError):
        DatabaseTable.database


def test_undefined_table():
    class Table(DatabaseDictable):
        pass

    with raises(AttributeError):
        Table.table

    class Table(DatabaseDictable):
        _database = True

    with raises(AttributeError):
        Table.table


def test_database():
    class DatabaseTable(DatabaseDictable):
        _database = True

    assert DatabaseTable.database is True

    class DatabaseTable(DatabaseDictable):
        _table = True

        @classmethod
        def _get_database(cls, table, name):
            return table

    assert DatabaseTable.database is True


def test_table():
    class DatabaseTable(DatabaseDictable):
        _table = True

    assert DatabaseTable.table is True

    class DatabaseTable(DatabaseDictable):
        _database = True

        @classmethod
        def _get_table(cls, database, name):
            return database

    assert DatabaseTable.table is True


def test_registry():
    del registry[:]

    class Foo(Dictable):
        pass

    assert registry == [Foo]

    class Bar(Dictable):
        pass

    assert registry == [Foo, Bar]
