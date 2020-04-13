# fishysites

List of fishy sites for Pihole blacklists. Mainly includes Czech domains.

## motivation

When searching for some shoes on the internet I arrived to a site that was evidently fishy - no contact,
funny domain registration metadata, too good prices to be true. I searched for the domain name and found
the list of potentionally fraudulent sites on https://www.urbag.cz/podvodne-eshopy/ so decided to compile
them and use for my Pihole that is already used for blocking advertisements.

## how to use

```
echo "https://raw.githubusercontent.com/vladak/fishysites/master/fishy_domains.txt" | \
    sudo tee -a /etc/pihole/adlists.list
sudo pihole -g
```

## how to refresh

```
curl -s -o fishy.html https://www.urbag.cz/podvodne-eshopy/
pip3 install -r requirements.txt
./parse.py > fishy_domains.txt
```
