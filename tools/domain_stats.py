#!/usr/bin/env python3

import sys
import os
import email
import traceback
from email.utils import parseaddr
from email.header import decode_header

def _recode_header(raw_header):
    return ''.join([
        t[0].decode(t[1] or 'ASCII') if isinstance(t[0], bytes) else t[0]
        for t in decode_header(raw_header)
    ])

def try_parse(filename):
    with open(filename, 'r', encoding='iso-8859-1') as i:
        msg = email.message_from_file(i)
        
        raw_from_header = msg.get('From', None)
        hdr_from_decoded = _recode_header(raw_from_header)

        hdr_from_parsed_real, hdr_from_parsed_addr = parseaddr(hdr_from_decoded)
        hdr_x_spam_flag = msg.get('X-Spam-Flag', None)
        hdr_x_spam_status = msg.get('X-Spam-Status', None)
        
        if hdr_from_parsed_addr:
            domain = hdr_from_parsed_addr[hdr_from_parsed_addr.index('@') + 1:]
            spam = (hdr_x_spam_flag is not None and hdr_x_spam_flag.upper() == 'YES') or (hdr_x_spam_status  is not None and hdr_x_spam_status.lower().startswith('yes'))
            
            return domain, spam

        print(f"Cannot inspect: {hdr_from_parsed_addr}", file=sys.stderr)
        return None
        
def scan(*dirs):
    
    stats = {}
    
    for dir in dirs:
        for root, dirs, files in os.walk(dir):
            
            if 'courierimapkeywords' in root or 'maildirfolder' in root:
                continue
            
            for f in files:
                if 'dovecot' in f or 'courier' in f or 'maildirfolder' in f or 'subscriptions' in f:
                    continue
    
                fullpath = os.path.join(root, f)
                try:
                    result = try_parse(fullpath) # tuple of domain, spam
                    if result is None:
                        continue
                    if result in stats:
                        stats[result] += 1
                    else:
                        stats[result] = 1
                    
                except Exception as e:
                    print(f"Failed to inspect {fullpath}: {e}")
                    print(traceback.format_exc())

    print("Result:")
    for k, v in stats.items():
        domain, spam = k
        print(f"{domain.rjust(40)}\t{spam}\t{v}")

if __name__ == "__main__":
    scan(*sys.argv[1:])
