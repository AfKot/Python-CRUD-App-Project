# Python-CRUD-App-Project
Overview of Project:
The Purpose of this project was to develop a CRUD application, build with Flask and coded with Python and HTML. 
My project is based on a movie directory, displaying information on both a Movie and the associated Director. You should be able to add a film along with all its details and link it to any director within the system. Both can be created separately and only the leading director can be selected for a Movie.

Prerequisites:
-	Visual Studio Code
-	GitHub
-	Google Cloud Platform
-	Jira

Instructions On how to operate:
1.	Set up a virtual machine using Google Cloud Platform (GCP):
-	Make an account if you haven’t already got one.
-	Go to VPC Network > Firewall and create a new firewall rule. The name and tag should be related to its purpose, in this case port-8080 and port-5000 (spaces should be replaced with ‘-‘).
-	Make sure the direction of traffic is set to Ingress (should be by default). 
-	Set the IPv4 ranges to 0.0.0.0/0 for port-5000 so that it is open to all.
-	Under Protocols and ports select the tcp box and type in 8080 for port-8080 and 5000 for port-5000. Then click Create.
-	Go to Compute Engine > VM instances and click Create Instance. Make sure the machine type is set to medium and the Boot disk is Ubuntu. Add in the network tags under Networking and press Create.
-	Open up VS Code and open up a Terminal. Type in ssh-keygen and press the Enter key when prompted.
-	Cd into the ssh directory and remove the known_hosts file. Then run cat .ssh/id_rsa.pub to view the public key.
Copy this key. Open up your VM instance created on GCP and edit it. Scroll down to SSH keys and click add item, then paste the key in and click Save.
-	Copy down the external ip address from the VM you created. Go back onto VS Code and open a Remote Window. Open the configuration file and add in the external ip address you copied as a HostName and input your username (on your device) into the User section. Save the file. 
-	Then open a remote window again click connect to Host. Select Linux and continue. You will then be connected to your VM instance.

2.	Connect to your GitHub Repo:
-	Now that you are connected to your VM instance, generate another ssh key as before.
-	Go to your Github account > Settings > SSH & GPGand add the ssh key.
-	Go to the repo which you want to clone, and copy the SSH code. On VS Code run: 
git clone <the ssh code you copied>




Testing: 
-	Done through Jenkins
-	Coverage at:   % (target was 85-95%)

Improvements:
-	Have a section for Co-Director(s) so that more people can be credited.
-	Implement a user login system so that information can be edited by verified sources.
-	

Author: 
-	Afzal Kotadia 
-	(Jira link: https://afzalk.atlassian.net/jira/software/projects/PFP/boards/5 )

Build With: 
-	Flask

Licences:


Acknowledgements:
-	Help and understanding from QA Academy.
-	Inspiration from IMDb.
-
