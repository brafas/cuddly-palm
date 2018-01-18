catNames = []
while True:
    print("Enter the name of cat " + str(len(catNames) +1) + " (Or enter nothing to stop.):")
    name = input()
    if name == '':
        break
    catNames = catNames + [name]
print("The Cat Names are:")
for name in catNames:
    print(' ' + name)

sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 22 -j DNAT --to-destination 192.168.0.111
