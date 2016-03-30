import os

# >> - query /etc/hosts/ for value (host)
sampleDNS = "localyuigkhost"

def parse_hosts(query):
    hosts = open("test.txt", "r")
    host_dict = {}

    for line in hosts:
        if line[0] != "#":
            host = line.split()
            if host:
                k, v = host[-1], host[0]
                if k not in host_dict:
                    host_dict[k] = []
                values = host_dict[k]
                values.append(v)

    if query in host_dict:
        return host_dict[query]
    else: return None

ips = parse_hosts(sampleDNS)

print(parse_hosts("127.0.0.1"))
