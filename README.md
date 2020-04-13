# fishysites

List of fishy sites for Pihole blacklists

## motivation

When searching for some shoes on the internet I arrived to a site that was evidently fishy - no contact, 
funny domain registration metadata, too good prices to be true. I searched for the domain name and found
the list of potentionally fraudulent sites on https://www.urbag.cz/podvodne-eshopy/ so decided to compile
them and use for my Pihole that is already used for blocking advertisements.

## how to use

```
echo "XXX" >> /etc/pihole/adlists.list
sudo pihole -g
```
