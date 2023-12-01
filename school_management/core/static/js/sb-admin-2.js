<!-- core/templates/core/base.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}School Management System{% endblock %}</title>

    <!-- Add your custom CSS files -->
    <link rel="stylesheet" href="{% static 'css/sb-admin-2.css' %}">
    <!-- If you prefer the minified version, you can use the following line instead -->
    <!-- <link rel="stylesheet" href="{% static 'css/sb-admin-2.min.css' %}"> -->

    <!-- Add your custom JS files -->
    <script src="{% static 'js/sb-admin-2.js' %}"></script>
    <!-- If you prefer the minified version, you can use the following line instead -->
    <!-- <script src="{% static 'js/sb-admin-2.min.js' %}"></script> -->

    <!-- Bootstrap CSS from CDN -->
    <!-- Remove the Bootstrap CDN link since you're using a custom theme -->
    <!-- Add any additional CSS files or styles specific to your project -->
    <style>
        body {
            padding-top: 56px;
        }

        .navbar {
            background-color: #007bff;
        }

        .navbar-dark .navbar-nav .nav-link {
            color: #ffffff;
        }

        .navbar-dark .navbar-toggler-icon {
            background-color: #ffffff;
        }

        .navbar-dark .navbar-toggler {
            border-color: #ffffff;
        }

        .container {
            margin-top: 20px;
        }

        .site-title {
            text-align: center;
            font-size: 24px;
            margin-bottom: 20px;
        }

        @media (max-width: 576px) {
            .navbar-collapse {
                text-align: center;
            }

            .navbar-toggler {
                margin: auto;
                display: block;
            }

            .navbar-nav {
                display: inline-block;
            }
        }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark">
        <div class="container">
            <a class="navbar-brand" href="#"><span class="site-title">School Management System</span></a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ml-auto">
                    <li class="nav-item active">
                        <a class="nav-link" href="{% url 'teachers' %}">Teachers</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'students' %}">Students</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'assignments' %}">Assignments</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'class_list' %}">Classes</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <div class="container">
        {% block content %}{% endblock %}
    </div>

    <!-- Bootstrap JS and Popper.js from CDN -->
    <!-- Remove the Bootstrap CDN scripts since you're using a custom theme -->
    <!-- Add any additional JS scripts specific to your project -->
</body>
</html>
