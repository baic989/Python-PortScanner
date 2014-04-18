import socket, sys, time

def skener(*args):
    host, od, do = args
    a = 0
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    do += 1
    try:
        ip = socket.gethostbyname(host)
    except socket.gaierror:
        print "You entered the adress in wrong format. Quitting..."
        sys.exit()
    print "\nScanning started: %s/%s" % (host, ip)
    print "On ports from %d to %d" % (od, do-1)
    print "Please wait...\n"
    for i in range(od, do):
        s.settimeout(0.5)
        t1 = time.time()
        spojen = s.connect_ex((ip, i))
        if spojen == 0:
            print "Port %d is: OPEN" % i
            a += 1
        else:
            pass
        s.close()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if a == 0:
        print "Sorry, no ports are open in range from %d to %d" % (od, do-1)
    t2 = time.time()
    trajanje_skeniranja = t2 - t1
    print "\nScanning finished in %f..." % trajanje_skeniranja
    print "Do you want to start again?"
    ponoviti = raw_input("Enter 'yes' to start again, or anything else to quit.\n> ")
    if "yes" in ponoviti:
        prompt()
    else:
        print "Quitting... Thank you for using Python Port Scanner."
        print "-" * 70
        sys.exit()

def start():
    print "-" * 70
    print "Today is:", time.asctime(time.localtime(time.time()))
    print "-" * 70
    print "\n\t\tWELCOME TO PYTHON PORT SCANNER"
    prompt()

def prompt():
    host = raw_input("\nPlease enter an adress to scan. Example: www.host.com\n> ")
    od = None
    do = None
    while od == None:
        try:
            od = int(raw_input("\nPort to start with:\n> "))
        except:
            print "A port is a number! Try again..."
    while do == None:
        try:
            do = int(raw_input("\nPort to finish with:\n> "))
        except:
            print "A port is a number! Try again..."
    return skener(host, od, do)

start()
