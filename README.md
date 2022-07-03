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
-	Go to VPC Network > Firewall and create a new firewall rule. The name and tag should be     related to its purpose, in this case port-8080 and port-5000 (spaces should be replaced with ‘-‘.
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

3.  Run the startup.sh script

4.  You can now run the app.py and check the testing coverage of the application using the runTest.sh script!

5.  Open the app on the external ip address on port 5000 and enjoy the app!


Testing: 
-	Done through Jenkins
-   Used Pytest and Pytest Cov to get a coverage report
-	Coverage at: 99%

Example test:

The following test was to to see if the information in the table of directors is equal to what we expect. We are checking to see that the director with id=2 within the table has the name "TestDir2". If this information is what we expect, we have successfully passed. 

class TestAddDir(TestBase):
    def test_add_director(self):
        response = self.client.post(
            url_for('addD'),
            data = dict(
                dir_name = "TestDir2"
                )
        )
        assert Directors.query.filter_by(dir_name = "TestDir2").first().id == 2

We successfully passed this test along with all the others, acheiving a 99% coverage and 14/14 tests passed.

Future Improvements:
-	Have a section for Co-Director(s) so that more people can be credited.
-	Implement a user login system so that information can be edited by verified sources.
-   Connect to a GCP database successfully.
	
Author: 
-	Afzal Kotadia 
-	(Jira link: https://afzalk.atlassian.net/jira/software/projects/PFP/boards/5 )

Licences:
This project is licensed under the MIT license - see the LICENSE.md file for details

Acknowledgements:
-	Help and understanding from QA Academy.
-	Inspiration from IMDb.
-   Thanks to Zake Ahmed and Kajan Kugananthajothy