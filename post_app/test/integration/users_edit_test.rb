require 'test_helper'

class UsersEditTest < ActionDispatch::IntegrationTest
  def setup
    @user= users(:andrew)
    @other_user= users(:archer)
  end
  
  test "unsuccessful edit" do
    log_in_as(@user, remember_me: '0')
    assert is_logged_in?
    get edit_user_path(@user)
    assert_template 'users/edit'
    patch user_path(@user), user: {name: "", email: "foo@invalid", password: "foo", password_confirmation: "bar"}
    assert_template :edit
    assert_select 'div#error_explanation'
  end
  
  test "successful edit" do
    log_in_as(@user, remember_me: '0')
    assert is_logged_in?
    get edit_user_path(@user)
    assert_template 'users/edit'
    name="Foo Bar"
    email="foo@bar.com"
    patch user_path(@user), user: {name: name, email: email, password: "", password_confirmation: ""}
    assert_redirected_to @user
    @user.reload
    assert_equal name, @user.name
    assert_equal email, @user.email
  end
  
  test "should redirect edit when not logged in" do
    get edit_user_path(@user)
    assert_redirected_to login_path
  end
  
  test "should redirect update when not logged in" do
    patch user_path(@user), user: { name: @user.name, email: @user.email }
    assert_redirected_to login_path
  end
    
  test "should redirect edit when logged in as wrong user" do
    log_in_as(@other_user, remember_me: '0')
    get edit_user_path(@user)
    assert_redirected_to root_url
  end

  test "should redirect update when logged in as wrong user" do
    log_in_as(@other_user, remember_me: '0')
    patch user_path(@user), user: { name: @user.name, email: @user.email }
    assert_redirected_to root_url
  end  
end
