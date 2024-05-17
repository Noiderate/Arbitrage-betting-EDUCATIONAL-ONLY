class TennisOBJ:
    def __init__(self, team1, odds1, team2, odds2):
        team1_cleaned = ''.join(team1.split()).upper()
        team2_cleaned = ''.join(team2.split()).upper()

        if team1_cleaned > team2_cleaned:
            temp = team2_cleaned 
            team2_cleaned = team1_cleaned
            team1_cleaned = temp

            temp2 = odds2
            odds2 = odds1
            odds1 = temp2


        self.team1 = team1_cleaned
        self.team2 = team2_cleaned
        self.odds1 = odds1
        self.odds2 = odds2
        
    
    def print_odds(self):
        print(f"team 1: {self.team1} | {self.odds1},  team 2:  {self.team2} | {self.odds2}")

class ComparisonOBJ:
        def __init__(self, team1, team2, odds1_web1, odds2_web1, odds1_web2, odds2_web2):
            self.team1 = team1
            self.team2 = team2
            self.odds1_web1 = float(odds1_web1)
            self.odds1_web2 = float(odds1_web2) 
            self.odds2_web1 = float(odds2_web1) 
            self.odds2_web2 = float(odds2_web2) 
        
        def print_odds(self):
            print(f"{self.team1}  |  {self.team2} \n{self.odds1_web1}  |  {self.odds2_web1} \n{self.odds1_web2}  |  {self.odds2_web2}")

        def find_arbitrage_opportunities(comparison_objects):
            arbitrage_opportunities = []

            for item in comparison_objects:
                combined_implied_probability_1 = 1 / item.odds1_web1 + 1/ item.odds2_web2
                combined_implied_probability_2 = 1 / item.odds2_web1 + 1 / item.odds1_web2
                
                if combined_implied_probability_1 < 1:
                    arbitrage_opportunities.append((item, combined_implied_probability_1))
                if combined_implied_probability_2 < 1:
                    arbitrage_opportunities.append((item, combined_implied_probability_2))

            return arbitrage_opportunities
        
        def print_all_items(items):
            for item in items:
                item.print_odds()
