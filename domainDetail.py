import whois


def whoisDomain(domain):
    w = whois.whois(domain)
    print(w)

if __name__ == '__main__':
    target = 'github.com'
    whoisDomain(target)
