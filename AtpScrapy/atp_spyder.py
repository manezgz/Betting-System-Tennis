# -*- coding: utf-8 -*-
import scrapy
import json
import pandas
from scrapy import Selector
from TennisMatch import TennisMatch

class SouqSpider(scrapy.Spider):
    year=""
    URL_APPEND="/results"
    BASE_URL ="http://www.atpworldtour.com"
    CSV_URL = "/home/brisbane.csv"
    name = "Atp 2016"  # Name of the Spider, required value
    start_urls = ["http://www.atpworldtour.com/en/scores/results-archive?"]

    def __init__(self, year='', *args, **kwargs):
        super(SouqSpider, self).__init__(*args, **kwargs)
        self.year=year
        self.start_urls=["http://www.atpworldtour.com/en/scores/results-archive?"+self.year]


    # Entry point for the spider
    def parse(self, response):
        for href in response.css('.tourney-details a::attr(href)'):
            url = href.extract()
            url=self.BASE_URL+url;
            #url=url.replace('overview',self.year+self.URL_APPEND)
            #url=url.replace('tournaments','scores/archive')
            #print url;
            yield scrapy.Request(url, callback=self.parseTournament)


    def parseTournament(self,response):
        for href in response.css('.day-table-score a::attr(href)'):
            url = href.extract()
            url=self.BASE_URL+url;
            yield scrapy.Request(url, callback=self.parse_item)



    # Method for parsing a product page
    def parse_item(self, response):
        tennis_match=TennisMatch()
        contador=0;
        print "----------------------"

        #Extract Tournament
        tennis_match.tournament=response.css('.section-title::text')[0].extract().strip()

        div = response.css('.won-game')
        tennis_match.winner_name=div.css("div.scoring-player a.scoring-player-name::text")[0].extract().strip()
        #Extract Players
        for a in response.css('.scoring-player-name::text'):
            if tennis_match.p1=="":
                tennis_match.p1 = a.extract().strip()
            else:
                tennis_match.p2 = a.extract().strip()
        #Extract Winner
        div = response.css('.won-game')
        tennis_match.winner_name=div.css("div.scoring-player a.scoring-player-name::text")[0].extract().strip()

        #Extract Round
        round = response.css('.title-area::text')[0].extract().strip()
        tennis_match.round=round;

        #Extract Duration
        duration = response.css('.time::text')[0].extract().strip()[-8:]
        tennis_match.duration=duration;

        #Extract Result
        table = response.css('.scores-table')
        trs = table.css("tbody tr");
        tr_winner=trs[0];
        tr_looser=trs[1];
        tds_winner=tr_winner.css('td');
        tds_looser=tr_looser.css('td');
        tennis_match.set1_games_p1=tds_winner[1].css('span::text')[0].extract().strip();
        tennis_match.set1_games_p2=tds_looser[1].css('span::text')[0].extract().strip();

        if(len(tds_winner)>=3):
            tennis_match.set2_games_p1=tds_winner[2].css('span::text')[0].extract().strip();
            tennis_match.set2_games_p2=tds_looser[2].css('span::text')[0].extract().strip();

        if(len(tds_winner)==4):
            tennis_match.set3_games_p1=tds_winner[3].css('span::text')[0].extract().strip();
            tennis_match.set3_games_p2=tds_looser[3].css('span::text')[0].extract().strip();
            tennis_match.sets_duration="3";
        elif(len(tds_winner)==5):
            tennis_match.set4_games_p1=tds_winner[4].css('span::text')[0].extract().strip();
            tennis_match.set4_games_p2=tds_looser[4].css('span::text')[0].extract().strip();
            tennis_match.sets_duration="4";
        elif(len(tds_winner)==6):
            tennis_match.set5_games_p1=tds_winner[5].css('span::text')[0].extract().strip();
            tennis_match.set5_games_p2=tds_looser[5].css('span::text')[0].extract().strip();
            tennis_match.sets_duration="5";
        elif(len(tds_winner)==3):
            tennis_match.sets_duration="2";
        tr_looser=trs[1];

        #extract Match Stats
        script = response.css('script[id="matchStatsData"]::text')
        s_json=script.extract()
        stats = json.loads(s_json[0]);
        stats_p1=stats[0]['playerStats'];
        stats_p2=stats[0]['opponentStats'];

        #Extract Aces
        tennis_match.aces_p1=stats_p1['Aces']
        tennis_match.aces_p2=stats_p2['Aces']

        #Extract Aces %
        tennis_match.aces_ratio_p1=stats_p1['AcesPercentage']
        tennis_match.aces_ratio_p2=stats_p2['AcesPercentage']

        #Extract Double Fouls
        tennis_match.double_faults_p1=stats_p1['DoubleFaults']
        tennis_match.double_faults_p2=stats_p2['DoubleFaults']

        #FirstService
        tennis_match.first_serve_percent_p1=stats_p1['FirstServePercentage']
        tennis_match.first_serve_percent_p2=stats_p2['FirstServePercentage']
        tennis_match.first_serve_dividend_p1=stats_p1['FirstServeDividend']
        tennis_match.first_serve_divisor_p1=stats_p1['FirstServeDivisor']
        tennis_match.first_serve_dividend_p2=stats_p2['FirstServeDividend']
        tennis_match.first_serve_divisor_p2=stats_p2['FirstServeDivisor']

        tennis_match.first_serve_percent_points_won_p1=stats_p1['FirstServePointsWonPercentage']
        tennis_match.first_serve_percent_points_won_p2=stats_p2['FirstServePointsWonPercentage']
        tennis_match.first_serve_points_won_dividend_p1=stats_p1['FirstServePointsWonDividend']
        tennis_match.first_serve_points_won_divisor_p1=stats_p1['FirstServePointsWonDivisor']
        tennis_match.first_serve_points_won_dividend_p2=stats_p2['FirstServePointsWonDividend']
        tennis_match.first_serve_points_won_divisor_p2=stats_p2['FirstServePointsWonDivisor']

        #SecondsService
        tennis_match.second_serve_percent_points_won_p1=stats_p1['SecondServePointsWonPercentage']
        tennis_match.second_serve_percent_points_won_p2=stats_p2['SecondServePointsWonPercentage']
        tennis_match.second_serve_points_won_dividend_p1=stats_p1['SecondServePointsWonDividend']
        tennis_match.second_serve_points_won_divisor_p1=stats_p1['SecondServePointsWonDivisor']
        tennis_match.second_serve_points_won_dividend_p2=stats_p2['SecondServePointsWonDividend']
        tennis_match.second_serve_points_won_divisor_p2=stats_p2['SecondServePointsWonDivisor']

        #Añadimos el tennis_match al array
        tennis_match.print_data()
        yield tennis_match.__dict__
