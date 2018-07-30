import argparse, pygeoip, webbrowser, sys, os, pygmaps, urllib2, gzip, time
from scapy.all import traceroute
from colors import red, yellow, green

class maintain(object):
    def download_db(self):
        print "Downloading database.."
        try:
            self.gz_file = "GeoLiteCity.dat.gz"
            self.url = "http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz"
            self.res = urllib2.urlopen(self.url)
            self.fh = open(self.gz_file, "w")
            self.fh.write(self.res.read())
            self.fh.close()
            self.dat_file = gzip.open(self.gz_file, 'rb')
            self.content = self.dat_file.read()
            self.dat_file.close()
            self.outF = file("GeoLiteCity.dat", 'wb')
            self.outF.write(self.content)
            self.outF.close()
            os.remove('GeoLiteCity.dat.gz')
        except:
            print "[!] Error downloading/updating database, try manually from http://dev.maxmind.com/geoip/legacy/geolite/"
            if os.path.isfile('GeoLiteCity.dat') == True:
                pass
            else:
                sys.exit(0)
        
     
    def db_status(self):
        try:
            self.update_time = 60*60*24*30
            self.db_time = os.path.getmtime('GeoLiteCity.dat')
            self.curr_time = time.time()
            self.db_age = self.curr_time-self.db_time
            if self.db_age > self.update_time:
                print "[!] Database update recommended!"
                print "[!] Updating..."
                self.download_db()
        except:
            if os.path.isfile('GeoLiteCity.dat') == False:
                print "[!] Database file not found!"
                self.download_db()
            else:
                print "[!] Error while checking database status"
                sys.exit(0)
                
class trace_route(object):  
    def geo_trace(self, tracer):
        print red("[!] Using scapy's traceroute")
        time.sleep(1)
        self.tracer = tracer
        self.trace, _ = traceroute([self.tracer] , verbose=0)
        self.hosts = self.trace.get_trace().values()[0]
        self.ips = [self.hosts[self.i][0] for self.i in range(1, len(self.hosts) + 1)]
        self.rawdata = pygeoip.GeoIP('GeoLiteCity.dat')
        self.i = 0
        self.path = []
        print yellow("Geotrace:")+red(str(self.tracer))
        while ( self.i < len(self.ips)):
            self.data = self.rawdata.record_by_addr(self.ips[self.i])
            if self.data == None:
                pass
            else:
                self.longi = self.data['longitude']
                self.lat = self.data['latitude']
                self.path.append((self.lat, self.longi))
                print yellow("[X] IP")+":"+yellow(str(self.ips[self.i]))+":"+ red(str(self.data['country_name']))
            self.i += 1
        self.tracemap = pygmaps.maps(self.lat ,self.longi,3)
        self.tracemap.addpath(self.path,"#FF0000")
        self.tracemap.draw('./geo_trace.html')
        while True:
            self.o_map = raw_input("Try to open geo_trace.html map in browser(y/ n):\n>").lower()
            if self.o_map.startswith('y'):
                try:
                    self.new = 2
                    webbrowser.open("geo_trace.html", new=self.new)
                    break
                except:
                    print '[!]Could not open map in web browser. Open "geo_trace.html" -file manually' 
                break
            elif self.o_map.startswith('n'):
                break
                
    def alt_traceroute(self,tracer):
        print red("[!] Using systems 'default' traceroute")
        time.sleep(1)
        self.tracer = tracer
        self.o_put = os.popen("traceroute -n "+self.tracer+"| tail -n+2 | awk '{ print $2 }'").read()
        self.raw_ips = self.o_put.split() # IP-address list
        self.ips = [ self.j for self.j in self.raw_ips if not self.j.startswith('*') ]
        self.rawdata = pygeoip.GeoIP('GeoLiteCity.dat')
        self.i = 0
        self.path = []
        print yellow("Geotrace:")+red(str(self.tracer))
        while ( self.i < len(self.ips)):
            self.data = self.rawdata.record_by_addr(self.ips[self.i])
            if self.data == None:
                pass
            else:
                self.longi = self.data['longitude']
                self.lat = self.data['latitude']
                self.path.append((self.lat, self.longi))
                print yellow("[X] IP")+":"+yellow(str(self.ips[self.i]))+":"+ red(str(self.data['country_name']))
            self.i += 1
        self.tracemap = pygmaps.maps(self.lat ,self.longi,3)
        self.tracemap.addpath(self.path,"#FF0000")
        self.tracemap.draw('./geo_trace.html')
        while True:
            self.o_map = raw_input("Tryccc to open geo_trace.html map in browser(y/ n):\n>").lower()
            if self.o_map.startswith('y'):
                try:
                    self.new = 2
                    webbrowser.open("geo_trace.html", new=self.new)
                    break
                except:
                    print '[!]Could not open map in web browser. Open "geo_trace.html" -file manually' 
                break
            elif self.o_map.startswith('n'):
                break
       
 
                
class location(object):
    def locate(self, target):
        self.target = target
        self.rawdata = pygeoip.GeoIP('GeoLiteCity.dat')
        try:
            self.data = self.rawdata.record_by_addr(self.target)
        except:
            self.data = self.rawdata.record_by_name(self.target)
        self.country = self.data['country_name']
        self.longi = self.data['longitude']
        self.lat = self.data['latitude']
        self.mymap = pygmaps.maps(self.lat, self.longi, 12)
        self.mymap.addpoint(self.lat, self.longi, "Target is near this area")
        self.mymap.draw('./target_location.html')
        print yellow("[!] Target: ")+red(str(self.target))
        print yellow("[x] Target's country: ")+red(str(self.country))
        print yellow("[x] Longitude: ")+red(str(self.longi))
        print yellow("[x] Latitude: ")+red(str(self.lat))
        print yellow('[x] Map of the location >')+red('"target_location.html"')
        while True:
            self.o_map = raw_input("Try to open target_location.html map in browser(y/ n):\n>").lower()
            if self.o_map.startswith('y'):
                try:
                    self.new = 2
                    webbrowser.open("target_location.html", new=self.new)
                    break
                except:
                     print '[!]Could not open map in web browser. Open "geo_trace.html" -file manually' 
                break
            elif self.o_map.startswith('n'):
                break

             
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="IP-address geolocator and geotracer")
    parser.add_argument("-t", "--target", type=str, help="Give ip-address or domain-name for locating.")
    parser.add_argument("-gT", "--geoTrace", type=str, help="Give ip-address or domain-name to tracing.")
    parser.add_argument("-d", "--download",action='store_true', help="Download/update maxmind geoip database")
    
    args = parser.parse_args()
    target = args.target
    tracer = args.geoTrace
    downl = args.download
    maintain = maintain()
    if not downl and not target and not tracer:
        parser.print_help()
        sys.exit(0)
    os.system('clear')
    maintain.db_status()
    if downl:
        maintain.download_db()
    if target:
        location = location()
        location.locate(target)
    if tracer:
        trace_route = trace_route()
        if os.getuid() == 0:   
            trace_route.geo_trace(tracer)
        elif os.getuid() != 0:
            trace_route.alt_traceroute(tracer)
