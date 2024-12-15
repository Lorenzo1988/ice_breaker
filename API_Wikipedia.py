import wikipediaapi
import requests


user_agent = "API_Wikipedia/1.0 (lorenzo.chiappetta88.dev@gmail.com)"
wiki = wikipediaapi.Wikipedia(
    user_agent=user_agent,
    language='it',
    extract_format=wikipediaapi.ExtractFormat.WIKI
)


class WikipediaAPIHandler:
    def __init__(self, language='it'):
        """
        Inizializza il gestore API per Wikipedia

        :param language: Lingua della Wikipedia (default: italiano)
        """
        self.wiki = wikipediaapi.Wikipedia(
            user_agent= user_agent,
            language=language,
            extract_format=wikipediaapi.ExtractFormat.WIKI
        )

    def get_page_summary(self, page_title):
        """
        Ottiene il sommario di una pagina Wikipedia

        :param page_title: Titolo della pagina
        :return: Sommario della pagina o None se non trovata
        """
        try:
            page = self.wiki.page(page_title)

            if not page.exists():
                return None

            return {
                'title': page.title,
                'summary': page.summary[:500] + '...' if len(page.summary) > 500 else page.summary,
                'url': page.fullurl,
                'length': len(page.text)
            }
        except Exception as e:
            print(f"Errore nel recuperare la pagina: {e}")
            return None

    def search_pages(self, query, max_results=5):
        """
        Cerca pagine su Wikipedia per una query

        :param query: Termine di ricerca
        :param max_results: Numero massimo di risultati
        :return: Lista di risultati di ricerca
        """
        try:
            url = f"https://{self.wiki.language}.wikipedia.org/w/api.php"
            params = {
                'action': 'query',
                'format': 'json',
                'list': 'search',
                'srsearch': query,
                'srlimit': max_results
            }

            response = requests.get(url, params=params)
            data = response.json()

            results = []
            for item in data.get('query', {}).get('search', []):
                results.append({
                    'title': item['title'],
                    'snippet': item['snippet']
                })

            return results
        except Exception as e:
            print(f"Errore nella ricerca: {e}")
            return []

    def get_full_page_content(self, page_title):
        """
        Recupera il contenuto completo di una pagina

        :param page_title: Titolo della pagina
        :return: Dizionario con dettagli completi della pagina
        """
        try:
            page = self.wiki.page(page_title)

            if not page.exists():
                return None

            return {
                'title': page.title,
                'full_text': page.text,
                'url': page.fullurl,
                'categories': list(page.categories.keys()),
                'references': list(page.references)
            }
        except Exception as e:
            print(f"Errore nel recuperare il contenuto completo: {e}")
            return None


# Esempio di utilizzo
if __name__ == "__main__":
    wiki_handler = WikipediaAPIHandler(language='it')

    # Esempio: Ottenere sommario
    #sommario = wiki_handler.get_page_summary('Python')
    #print("Sommario:", sommario)

    # Esempio: Ricerca
    #risultati = wiki_handler.search_pages('Intelligenza artificiale')
    #print("Risultati ricerca:", risultati)

    # Esempio: Contenuto completo
    # contenuto = wiki_handler.get_full_page_content('Roma')
    #print("Contenuto completo:", contenuto)



###################
if __name__ == "__main__":
    input = input("Cosa vuoi cercare su Wikipedia?")

    wiki = WikipediaAPIHandler(language='it')
    sommario = wiki.get_page_summary(input)
    print(sommario)