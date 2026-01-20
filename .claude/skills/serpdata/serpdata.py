#!/usr/bin/env python3
"""
SerpData Search Skill
Wyszukuje top 10 wyników organicznych z Google używając SerpData API.
"""

import sys
import requests
import json

API_URL = "https://api.serpdata.io/v1/search"
API_KEY = "nodeshub_5fa61b122fb24c28d7f8fec07020fdfc-wXLWsmbjigY"

def search_serpdata(keyword, hl="pl", gl="pl"):
    """
    Wykonuje zapytanie do SerpData API.

    Args:
        keyword: Słowo kluczowe do wyszukania
        hl: Język (domyślnie: pl)
        gl: Kraj (domyślnie: pl)

    Returns:
        Lista wyników organicznych
    """
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    params = {
        "keyword": keyword,
        "hl": hl,
        "gl": gl
    }

    try:
        response = requests.get(API_URL, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        if data.get("data", {}).get("success"):
            results = data.get("data", {}).get("results", {})
            organic_results = results.get("organic_results", [])
            return organic_results
        else:
            print("❌ Błąd: API zwróciło status success=false")
            return []

    except requests.exceptions.RequestException as e:
        print(f"❌ Błąd podczas zapytania do API: {e}")
        return []
    except json.JSONDecodeError as e:
        print(f"❌ Błąd podczas parsowania odpowiedzi JSON: {e}")
        return []

def display_results(keyword, results):
    """
    Wyświetla wyniki wyszukiwania w sformatowany sposób.

    Args:
        keyword: Słowo kluczowe
        results: Lista wyników organicznych
    """
    print(f"\n# Wyniki wyszukiwania dla: {keyword}\n")

    if not results:
        print("ℹ️  Brak wyników organicznych dla tego zapytania.\n")
        return

    print(f"## Top {min(len(results), 10)} wyników organicznych:\n")

    for i, result in enumerate(results[:10], 1):
        title = result.get("title", "Brak tytułu")
        url = result.get("url", "Brak URL")
        description = result.get("description", "Brak opisu")

        print(f"{i}. {title}")
        print(f"   URL: {url}")
        print(f"   {description}\n")

def main():
    """Główna funkcja skilla."""
    if len(sys.argv) < 2:
        print("❌ Błąd: Nie podano słowa kluczowego")
        print("\nUżycie: /serpdata <słowo kluczowe>")
        print("\nPrzykłady:")
        print("  /serpdata krzesła")
        print("  /serpdata Pressure washer")
        sys.exit(1)

    # Pobierz słowo kluczowe z argumentów (łączy wszystkie argumenty w jeden string)
    keyword = " ".join(sys.argv[1:])

    # Wykonaj wyszukiwanie
    results = search_serpdata(keyword)

    # Wyświetl wyniki
    display_results(keyword, results)

if __name__ == "__main__":
    main()
