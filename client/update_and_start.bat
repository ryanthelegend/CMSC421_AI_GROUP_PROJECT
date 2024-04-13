python3 -m venv venv
./venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt

cd ./src
npm install --legacy-peer-deps

# Start npm in a background process
npm start &

# Store the process id of npm start
NPM_PID=$!

# Wait for the npm process to stop running
wait $NPM_PID

# Once npm has stopped running, the script will continue and eventually terminate.