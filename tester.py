__author__ = 'Pedro Sernadela sernadela@ua.pt'

import scaleus


s = scaleus.Scaleus('http://localhost/api/v1/')

## Datasets
print '\nDatasets:\n'

s.add_dataset('tester')
print s.get_datasets()
s.remove_dataset('tester')
print s.get_datasets()

## Triples
print '\nTriples:\n'

s.add_triple('default', 'http://bioinformatics.ua.pt/', 'http://purl.org/dc/elements/1.1/title', 'Bioinformatics UA')
s.remove_triple('default', 'http://bioinformatics.ua.pt/', 'http://purl.org/dc/elements/1.1/title', 'Bioinformatics UA')

## Namespaces
print '\nNamespaces:\n'

print s.get_namespaces('default')
s.add_namespace('default', 'bio', 'http://bioinformatics.ua.pt/')
print s.get_namespaces('default')
s.remove_namespace('default', 'bio')
print s.get_namespaces('default')

## SPARQL
print '\nSPARQL:\n'

query = 'SELECT * { ?s ?p ?o } LIMIT 100'
inference = 'true'
rules = '[rdfs6:  (?a ?p ?b), (?p rdfs:subPropertyOf ?q) -> (?a ?q ?b)]' + '[rdfs9:  (?x rdfs:subClassOf ?y), (?a rdf:type ?x) -> (?a rdf:type ?y)]'
format = 'json'
print s.sparql('default', query, inference, rules, format)
