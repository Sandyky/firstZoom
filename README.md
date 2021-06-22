1stZoom Assignment
 
 Stepts to install the dependencies and run the project
 Step 1: create the virtual environment 
         vitualenv venv 
         if virtualenv not install then install it using the below command
          pip install virtualenv
          
 Step 2: activate the virtual environment
        windows: venv/Scripts/activate.ps1
        linux: source venv/bin/activate
        
 Step 3: Clone the repository
        git clone https://github.com/Sandyky/1stZoom.git
        
 Step 4: Install the requirements to run the projects
          pip install -r requirements.txt
          
 Step 5: To run
        locate the directory where manage.py file exist and then run following commands
        python manage.py runserver
        open the url on your browser
        http://127.0.0.1:8000/
        
 If database file not there then run the following commands
 1. python manage.py makemigrations
 2. python manage.py migrate
 3. python manage.py runserver
 
 
         
