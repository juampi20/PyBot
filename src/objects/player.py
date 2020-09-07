from riotwatcher import LolWatcher
import os

watcher = LolWatcher(os.environ.get("RIOT_API_TOKEN"))
default_region = "la2"

class Player:
    def __init__(self, name: str):
        summoner = watcher.summoner.by_name(default_region, name)

        # Main account information
        self.name = summoner['name']
        self.level = str(summoner['summonerLevel'])
        self.revision_date = summoner['revisionDate']
        self.id = summoner['id']
        self.account_id = summoner['accountId']
        self.profile_icon_id = summoner["profileIconId"]

        # Ranked information
        self.solo_rank = 'N/A'
        self.flex_rank = 'N/A'
        self.solo_duo_tier = 'N/A'
        self.flex_tier = 'N/A'
        
        self.get_ranked_stats()

    def to_string(self):
        print(f"""
        Summoner:
        \tName: {self.name}
        \tID: {self.id}
        \tAccount ID: {self.account_id}
        \tLevel: {self.level}
        \tRevision date: {self.revision_date}
        \tProfile icon ID: {self.profile_icon_id}
        """)

        print(f"""
        Tier:
        Solo/Duo: {self.solo_duo_tier}
        Flex 5v5: {self.flex_tier}
        """)

        print(f"""
        Ranked:
        \tSolo/Duo: {self.solo_rank}
        \tFlex 5v5: {self.flex_rank}
        """)

    def get_ranked_stats(self):
        ranked_stats = watcher.league.by_summoner(default_region, self.id)
           
        for stats in ranked_stats:
            if stats['queueType'] == 'RANKED_SOLO_5x5':
                self.solo_rank = rank_to_string(stats)
                self.solo_duo_tier = stats['tier'].lower().capitalize()
            elif stats['queueType'] == 'RANKED_FLEX_SR':
                self.flex_rank = rank_to_string(stats)
                self.flex_tier = stats['tier'].lower().capitalize()

def rank_to_string(ranked_stats):
    tier = ranked_stats['tier'].lower().capitalize()
    rank = str(ranked_stats['rank'])
    league_points = str(ranked_stats['leaguePoints'])

    ret = tier + ' ' + rank + ' (' + league_points + 'LP)'

    return ret
