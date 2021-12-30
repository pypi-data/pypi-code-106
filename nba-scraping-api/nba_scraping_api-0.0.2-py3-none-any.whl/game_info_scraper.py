import json
import pickle
from datetime import datetime
from io import StringIO

import boto3
import pandas as pd
import requests
from bs4 import BeautifulSoup
import os 


class GameMetaInfoScraper:
    def __init__(self, year: str, month: str, day: str, s3_client):
        self.year = year
        self.month = month
        self.day = day
        self.s3_client = s3_client

    def scrape_games(self) -> pd.DataFrame:
        date_info = f"{self.year}-{self.month}-{self.day}"

        url = f"https://www.nba.com/games?date={date_info}"
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")

        game_urls = []

        for link in soup.find_all("a"):
            href = link["href"]
            if (
                "/game/" in href
                and "watch" not in href
                and "box-score" not in href
                and href not in game_urls
            ):
                game_urls.append(href)

        game_info_list = []

        for url in game_urls:
            if len(str(self.month)) < 2:
                month = f"0{month}"

            teams = url.split("/")[2]
            home_team = teams.split("-")[2].upper()
            away_team = teams.split("-")[0].upper()
            game_id = teams.split("-")[3]

            mid = f"{home_team}{self.month}{self.day}"

            game_info = {
                "mid": mid,
                "game_id": str(game_id),
                "game_url": f"https://www.nba.com{url}",
                "home_team": home_team,
                "away_team": away_team,
            }

            game_info_list.append(game_info)

        game_info_df = pd.DataFrame(game_info_list)

        return game_info_df

    def convert_odds(self, odd: str) -> float:
        odd_int = int(odd[1:])
        if odd[0] == "+":
            return (odd_int / 100) + 1
        else:
            return (100 / odd_int) + 1

    def scrape_odds(self) -> pd.DataFrame:
        url = "https://www.oddsshark.com/nba/odds"
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")

        game_data = soup.find_all(attrs={"class": "op-item-row-wrapper not-futures"})

        odds_features_list = []

        for game in game_data:
            money_lines = game.find_all(attrs={"class": "op-item op-spread op-opening"})

            home_odds = eval(money_lines[1]["data-op-moneyline"])["fullgame"]
            away_odds = eval(money_lines[0]["data-op-moneyline"])["fullgame"]

            if home_odds and away_odds:
                home_odds_converted = self.convert_odds(home_odds)
                away_odds_converted = self.convert_odds(away_odds)

                if home_odds_converted > away_odds_converted:
                    home_favored = False
                else:
                    home_favored = True

                odds_features = {
                    "home_odds": home_odds_converted,
                    "away_odds": away_odds_converted,
                    "home_favored": home_favored,
                }

                odds_features_list.append(odds_features)

        odds_df = pd.DataFrame(odds_features_list)
        mids = self.create_game_id(r)
        odds_df["mid"] = mids[: len(odds_df)]

        return odds_df


    def create_game_id(self, r) -> list:
        abbrev_dict = pickle.load(open("scraper/team_abbrev_dict.pkl", "rb"))
        game_events = json.loads(
            str(r.content)
            .split('<script type="application/ld+json">')[1]
            .split("</script>")[0]
            .replace("\\n", "")
        )

        mids = []

        for event in game_events:
            if len(str(self.month)) < 2:
                self.month = f"0{self.month}"

            home_team_name = event["homeTeam"]["name"]
            home_team_abbrev = abbrev_dict[home_team_name]
            mid = f"{home_team_abbrev}{self.month}{self.day}"
            mids.append(mid)

        return mids

    def merge_and_save_csv(self):
        game_info_df = self.scrape_games()
        odds_df = self.scrape_odds()

        betting_info_df = pd.merge(game_info_df, odds_df, on="mid", how="inner")
        betting_info_df["completed"] = False

        csv_buf = StringIO()
        betting_info_df.to_csv(csv_buf, header=True, index=False)
        csv_buf.seek(0)

        if datetime.now().hour in range(0, 8):
            use_day = datetime.now().day - 1
        else:
            use_day = datetime.now().day

        self.s3_client.put_object(
            Bucket="ml-nba-betting",
            Body=csv_buf.getvalue(),
            Key=f"nba_games/nba_games_{self.year}_{self.month}_{use_day}.csv",
        )


def scrape_games() -> None:

    aws_access_key_id = "AKIAY2SCPCT6XKAIJI6L"
    aws_secret_access_key = "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"
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
    )

    year = str(datetime.now().year)
    month = str(datetime.now().month)
    day = str(datetime.now().day)

    g = GameMetaInfoScraper(year=year, month=month, day=day, s3_client=s3_client)
    g.merge_and_save_csv()


if __name__ == "__main__":
    scrape_games()
