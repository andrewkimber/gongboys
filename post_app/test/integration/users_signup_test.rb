require 'test_helper'

class UsersSignupTest < ActionDispatch::IntegrationTest

  test "invalid signup information" do
    get new_user_path
    assert_no_difference "User.count" do
      post users_path, user: { name: "", email: "user@invalid", password:"foo", password_confirmation: "foo" }
    end
    ##Rails 5부터는 post users_path, params: { user: {name: asdfasdfasdf}} 로 strong parameter를 삽입해줘야 한다!!!
    assert_template 'users/new'
    assert_select 'div#error_explanation'
  end
  
  test "valid signup information" do
    get new_user_path
    assert_difference "User.count", 1 do
      post users_path, user: {name:"Foo Bar", email: "foobar@valid.com", password:"foobar", password_confirmation:"foobar"}
    end
    follow_redirect!
    assert_template 'users/show'
    assert_select 'p#notice'
    assert is_logged_in?
  end
end