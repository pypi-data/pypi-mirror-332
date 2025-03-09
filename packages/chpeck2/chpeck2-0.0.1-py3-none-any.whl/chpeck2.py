from bs4 import BeautifulSoup
import requests as rq
import pandas as pd


class RecipeScraper:
    def __init__(self) -> None:
        self.soup: BeautifulSoup | None = None
        self.data_frame = None

    def scrape_url(self, url: str) -> None:
        response: rq.Response = rq.get(url)
        response.encoding = "utf-8"

        self.soup = BeautifulSoup(response.text, "html.parser")

    def get_tables_data(self) -> pd.DataFrame:
        if self.data_frame is not None:
            return self.data_frame

        tables = self.soup.find_all("table")[1:]
        headers = self.soup.find_all("h2")

        data_tables: list = []
        for i, table in enumerate(tables):
            data_tables.append({
                "table_name": headers[i].text,
                "table_data": []
            })

            for row in table.find_all("tr")[1:]:
                cells = row.find_all("td")

                data_tables[i]["table_data"].append({
                    "name": cells[0].text,
                    "ingredients": cells[1].text,
                    "image": cells[2].find("img")["src"],
                    "description": cells[3].text
                })

        self.data_frame = pd.DataFrame(data_tables)
        return self.data_frame


if __name__ == '__main__':
    rs = RecipeScraper()
    rs.scrape_url("https://www.minecraftcrafting.info/")
    print(rs.get_tables_data())
