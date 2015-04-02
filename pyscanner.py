import socket, sys, time

def portScanner(*args):
    host, portFrom, portTo = args
    openPortsCounter = 0
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    portTo += 1
    try:
        ip = socket.gethostbyname(host)
    except socket.gaierror:
        print "You entered the adress in wrong format. Quitting..."
        sys.exit()
    print "\nScanning started: %s/%s" % (host, ip)
    print "On ports from %d to %d" % (portFrom, portTo-1)
    print "Please wait...\n"
    for i in range(portFrom, portTo):
        s.settimeout(0.5)
        t1 = time.time()
        connected = s.connect_ex((ip, i))
        if connected == 0:
            print "Port %d is: OPEN" % i
            openPortsCounter += 1
        else:
            pass
        s.close()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if openPortsCounter == 0:
        print "Sorry, no ports are open in range from %d to %d" % (portFrom, portTo-1)
    t2 = time.time()
    scanTime = t2 - t1
    print "\nScanning finished in %f..." % scanTime
    print "Do you want to start again?"
    repeat = raw_input("Enter 'yes' to start again, or anything else to quit.\n> ")
    if "yes" || "y" in repeat:
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
    portFrom = None
    portTo = None
    while portFrom == None:
        try:
            portFrom = int(raw_input("\nPort to start with:\n> "))
        except:
            print "A port is a number! Try again..."
    while portTo == None:
        try:
            portTo = int(raw_input("\nPort to finish with:\n> "))
        except:
            print "A port is a number! Try again..."
    return portScanner(host, portFrom, portTo)

start()
