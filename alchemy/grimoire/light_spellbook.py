from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "wind"]


def light_spell_record(spell_name: str, ingredients: list[str]) -> str:
    if validate_ingredients(ingredients) == "VALID":
        return (f"Spell recorded: {set(ingredients)} - VALID")
    else:
        return ("Spell rejected")
