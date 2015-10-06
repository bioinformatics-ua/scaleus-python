__author__ = 'Pedro Sernadela sernadela@ua.pt'

import requests
import json

class Scaleus:
    def __init__(self, host):
        self.host = host

    def get_datasets(self):
        content = requests.get(self.host + 'dataset/')
        return json.loads(content.text)

    def add_dataset(self, name):
        content = requests.post(self.host + 'dataset/' + name)
        content.raise_for_status()

    def remove_dataset(self, name):
        content = requests.delete(self.host + 'dataset/' + name)
        content.raise_for_status()

    def add_triple(self, dataset, sub, prop, obj):
        data = {'s': sub, 'p': prop, 'o': obj}
        content = requests.post(self.host + 'store/' + dataset, json=data)
        content.raise_for_status()

    def remove_triple(self, dataset, sub, prop, obj):
        data = {'s': sub, 'p': prop, 'o': obj}
        content = requests.delete(self.host + 'store/' + dataset, json=data)
        content.raise_for_status()

    def add_namespace(self, dataset, prefix, namespace):
        data = {'prefix': prefix, 'namespace': namespace}
        content = requests.post(self.host + 'namespaces/' + dataset, json=data)
        content.raise_for_status()

    def remove_namespace(self, dataset, prefix):
        content = requests.delete(self.host + 'namespaces/' + dataset + '/' + prefix)
        content.raise_for_status()

    def get_namespaces(self, dataset):
        content = requests.get(self.host + 'namespaces/' + dataset)
        return json.loads(content.text)

    def sparql(self, dataset, query, inference, rules, format):
        payload = {'query': query, 'inference': inference, 'rules': rules, 'format': format}
        content = requests.get(self.host + 'sparqler/' + dataset + '/sparql', params=payload)
        return content.text
