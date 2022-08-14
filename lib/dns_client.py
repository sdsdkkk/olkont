import dns.message
import dns.name
import dns.query

VALID_PROTOCOLS = ['tcp', 'udp', 'tls', 'https']

class DNSClient:
    def __init__(self, transport_protocol, dns_server):
        if transport_protocol == 'tcp':
            self._query = dns.query.tcp
        elif transport_protocol == 'udp':
            self._query = dns.query.udp
        elif transport_protocol == 'tls':
            self._query = dns.query.tls
        elif transport_protocol == 'https':
            self._query = dns.query.https
        else:
            raise Exception('Invalid transport protocol, list of valid protocols: {}'.format(VALID_PROTOCOLS))
        
        self._transport_protocol = transport_protocol
        self._dns_server = dns_server

    def dns_configs(self):
        return '{} {}'.format(self._transport_protocol, self._dns_server)
    
    def query(self, target_domain):
        qname = dns.name.from_text(target_domain)
        q = dns.message.make_query(qname, dns.rdatatype.A)
        response = self._query(q, self._dns_server)
        return response
