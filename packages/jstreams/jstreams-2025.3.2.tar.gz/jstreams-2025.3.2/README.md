# jstreams

jstreams is a Python library aiming to replicate the following:
- Java Streams and Optional functionality
- a basic ReactiveX implementation
- a minimal replication of Java's vavr.io Try
- a basic dependency injection container
- some utility classes for threads as well as JavaScript-like timer and interval functionality

The library is implemented with type safety in mind.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install jstreams.

```bash
pip install jstreams
```

## Usage
### v2025.3.2
This version adds more dependency injection options (for usage, check the Dependency injection section below):
- *resolveVariables* decorator - provides class level variable injection
- *resolveDependencies* decorator - provides class level dependency injection
- *component* decorator - provides decoration for classes. A decorated class will be injected once its module is imported
- *InjectedVariable* class - a class providing access to a injected variable without the need for decoration or using the `injector` directly
- added callable functionality to `InjectedDependency` and `OptionalInjectedDependency` classes. You can now call `dep()` instead of `dep.get()`
### v2025.2.11
Version 2025.2.11 adds the following enhancements:
#### Pair and Triplet
The **Pair** and **Triplet** classes are object oriented substitutions for Python tuples of 2 and 3 values. A such, they don't need to be unpacked and can be used by calling the **left**, **right** and **middle**(Triplets only) methods.
For enhanced support with predicates and streams, **jstreams** also provides the following predicates dedicated to pairs and triplets:
- *leftMatches* - A predicate that takes another predicate as a parameter, and applies it to the **left** of a Pair/Triplet
- *rightMatches* - A predicate that takes another predicate as a parameter, and applies it to the **right** of a Pair/Triplet
- *middleMatches* - A predicate that takes another predicate as a parameter, and applies it to the **middle** of a Triplet

```python
p = pair("string", 0)
pred = rightMatches(isZero)
pred(p) 
# Returns True since the right value is, indeed, zero

# Usage with optional
optional(pair("string", 0)).filter(leftMatches(contains("tri"))).filter(rightMatches(isZero)).get() 
# Returns the pair, since both fields match the given predicates

# Usage with stream
pairs = [pair("test", 1), pair("another", 11), pair("test1", 2)]
stream(pairs).filter(leftMatches(contains("test"))).filter(rightMatches(isHigherThan(1))).toList() 
# Produces [pair("test1", 2)], since this is the only item that can pass both filters

```
#### New predicates
The following general purpose predicates have been added:
- *isKeyIn* - checks if the predicate argument is present as a key in the predicate mapping
- *isValueIn* - checks if the predicate argument is present as a value in the predicate mapping
```python
predIsKeyIn = isKeyIn({"test": "1"})
predIsKeyIn("test") 
# Returns True, since the given string is a key in the predicate dictionary

predIsKeyIn("other") 
# Returns False, since the givem string is not a key in the predicate dictionary

predIsValueIn = isValueIn({"test": "1"})
predIsValueIn("1")
# Returns True, since the given string is a value in the predicate dictionary

predIsValueIn("0")
# Returns False, since the given string is not a value in the predicate dictionary

```
### v2025.2.9
From this version onwards, **jstreams** is switching the the following semantic versioning *YYYY.M.R*. YYYY means the release year, M means the month of the release within that year, and R means the number of release within that month. So, 2025.2.9 means the ninth release of February 2025.

Version v2025.2.9 updates the *Predicate*, *PredicateWith*, *Mapper*, *MapperWith* and *Reducer* classes to be callable, so they can now be used without explicitly calling their underlying methods. This change allows predicates, mappers and reducers to be used as functions, not just in *Stream*, *Opt* and *Case* operations. v2025.2.9 also introduces a couple of new predicates:
- hasKey - checks if a map contains a key
- hasValue - checks if a map contains a value
- isInInterval - checks if a value is in a closed interval, alias for *isBetweenClosed*
- isInOpenInterval - checks if a value is in an open interval, aloas for *isBetween*
- contains - checks if an Iterable contains an element (the symetrical function for *isIn*)
- allOf - produces a new predicate that checks for a list of given predicates. Returns True if all predicates are satisfied
- anyOf - produces a new predicate that checks for a list of given predicates. Returns True if any of the predicates are satisfied
- noneOf - produces a new predicate that checks for a list of given predicates. Returns True if none of the predicates are satisfied
- Not - alias of *not_*
- NotStrict - alias of *notStrict*

The *Predicate* and *PredicateWith* classes have been enriched with the *And* and *Or* methods in order to be chained with another predicate.

```python
# Define a predicate
isNonePredicate = predicateOf(isNone)

# Before 2025.2.9
isNonePredicate.Apply(None) # Returns True
isNonePredicate.Apply("test") # Returns False

# After 2025.2.9
isNonePredicate(None) # Returns True, internally calls the *Apply* method of the predicate
isNonePredicate("test") # Returns False

# Chain predicates
chainedPredicate = predicateOf(isNotNone).And(equals("test"))
chainedPredicate("test") # Returns True, since the parameter is not none and matches the equals predicate
chainedPredicate(None) # Returns False, since the parameter fails the first predicate, isNotNone
chainedPredicate("other") # Returns False, since the parameter passes the isNotNone
```

### v4.1.0 

#### What's new?
Version 4.1.0 introduces the *Match* and *Case* classes that can implement switching based on predicate functions and predicate classes.

```python
# Returns the string "Hurray!"
match("test").of(
    case("test", "Hurray!"),
    case("test1", "Not gonna happen")
)

# Default casing, as a fallback for when the value doesn't match any of the cases
# IMPORTANT NOTE! The default case should ALWAYS be called last, as it will break the match if called before all cases are tested.
match("not-present").of(
    case("test", "Hurray!"),
    case("test1", "Not gonna happen"),
    defaultCase("Should never get here!")
)
```

Version 4.0.0 introduces the *Predicate*, *Mapper* and *Reducer* classes that can replace the functions used so far for predicate matchig, mapping and reducing of streams. The added advantage for these classes is that they can be extended and can contain dynamic business logic.
```python
# Take the numbers from a stream until the third prime number is found.

def isPrime(value: int) -> bool:
    ...

class TakeUntilThreePrimes(Predicate[int]):
    def __init__(self) -> None:
        self.numberOfPrimesFound = 0

    def Apply(self, value: int) -> bool:
        if self.numberOfPrimesFound >= 3:
            return False

        if isPrime(value):
            self.numberOfPrimesFound += 1
        return True

# Then we take a stream if ints
Stream([3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15]).takeWhile(TakeUntilThreePrimes()).each(print)
# This will print 3, 4, 5, 6, 8, 9, 10, 11, then stop the stream since three prime numbers were found.
```

#### BREAKING CHANGES

In version 4.0.0, the Opt class has been refactored to fall in line with the Java implementation. The methods *getOrElse*, *getOrElseOpt*, *getOrElseGet* and *getOrElseGetOpt* have been removed, and the methods *orElse*, *orElseOpt*, *orElseGet* and *orElseGetOpt* will be replacing them. The older signatures for the *orElse* and *orElseOpt* have been changed to adapt to this change. In order to migrate you can follow this guide:

```python
# Old usage of orElse
Opt(None).orElse(lambda: "test")
# can be replaced with
Opt(None).orElseGet(lambda: "test")

# Old usage of getOrElse
Opt(None).getOrElse("test")
# can be replaced with
Opt(None).orElse("test")

# Old usage of getOrElseGet, which was the same as orElse
Opt(None).getOrElseGet(lambda: "test")
# can be replaced with
Opt(None).orElseGet(lambda: "test")
```

### Streams

```python
from jstreams import Stream

# Applies a mapping function on each element then produces a new string
print(Stream(["Test", "Best", "Lest"]).map(str.upper).collect())
# will output ["TEST", "BEST", "LEST"]

# Filter the stream elements
print(Stream(["Test", "Best", "Lest"])
            .filter(lambda s: s.startswith("T"))
            .collect())
# Will output ['Test']

# isNotEmpty checks if the stream is empty
print(Stream(["Test", "Best", "Lest"])
            .filter(lambda s: s.startswith("T"))
            .isNotEmpty())
# Will output True

# Checks if all elements match a given condition
print(Stream(["Test", "Best", "Lest"]).allMatch(lambda s: s.endswith("est")))
# Will output True

print(Stream(["Test", "Best", "Lest"]).allMatch(lambda s: s.startswith("T")))
# Will output False

# Checks if any element matches a given condition
print(Stream(["Test", "Best", "Lest"]).anyMatch(lambda s: s.startswith("T")))
# Will output True

# Checks if no elements match the given condition
print(Stream(["Test", "Best", "Lest"]).noneMatch(lambda s: s.startswith("T")))
# Will output False

# Gets the first value of the stream as an Opt (optional object)
print(Stream(["Test", "Best", "Lest"])
            .findFirst(lambda s: s.startswith("L"))
            .getActual())
# Will output "Lest"

# Returns the first element in the stream
print(Stream(["Test", "Best", "Lest"]).first())
# Will output "Test"

# cast casts the elements to a different type. Useful if you have a stream
# of base objects and want to get only those of a super class
print(Stream(["Test1", "Test2", 1, 2])
            .filter(lambda el: el == "Test1")
            # Casts the filtered elements to the given type
            .cast(str)
            .first())
# Will output "Test1"

# If the stream elements are Iterables, flatMap will produce a list of all contained items
print(Stream([["a", "b"], ["c", "d"]]).flatMap(list).toList())
# Will output ["a", "b", "c", "d"]

# reduce will produce a single value, my applying the comparator function given as parameter
# in order to decide which value is higher. The comparator function is applied on subsequent elements
# and only the 'highest' one will be kept
print(Stream([1, 2, 3, 4, 20, 5, 6]).reduce(max).getActual())
# Will output 20

# notNull returns a new stream containing only non null elements
print(Stream(["A", None, "B", None, None, "C", None, None]).nonNull().toList())
# Will output ["A", "B", "C"]

```

### Opt
```python
from jstreams import Opt

# Checks if the value given is present
Opt(None).isPresent() # Will return False
Opt("test").isPresent() # Will return True


# There are two ways of getting the value from the Opt object. The get returns a non optional
# value and  will raise a value error if the object is None. On the other hand, getActual returns
# an optional object and does not raise a value error
Opt("test").get() # Does not fail, and returns the string "test"
Opt(None).get() # Raises ValueError since None cannot be casted to any type
Opt(None).getActual() # Returns None, does not raise value error

# The ifPresent method will execute a lambda function if the object is present
Opt("test").ifPresent(lambda s: print(s)) # Will print "test"
Opt(None).ifPresent(lambda s: print(s)) # Does nothing, since the object is None

# The orElse method will return the value of the Opt if not None, otherwise the given parameter
Opt("test").orElse("test1") # Will return "test", since the value is not None
Opt(None).orElse("test1") # Will return "test1", since the value is  None

# The orElseGet method will return the value of the Opt if not None, otherwise it will execute 
# the given function and return its value
Opt("test").orElseGet(lambda: "test1") # Will return "test", since the value is not None
Opt(None).orElseGet(lambda: "test1") # Will return "test1", since the value is  None

# stream will convert the object into a stream.
Opt("test").stream() # Is equivalent with Stream(["test"])
Opt(["test"]).stream() # Is equivalent with Stream([["test"]]). Notice the list stacking

# flatStream will convert the object into a stream, with the advantage that it can
# detect whether the object is a list and avoids stacking lists of lists.
Opt("test").flatStream() # Is equivalent with Stream(["test"])
Opt(["test", "test1", "test2"]).flatStream() # Is equivalent with Stream(["test", "test1", "test2"])

```

### Predicates
Predicates are functions and function wrappers that can be used to filter streams and optionals. **jstreams** contains a comprehensive list of predefined predicates. The names are pretty self explanatory. Here are some of the predicates included:
- isTrue
- isFalse
- isNone
- isNotNone
- isIn
- isNotIn
- equals
- isBlank
- default
- allNone
- allNotNone
- strContains
- strContainsIgnoreCase
- strStartsWith
- strStartsWithIgnoreCase
- strEndsWith
- strEndsWithIgnoreCase
- strMatches
- strNotMatches
- strLongerThan
- strShorterThan
- strLongerThanOrEqual
- strShorterThanOrEqual
- equalsIgnoreCase
- isEven
- isOdd
- isPositive
- isNegative
- isZero
- isInt
- isBeween
- isBeweenClosed
- isBeweenClosedStart
- isBeweenClosedEnd
- not_
- notStrict
- hasKey
- hasValue
- isInInterval
- isInOpenInterval
- contains
- anyOf
- allOf
- noneOf

The predicates provided fall into one of two categories:
- functions - can be applied directly to a value
- function wrappers - take comparison parameters and then can be applied to a value

Examples:
```python
from jstreams import isBlank, isNotBlank, isZero, isBetween, not_

# functions
isBlank("test") # returns False
isZero(0) # returns True

# function wrappers
isBetween(1,10)(5) # First call generates the wraper, that can then be used for the value comparison
# reusing a function wrapper
isBetween1And10 = isBetween(1, 10)
isBetween1And10(5) # Returns True
isBetween1And10(20) # Returns False

not_(isBlank)("test") # Returns True. The not_ predicate negates the given predicate, in this case isBlank, then applies it to the given value "test"

# Usage with Opt and Stream
Stream([2, 4, 5, 20, 40]).filter(isBetween(0, 10)).toList() # Results in [2, 4, 5], since the rest of the items are filtered out
# Usage of not with Opt and Stream
Stream(["", "", "", "test"]).filter(not_(isBlank)).toList() # Results in ["test"] since the rest of the items are blank
# this is equivalent to 
Stream(["", "", "", "test"]).filter(isNotBlank).toList() # isNotBlank is another predefined predicate that uses not_(isBlank) in its actual implementation
# Check if a stream contains the value 0
Stream([1, 2, 4, 0, 5]).anyMatch(isZero) # Returns True, since 0 exists in the stream
```


### Try
```python
# The Try class handles a chain of function calls with error handling

def throwErr() -> None:
    raise ValueError("Test")

def returnStr() -> str:
    return "test"

# It is important to call the get method, as this method actually triggers the entire chain
Try(throwErr).onFailure(lambda e: print(e)).get() # The onFailure is called

Try(returnStr).andThen(lambda s: print(s)).get() # Will print out "test"

# The of method can actually be used as a method to inject a value into a Try without
# actually calling a method or lambda
Try.of("test").andThen(lambda s: print(s)).get() # Will print out "test"
```

### ReactiveX
The **jstreams** library includes a basic implementation of the ReactiveX API including observables, subjects and a handful of reactive operators.

#### Observables
Observables that are currently implemented in **jstreams** are of two types:
- *Single* - will only hold a single value
- *Flowable* - will hold an iterable providing values

##### Single
```python
from jstreams import Single

singleObs = Single("test")
# Will print out "test"
# When subscribing, the observable will emit the value it holds
# to the subscriber
singleObs.subscribe(
    lambda s: print(s)
)
```

##### Flowable
```python
from jstreams import Flowable

flowableObs = Flowable(["test1", "test2"])
# Will print out "test1" then "test2"
# When subscribing, the observable will emit the values it holds
# to the subscriber
flowableObs.subscribe(
    lambda s: print(s)
)
```
#### Subjects
**jstreams** implements the following Subject types:
- *BehaviorSubject* - will only hold a single value, keep it stored, then emit it whenever a subscriber subscribes, then emit any change to all subscribers
- *PublishSubject* - similar to *BehaviorSubject*, but only emits a change to all subscribers. No emission happens when subscribing
- *ReplaySubject* - will hold an list of past values and emit them all when subscribing to the subject. Subsequent changes are also emitted

##### BehaviorSubject
```python
from jstreams import BehaviorSubject

# Initialize the subject with a default value
subject = BehaviorSubject("A")
subject.onNext("B")

# Will print out "B" as this is the current value stored in the Subject
subject.subscribe(
    lambda s: print(s)
)

# Will print out "C" as this is the next value stored in the Subject,
# any new subscription at this point will receive "C"
subject.onNext("C")

# For long lived subjects and observables, it is wise to call the
# dispose method so that all subscriptions can be cleared and no
# references are kept. The subject can be reused, but all 
# subscriptions will need to be re-registered
subject.dispose()
```

##### PublishSubject
```python
from jstreams import PublishSubject

# Initialize the subject. Since the subject doesn't hold any initial value
# it cannot infer the type, so the type needs to be specified
subject = PublishSubject(str)

# Nothing happens at this point, since PublishSubject won't store the current value
subject.subscribe(
    lambda s: print(s)
)

# Will print out "C" as this is the next value sent tothe Subject.
# Any new subscription after this call not receive a value
subject.onNext("C")

# No value is sent to the subscriber, so nothing to print
subject.subscribe(
    lambda s: print(s)
)

# For long lived subjects and observables, it is wise to call the
# dispose method so that all subscriptions can be cleared and no
# references are kept. The subject can be reused, but all 
# subscriptions will need to be re-registered
subject.dispose()
```

##### ReplaySubject
```python
from jstreams import ReplaySubject

# Initialize the subject with a default value
subject = ReplaySubject(["A", "B", "C"])

# Will print out "A", then "B", then "C" as this the subject will replay
# the entire list of values whnever someone subscribes
subject.subscribe(
    lambda s: print(s)
)

# Will print out "C" as this is the next value added in the Subject,
# any new subscription at this point will receive "A", then "B", then "C"
subject.onNext("C")

# For long lived subjects and observables, it is wise to call the
# dispose method so that all subscriptions can be cleared and no
# references are kept. The subject can be reused, but all 
# subscriptions will need to be re-registered
subject.dispose()
```

#### Operators
**jstreams** provides a couple of operators, with more operators in the works.
The current operators are:
- *map* - converts a value to a different form or type
- *filter* - blocks or allows a value to be passed to the subscribers
- *reduce* - causes the observable to emit a single value produced by the reducer function.
- *take* - takes a number of values and ignores the rest
- *takeWhile* - takes values as long as they match the given predicate. Once a value is detected that does not match, no more values will be passing through
- *takeUntil* - takes values until the first value is found matching the given predicate. Once a value is detected that does not match, no more values will be passing through
- *drop* - blocks a number of values and allows the rest to pass through
- *dropWhile* - blocks values that match a given predicate. Once the first value is found not matching, all remaining values are allowed through
- *dropUntil* - blocks values until the first value that matches a given predicate. Once the first value is found matching, all remaining values are allowed through

##### Map - rxMap
```python
from jstreams import ReplaySubject, rxMap

# Initialize the subject with a default value
subject = ReplaySubject(["A", "BB", "CCC"])
# Create an operators pipe
pipe = subject.pipe(
    # Map the strings to their length
    rxMap(lambda s: len(s))
)
# Will print out 1, 2, 3, the lengths of the replay values
pipe.subscribe(
    lambda v: print(v)
)
```

##### Filter - rxFilter
```python
from jstreams import ReplaySubject, rxFilter

# Initialize the subject with a default value
subject = ReplaySubject(["A", "BB", "CCC"])
# Create an operators pipe
pipe = subject.pipe(
    # Filters the values for length higher than 2
    rxFilter(lambda s: len(s) > 2)
)
# Will print out "CCC", as this is the only string with a length higher than 2
pipe.subscribe(
    lambda v: print(v)
)
```

##### Reduce - rxReduce
```python
from jstreams import ReplaySubject, rxReduce

# Initialize the subject with a default value
subject = ReplaySubject([1, 20, 3, 12])
# Create an operators pipe
pipe = subject.pipe(
    # Reduce the value to max
    rxReduce(max)
)
# Will print out 1, then 20 since 1 is the first value, then 20, as the maximum between 
# the previous max (1) and the next value (20)
pipe.subscribe(
    lambda v: print(v)
)
```
##### Take - rxTake
```python
from jstreams import ReplaySubject, rxTake

subject = ReplaySubject([1, 7, 20, 5, 100, 40])
pipe1 = subject.pipe(
    rxTake(int, 3)
)
# Will print out the first 3 elements, 1, 7 and 20
pipe1.subscribe(
    lambda v: print(v)
)
# Won't print anything anymore since the first 3 elements were already taken
subject.onNext(9)
```

##### TakeWhile - rxTakeWhile
```python
from jstreams import ReplaySubject, rxTakeWhile

subject = ReplaySubject([1, 7, 20, 5, 100, 40])
pipe1 = subject.pipe(
    rxTakeWhile(lambda v: v < 10)
)
# Will print out 1, 7, since 20 is higher than 10
pipe1.subscribe(
    lambda v: print(v)
)
# Won't print anything since the while condition has already been reached
subject.onNext(9)
```

##### TakeUntil - rxTakeUntil
```python
from jstreams import ReplaySubject, rxTakeUntil

subject = ReplaySubject([1, 7, 20, 5, 100, 40])
pipe1 = subject.pipe(
    rxTakeUntil(lambda v: v > 10)
)
# Will print out 1, 7, since 20 is higher than 10, which is our until condition
pipe1.subscribe(
    lambda v: print(v)
)
# Won't print anything since the until condition has already been reached
subject.onNext(9)
```

##### Drop - rxDrop
```python
from jstreams import ReplaySubject, rxDrop

subject = ReplaySubject([1, 7, 20, 5, 100, 40])
self.val = []
pipe1 = subject.pipe(
    rxDrop(int, 3)
)
# Will print out 5, 100, 50, skipping the first 3 values
pipe1.subscribe(
    lambda v: print(v)
)
# Will print out 9, since it already skipped the first 3 values
subject.onNext(9)
```

##### DropWhile - rxDropWhile
```python
from jstreams import ReplaySubject, rxDropWhile

subject = ReplaySubject([1, 7, 20, 5, 100, 40])
self.val = []
pipe1 = subject.pipe(
    rxDropWhile(lambda v: v < 100)
)
# Will print 100, 40, since the first items that are less than 100 are dropped
pipe1.subscribe(lambda v: print(v))
# Will 9, since the first items that are less than 100 are dropped, and 9 appears after the drop while condition is fulfilled
subject.onNext(9)
```

##### DropUntil - rxDropUntil
```python
from jstreams import ReplaySubject, rxDropWhile

subject = ReplaySubject([1, 7, 20, 5, 100, 40])
self.val = []
pipe1 = subject.pipe(
    rxDropUntil(lambda v: v > 20)
)
# Will print out 100, 40, skipping the rest of the values until the first one 
# that fulfills the condition appears
pipe1.subscribe(self.addVal)
# Will print out 9, since the condition is already fulfilled and all remaining values will
# flow through
subject.onNext(9)
```

##### Combining operators
```python
from jstreams import ReplaySubject, rxReduce, rxFilter

# Initialize the subject with a default value
subject = ReplaySubject([1, 7, 11, 20, 3, 12])
# Create an operators pipe
pipe = subject.pipe(
    # Filters only the values higher than 10
    rxFilter(lambda v: v > 10)
    # Reduce the value to max
    rxReduce(max)
)
# Will print out 11, then 20 since 11 is the first value found higher than 10, then 20, as the maximum between the previous max (11) and the next value (20)
pipe.subscribe(
    lambda v: print(v)
)
```

##### Chaining pipes
**jstreams** allows pipes to be chained
```python
subject = ReplaySubject(range(1, 100))
val = []
val2 = []
chainedPipe = subject.pipe(
                rxTakeUntil(lambda e: e > 20)
            )
            .pipe(
                rxFilter(lambda e: e < 10)
            )
# val will contain 0..9
chainedPipe.subscribe(val.append)

# pipes allow multiple subscriptions
val2 = []
# val2 will contain 0..9
chainedPipe.subscribe(val2.append)
```

#### Custom operators
**jstreams** allows you to implement your own operators using two main base classes:
- *BaseMappingOperator* - any operator that can transform one value to another
- *BaseFilteringOperator* - any operator that can allow a value to pass through or not

As an example, you can see below the implementation of the reduce operator.
```python
class ReduceOperator(BaseFilteringOperator[T]):
    def __init__(self, reducer: Callable[[T, T], T]) -> None:
        self.__reducer = reducer
        self.__prevVal: Optional[T] = None
        super().__init__(self.__mapper)

    def __mapper(self, val: T) -> bool:
        if self.__prevVal is None:
            # When reducing, the first value is always returned
            self.__prevVal = val
            return True
        reduced = self.__reducer(self.__prevVal, val)
        if reduced != self.__prevVal:
            # Push and store the reduced value only if it's different than the previous value
            self.__prevVal = reduced
            return True
        return False
```

### Dependency injection container
The dependency injection container built into **jstreams** is a simple and straightforward implementation, providing two sets of methods for:
- providing dependencies
- retrieving dependencies
The container does not support parameter injection or constructor injection, but does (as of March 2025) support attributes injection.

#### How can I use the dependency injection container
The idea behind the DI container is to use interfaces in order to provide functionality in applications.
```python
import abc
from jstreams import injector

# Use the abstraction of interfaces
class MyInterface(abc):
    def doSomething(self) -> None:
        pass

# This is the actual class we want to use
class MyConcreteClass(MyInterface):
    def doSomething(self) -> None:
        print("Something got done")

injector().provide(MyInterface, MyConcreteClass())

# When the functionality defined by the interface is needed, you can retrieve it
myObj = injector().get(MyInterface)
myObj.doSomething()

# Then, during testing, you can mock the interface
class MyInterfaceMock(MyInterface):
    def __init__(self) -> None:
        self.methodCalled = False
    
    def doSomething(self) -> None:
        self.methodCalled = True

# the provide it to the injector before executing your tests
mock = MyInterfaceMock()
injector().provide(MyInterface, mock)
## execute test code
# then check if the execution happened
assertTrue(mock.methodCalled)
```

#### Providing and retrieving non qualified dependencies
```python
from jstreams import injector
from mypackage import MyClass, MyOtherClass

# Providing a single dependency using the Injector object
injector().provide(MyClass, MyClass())

# Providing multiple dependecies
injector().provideDependencies({
    MyClass: MyClass(),
    MyOtherClass: MyOtherClass(),
})

# Retrieve using get. This method will raise a ValueError if no object was provided for MyClass
myClass = injector().get(MyClass)

# Retrieve using find. This method returns an Optional and does not raise a ValueError. The missing dependency needs to be handled by the caller
myOtherClass = injector().find(MyOtherClass)
```

Dependencies can also be provided by using the `component` decorator:
```python
@component()
class Service:
    def doSomething(self) -> None:
        print("Do something")

injector().get(Service).doSomething() # Will print out "Do something"
```

Components can be defined using two different strategies:
- Lazy
- Eager

A lazy component will only be instatianted when needed:

```python
@component(Strategy.LAZY)
class Service:
    def doSomething(self) -> None:
        print("Do something")

# The dependency is not yet instantiated
injector().get(Service) # Now the dependency is created
```

An eager component will be instantiated once its module or the class itself is imported:
```python
@component(Strategy.EAGER)
class Service:
    def doSomething(self) -> None:
        print("Do something")

# The dependency is already instantiated
injector().get(Service) # Now the dependency can be retrieved
```

You can also use the `component` decorator to specify the class/interface the service needs to substitute
```python
@component(Strategy.LAZY, ServiceInterface)
class Service(ServiceInterface):
    def serviceMethod(self) -> None:
        pass

# Inject the dependency using the interface
injector().get(ServiceInterface)
```

#### Providing and retrieving qualified dependencies
```python
from jstreams import injector
from mypackage import MyClass, MyNotCalledClass

# Providing a single dependency using the Injector object and a qualified name
injector().provide(MyClass, MyClass(), "qualifiedName")

# Retrieve the first object using get by its name. This method will raise a ValueError if no object was provided for MyClass and the given qualifier
myClass = injector().get(MyClass, "qualifiedName")
# Retrieve the second provided object by its qualified name. 
myClassDifferentInstance = injector().get(MyClass, "differentName")

# Retrieve using find. This method returns an Optional and does not raise a ValueError. The missing dependency needs to be handled by the caller
myClass = injector().find(MyClass, "qualifiedName")
# or get the different instance
myClassDifferentInstance = injector().find(MyClass, "differentName")

# Using defaults. This method will try to resolve the object for MyNotCalledClass, and if no object is found, the builder function provider will be called and its return value returned and used by the container for the given class.
myNotCalledObject = injector().findOr(MyNotCalledClass, lambda: MyNotCalledClass())
```

#### Providing and retrieving variables
```python
from jstreams import injector

# Provide a single variable of type string
injector().provideVar(str, "myString", "myStringValue")

# Provide a single variable of type int
injector().provideVar(int, "myInt", 7)

# Provide multiple variables
injector().provideVariables([
    (str, "myString", "myStringValue"),
    (int, "myInt", 7),
])

# Retrieving a variable value using get. This method will raise a ValueError if no object was provided for the variable class and the given name
myString = injector().getVar(str, "myString")
# retrieving another value using find. This method returns an Optional and does not raise a ValueError. The missing value needs to be handled by the caller
myInt = injector().findVar(int, "myInt")
# retrieving a value with a default fallback if the value is not present
myString = injector().findVarOr(str, "myStrint", "defaultValue")
```
Qualified dependencies can also be injected by using the `component` decorator:
You can also use qualifiers with the `component` decorator:
```python
@component(Strategy.LAZY, ServiceInterface, "service")
class Service(ServiceInterface):
    def serviceMethod(self) -> None:
        pass

# Inject the dependency using the interface and a qualifier
injector().get(ServiceInterface, "service")
```

#### Attribute injection
Attributes can be injected by providing the dependency classes or variable definitions.
```python
@resoveDependencies({
    "myAttribute": AttributeClassName
})
class MyDependentComponent:
    myAttribute: AttributeClassName

# Provide the dependency at some point before actually instantiating a MyDependentComponent object
injector().provide(AttributeClassName, AttributeClassName())

myDepComp = MyDependentComponent() # The dependency gets injected when the constructor is called
myDepComp.myAttribute # Will have the value provided


@resolveVariables({
    "myVariable": StrVariable("myVar"), # Type agnostic syntax: Variable(str, "myVar")
})
class MyVariableNeededComponent:
    myVariable: str

injector().provideVar(str, "myVariable", "myVariableValue")

myVarNeededComp = MyVariableNeededComponent() # Value gets injected when the constructor is called
print(myVarNeededComp.myVariable) # Will print out 'myVariableValue'
```

#### Injected dependecies
Injected dependecies can be used when the needed dependencies are not present in the container ahead of time. For example, you can create a class that requires a dependency even if the dependency is not yet present, provide the dependency later on, then use it in the class you've initialized.

Injected dependencies are available through 3 classes:
- InjectedDependency
- OptionalInjectedDependency
- InjectedVariable

```python
injector().provide(str, "Test")
dep = InjectedDependency(str)
# you can either use the get() method, or use the callable functionality of the class
print(dep.get()) # will print out "Test"
# or the equivalent
print(dep()) # will also print out "Test"
```

### Threads

#### LoopingThread

```python
from jstreams import LoopingThread
from time import sleep

class MyThread(LoopingThread):
    def __init__(self) -> None:
        LoopingThread.__init__(self)
        self.count = 0
    
    def loop(self) -> None:
        # Write here the code that you want executed in a loop
        self.count += 1
        print(f"Executed {self.count} times")
        # This thread calls the loop implementation with no delay. Any sleeps need to be handled in the loop method
        sleep(1)
thread = MyThread()
thread.start()
sleep(5)
# Stop the thread from loopiong
thread.cancel()
```

#### CallbackLoopingThread
This looping thread doesn't require overriding the loop method. Instead, you provide a callback
```python
from jstreams import import CallbackLoopingThread
from time import sleep

def threadCallback() -> None:
    print("Callback executed")
    sleep(1)

thread = CallbackLoopingThread(threadCallback)
# will print "Callback executed" until the thread is cancelled
thread.start()

sleep(5)
# Stops the thread from looping
thread.cancel()
```
#### Timer
The Timer thread will start counting down to the given time period, and execute the provided callback once the time period has ellapsed. The timer can be cancelled before the period expires.
```python
from jstreams import import Timer
from time import sleep

timer = Timer(10, 1, lambda: print("Executed"))
timer.start()
# After 10 seconds "Executed" will be printed
```

```python
from jstreams import import Timer
from time import sleep

# The first parameter is the time period, the second is the cancelPollingInterval.
# The cancel polling interval is used by the timer to check if cancel was called on the timer.
timer = Timer(10, 1, lambda: print("Executed"))
timer.start()
sleep(5)
timer.cancel()
# Nothing will be printed, as this timer has been canceled before the period could ellapse
```

#### Interval
The interval executes a given callback at fixed intervals of time.
```python
from jstreams import Interval
from time import sleep
interval = Interval(2, lambda: print("Interval executed"))
interval.start()
# Will print "Interval executed" every 2 seconds
sleep(10)
# Stops the interval from executing
interval.cancel()
```

#### CountdownTimer
The countdown timer is similar in functionality with the Timer class, with the exception that this timer cannot be canceled. Once started, the callback will always execute after the period has ellapsed.
```python
from jstreams import CountdownTimer

CountdownTimer(5, lambda: print("Countdown executed")).start()
# Will always print "Countdown executed" after 5 seconds
```

#### JS-like usage
jstreams also provides some helper functions to simplify the usage of timers in the style of JavaScript.

```python
from jstreams import setTimer, setInterval, clear

# Starts a timer for 5 seconds
setTimer(5, lambda: print("Timer done"))

# Starts an interval at 5 seconds
setInterval(5, lambda: print("Interval executed"))

# Starts another timer for 10 seconds
timer = setTimer(10, lambda: print("Second timer done"))
# Wait 5 seconds
sleep(5)
# Clear the timer. The timer will not complete, since it was cancelled
clear(timer)

# Starts another interval at 2 seconds
interval = setInterval(2, lambda: print("Second interval executed"))
# Allow the interval to execute for 10 seconds
sleep(10)
# Cancel the interval. This interval will stop executing the callback
clear(interval)
```

## License

[MIT](https://choosealicense.com/licenses/mit/)