from alchemy.grimoire import light_spellbook

if __name__ == "__main__":
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    
    ingredients = ("earth", "wind", "fire")

    res = light_spellbook.light_spell_record("Fantasy", list(ingredients))
    print(f"Testing record light spell: {res}")