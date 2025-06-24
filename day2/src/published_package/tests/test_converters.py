from stringcase_utils import to_snake_case, to_camel_case

def test_conversion():
    assert to_snake_case("CamelCase") == "camel_case"
    assert to_camel_case("snake_case") == "snakeCase"
