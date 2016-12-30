require 'watir'
require 'pry-rails'
require 'nokogiri'

endpoint = "http://finance.naver.com/item/main.nhn?code=005930"
browser = Watir::Browser.new(:chrome)
browser.goto endpoint
browser.ul(class: "tabs_submenu tab_total_submenu").a(class: "tab2").click

data = []
for i in 1..30 do
	doc = Nokogiri::HTML.parse(browser.iframe(index: 8).html)
	stock_table = doc.at_css("table")
	rows = stock_table.css("tr")
	rows = rows.select {|row| row.css("th").empty? && row.css("td").count >1 }
	
	rows.map! { |row|
		[row.at_css("td:nth-child(1)").text, row.at_css("td:nth-child(2)").text]  ##.try 지움!
		}

	rows.each { |row|
		data.push row  ##append 대신 push로!
	}


	if i%10 == 0 
		browser.iframe(index: 8).table(class: "Nnavi").link(text: "다음").click  ##click 붙임!
	else
		browser.iframe(index: 8).table(class: "Nnavi").link(text: "#{i+1}").click #여기도 데헷!
	end


	sleep 0.5

end

puts data  #출력출력
