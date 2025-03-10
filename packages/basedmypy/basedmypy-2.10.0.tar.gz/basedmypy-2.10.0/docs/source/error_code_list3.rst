.. _error-codes-based:

Error codes unique to basedmypy
===============================

.. _code-decorated-any:

Check that a decorated function isn't dynamic [decorated-any]
-------------------------------------------------------------

From :confval:`disallow_any_decorated`

.. _code-any:

Ban any expression that contains ``Any`` [any]
----------------------------------------------

From :confval:`disallow_any_expr`

.. _code-subclass-any:

Don't subclass ``Any`` [subclass-any]
----------------------------------------

From :confval:`disallow_subclassing_any`

.. _code-no-untyped-usage:

Don't use anything that contains ``Any`` [no-untyped-usage]
-----------------------------------------------------------

From :confval:`no_untyped_usage`

.. _code-unsafe-variance:

Check that type variables are used in accordance with their variance [unsafe-variance]
--------------------------------------------------------------------------------------

.. code-block:: python

    inT = TypeVar("inT", contravariant=True)
    outT = TypeVar("outT", covariant=True)

    class X(Generic[inT, outT]):
        def foo(self,
            t: outT  # This usage of this covariant type variable is unsafe as a return type.  [unsafe-variance]
        ) -> inT:  # This usage of this contravariant type variable is unsafe as a return type.  [unsafe-variance]
            pass

.. _code-typeguard-limitation:

Unsupported usages of typeguards [typeguard-limitation]
-------------------------------------------------------

Mypy does not yet support typeguarding a star argument:

.. code-block:: python

    def guard(x: object) -> x is int: ...

    x: object
    xs = x,
    assert guard(*xs)  # Type guard on star argument is not yet supported  [typeguard-limitation]
    reveal_type(x)  # object

.. _code-typeguard-subtype:

Check that typeguard definitions are valid [typeguard-subtype]
--------------------------------------------------------------

.. code-block:: python

    def guard(x: str) -> x is int:  # A type-guard's type must be assignable to its parameter's type. (guard has type "int", parameter has type "str")  [typeguard-subtype]
        ...

.. _code-regex:

Check for regex issues [regex]
------------------------------

.. code-block:: python

    re.compile("(foo).*)")  # error: unbalanced parenthesis at position 7  [regex]
    m = re.match("(?P<name>\w+)", s)
    assert m
    m.group("nane")  # error: no such group: 'nane'  [regex]

.. _code-helpful-string:

Check that strings are useful [helpful-string]
----------------------------------------------

Catching unintentional values in f-strings:

.. code-block:: python

    def make_id(i: int | None) -> str:
        return f"id-{i}"  # The string for "None" isn't helpful for a user-facing message  [helpful-string]

.. _code-bad-cast:

Check that casts are valid [bad-cast]
-------------------------------------

Casting between two non-overlapping types is often a mistake:

.. code-block:: python

    a: int
    cast(str, a)  # Conversion of type "int" to type "str" may be a mistake because neither type sufficiently overlaps with the other. If this was intentional, convert the expression to "object" first.  [bad-cast]

.. _code-callable-functiontype:

Check for bad usages of callabes and function types [callable-functiontype]
---------------------------------------------------------------------------

Because functions can create methods when accessed in certain ways,
basedmypy has checks regarding their usages:

.. code-block:: python

    class A:
        a: "(int) -> object" = lambda i: i + 1  # Assigning a "FunctionType" on the class will become a "MethodType"  [callable-functiontype]

    A().a(1)  # runtime TypeError: <lambda>() takes 1 positional argument but 2 were given

.. _code-possible-function:

Check that callables are valid [possible-function]
--------------------------------------------------

Because a function can create methods when accessed in certain ways,
basedmypy has lint rules regarding their validity as ``Callable``\s:

.. code-block:: python

    c: "(int) -> object" = lambda i: i + 1
    class A:
        a: "(int) -> object" = c  # This "CallableType" could be a "FunctionType", which when assigned via the class, would produce a "MethodType"  [possible-function]

    A().a(1)  # runtime TypeError: <lambda>() takes 1 positional argument but 2 were given


.. _code-unhandled-scenario:

A scenario isn't being handled correctly by basedmypy itself
------------------------------------------------------------

Sometimes, the implementation of a the type system is not completely sound
and basedmypy needs to be updated.


.. _code-type-check-only:

Support typing.type_check_only [type-check-only]
------------------------------------------------

Something is being used in a runtime position that is not actually
accessible or available at runtime.

.. _code-reveal:

# deprecated

.. _code-no-any-decorated:

.. _code-no-any-explicit:

.. _code-no-any-expr:

.. _code-no-subclass-any:
