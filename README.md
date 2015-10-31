# Spellingsvarianten van Nederlandse plaatsnamen 

Deze repository bevat een overzicht van veelvoorkomende spelfouten van Nederlandse woonplaatsen. Het bestand is gebaseerd op gegevens van het CBS. Het bestand heeft een variable 'Variant' welke een spellingsvariant van de daadwerkelijke plaatsnaam kan zijn. De werkelijke plaatsnaam is gegeven. Evenals de plaatsnaamcode, de provincie en landsdeel.

In het bestand input/miscellaneous.csv kunnen plaatsnamen of spellingsvarianten worden toegevoegd waarna ze met parse.py bij het hoofdbestand kunnen worden gevoegd. Het is belangrijk dat de Woonplaats in dit bestand een woonplaats is die terug te vinden is in raw/Woonplaatsen_in_Nederland.csv. Een voorbeeld is Den Haag als variant van 's-Gravenhage. 

In het bestand input/misspelling.csv kunnen bekende spellingsfouten/varianten worden toegevoegd. Bijvoorbeeld 'wijk' en 'wijck'. 

De csv heeft als scheidingsteken ; en is UTF-8 gecodeerd. 

Voorbeeld van de data:

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
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
      <th>1433</th>
      <td>nijelamer</td>
      <td>Nijelamer</td>
      <td>1728</td>
      <td>Weststellingwerf</td>
      <td>GM0098</td>
      <td>Friesland</td>
      <td>PV21</td>
      <td>Noord-Nederland</td>
      <td>LD01</td>
    </tr>
    <tr>
      <th>2575</th>
      <td>nybroek</td>
      <td>Nijbroek</td>
      <td>2607</td>
      <td>Voorst</td>
      <td>GM0285</td>
      <td>Gelderland</td>
      <td>PV25</td>
      <td>Oost-Nederland</td>
      <td>LD02</td>
    </tr>
    <tr>
      <th>2968</th>
      <td>hei&amp;boeicop</td>
      <td>Hei- en Boeicop</td>
      <td>2109</td>
      <td>Zederik</td>
      <td>GM0707</td>
      <td>Zuid-Holland</td>
      <td>PV28</td>
      <td>West-Nederland</td>
      <td>LD03</td>
    </tr>
    <tr>
      <th>2735</th>
      <td>boven leeuwen</td>
      <td>Boven-Leeuwen</td>
      <td>1770</td>
      <td>West Maas en Waal</td>
      <td>GM0668</td>
      <td>Gelderland</td>
      <td>PV25</td>
      <td>Oost-Nederland</td>
      <td>LD02</td>
    </tr>
    <tr>
      <th>2757</th>
      <td>s graveland</td>
      <td>'s-Graveland</td>
      <td>3000</td>
      <td>Wijdemeren</td>
      <td>GM1696</td>
      <td>Noord-Holland</td>
      <td>PV27</td>
      <td>West-Nederland</td>
      <td>LD03</td>
    </tr>
    <tr>
      <th>1551</th>
      <td>oostknollendam</td>
      <td>Oostknollendam</td>
      <td>2285</td>
      <td>Wormerland</td>
      <td>GM0880</td>
      <td>Noord-Holland</td>
      <td>PV27</td>
      <td>West-Nederland</td>
      <td>LD03</td>
    </tr>
    <tr>
      <th>1030</th>
      <td>klarenbeek</td>
      <td>Klarenbeek</td>
      <td>2606</td>
      <td>Voorst</td>
      <td>GM0285</td>
      <td>Gelderland</td>
      <td>PV25</td>
      <td>Oost-Nederland</td>
      <td>LD02</td>
    </tr>
    <tr>
      <th>1345</th>
      <td>munnekeburen</td>
      <td>Munnekeburen</td>
      <td>1725</td>
      <td>Weststellingwerf</td>
      <td>GM0098</td>
      <td>Friesland</td>
      <td>PV21</td>
      <td>Noord-Nederland</td>
      <td>LD01</td>
    </tr>
    <tr>
      <th>1594</th>
      <td>oude willem</td>
      <td>Oude Willem</td>
      <td>3117</td>
      <td>Westerveld</td>
      <td>GM1701</td>
      <td>Drenthe</td>
      <td>PV22</td>
      <td>Noord-Nederland</td>
      <td>LD01</td>
    </tr>
    <tr>
      <th>2731</th>
      <td>beneden leeuwen</td>
      <td>Beneden-Leeuwen</td>
      <td>1769</td>
      <td>West Maas en Waal</td>
      <td>GM0668</td>
      <td>Gelderland</td>
      <td>PV25</td>
      <td>Oost-Nederland</td>
      <td>LD02</td>
    </tr>
  </tbody>
</table>

