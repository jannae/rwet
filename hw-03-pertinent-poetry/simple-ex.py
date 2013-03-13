from calais import Calais

API_KEY = "s5mba8qn5qb4vjmc663qxn8m"
calais = Calais(API_KEY, submitter="jannae")

result = calais.analyze("George Bush was the President of the United States of America until 2009.  Barack Obama is the new President of the United States now.")

result.print_summary()