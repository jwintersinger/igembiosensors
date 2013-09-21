iGEM Biosensors DB
==================

0. Create Python 2 virtual environment for project.

        mkdir ~/.virtualenvs
        cd ~/.virtualenvs
        virtualenv2 igembiosensors
        source igembiosensors/bin/activate
        cd -

1. Install Django 1.6. As this version is still in beta as of this writing, you must install from GitHub.

        pip install git+git://github.com/django/django.git@1.6b4

2. Install dependencies.

        pip install django-taggit django-widget-tweaks

3. Clone and configure project.

        git clone https://github.com/jwintersinger/igembiosensors.git
        cd igembiosensors/igembiosensors
        cp settings_deployment.py.example settings_deployment.py
        # If you please, change database. PostgreSQL works well in production. If
        # you're not using SQLite, see
        # https://docs.djangoproject.com/en/dev/ref/settings/#databases for
        # instructions on configuring DB settings.
        vim settings_deployment.py
        cd ..
        
4. Synchronize database.
        
        # When asked if you wish to create a superuser account, select "yes", then
        # enter a username and password. (You need not enter an e-mail address.) If
        # you forget your password or need to create another superuser account
        # later, see these two commands:
        #  python2 manage.py help changepassword
        #  python2 manage.py help createsuperuser
        python2 manage.py syncdb
        
5. Run server.
        
        python2 manage.py runserver 0.0.0.0:8000
        # Now, access http://<your_ip>:8000 in your web browser.
        
6. Set up additional user accounts. Access `http://<your_ip>:8000/admin/` in your web browser. You have two options:
    1. Make additional users superusers. This means that these users will be able to add new users themselves.
        1. Click the Add link next to Users under the Auth heading.
        2. Enter a username, password, and password confirmation, then click Save.
        3. On the next screen, under the Permissions heading, check both the `Staff status` and `Superuser status` checkboxes.
        4. Click Save.

    2. Make additional users limited users. They will not be able to add new users themselves.
        1. Create a group setting permissions for these users. You need do this only once.
            1. Click the Add link next to Groups under the Auth heading.
            2. Enter an appropriate group name, such as `Project editors`.
            3. Under `Available permissions`, in the text field next to the
               magnifying glass, type `biosensorsdb`, then click `Choose all`.
               Note that you  can, for example, forbid users from creating new
               categories -- simply omit the `Can {add,change,delete} category`
               permissions. Users will be able to add projects to existing
               categories, but not create or modify the list of categories.
            4. Click Save.

        2. Add the users.
            1. From the administration home, Click the Add link next to Users under the Auth heading.
            2. Enter a username, password, and password confirmation, then click Save.
            3. On the next screen, under the Permissions heading, check `Staff status` checkbox.
            4. Under `Available groups`, select the group you created in the
               previous step, then click the right arrow icon to add the user to
               this group.
            5. Click Save.

7. After entering production data, backup the database.

        # Use --natural flag because django-taggit references contenttypes.
        python2 manage.py dumpdata --indent=2 --natural biosensorsdb taggit > backups/biosensors_data.json
        # To load backup, execute the following:
        # python2 manage.py loaddata backups/biosensors_data.json
