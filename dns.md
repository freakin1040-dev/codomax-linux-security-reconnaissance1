# DNS and Domain Information Gathering

DNS translates domain names into resource records.

| Record | Purpose |
|---|---|
| A | Maps a name to an IPv4 address |
| AAAA | Maps a name to an IPv6 address |
| MX | Lists mail-exchange servers |
| NS | Lists authoritative name servers |
| TXT | Stores text data, often verification or email policy |
| CNAME | Alias to another canonical name |

Commands on Ubuntu:
```bash
nslookup example.com
```
If `dig` is installed:
```bash
dig example.com A
dig example.com MX
dig example.com NS
```
Install DNS utilities on Ubuntu if needed:
```bash
sudo apt update
sudo apt install dnsutils
```

Use `example.com` for basic command practice, or a domain you own/are permitted to research. DNS responses can change and depend on resolver/cache settings. Record the date and actual output; do not copy illustrative IPs as findings.

WHOIS/RDAP services can expose registrar, creation/expiry, and name-server information, but privacy redaction and registry policies may limit details.
