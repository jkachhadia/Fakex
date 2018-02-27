import subprocess
import sys

searchQuery = sys.argv[1]

#fork processes
outToi = open('logs/toi', 'w')
errToi = open('logs/toi', 'w')
outIe = open('logs/ie', 'w')
errIe = open('logs/ie', 'w')
toi = subprocess.Popen(['python','toi.py',searchQuery], stdout=outToi, stderr=errToi)
ie = subprocess.Popen(['python','indianExpress.py', searchQuery], stdout=outIe, stderr=errIe)

#wait for processes to terminate
toi.wait();
ie.wait();

#flush the logs