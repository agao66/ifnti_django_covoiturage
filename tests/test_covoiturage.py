from covoiturage.models import Trajet


def test_covoiturage_d_un_trajet(db):
    trajet = Trajet.objects.create(
        conducteur="affo",
        ville_depart="sokode",
        ville_arrivee="lome",
        date_depart="2026-10-18",
        heure_depart="18:00",
        places=4,
        prix_place=4000
    )
    
    assert trajet.conducteur
    assert trajet.ville_depart
    assert trajet.ville_arrivee
    assert trajet.date_depart
    assert trajet.heure_depart
    assert trajet.places
    assert trajet.prix_place
   