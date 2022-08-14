from lib.dns_client import DNSClient
from random import sample
from datetime import datetime

class DNSClientManager:
    def __init__(self, client_configs):
        self.clients = []
        for config in client_configs:
            self.clients.append(self._init_client(config[0], config[1]))

    def set_domain_list(self, domain_list):
        self._domain_list = domain_list
    
    def query(self, domain):
        for client in self.clients:
            client.query(domain)
            self._print_log('{} {}'.format(client.dns_configs(), domain))

    def random_query(self, num_active_clients, num_targeted_domains):
        if self._domain_list is None:
            raise Exception('Domain list is empty')
        
        active_clients = sample(self.clients, num_active_clients)

        for client in active_clients:
            targeted_domains = sample(self._domain_list, num_targeted_domains)
    
            for domain in targeted_domains:
                client.query(domain)
                self._print_log('{} {}'.format(client.dns_configs(), domain))

    def _print_log(self, message):
        print('[{}] {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), message))

    def _init_client(self, transport_protocol, dns_server):
        return DNSClient(transport_protocol, dns_server)