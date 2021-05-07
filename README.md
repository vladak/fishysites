# fishysites

List of fishy sites for [Pihole](https://pi-hole.net/) blacklists. Includes mainly Czech domains suspected of performing
phishing attacks and being fraudulent.

## Motivation

When searching for some shoes on the internet I arrived to a site that was evidently fishy - no contact,
funny domain registration metadata, too good prices to be true. I searched for the domain name and found
the list of potentionally fraudulent sites on https://www.urbag.cz/podvodne-eshopy/ so decided to compile
them and use for my Pihole that is already used for blocking advertisements.

## How to use

To delete all custom lists from the gravity database:

```
sudo sqlite3 /etc/pihole/gravity.db "DELETE FROM adlist"
```

Insert the custom list:

```
sudo sqlite3 /etc/pihole/gravity.db \
    "INSERT INTO adlist (Address) VALUES ('https://raw.githubusercontent.com/vladak/fishysites/master/fishy_domains.txt');" 
```

refresh:
    
```
sudo pihole -g
```

## How to refresh the list of domains

```
curl -s -o fishy.html https://www.urbag.cz/podvodne-eshopy/
pip3 install -r requirements.txt
./parse.py > fishy_domains.txt
```
