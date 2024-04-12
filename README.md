## Getting started:

### Seting up the environment

Navigate to the backend directory and run the following commands. 

`python3 -m venv venv`

`source venv/bin/activate`

`python -m pip install --upgrade pip`

`pip install -r CPUrequirements.txt`

* If you have access to a GPU, you can run the requirements.txt in the root folder. 

* Once the backend is running and waiting for POST, you may start another terminal and navigate to the client directory, where you can run the following commands
`npm install`
`npm start`

* The webpage will start automatically, from which you may test out the chatbox. 
* IMPORTANT NOTE: currently the ports are configured to my specifications, so feel free to change the ports from 5001 to something else (5000 is recommended). 





* To close the backend: `screen -S backend -X quit`





