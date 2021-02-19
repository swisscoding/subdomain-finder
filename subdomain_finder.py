#!/usr/local/bin/python3
# Made by @swisscoding on Instagram

from colored import stylize, fg
import requests

# decoration
print(stylize("\n---- | Subdomain finder | ----\n", fg("red")))

# class
class SubdomainFinder:
    def __init__(self, domain, subdomains):
        self.domain = domain
        self.subdomains = subdomains

    # output magic method
    def __repr__(self):
        subdomains_list = self.find_all(self.domain, self.subdomains)
        subdomains_string = stylize(", ".join(subdomains_list), fg("red"))
        return f"\nValid subdomains:\n{subdomains_string}\n\nExample: \
{subdomains_list[0]}.{self.domain}\n"

    # methods
    def find_all(self, domain, subdomains):
        # a list of discovered subdomains
        valid_subdomains = []

        for subdomain in subdomains:
            # url
            url = f"http://{subdomain}.{domain}"
            try:
                requests.get(url)
                # subdomain found
                valid_subdomains.append(subdomain)
            except:
                pass

        return valid_subdomains

# main execution
if __name__ == "__main__":
    # user interaction
    domain = input("Domain: ")
    subdomains = input("All subdomains to try: ").split(", ")

    print(SubdomainFinder(domain, subdomains))
