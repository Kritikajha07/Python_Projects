# Modifying Global Scope

helpers = 1


def increase_enemies():
    global helpers

    enemies = helpers + 1
    print(f"enemies inside house: {enemies}")


increase_enemies()
print(f"enemies outside house: {helpers}")


