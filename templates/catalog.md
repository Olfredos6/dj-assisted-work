
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css">
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"
        integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo"
        crossorigin="anonymous"></script>

    <title>Bookstore</title>
    <style>
        header {
            position: sticky;
            top: 0;
            z-index: 1020;
        }

        footer {
            position: sticky;
            bottom: 0;
        }

        .content {
            overflow-y: auto;
            height: calc(100vh - 56px - 64px);
            /* 100vh minus header and footer height */
        }

        .card-img-top {
            max-height: 300px;
            overflow: hidden;
        }
    </style>
</head>

<body>

    <!-- Index page -->

    <div class="container">

        <!-- Header -->

        <header
            class="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom box-shadow">
            <h1 class="my-0 mr-md-auto font-weight-normal">Bookstore</h1>
            <nav class="my-2 my-md-0 mr-md-3">
                <a class="p-2 text-dark" href="{% url  'index' %}">Accueil</a>
                <a class="p-2 text-dark" href="{% url 'catalog' %}">Catalogue</a>
            </nav>

            <form class="form-inline d-none d-md-flex mr-auto">
                <input class="form-control" type="search" placeholder="Search" aria-label="Search">
                <button class="btn btn-outline-success" type="submit">Chercher</button>
            </form>

            <div class="dropdown">
                <button class="btn btn-secondary dropdown-toggle" type="button" id="accountButton"
                    data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    <i class="fas fa-user"></i>
                </button>

                <div class="dropdown-menu dropdown-menu-right" aria-labelledby="accountButton">
                    <div class="dropdown-item" data-toggle="modal" data-target="#signInModal">Sign In</div>
                    <div class="dropdown-item" data-toggle="modal" data-target="#signUpModal">Sign Up</div>
                </div>
            </div>

        </header>

        <section id="featured" class="py-1">
            <div class="container">
                <div class="row">

                    <div class="col-4 col-md-3 mb-4">
                        <div class="card h-100 border-0 box-shadow">
                            <img src="{{ book.image }}" class="card-img-top" alt="...">
                            <div class="card-body pb-0 pt-2">
                                <h5 class="card-title"> [Titre du livre] </h5>
                                <p class="card-text">
                                    <span class="font-weight-bold"> [Listes des auteurs]</span>
                                    <br>
                                    Publié en <span class="font-italic">[Année de publication]</span>
                                    <br>
                                    [Prix du livre]
                                </p>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </section>


        <!-- Footer -->

        <footer class="bg-white py-4 mt-auto">
            <div class="container-fluid px-4 px-lg-5">
                <div class="small text-center text-muted">Copyright &copy; 2023 - Bookstore</div>
            </div>
        </footer>

    </div>

    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js"></script>


    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"
        integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo"
        crossorigin="anonymous"></script>
</body>

</html>
```