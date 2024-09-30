Django signals are executed synchronously.
This means that when a signal is emitted, the connected signal handlers are executed immediately in the same thread and process as the code that emitted the signal.
STEP BY STEP ANALYSIS OF PROJECT
Step 1: Create Django project using the Terminal
         (In Terminal) django-admin startproject asyn
         cd asyn (by using this command we entered the project)
Step 2: Create an app inside the project by this command
         python manage.py startapp syn
Step 3: Update the setting (like we have to add our app into the asyn setting like
         (we already has the installed apps code there so we should add our app to it like the below example)
         INSTALLED_APPS = ['syn',]
Step 4: Create an signals.py inside the app(syn) and define the code as a custom signal and handler that logs execution
Step 5: write the code side the (syn/views.py) that emits the signal and logs the execution order
Step 6: In the main project urls(asyn/urls.py) add the URL pattern for the views
Step 7: Lets run the server by the command in the terminal as
        python manage.py runserver
step 8: lets open navigated page in the browser as htts://127.0.0.1:8000/emit_signal/
we will get the desired output.
