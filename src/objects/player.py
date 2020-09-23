import json
import datetime
from settings import RIOT_API_TOKEN
from riotwatcher import LolWatcher


watcher = LolWatcher(RIOT_API_TOKEN)
default_region = 'las'


class Player:
    def __init__(self, name):
        print('[Player] Buscando.')
        summoner = watcher.summoner.by_name(default_region, 'Franxs')
        print(summoner)
        print('[Player] Encontrado.')
        # Main account information
        self.name = summoner['name']
        self.summoner_level = str(summoner['summonerLevel'])
        self.revision_date = summoner['revisionDate']
        self.id = summoner['id']
        self.account_id = summoner['accountId']

        # Ranked information
        self.solo_rank = 'N/A'
        self.flex_rank = 'N/A'
        self.threes_rank = 'N/A'
        self.solo_duo_tier = 'N/A'
        self.flex_tier = 'N/A'
        self.threes_tier = 'N/A'

        self.get_ranked_stats()

    def to_string(self):
        ret = 'Name: ' + self.name + '\n'
        ret += '\tSummoner Level: ' + self.summoner_level + '\n'
        ret += '\tRevision Date: ' + datetime.datetime.fromtimestamp(
            self.revision_date/1000.0).strftime('%m-%d-%Y %H:%M:%S') + '\n'
        ret += '\tID: ' + str(self.id) + '\n'
        ret += '\tAccount ID: ' + str(self.account_id) + '\n'
        ret += '\tRanked: \n'
        ret += '\t\tSolo/Duo - ' + self.solo_rank + '\n'
        ret += '\t\tFlex 5v5 - ' + self.flex_rank + '\n'
        ret += '\t\tFlex 3v3 - ' + self.threes_rank

        return ret

    def get_ranked_stats(self):
        ranked_stats = watcher.league.by_summoner(default_region, self.id)

        for stats in ranked_stats:
            queue_type = stats.get('queueType')

            if queue_type == 'RANKED_SOLO_5x5':
                self.solo_rank = rank_to_string(stats)
                self.solo_duo_tier = stats.get('tier').lower().capitalize()
            elif queue_type == 'RANKED_FLEX_SR':
                self.flex_rank = rank_to_string(stats)
                self.flex_tier = stats.get('tier').lower().capitalize()
            else:
                self.threes_rank = rank_to_string(stats)
                self.threes_tier = stats.get('tier').lower().capitalize()

    def get_version(self):
        versions = watcher.data_dragon.versions_for_region(default_region)
        return versions[0]


def rank_to_string(ranked_stats):
    tier = ranked_stats.get('tier').lower().capitalize()
    rank = ranked_stats.get('rank')
    league_points = str(ranked_stats.get('leaguePoints'))

    ret = tier + ' ' + rank + ' (' + league_points + 'LP)'

    return ret
