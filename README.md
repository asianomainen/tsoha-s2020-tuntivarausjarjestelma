# Tuntivarausjärjestelmä

Sovellus kehitetään liikuntatuntien varaamiseen. Käyttäjä voi luoda käyttäjätunnuksen ja ilmoittautua sovelluksen kautta tunneille. Ylläpitäjä voi luoda uusia liikuntatunteja ja poistaa niitä. Ylläpitäjä voi myös hallita käyttäjiä.

<hr>

<b>Sovelluksen ominaisuudet ja edistyminen:</b>

1. Käyttäjä pystyy luomaan käyttäjätilin
   - [x] Käyttäjältä kerätään tiedot:
     - [x] Etunimi
     - [x] Sukunimi
     - [x] Käyttäjätunnus
     - [x] Sähköpostiosoite
     - [x] Puhelinnumero
   - [x] Käyttäjä voi:
      - [x] Päivittää tietojaan
      - [x] Poistaa tilinsä
      - [x] Lähettää ylläpidolle palautetta
      - [x] <b>Käyttäjä voi olla ylläpitäjä, joka voi:</b>
        - [x] lisätä liikuntatunteja
        - [x] muokata liikuntatunteja
        - [x] poistaa liikuntatunteja
        - [x] poistaa liikuntatuntien osallistujia
        - [x] selata käyttäjien tietoja
        - [x] muokata käyttäjien tietoja
        - [x] poistaa käyttäjiä

2. Ilmoittautumisjärjestelmä
   - [x] Käyttäjä näkee tulevat liikuntatunnit etusivulla listattuna 
   - [x] Käyttäjä voi ilmoittautua tunnille
     - [x] Samalle tunnille ei voi ilmoittautua enemmän kuin kerran
   - [x] Käyttäjä voi peruuttaa ilmoittautumisensa
     - [x] Ilmoittautumisen voi peruuttaa vain mikäli käyttäjä on ilmoittautunut tunnille
   - [x] Ilmoittautumisen voi peruuttaa viimeistään 12h etukäteen
   - [x] Mikäli tunti on täynnä, niin käyttäjä voi ilmoittautua varasijalle
   - [x] Käyttäjä näkee tunnit mille hän on ilmoittautunut
   - [x] Käyttäjä näkee kuinka paljon tunnilla on tilaa (esim. "Paikkoja varattu 12/20")
   - [x] Menneet tunnit poistuvat automaattisesti tuntilistalta
- [x] Koodin refaktorointi
- [x] HTML-sivupohjan luominen ja sen käyttöönotto
- [x] Käyttäjätietojen vaatimusten määrittely (käyttäjätunnuksen pituus, salasanan pituus, liikuntatunnnin kesto, yms.)
- [x] Sovelluksen ulkoasun toteutus
- [x] Tietosuojaseloste (kirjoitetaan loppuun myöhemmin)

<hr>
<h2>Sovelluksen testaaminen:</h2>

Linkki sovellukseen: https://movemint.herokuapp.com/

Sovellusta voi testata yllä mainittujen ominaisuuksien puitteissa. Testaaja voi halutessaan luoda uuden tunnuksen testaamista varten tai käyttää alla olevia tunnuksia.<br>

<b>Testaamista varten on luotu sekä testikäyttäjä että ylläpitäjä:</b> 
<hr>
<h3>Käyttäjä</h3>
<br>
<b>Käyttäjänimi:</b> Testi1<br>
<b>Salasana:</b> Testi1<br /><br />

Sisäänkirjauduttuaan käyttäjä näkee etusivulla linkit muille sivuille ("Etusivu", "Kaikki tunnit", "Omat tunnit", "Käyttäjätiedot" ja "Kirjaudu ulos") ja neljä valmiiksi luotua liikuntatuntia, jolle hän voi ilmoittautua (ja perua ilmoittautumisensa).<br /><br />
Testatessa kannattaa huomioida sivun yläreunassa näkyvät viestit, esim. "Käyttäjätunnus tai salasana väärin.", "Ilmoittautuminen onnistui", yms.<br /><br />
Mikäli kirjautumista yritetään tunnuksilla, joita ei ole luotu tai salasana syötetään väärin, niin käyttäjä saa ilmoitukset "Käyttäjätunnus tai salasana väärin."<br /><br />
Käyttäjä voi ilmoittautua vain kerran yhdelle tunnille. Hän ei myöskään voi perua ilmoittautumistaan mikäli hän ei ole ilmoittautunut tunnille.<br /><br />
Testaaja voi tarkastella kaikkia tulevia tunteja "Kaikki tunnit" sivulla tai pelkästään tunteja joille hän on ilmoittautunut "Omat tunnnit" sivulla.
Testaaja voi myös hallinnoida käyttäjätietojaan etusivulla olevalla "Käyttäjätiedot" linkillä. Käyttäjätiedot-sivulla testaaja voi muokata käyttäjän tietoja tai poistaa käyttäjän kokonaan (testaamista varten luotua "testi" käyttäjää ei voi poistaa, mutta sen tietoja voi muokata).
<hr>
<h3>Ylläpitäjä</h3>
<br>
<b>Käyttäjänimi:</b> Admin1<br>
<b>Salasana:</b> Admin1<br /><br />

Sisäänkirjauduttuaan ylläpitäjä näkee etusivulla linkit muille sivuille ("Etusivu", "Kaikki käyttäjät", "Kaikki tunnit", "Luo uusi liikuntatunti", "Palautteet" ja "Kirjaudu ulos")<br /><br />
Mikäli ylläpitäjä luo uuden liikuntatunnin, niin se lisätään "Kaikki tunnit" sivulla näkyvään listaan. Samalla sivulla ylläpitäjä voi myös tarkastella kaikkia liikuntatunteja sekä muokata tai poistaa tunteja ja poistaa tuntien osallistujia.<br /><br />
Testaaja voi ylläpitäjänä tarkastella "Kaikki käyttäjät" sivulla kaikkien käyttäjien tietoja, muokata niitä ja myös poistaa käyttäjiä kokonaan (testaamista varten luotua "Testi1" käyttäjää ei voi poistaa).
