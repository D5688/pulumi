# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['ComponentArgs', 'Component']

@pulumi.input_type
class ComponentArgs:
    def __init__(__self__, *,
                 a: bool,
                 c: int,
                 e: str,
                 b: Optional[bool] = None,
                 bar: Optional['FooArgs'] = None,
                 baz: Optional[Sequence[pulumi.Input['FooArgs']]] = None,
                 baz_map: Optional[Mapping[str, pulumi.Input['FooArgs']]] = None,
                 d: Optional[int] = None,
                 f: Optional[str] = None,
                 foo: Optional[pulumi.Input['FooArgs']] = None):
        """
        The set of arguments for constructing a Component resource.
        """
        ComponentArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            a=a,
            c=c,
            e=e,
            b=b,
            bar=bar,
            baz=baz,
            baz_map=baz_map,
            d=d,
            f=f,
            foo=foo,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             a: Optional[bool] = None,
             c: Optional[int] = None,
             e: Optional[str] = None,
             b: Optional[bool] = None,
             bar: Optional['FooArgs'] = None,
             baz: Optional[Sequence[pulumi.Input['FooArgs']]] = None,
             baz_map: Optional[Mapping[str, pulumi.Input['FooArgs']]] = None,
             d: Optional[int] = None,
             f: Optional[str] = None,
             foo: Optional[pulumi.Input['FooArgs']] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if a is None:
            raise TypeError("Missing 'a' argument")
        if c is None:
            raise TypeError("Missing 'c' argument")
        if e is None:
            raise TypeError("Missing 'e' argument")
        if baz_map is None and 'bazMap' in kwargs:
            baz_map = kwargs['bazMap']

        _setter("a", a)
        _setter("c", c)
        _setter("e", e)
        if b is not None:
            _setter("b", b)
        if bar is not None:
            _setter("bar", bar)
        if baz is not None:
            _setter("baz", baz)
        if baz_map is not None:
            _setter("baz_map", baz_map)
        if d is not None:
            _setter("d", d)
        if f is not None:
            _setter("f", f)
        if foo is not None:
            _setter("foo", foo)

    @property
    @pulumi.getter
    def a(self) -> bool:
        return pulumi.get(self, "a")

    @a.setter
    def a(self, value: bool):
        pulumi.set(self, "a", value)

    @property
    @pulumi.getter
    def c(self) -> int:
        return pulumi.get(self, "c")

    @c.setter
    def c(self, value: int):
        pulumi.set(self, "c", value)

    @property
    @pulumi.getter
    def e(self) -> str:
        return pulumi.get(self, "e")

    @e.setter
    def e(self, value: str):
        pulumi.set(self, "e", value)

    @property
    @pulumi.getter
    def b(self) -> Optional[bool]:
        return pulumi.get(self, "b")

    @b.setter
    def b(self, value: Optional[bool]):
        pulumi.set(self, "b", value)

    @property
    @pulumi.getter
    def bar(self) -> Optional['FooArgs']:
        return pulumi.get(self, "bar")

    @bar.setter
    def bar(self, value: Optional['FooArgs']):
        pulumi.set(self, "bar", value)

    @property
    @pulumi.getter
    def baz(self) -> Optional[Sequence[pulumi.Input['FooArgs']]]:
        return pulumi.get(self, "baz")

    @baz.setter
    def baz(self, value: Optional[Sequence[pulumi.Input['FooArgs']]]):
        pulumi.set(self, "baz", value)

    @property
    @pulumi.getter(name="bazMap")
    def baz_map(self) -> Optional[Mapping[str, pulumi.Input['FooArgs']]]:
        return pulumi.get(self, "baz_map")

    @baz_map.setter
    def baz_map(self, value: Optional[Mapping[str, pulumi.Input['FooArgs']]]):
        pulumi.set(self, "baz_map", value)

    @property
    @pulumi.getter
    def d(self) -> Optional[int]:
        return pulumi.get(self, "d")

    @d.setter
    def d(self, value: Optional[int]):
        pulumi.set(self, "d", value)

    @property
    @pulumi.getter
    def f(self) -> Optional[str]:
        return pulumi.get(self, "f")

    @f.setter
    def f(self, value: Optional[str]):
        pulumi.set(self, "f", value)

    @property
    @pulumi.getter
    def foo(self) -> Optional[pulumi.Input['FooArgs']]:
        return pulumi.get(self, "foo")

    @foo.setter
    def foo(self, value: Optional[pulumi.Input['FooArgs']]):
        pulumi.set(self, "foo", value)


class Component(pulumi.ComponentResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 a: Optional[bool] = None,
                 b: Optional[bool] = None,
                 bar: Optional[pulumi.InputType['FooArgs']] = None,
                 baz: Optional[Sequence[pulumi.Input[pulumi.InputType['FooArgs']]]] = None,
                 baz_map: Optional[Mapping[str, pulumi.Input[pulumi.InputType['FooArgs']]]] = None,
                 c: Optional[int] = None,
                 d: Optional[int] = None,
                 e: Optional[str] = None,
                 f: Optional[str] = None,
                 foo: Optional[pulumi.Input[pulumi.InputType['FooArgs']]] = None,
                 __props__=None):
        """
        Create a Component resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ComponentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Component resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ComponentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ComponentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ComponentArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 a: Optional[bool] = None,
                 b: Optional[bool] = None,
                 bar: Optional[pulumi.InputType['FooArgs']] = None,
                 baz: Optional[Sequence[pulumi.Input[pulumi.InputType['FooArgs']]]] = None,
                 baz_map: Optional[Mapping[str, pulumi.Input[pulumi.InputType['FooArgs']]]] = None,
                 c: Optional[int] = None,
                 d: Optional[int] = None,
                 e: Optional[str] = None,
                 f: Optional[str] = None,
                 foo: Optional[pulumi.Input[pulumi.InputType['FooArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is not None:
            raise ValueError('ComponentResource classes do not support opts.id')
        else:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ComponentArgs.__new__(ComponentArgs)

            if a is None and not opts.urn:
                raise TypeError("Missing required property 'a'")
            __props__.__dict__["a"] = a
            __props__.__dict__["b"] = b
            bar = _utilities.configure(bar, FooArgs, False)
            __props__.__dict__["bar"] = bar
            __props__.__dict__["baz"] = baz
            __props__.__dict__["baz_map"] = baz_map
            if c is None and not opts.urn:
                raise TypeError("Missing required property 'c'")
            __props__.__dict__["c"] = c
            __props__.__dict__["d"] = d
            if e is None and not opts.urn:
                raise TypeError("Missing required property 'e'")
            __props__.__dict__["e"] = e
            __props__.__dict__["f"] = f
            foo = _utilities.configure(foo, FooArgs, True)
            __props__.__dict__["foo"] = foo
        super(Component, __self__).__init__(
            'example::Component',
            resource_name,
            __props__,
            opts,
            remote=True)

    @property
    @pulumi.getter
    def a(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "a")

    @property
    @pulumi.getter
    def b(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "b")

    @property
    @pulumi.getter
    def bar(self) -> pulumi.Output[Optional['outputs.Foo']]:
        return pulumi.get(self, "bar")

    @property
    @pulumi.getter
    def baz(self) -> pulumi.Output[Optional[Sequence['outputs.Foo']]]:
        return pulumi.get(self, "baz")

    @property
    @pulumi.getter
    def c(self) -> pulumi.Output[int]:
        return pulumi.get(self, "c")

    @property
    @pulumi.getter
    def d(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "d")

    @property
    @pulumi.getter
    def e(self) -> pulumi.Output[str]:
        return pulumi.get(self, "e")

    @property
    @pulumi.getter
    def f(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "f")

    @property
    @pulumi.getter
    def foo(self) -> pulumi.Output[Optional['outputs.Foo']]:
        return pulumi.get(self, "foo")

