# Spellingsvarianten van Nederlandse plaatsnamen 

Deze repository bevat een overzicht van veelvoorkomende spelfouten van Nederlandse woonplaatsen. Het bestand is gebaseerd op gegevens van het CBS. Het bestand heeft een variable 'Variant' welke een spellingsvariant van de daadwerkelijke plaatsnaam kan zijn (ook de juiste versie is terug te vinden). De werkelijke plaatsnaam is gegeven evenals de plaatsnaamcode, de provincie en landsdeel.

In het bestand input/miscellaneous.csv kunnen plaatsnamen of spellingsvarianten worden toegevoegd waarna ze met parse.py bij het hoofdbestand kunnen worden gevoegd. Het is belangrijk dat de Woonplaats in dit bestand een woonplaats is die terug te vinden is in raw/Woonplaatsen_in_Nederland.csv. Een voorbeeld is Den Haag als variant van 's-Gravenhage. 

In het bestand input/misspelling.csv kunnen bekende spellingsfouten/varianten worden toegevoegd. Bijvoorbeeld 'wijk' en 'wijck'. 

De csv heeft als scheidingsteken ; en is UTF-8 gecodeerd. 

Voorbeeld van de data:

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Variant</th>
      <th>Woonplaats</th>
      <th>Woonplaatscode</th>
      <th>Gemeente</th>
      <th>Gemeente_code</th>
      <th>Provincie</th>
      <th>Provincie_code</th>
      <th>Landsdeel</th>
      <th>Landsdeel_code</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>bos &amp; duin</td>
      <td>Bosch en Duin</td>
      <td>2823</td>
      <td>Zeist</td>
      <td>GM0355</td>
      <td>Utrecht</td>
      <td>PV26</td>
      <td>West-Nederland</td>
      <td>LD03</td>
    </tr>
    <tr>
      <td>broeksterwald</td>
      <td>Broeksterwâld</td>
      <td>3265</td>
      <td>Dantumadiel</td>
      <td>GM1891</td>
      <td>Friesland</td>
      <td>PV21</td>
      <td>Noord-Nederland</td>
      <td>LD01</td>
    </tr>
    <tr>
      <td>loenga</td>
      <td>Loënga</td>
      <td>3505</td>
      <td>Súdwest-Fryslân</td>
      <td>GM1900</td>
      <td>Friesland</td>
      <td>PV21</td>
      <td>Noord-Nederland</td>
      <td>LD01</td>
    </tr>
    <tr>
      <td>westerhaar vriezenveensewyk</td>
      <td>Westerhaar-Vriezenveensewijk</td>
      <td>3327</td>
      <td>Twenterand</td>
      <td>GM1700</td>
      <td>Overijssel</td>
      <td>PV23</td>
      <td>Oost-Nederland</td>
      <td>LD02</td>
    </tr>
    <tr>
      <td>kootwijck</td>
      <td>Kootwijk</td>
      <td>1062</td>
      <td>Barneveld</td>
      <td>GM0203</td>
      <td>Gelderland</td>
      <td>PV25</td>
      <td>Oost-Nederland</td>
      <td>LD02</td>
    </tr>
    <tr>
      <td>wanswert</td>
      <td>Wânswert</td>
      <td>3210</td>
      <td>Ferwerderadiel</td>
      <td>GM1722</td>
      <td>Friesland</td>
      <td>PV21</td>
      <td>Noord-Nederland</td>
      <td>LD01</td>
    </tr>
    <tr>
      <td>bleiswijck</td>
      <td>Bleiswijk</td>
      <td>1689</td>
      <td>Lansingerland</td>
      <td>GM1621</td>
      <td>Zuid-Holland</td>
      <td>PV28</td>
      <td>West-Nederland</td>
      <td>LD03</td>
    </tr>
    <tr>
      <td>beek &amp; donk</td>
      <td>Beek en Donk</td>
      <td>1446</td>
      <td>Laarbeek</td>
      <td>GM1659</td>
      <td>Noord-Brabant</td>
      <td>PV30</td>
      <td>Zuid-Nederland</td>
      <td>LD04</td>
    </tr>
    <tr>
      <td>berg &amp; terblijt</td>
      <td>Berg en Terblijt</td>
      <td>1716</td>
      <td>Valkenburg aan de Geul</td>
      <td>GM0994</td>
      <td>Limburg</td>
      <td>PV31</td>
      <td>Zuid-Nederland</td>
      <td>LD04</td>
    </tr>
    <tr>
      <td>sibrandahus</td>
      <td>Sibrandahûs</td>
      <td>3274</td>
      <td>Dantumadiel</td>
      <td>GM1891</td>
      <td>Friesland</td>
      <td>PV21</td>
      <td>Noord-Nederland</td>
      <td>LD01</td>
    </tr>
  </tbody>
</table>

