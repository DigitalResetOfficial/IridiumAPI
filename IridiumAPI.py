#Import Json Library
import json
import os
#Open Api
fApi = open("api.json","r")
#Load Api
Api = json.load(fApi)
#Get Hostname
HostName = Api['Host']
LocalPort = Api['Port']
print("Connected to: " + HostName + ":" + LocalPort)
#Get Access
User = Api['Username']
Pass = Api['Password']
aKey = Api['apiKey']
print("Granted Access To Server @ " + aKey)
#Close The Server
fApi.close()

#Open API Server
import os
workspace = os.path.dirname(os.path.realpath(__file__))
fServer = open(workspace + "/config/server.json","r")
Server = json.load(fServer)
#Create Repositories
if not os.path.exists(workspace + "/" + Server['public_repo']):
    os.makedirs(workspace + "/" + Server['public_repo'])
if not os.path.exists(workspace + "/" + Server['private_repo']):
    os.makedirs(workspace + "/" + Server['private_repo'])
if not os.path.exists(workspace + "/" + Server['developer_repo']):
    os.makedirs(workspace + "/" + Server['developer_repo'])
#Close API Server
fServer.close()

print("Starting Iridium FTP Service")
server = os.popen("sudo python -m SimpleHTTPServer")
