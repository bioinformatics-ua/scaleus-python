__author__ = 'Pedro Sernadela sernadela@ua.pt'

import scaleus


s = scaleus.Scaleus('http://localhost/api/v1/')

## Datasets
print '\nDatasets:\n'

dataset = 'tester'

s.add_dataset(dataset)
print s.get_datasets()
s.remove_dataset(dataset)
print s.get_datasets()

## Triples
print '\nTriples:\n'

dataset = 'default'
sub = 'http://bioinformatics.ua.pt/'
pred = 'http://purl.org/dc/elements/1.1/title'
obj = 'Bioinformatics UA'

s.add_triple(dataset, sub, pred, obj)
s.remove_triple(dataset, sub, pred, obj)

## Namespaces
print '\nNamespaces:\n'

dataset = 'default'
prefix = 'bio'
namespace = 'http://bioinformatics.ua.pt/'

print s.get_namespaces(dataset)
s.add_namespace(dataset, prefix, namespace)
print s.get_namespaces(dataset)
s.remove_namespace(dataset, prefix)
print s.get_namespaces(dataset)

## SPARQL
print '\nSPARQL:\n'

dataset = 'default'
query = 'SELECT * { ?s ?p ?o } LIMIT 100'
inference = 'true'
rules = '[rdfs6:  (?a ?p ?b), (?p rdfs:subPropertyOf ?q) -> (?a ?q ?b)]' + '[rdfs9:  (?x rdfs:subClassOf ?y), (?a rdf:type ?x) -> (?a rdf:type ?y)]'
format = 'json'
print s.sparql(dataset, query, inference, rules, format)
