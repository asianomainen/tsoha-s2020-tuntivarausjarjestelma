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
   - [ ] Käyttäjä voi olla ylläpitäjä, joka voi
     - [x] lisätä liikuntatunteja
     - [ ] poistaa liikuntatunteja
     - [ ] lisätä ja poistaa liikuntatuntien osallistujia
     - [ ] selata käyttäjien tietoja
     - [ ] poistaa käyttäjiä

2. Ilmoittautumisjärjestelmä
   - [ ] Käyttäjä näkee liikuntatunnit kalenterinäkymästä 
     - Tunnit näkyvät tällä hetkellä listattuna etusivulla
   - [x] Käyttäjä voi ilmoittautua tunnille
     - [ ] Samalle tunnille ei voi ilmoittautua enemmän kuin kerran
   - [x] Käyttäjä voi peruuttaa ilmoittautumisensa
     - [ ] Ilmoittautumisen voi peruuttaa vain mikäli käyttäjä on ilmoittautunut tunnille
   - [ ] Tunnin voi varata korkeintaan kaksi viikkoa etukäteen
   - [ ] Ilmoittautumisen voi peruuttaa viimeistään 12h etukäteen
   - [ ] Mikäli tunti on täynnä, niin käyttäjä voi ilmoittautua varasijalle
   - [ ] Käyttäjä näkee tunnit mille hän on ilmoittautunut
   - [ ] Käyttäjä näkee kuinka paljon tunnilla on tilaa (esim. "osallistujia 12/20")
- [ ] Koodin refaktorointi
   - Sovelluksen rakennetta tullaan muuttamaan laajasti. Toimintoja jaetaan järkevästi moduuleihin ja funktioihin ja koodin toisteisuutta vähennetään.

<hr>
<b>Sovelluksen testaaminen:</b>

Linkki sovellukseen: https://movemint.herokuapp.com/

Sovellusta voi testata yllä mainittujen ominaisuuksien puitteissa. Testaaja voi halutessaan luoda uuden tunnuksen testaamista varten, koska tällä hetkellä sovelluksessa kaikki toiminnot ovat tavallisen käyttäjän suoritettavissa.<br>

Käytettävissä on myös valmiiksi luotu käyttäjätunnus:

<b>Käyttäjänimi:</b> testi<br>
<b>Salasana:</b> testi

Sisäänkirjauduttuaan testaaja näkee etusivulla linkit muille sivuille ("Käyttäjätiedot", "Luo uusi liikuntatunti" ja "Kirjaudu ulos") ja yhden valmiiksi luodun liikuntatunnin, jolle hän voi ilmoittautua (ja perua ilmoittautumisensa). Mikäli testaaja luo uuden liikuntatunnin, niin se lisätään etusivulla näkyvään listaan. Testaaja voi myös hallinnoida käyttäjätietojaan etusivulla olevalla "Käyttäjätiedot" linkillä. Käyttäjätiedot-sivulla testaaja voi muokata käyttäjän tietoja tai poistaa käyttäjän kokonaan (testaamista varten luotua "testi" käyttäjää ei voi poistaa).

