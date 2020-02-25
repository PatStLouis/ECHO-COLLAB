<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>EchoWeb</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
        <link rel="stylesheet" type="text/css" href="css/Echo-net.css">
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
        <script src="script.js" defer></script>
    </head>
    <body>
        <header>
            <img class="logo" src="images/Logo.png" alt="LogoSystème" >
            <nav class="navbar navbar-expand-sm navbar-dark bg-dark mb-4">
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <section class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="nav nav-pills nav-fill">
                        <li class="nav-item">
                            <a class="nav-link" href="index.html">Accueil</a>
                        </li>
                        <li class="nav-item dropdown">
                            <a class="nav-link active" aria-current="true">[Echo|Hack]]</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">[Echo|Express]</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">[Echo|Junior]</a>
                        </li>
                    </ul>
                </section>
            </nav>
        </header>
        <main class="container">
            <!-- @TODO Add regex -->
            <form method="POST" action="email.php">
                <section class="form-group">
                    <label for="email">Adresse courriel</label>
                    <input type="email" class="form-control" id="email" name="email" placeholder="courriel@exemple.com">
                </section>
                <section class="form-group">
                    <label for="nom">Nom</label>
                    <input type="text" class="form-control" id="nom" name="nom" placeholder="Tremblay">
                </section>
                <section class="form-group">
                    <label for="prenom">Prénom</label>
                    <input type="text" class="form-control" id="prenom" name="prenom" placeholder="Pierre">
                </section>
                <section class="form-group">
                    <label for="msg">Message</label>
                    <textarea class="form-control" id="msg" name="msg" placeholder="Écrivez votre message ici"> </textarea>
                </section>
                <button type="submit" class="btn btn-primary">Soumettre</button>
            </form>
        </main>
    </body>
</html>