# SerpData Search Skill

Wyszukaj top 10 wyników organicznych z Google używając SerpData API.

## Użycie

```
/serpdata <słowo kluczowe>
```

## Przykłady

- `/serpdata Pressure washer` - wyszukaj wyniki dla "Pressure washer"
- `/serpdata krzesła` - wyszukaj wyniki dla "krzesła"

## Instalacja

Skill wymaga zainstalowania zależności:

```bash
pip install -r requirements.txt
```

## Opis

Skill wykonuje zapytanie do SerpData API i zwraca top 10 wyników organicznych z Google.

## Techniczne szczegóły

- Język: Python 3
- Zależności: requests
- API: https://api.serpdata.io/v1/search
- Lokalizacja: Polska (hl=pl, gl=pl)
