#!/usr/bin/env python3
import codecs
from dataclasses import dataclass

tlds = []

with codecs.open('public_suffix_list.dat.txt', encoding='utf8') as suffix_file:
    for raw_line in suffix_file:
        line = raw_line.strip()
        
        if not line or line.startswith('//'):
            continue
        
        if line not in tlds:
            tlds.append(line)
        
tlds = sorted(tlds, key=lambda x: x.count('.'), reverse=True)


grouped_stats = {}


@dataclass
class DomainStats:
    domain: str
    num_hams: int
    num_spams: int

    @property
    def percent_spam(self):
        return (self.num_spams * 100) / (self.num_hams + self.num_spams)


with open('domain_stats.txt', 'r') as f:
    for line in f:
        domain, is_spam_str, count = line.strip().split('\t')
        is_spam = is_spam_str == 'True'
        
        domain_chunks = domain.lower().split('.')
        
        for i in range(len(domain_chunks)):
            partial_domain = '.'.join(domain_chunks[i:])


            if partial_domain in tlds:

                if partial_domain in grouped_stats:
                    if is_spam:
                        grouped_stats[partial_domain].num_spams += int(count)
                    else:
                        grouped_stats[partial_domain].num_hams += int(count)
                else:
                    grouped_stats[partial_domain] = DomainStats(domain=partial_domain,
                                                                num_hams=int(count) if not is_spam else 0,
                                                                num_spams=int(count) if is_spam else 0)

for domain_stat in sorted(grouped_stats.values(), key=lambda ds: (ds.percent_spam, ds.num_spams), reverse=True):
    
    if domain_stat.num_spams > 20 and (domain_stat.percent_spam > 90 or (domain_stat.num_hams < domain_stat.num_spams)):
        print(f"{domain_stat.domain.ljust(20)}\t{str(domain_stat.num_hams).ljust(8)}{str(domain_stat.num_spams).ljust(8)}{domain_stat.percent_spam}")
