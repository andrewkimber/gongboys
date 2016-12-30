## ruby stocks.rb code num
##code: 주식 코드
##num: num*10개의 data를 뽑아냄.

require 'watir'
require 'pry-rails'
require 'nokogiri'
require 'csv'

browser = Watir::Browser.new(:chrome)
file = File.new('stock_%{code}.txt' % {:code => ARGV[0]},'w+')
csv = CSV.open('stock_%{code}.csv' % {:code => ARGV[0]}, 'a')

num=1

while num <= ARGV[1].to_i
  endpoint = "http://finance.naver.com/item/sise_day.nhn?code=%{code}&page=%{num}" % {:code => ARGV[0], :num => num}
  browser.goto(endpoint)
  doc = Nokogiri::HTML.parse(browser.html)
  rows = doc.xpath('//tr[@onmouseover="mouseOver(this)"]')
  rows.each do |row|
    tuple = []
    row.css("td").each do |td|
      if td == row.css('td').first
        tuple << td.text.split(",").join()
      else
        tuple << td.text.split(",").join().to_i
      end
    end
    file.write(tuple.to_s + "\n")
    csv << tuple
  end
  num += 1
end
