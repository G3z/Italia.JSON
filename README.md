Italia.json
===========

File JSON contenente dati geografici di uso comune. Il repository contiene:
- combine.py: tool per il join di regioni con comuni
- comuni.csv: lista dei comuni italiani
- italia.json: json con regioni e province
- italia_comuni.json: json con regioni, province e comuni

##install via npm##

```javascript
npm install italia
```

```javascript
var italia = require('italia');
var regioni = italia.regioni.map(function(r){ return r.nome }).join(", ");
// 'Abruzzo, Basilicata, Calabria, Campania, Emilia-Romagna, Friuli-Venezia Giulia, Lazio, Liguria, Lombardia, Marche, Molise, Piemonte, Puglia, Sardegna, Sicilia, Toscana, Trentino-Alto Adige, Umbria, Valle d\'Aosta, Veneto'
```

Changelog
===========

- modulo npm `npm install italia`
- combine.py combina il csv contenente i comuni, con il json contenente le regioni
- Aggiunta delle regioni e dei comuni, comprendenti di cap e codice istat
- Regioni ordinate per ordine lessicografico sul nome
- Lista delle regioni e provincie italiane
