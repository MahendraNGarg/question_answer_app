
To configure this application in Ubunut follow these instruction.

Download the applicaiton and put into a directory like home, then navigate to home directory and create a virtual environment with python2.7 by following command

virtualenv env

if this command did not work then you need to install virtul env in the system, before installing virtual environment we need to install pip by following command.

		sudo apt-get -y install python-pip

once it installed then install virtual environment

		sudo apt-get install python-setuptools python-dev build-essential git-core -y
		sudo pip install virtualenv

once these install then create a new virtual environment for your application.
		
		virtualenv env

need to activate this by following command
		
		source env/bin/activate

	env is the directory of virtual environment created.


once this virtual env got activated your terminal look like this
		
		(env) mypc@mypc:~$

then navigate to applicaiton directory and run following command
		
		pip install -r requirements.txt

once this installed on the package then you just need to run follwing command to run this application

		python manage.py migrate
		python manage.py runserver



You can browse it on browser by following address 
			
			https://question-assessment.herokuapp.com/

You can access the questions and specific questions by the following API URL
			
			https://question-assessment.herokuapp.com/api/questions?api_key=39843

			https://question-assessment.herokuapp.com/api/questions/1?api_key=39843


that's it!

All the best! :-)
