# Sets:
A set is a collection of distinct elements.
A set add operation adds an element to the set, provided an equal element doesn't already exist in the set.
A set is an unordered collection.

Set elements may be primitive data values, such as numbers or strings, or objects with numerous data members.
When storing objects, set implementations commonly distinguish elements based on an element's key value:
A primitive data value that serves as a unique identifier for the element.

Sets are commonly implemented to use keys for all element types.
When storing objects, the set retrieves an object's key via an external function or predetermined knowledge of which property is the key value.
When storing primitive data values, each primitive data value's key is itself.

Given a key, a set remove operation removes the element with the specified key from the set.

Given a key, a set search operation returns the set element with the specified key, or null if no such element exists.
The search operation can be used to implement a subset test.
A set X is a subset of set Y only if every element of X is also an element of Y.

## Set Operations:
### Union, Intersection, and Difference:
The union of sets X and Y, denoted as X &cup; Y, is a set that contains every element from X, every element from Y, and no additional elements.

The intersection of sets X and Y, denoted as X &cap; Y, is a set that contains every element that is in both X and Y, and no additional elements.

The difference of sets X and Y, denoted as X \ Y, is a set that contains every element that is in X but not in Y, and no additional elements.

The union and intersection operations are cumulative, so X &cup; Y = Y &cup; X and X &cap; Y = Y &cap; X.
The difference operation is not cumulative.

### Filter and Map:
A filter operation on set X produces a subset containing only elements from X that satisfy a particular condition.
The condition for filtering is commonly represented by a filter predicate:
A function that takes an element as an argument and returns a boolean value indicating whether or not that element will be in the filtered subset.

A map operation on set X produces a new set by applying some function F to each element.

## Static and Dynamic Set Operations:
A dynamic set is a set that can change after being constructed.
A static set is a set that doesn't change after being constructed.
A collection of elements is commonly provided during construction of a static set, each of which is added to the set.

Static sets support most set operations by returning a new set representing the operation's result.
The table below summarizes the common operations for static and dynamic sets.

|Operation|Dynamic set support?|Static set support|
|---------|--------------------|------------------|
|Construction from a collection of values|Yes|Yes|
|Count number of elements|Yes|Yes|
|Search|Yes|Yes|
|Add element|Yes|No|
|Remove element|Yes|No|
|Union(returns new set)|Yes|Yes|
|Intersection (returns new set)|Yes|Yes|
|Difference (returns new set)|Yes|Yes|
|Filter (returns new set)|Yes|Yes|
|Map (returns new set)|Yes|Yes|
