#### ruby football.rb first_month last_month league
###league: epl, primera, bundesliga, seria,ligue1, eredivisie, champs, europa


require 'watir'
require 'nokogiri'
require 'pry-rails'
require 'csv'

first_month=ARGV[0]
last_month=ARGV[1]
league=ARGV[2]

browser = Watir::Browser.new(:chrome)
file= CSV.open("%{league} %{first_month}_%{last_month}.csv" \
      % { :league => league, :first_month => first_month.to_s, :last_month => last_month.to_s },'a')



month=first_month.to_i

while month <= last_month.to_i

  endpoint = "http://sports.news.naver.com/wfootball/schedule/index.nhn?date=20161205&year=2016&month=%{month}&category=%{league}" \
                                                  % { :month => month, :league => league }
  browser.goto(endpoint)
  doc = Nokogiri::HTML.parse(browser.html)
  schedule = doc.at_css("#_monthlyScheduleList")
  rows = schedule.css("tr")
  
  selected_rows = rows.select do |row|
    #the former rules out rows with no-game, and the latter rules out rows with before_game.
    row.css(".time_place").count!=0 && row.css(".before_game").count==0
  end
  
  selected_rows.each do |row|
    time = row.css(".time").text
    teams = row.css(".name")
    scores = row.css(".score")
    team1 = teams[0].text
    team2 = teams[1].text
    score1 = scores[0].text
    score2 = scores[1].text
    #string = "%{team1} %{score1} : %{score2} %{team2} \n" % {:team1 => team1, :team2 => team2, :score1 => score1, :score2 => score2}
    file << [time, team1,score1,score2,team2]
  end
  month += 1
end
