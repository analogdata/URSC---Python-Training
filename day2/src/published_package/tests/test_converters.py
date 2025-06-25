from stringcase_utils.converters import to_snake_case, to_camel_case

def test_to_snake_case():
    assert to_snake_case("CamelCase") == "camel_case"

def test_to_camel_case():
    assert to_camel_case("snake_case") == "snakeCase"