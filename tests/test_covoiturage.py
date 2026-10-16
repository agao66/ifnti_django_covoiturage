from covoiturage.models import Trajet


def test_covoiturage_d_un_trajet:
    trajet = Trajet.objects.create(
        conducteur="affo",
        ville_depart="sokode",
        ville_arriver="lome",
        date_depart="2026-10-18",
        heure_depart="18:00",
        places=4,
        prix_place=4000
    )
   