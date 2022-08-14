import argparse
import time
import random
import lib.dns_client_manager as client_manager
import lib.config_parser as config_parser

parser = argparse.ArgumentParser(description='Send a bunch of noisy DNS requests to targeted DNS servers')

parser.add_argument('--targets', dest='targets', action='store', type=str,
                    required=True, help='path to file containing list of servers to be targeted')
parser.add_argument('--domains', dest='domains', action='store', type=str,
                    required=True, help='path to file containing list of domains to be queried to the target DNS servers')
parser.add_argument('--ntargets', dest='ntargets', action='store', type=int,
                    required=False, default=1, help='number of target servers to be targeted per iteration')
parser.add_argument('--ndomains', dest='ndomains', action='store', type=int,
                    required=False, default=1, help='number of domains to be queried per iteration')

args = parser.parse_args()

client_configs = config_parser.load_client_configs(args.targets)
domain_list = config_parser.load_domain_list(args.domains)

dq = client_manager.DNSClientManager(client_configs)
dq.set_domain_list(domain_list)

while True:
    try:
        dq.random_query(args.ntargets, args.ndomains)
        delay_variant = random.randrange(-30, 31)
        time.sleep(60 + delay_variant)
    except KeyboardInterrupt:
        print('Exiting...')
        exit()
