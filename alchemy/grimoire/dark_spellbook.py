from .dark_validator import validate_ingredients_dark


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: list[str]) -> str:
    if validate_ingredients_dark(ingredients) == "VALID":
        return ("Spell recorded")
    else:
        return ("Spell rejected")
