data = (
    ("Toyota", "Avensis"),
    ("Toyota", "Auris"),
    ("Toyota", "Corolla"),
    ("Audi", "A3"),
)

cars = {}
for brand, model in data:
    cars.setdefault(brand, [])
    cars[brand].append(model)

for model in cars.get("Toyota", []):
    print(model)

