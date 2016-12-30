##ruby druginfo.rb

require 'watir'
require 'nokogiri'
require 'pry-rails'

medication = ARGV[0].to_s  ##얘를 ARGV로 넣고 싶었으나.... Commandline이 그지같이 한글을 인식을 못해서 ㅠㅠ

file = File.new('%{medication}.txt' % {:medication => medication}, 'w+')

browser = Watir::Browser.new(:phantomjs)

browser.goto("http://patient.druginfo.co.kr/cp/kaphd/search/search_cp_main.aspx")
browser.text_field(:id => 'product').set medication
browser.button(:name => 'Image101').click
browser.a(:class => 'search02').click
browser.img(:width => '103').click


##원하는 iframe이 nested iframe이라, mother -> child 순서로 순차적으로 접근해야.
browser.driver.switch_to.frame('patient')
browser.driver.switch_to.frame('iframeRight')

doc = Nokogiri::HTML.parse(browser.html)
table = doc.at_css(".t_td4")

rows = table.css('tr').select { |row| row.css("td").count==6 }

rows.each do |row|
  code = row.css('td')[1].text #상병코드
  name = row.css('td')[4].text #상병명
  file.write(code+", "+name+ " \n")
end

puts "Finished!"
