============
django-reality-polls
============

django-reality-polls is a Django app to conduct web-based polls. For each
question, visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Install django-reality-polls using pip::

   pip install django_reality_polls==0.1

2. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...,
        "django_reality_polls",
        ...,
    ]

3. Include the polls URLconf in your project urls.py like this::

    path("polls/", include("django_reality_polls.urls")),

4. Run ``python manage.py migrate`` to create the models.

5. Start the development server and visit the admin to create a poll.

6. Visit the ``/polls/`` URL to participate in the poll.