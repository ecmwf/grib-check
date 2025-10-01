# Components

This section describes the components used in GribCheck.

## Grib

The Grib class represents all messages in a GRIB file.
It can be used to iterate over all these messages in a Pythonic way.

## Message

A message is a wrapper around the ecCodes handle, with the key difference that it provides automatic memory management.

To get the value of a key, we can use either the `get` method or the square brackets `[]` operator.
While square brackets are more convenient, it returns the value in the native format (e.g., a string).
The `get` method, on the other hand, can return the value in a specific format, such as `float`, `int`, or `str`.

```python
grib = Grib("path/to/file.grib2")
message = grib.next()
print(f"message['stream'] = {message['stream']}")
# message['stream'] = enfo
print(f"message.get('stream', int) = {message.get('stream', int)}")
# message.get('stream', int) = 1035
```
## KeyValue type

Values returned by a Message are stored in a KeyValue type.
Each KeyValue contains the key name, the value (which can be a number or a string), and the corresponding data type.

```python
a = KeyValue("a", 5)
print(f"a.key() = {a.key()}\n a.value() = {a.value()}\n a.type() = {a.type()}")
# a.key() = a
# a.value() = 5
# a.type() = <class 'int'>
```

### Mathematical operations

KeyValue supports various mathematical operations. These operations serve two purposes:
First, they modify the value as expected.
Secondly, they construct a mathematical expression in string format to demonstrate how the value was calculated.
This can help users to understand the logic behind the calculations.

The key changes the format of the string representation of the KeyValue after the operation.
For example, if we add two KeyValue objects together, the resulting KeyValue will have a string representation that shows the addition operation.
Inside the parentheses, the string representation of the KeyValue is displayed.


```python
a = KeyValue("a", 5)
b = KeyValue("b", 6)
c = a + b

print(f"c.key() = {c.key()}")
# c.value() = a(5) + b(6)

print(f"c.value() = {c.value()}")
# c.value() = 11

print(f"{c} = {c.value()}")
# a(5) + b(6) = 11
```

## Report

A report serves as a container for various entities, such as assertions, informational messages, and nested reports.
Each report has a status, which is determined by the statuses of the entities it contains.
For example, if a single assertion fails, the report's status will be set to "fail" accordingly.
Reports can also be nested, and the same rules for status propagation apply to nested reports as well.

```python
        report = Report("Extended check")
        report.add(Ge(message['bitsPerValue'], 0))
```

## Assertion

An assertion verifies whether values meet the expected conditions.
For example, we can check whether `bitsPerValue` is a positive number.
A typical report contains one or more assertions.

```python
Ge(message['a'], message['b']) # a >= b
```
