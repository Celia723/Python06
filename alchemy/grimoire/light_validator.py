
def validate_ingredients(ingredients: list[str]) -> str:
    from .light_spellbook import light_spell_allowed_ingredients

    valid_elements = light_spell_allowed_ingredients()
    for ingredient in ingredients:
        if ingredient not in valid_elements:
            return "INVALID"
    return "VALID"
