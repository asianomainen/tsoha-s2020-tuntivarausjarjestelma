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
   - [x] Käyttäjä voi päivittää tietojaan
   - [x] Käyttäjä voi poistaa tilinsä
   - [x] Käyttäjä voi olla ylläpitäjä, joka voi
     - [x] lisätä liikuntatunteja
     - [x] muokata liikuntatunteja
     - [x] poistaa liikuntatunteja
     - [ ] lisätä liikuntatuntien osallistujia
     - [x] poistaa liikuntatuntien osallistujia
     - [x] selata käyttäjien tietoja
     - [x] muokata käyttäjien tietoja
     - [x] poistaa käyttäjiä

2. Ilmoittautumisjärjestelmä
   - [ ] Käyttäjä näkee liikuntatunnit kalenterinäkymästä 
     - Tunnit näkyvät tällä hetkellä listattuna etusivulla
   - [x] Käyttäjä voi ilmoittautua tunnille
     - [x] Samalle tunnille ei voi ilmoittautua enemmän kuin kerran
   - [x] Käyttäjä voi peruuttaa ilmoittautumisensa
     - [x] Ilmoittautumisen voi peruuttaa vain mikäli käyttäjä on ilmoittautunut tunnille
   - [ ] Ilmoittautumisen voi peruuttaa viimeistään 12h etukäteen
   - [x] Mikäli tunti on täynnä, niin käyttäjä voi ilmoittautua varasijalle
   - [x] Käyttäjä näkee tunnit mille hän on ilmoittautunut
   - [x] Käyttäjä näkee kuinka paljon tunnilla on tilaa (esim. "Paikkoja varattu 12/20")
- [x] Koodin refaktorointi
- [x] HTML-sivupohjan luominen ja sen käyttöönotto
- [ ] Käyttäjätietojen vaatimusten määrittely (käyttäjätunnuksen pituus, salasanan pituus, liikuntatunnnin kesto, yms.)
- [ ] Sovelluksen ulkoasun toteutus

<hr>
<h2>Sovelluksen testaaminen:</h2>

Linkki sovellukseen: https://movemint.herokuapp.com/

Sovellusta voi testata yllä mainittujen ominaisuuksien puitteissa. Testaaja voi halutessaan luoda uuden tunnuksen testaamista varten, koska tällä hetkellä sovelluksessa kaikki toiminnot ovat tavallisen käyttäjän suoritettavissa.<br>

<b>Testaamista varten on luotu sekä testikäyttäjä että ylläpitäjä:</b> 
<hr>
<h3>Käyttäjä</h3>
<br>
<b>Käyttäjänimi:</b> testi<br>
<b>Salasana:</b> testi<br /><br />

Sisäänkirjauduttuaan käyttäjä näkee etusivulla linkit muille sivuille ("Etusivu", "Käyttäjätiedot" ja "Kirjaudu ulos") ja kaksi valmiiksi luotua liikuntatuntia, jolle hän voi ilmoittautua (ja perua ilmoittautumisensa).<br /><br />
Testatessa kannattaa huomioida sivun yläreunassa näkyvät viestit, esim. "Käyttäjätunnus tai salasana väärin.", "Ilmoittautuminen onnistui", yms.<br /><br />
Mikäli kirjautumista yritetään tunnuksilla, joita ei ole luotu tai salasana syötetään väärin, niin käyttäjä saa ilmoitukset "Käyttäjätunnus tai salasana väärin."<br /><br />
Käyttäjä voi ilmoittautua vain kerran yhdelle tunnille. Hän ei myöskään voi perua ilmoittautumistaan mikäli hän ei ole ilmoittautunut tunnille.<br /><br />
Testaaja voi myös hallinnoida käyttäjätietojaan etusivulla olevalla "Käyttäjätiedot" linkillä. Käyttäjätiedot-sivulla testaaja voi muokata käyttäjän tietoja tai poistaa käyttäjän kokonaan (testaamista varten luotua "testi" käyttäjää ei voi poistaa, mutta sen tietoja voi muokata).
<hr>
<h3>Ylläpitäjä</h3>
<br>
<b>Käyttäjänimi:</b> admin<br>
<b>Salasana:</b> admin<br /><br />

Sisäänkirjauduttuaan ylläpitäjä näkee etusivulla linkit muille sivuille ("Etusivu", "Kaikki käyttäjät", "Kaikki tunnit", "Luo uusi liikuntatunti" ja "Kirjaudu ulos")<br /><br />
Mikäli ylläpitäjä luo uuden liikuntatunnin, niin se lisätään etusivulla näkyvään listaan. Ylläpitäjä voi myös tarkastella kaikkia liikuntatunteja "Kaikki tunnit" sivulla sekä muokata tai poistaa tunteja.<br /><br />
Testaaja voi ylläpitäjänä tarkastella "Kaikki käyttäjät" sivulla kaikkien käyttäjien tietoja, muokata niitä ja myös poistaa käyttäjiä kokonaan (testaamista varten luotua "testi" käyttäjää ei voi poistaa).
