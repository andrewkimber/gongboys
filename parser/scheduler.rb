### ruby scheduler.rb ARG
### ARG options: epl, primera, bundesliga, seria,ligue1, eredivisie, champs, europa

### gem install these tools to run this file.
require 'watir'
require 'nokogiri'
require 'pry-rails' # not necessary if you are not planning to try stuff on the rails console
require 'csv'
require 'date'

# browser setup, file setup
browser = Watir::Browser.new(:phantomjs)
file= CSV.open("scheduler_%{league}.csv" % {:league => ARGV[0]} ,'a')  #CSV 파일을 만듭니다


# 2017년 1월부터 5월까지의 리그 일정표를 따옵니다.
(1..5).each do |month|
  endpoint = "http://sports.news.naver.com/wfootball/schedule/index.nhn?date=20161205&year=2017&month=%{month}&category=%{league}" \
                                                  % { :month => month, :league => ARGV[0]}
  browser.goto(endpoint)
  doc = Nokogiri::HTML.parse(browser.html)
  schedule = doc.at_css("#_monthlyScheduleList")
  rows = schedule.css("tr") #select all the rows!
  
  date = ""  #initializing the date. If you don't do this, then the date will be scoped only inside the rows.each loop coded below.
  
  rows.each do |row|
    # site inspect를 해보면 날짜가 바뀔 때마다 .division class를 씁니다. 이 점에 착안해서 날짜를 keep track 하도록 짰습니다.
    ### row.css('.division').count > 0   :this code wouldn't work,
    ### since it would only look for '.division' element "BELOW" the row, not including the row itself.
    if row.first && (row.first[1] == "division" || row.first[1] == "today first")  # row.first refers to the ["class", "division"] TUPLE! 
      date = row.at_css('.inner').text.split().join(' ')   # 앞 뒤에 붙은 불필요한 \t\t\t 들 제거...
    end
    if row.css(".time_place").count > 0  #if there no game that day, skip.
      time = row.css(".time").text
      teams = row.css(".name")
      team1 = teams[0].text
      team2 = teams[1].text
      file << [date, time, team1, team2]
    end
  end
  puts "%{month} finished." % {:month => Date::MONTHNAMES[month]}
end

puts '"scheduler_%{league}.csv" created!' % {:league => ARGV[0]} 

