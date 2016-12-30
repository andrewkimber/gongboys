# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rake db:seed (or created alongside the db with db:setup).
#
# Examples:
#
#   cities = City.create([{ name: 'Chicago' }, { name: 'Copenhagen' }])
#   Mayor.create(name: 'Emanuel', city: cities.first)
User.create!(name:  "김재윤",
             email: "andrewkimber@naver.com",
             password:              "asdfasdf",
             password_confirmation: "asdfasdf",
             admin: true)


99.times do |n|
  name  = Faker::Name.name
  email = "example-#{n+1}@railstutorial.org"
  password = "password"
  User.create!(name:  name,
               email: email,
               password:              password,
               password_confirmation: password)
end

50.times do |i|
  User.find_by(name: "김재윤").posts.create!(title: "Post #{i}", body: BetterLorem.p(5, false, false))
end