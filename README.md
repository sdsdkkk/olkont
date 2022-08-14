# Olkont: DNS Query Noise Maker

Olkont is a tool to send DNS queries to a bunch of targeted DNS servers simply to add noise to the servers' traffic and logs.

Example usage:

```
$ python3 olkont.py --targets examples/target_servers.txt --domains examples/queried_domains.txt --ntargets 2 --ndomains 1
```

The `--targets` argument should contain a path to a text file listing the DNS servers to be queried. The file must follow the following formatting.

```
[server 1 transport protocol] [server 1 address]
[server 2 transport protocol] [server 2 address]
...
[server n transport protocol] [server n address]
```

If there are more than one identical entries of the same transport protocol and server address pair, multiple DNS clients will be made to query to the target DNS server. The supported protocol values are TCP, UDP, TLS, and HTTPS.

The `--domains` argument should contain a path to a text file listing the domains to be queried when making the noise. The text file must be a line-separated list of queryable domain names.

The `--ntargets` argument is optional (default value is 1), this argument defines the number of DNS clients to be randomly picked on each cycle to perform DNS queries to the targeted DNS servers associated with the clients.

The `--ndomains` argument is optional (default value is 1), this argument defines the number of domains to be randomly picked to be queried to the targeted DNS servers on each cycle.

# Warning

This script is made for educational purpose, using this on a DNS server owned by someone else might cause disruption to their business/tech operations. **Do not** target systems other than your own without permission.
