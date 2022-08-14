def load_client_configs(filename):
    file = open(filename, 'r')
    config_lines = file.read().splitlines()
    file.close()

    client_entries = []
    
    for line in config_lines:
        client_entries.append(line.split())
    
    return client_entries

def load_domain_list(filename):
    file = open(filename, 'r')
    list_entries = file.read().splitlines()
    file.close()

    return list_entries