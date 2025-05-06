import requests
import pandas as pd
from bs4 import BeautifulSoup

def get_scouting_report(player_slug):
    """
    Given a 'player_slug' (e.g., 'victor-wembanyama'),
    this function scrapes the scouting report from nbadraft.net.
    Returns the combined text from Strengths, Weaknesses, and Outlook.
    """
    url = f"https://www.nbadraft.net/players/{player_slug}/"
    response = requests.get(url)
    
    # Check for a successful response
    if response.status_code != 200:
        print(f"Could not retrieve page for {player_slug}. Status code: {response.status_code}")
        return ""
    
    soup = BeautifulSoup(response.text, 'html.parser')

    # Look for the div with id="analysis"
    analysis_div = soup.find("div", {"id": "analysis"})
    if not analysis_div:
        print(f"No analysis section found for {player_slug}.")
        return ""
    
    # Extract all text (Strengths, Weaknesses, Outlook) from the analysis div
    scouting_report_text = analysis_div.get_text(separator="\n", strip=True)
    
    return scouting_report_text


def main():
    # Complete list of likely player slugs for the 2023 NBA Rookies
    player_slugs = [
        "victor-wembanyama",
        "brandon-miller",
        "scoot-henderson",
        "amen-thompson",
        "ausar-thompson",
        "anthony-black",
        "bilal-coulibaly",
        "jarace-walker",
        "taylor-hendricks",
        "cason-wallace",
        "jett-howard",
        "dereck-lively",
        "gradey-dick",
        "jordan-hawkins",
        "kobe-bufkin",
        "keyonte-george",
        "jalen-hood-schifino",
        "jaime-jaquez",
        "brandin-podziemski",
        "cam-whitmore",
        "dariq-whitehead",
        "noah-clowney",
        "kris-murray",
        "olivier-maxence-prosper",
        "marcus-sasser",
        "ben-sheppard",
        # Nick Smith is often listed as Nick Smith Jr.
        "nick-smith",
        "brice-sensabaugh",
        "julian-strawther",
        "kobe-brown",
        "james-nnaji",
        "jalen-pickett",
        "leonard-miller",
        "colby-jones",
        "julian-phillips",
        # Sometimes listed as Andre Jackson Jr.
        "andre-jackson",
        "hunter-tyson",
        "jordan-walsh",
        "mouhamed-gueye",
        "maxwell-lewis",
        "amari-bailey",
        "tristan-vukcevic",
        "rayan-rupert",
        "sidy-cissoko",
        # Often referred to as GG Jackson
        "gg-jackson",
        "seth-lundy",
        "mojave-king",
        "jordan-miller",
        "emoni-bates",
        "keyontae-johnson",
        "jalen-wilson",
        "toumani-camara",
        "jaylen-clark",
        "jalen-slawson",
        "isaiah-wong",
        "tarik-biberovic",
        "trayce-jackson-davis",
        "chris-livingston"
    ]

    data = []

    for slug in player_slugs:
        report = get_scouting_report(slug)
        # Convert slug to a more readable name if desired
        # For example, "victor-wembanyama" -> "Victor Wembanyama"
        player_name = slug.replace("-", " ").title()
        
        data.append({
            "PlayerName": player_name,
            "ScoutingReport": report
        })
    
    # Create a DataFrame and save to CSV
    df = pd.DataFrame(data, columns=["PlayerName", "ScoutingReport"])
    df.to_csv("2023_nba_draft_scouting_reports.csv", index=False)
    print("CSV file '2023_nba_draft_scouting_reports.csv' created successfully.")


if __name__ == "__main__":
    main()
