

if __name__ == "__main__":
    print("=== Kaboom 1 ===")
    print("Secretly accessing dark_spellbook.py directly...")
    from alchemy.grimoire import dark_spellbook

    ingredients = ["bats", "frogs", "arsenic"]
    # Intentamos registrar el hechizo oscuro
    res = dark_spellbook.dark_spell_record("Avada Kedavra", ingredients)
    print(res)
