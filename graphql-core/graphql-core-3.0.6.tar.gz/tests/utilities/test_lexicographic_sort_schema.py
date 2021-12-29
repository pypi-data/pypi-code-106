from graphql.pyutils import dedent
from graphql.utilities import build_schema, print_schema, lexicographic_sort_schema


def sort_sdl(sdl):
    schema = build_schema(sdl)
    return print_schema(lexicographic_sort_schema(schema))


def describe_lexicographic_sort_schema():
    def sort_fields():
        sorted_sdl = sort_sdl(
            """
            input Bar {
              barB: String!
              barA: String
              barC: [String]
            }

            interface FooInterface {
              fooB: String!
              fooA: String
              fooC: [String]
            }

            type FooType implements FooInterface {
              fooC: [String]
              fooA: String
              fooB: String!
            }

            type Query {
              dummy(arg: Bar): FooType
            }
            """
        )

        assert sorted_sdl == dedent(
            """
            input Bar {
              barA: String
              barB: String!
              barC: [String]
            }

            interface FooInterface {
              fooA: String
              fooB: String!
              fooC: [String]
            }

            type FooType implements FooInterface {
              fooA: String
              fooB: String!
              fooC: [String]
            }

            type Query {
              dummy(arg: Bar): FooType
            }
            """
        )

    def sort_implemented_interfaces():
        sorted_sdl = sort_sdl(
            """
            interface FooA {
              dummy: String
            }

            interface FooB {
              dummy: String
            }

            interface FooC {
              dummy: String
            }

            type Query implements FooB & FooA & FooC {
              dummy: String
            }
            """
        )

        assert sorted_sdl == dedent(
            """
            interface FooA {
              dummy: String
            }

            interface FooB {
              dummy: String
            }

            interface FooC {
              dummy: String
            }

            type Query implements FooA & FooB & FooC {
              dummy: String
            }
            """
        )

    def sort_types_in_union():
        sorted_sdl = sort_sdl(
            """
            type FooA {
              dummy: String
            }

            type FooB {
              dummy: String
            }

            type FooC {
              dummy: String
            }

            union FooUnion = FooB | FooA | FooC

            type Query {
              dummy: FooUnion
            }
            """
        )

        assert sorted_sdl == dedent(
            """
            type FooA {
              dummy: String
            }

            type FooB {
              dummy: String
            }

            type FooC {
              dummy: String
            }

            union FooUnion = FooA | FooB | FooC

            type Query {
              dummy: FooUnion
            }
            """
        )

    def sort_enum_types():
        sorted_sdl = sort_sdl(
            """
            enum Foo {
              B
              C
              A
            }

            type Query {
              dummy: Foo
            }
            """
        )

        assert sorted_sdl == dedent(
            """
            enum Foo {
              A
              B
              C
            }

            type Query {
              dummy: Foo
            }
            """
        )

    def sort_field_arguments():
        sorted_sdl = sort_sdl(
            """
            type Query {
              dummy(argB: Int!, argA: String, argC: [Float]): ID
            }
            """
        )

        assert sorted_sdl == dedent(
            """
            type Query {
              dummy(argA: String, argB: Int!, argC: [Float]): ID
            }
            """
        )

    def sort_types():
        sorted_sdl = sort_sdl(
            """
            type Query {
              dummy(arg1: FooF, arg2: FooA, arg3: FooG): FooD
            }

            type FooC implements FooE {
              dummy: String
            }

            enum FooG {
              enumValue
            }

            scalar FooA

            input FooF {
              dummy: String
            }

            union FooD = FooC | FooB

            interface FooE {
              dummy: String
            }

            type FooB {
              dummy: String
            }
            """
        )

        assert sorted_sdl == dedent(
            """
            scalar FooA

            type FooB {
              dummy: String
            }

            type FooC implements FooE {
              dummy: String
            }

            union FooD = FooB | FooC

            interface FooE {
              dummy: String
            }

            input FooF {
              dummy: String
            }

            enum FooG {
              enumValue
            }

            type Query {
              dummy(arg1: FooF, arg2: FooA, arg3: FooG): FooD
            }
            """
        )

    def sort_directive_arguments():
        sorted_sdl = sort_sdl(
            """
            directive @test(argC: Float, argA: String, argB: Int) on FIELD

            type Query {
              dummy: String
            }
            """
        )

        assert sorted_sdl == dedent(
            """
            directive @test(argA: String, argB: Int, argC: Float) on FIELD

            type Query {
              dummy: String
            }
            """
        )

    def sort_directive_locations():
        sorted_sdl = sort_sdl(
            """
            directive @test(argC: Float, argA: String, argB: Int) on UNION | FIELD | ENUM

            type Query {
              dummy: String
            }
            """  # noqa: E501
        )

        assert sorted_sdl == dedent(
            """
            directive @test(argA: String, argB: Int, argC: Float) on ENUM | FIELD | UNION

            type Query {
              dummy: String
            }
            """  # noqa: E501
        )

    def sort_directives():
        sorted_sdl = sort_sdl(
            """
            directive @fooC on FIELD

            directive @fooB on UNION

            directive @fooA on ENUM

            type Query {
              dummy: String
            }
            """
        )

        assert sorted_sdl == dedent(
            """
            directive @fooA on ENUM

            directive @fooB on UNION

            directive @fooC on FIELD

            type Query {
              dummy: String
            }
            """
        )

    def sort_recursive_types():
        sorted_sdl = sort_sdl(
            """
            interface FooC {
              fooB: FooB
              fooA: FooA
              fooC: FooC
            }

            type FooB implements FooC {
              fooB: FooB
              fooA: FooA
            }

            type FooA implements FooC {
              fooB: FooB
              fooA: FooA
            }

            type Query {
              fooC: FooC
              fooB: FooB
              fooA: FooA
            }
            """
        )

        assert sorted_sdl == dedent(
            """
            type FooA implements FooC {
              fooA: FooA
              fooB: FooB
            }

            type FooB implements FooC {
              fooA: FooA
              fooB: FooB
            }

            interface FooC {
              fooA: FooA
              fooB: FooB
              fooC: FooC
            }

            type Query {
              fooA: FooA
              fooB: FooB
              fooC: FooC
            }
            """
        )
