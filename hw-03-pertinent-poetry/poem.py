from calais import Calais

API_KEY = "s5mba8qn5qb4vjmc663qxn8m"
calais = Calais(API_KEY, submitter="jannae")

result = calais.analyze_file("sotu2012.txt")

result.print_summary()

def print_entities(self):
    if not hasattr(self, "entities"):
        return None
    for item in self.entities:
        print "%s: %s (%.2f)" % (item['_type'], item['name'], item['relevance'])
