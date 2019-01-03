favorite_places = {
    'Alice': ['qwerq', 'qwertt', 'rweywfgds'],
    'Steven': ['wertadf', 'ewtygw'],
    'Joy': ['qwretggqwrg', 'khfggdsfg', 'imtfghndf']
    }

for name, places in favorite_places.items():
    print("\n" + name.title() + " likes the following places:")
    for place in places:
        print("- " + place.title())