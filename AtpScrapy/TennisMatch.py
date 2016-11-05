__author__ = 'mane'

class TennisMatch:
    def __init__(self):
        self.p1="";
        self.p2="";
        self.winner_name="";
        self.duration="";
        self.round="";
        self.aces_p1=""
        self.double_fouls_p1=""
        self.double_fouls_p2=""
        self.aces_p2=""
        self.aces_ratio_p1=""
        self.aces_ratio_p2=""
        self.sets_duration=""
        self.set1_games_p1=""
        self.set1_games_p2=""
        self.set2_games_p1=""
        self.set2_games_p2=""
        self.set3_games_p1=""
        self.set3_games_p2=""
        self.set4_games_p1=""
        self.set4_games_p2=""
        self.set5_games_p1=""
        self.set5_games_p2=""
        self.double_faults_p1=""
        self.double_faults_p2=""
        self.first_serve_percent_p1=""
        self.first_serve_percent_p2=""
        self.first_serve_dividend_p1=""
        self.first_serve_divisor_p1=""
        self.first_serve_dividend_p2=""
        self.first_serve_divisor_p2=""
        self.first_serve_percent_points_won_p1=""
        self.first_serve_percent_points_won_p2=""
        self.first_serve_points_won_dividend_p1=""
        self.first_serve_points_won_divisor_p1=""
        self.first_serve_points_won_dividend_p2=""
        self.first_serve_points_won_divisor_p2=""
        self.second_serve_percent_points_won_p1=""
        self.second_serve_percent_points_won_p2=""
        self.second_serve_points_won_dividend_p1=""
        self.second_serve_points_won_divisor_p1=""
        self.second_serve_points_won_dividend_p2=""
        self.second_serve_points_won_divisor_p2=""
        self.tournament=""
        self.match_date=""

    def print_data(self):
        print "Tournament {}".format(self.tournament)
        print "Round "+self.round
        print "Duration "+self.duration
        print "Winner "+self.winner_name
        print "P1 "+self.p1
        print "P2 "+self.p2
        print "Set Duration {} ".format(self.sets_duration)
        print "P1 S1 Games {} ".format(self.set1_games_p1)
        print "P2 S1 Games {} ".format(self.set1_games_p2)
        print "P1 S2 Games {} ".format(self.set2_games_p1)
        print "P2 S2 Games {} ".format(self.set2_games_p2)
        print "P1 S3 Games {} ".format(self.set3_games_p1)
        print "P2 S3 Games {} ".format(self.set3_games_p2)
        print "Aces P1 {}".format(self.aces_p1)
        print "Aces P2 {}".format(self.aces_p2)
        print "Aces % P1 {}".format(self.aces_ratio_p1)
        print "Aces % P2 {}".format(self.aces_ratio_p2)
        print "Double Faults P1 {}".format(self.double_faults_p1)
        print "Double Faults P2 {}".format(self.double_faults_p2)
        print "First Serve Percentage P1 {}".format(self.first_serve_percent_p1)
        print "First Serve Percentage P2 {}".format(self.first_serve_percent_p2)
        print "First Serve Percentage P1 {}/{}".format(self.first_serve_dividend_p1,self.first_serve_divisor_p1)
        print "First Serve Percentage P2 {}/{}".format(self.first_serve_dividend_p2,self.first_serve_divisor_p2)
        print "First Serve Points Won P1 % {}".format(self.first_serve_percent_points_won_p1)
        print "First Serve Points Won P2 % {}".format(self.first_serve_percent_points_won_p2)
        print "First Serve Points Won P1 {}/{}".format(self.first_serve_points_won_dividend_p1,self.first_serve_points_won_divisor_p1)
        print "First Serve Points Won P2 {}/{}".format(self.first_serve_points_won_dividend_p2,self.first_serve_points_won_divisor_p2)
        print "Second Serve Points Won P1 % {}".format(self.second_serve_percent_points_won_p1)
        print "Second Serve Points Won P2 % {}".format(self.second_serve_percent_points_won_p2)
        print "Second Serve Points Won P1 {}/{}".format(self.second_serve_points_won_dividend_p1,self.first_serve_points_won_divisor_p1)
        print "First Serve Points Won P2 {}/{}".format(self.second_serve_points_won_dividend_p2,self.first_serve_points_won_divisor_p2)

        print "----------------------"


