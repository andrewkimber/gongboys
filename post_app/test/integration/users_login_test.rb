require 'test_helper'

class UsersLoginTest < ActionDispatch::IntegrationTest
  
  def setup
    @user=users(:andrew)
  end
  
  test "login with invalid information" do
    get login_path
    assert_template 'sessions/new'
    post login_path, session: {email: " ", password: " "}
    assert_not is_logged_in?
    assert_redirected_to login_path
    follow_redirect!
    get root_path
    assert_template 'posts/index'
  end
  
  test "login with valid information" do
    get root_path
    assert_select "a[href=?]", new_post_path, count: 0
    assert_select "a[href=?]", login_path
    assert_select "a[href=?]", logout_path, count: 0
    assert_select "a[href=?]", new_user_path
    assert_select "a[href=?]", user_path(@user), count: 0
    #now let's log in.
    get login_path
    post login_path, session: {email: @user.email, password: 'asdfasdf'}
    assert is_logged_in?
    assert_redirected_to @user
    follow_redirect!
    assert_template 'users/show'
    assert_select "a[href=?]", new_post_path
    assert_select "a[href=?]", login_path, count: 0
    assert_select "a[href=?]", logout_path
    assert_select "a[href=?]", user_path(@user)
    assert_select "a[href=?]", new_user_path, count: 0
  end
  
  test "login with valid information followed by logout" do
    get login_path
    post login_path, session: { email:    @user.email,
                                          password: 'asdfasdf' }
    assert is_logged_in?
    assert_redirected_to @user
    follow_redirect!
    delete logout_path
    assert_not is_logged_in?
    assert_redirected_to root_path
    follow_redirect!
    assert_template 'posts/index'
  end
  
  test "login followed by two logouts" do
    get login_path
    post login_path, session: {email: @user.email, password: 'asdfasdf'}
    assert is_logged_in?
    assert_redirected_to @user
    follow_redirect!
    delete logout_path
    assert_not is_logged_in?
    assert_redirected_to root_path
    #Simulating the second logout click in the second wondow
    delete logout_path
    follow_redirect!
    assert_template 'posts/index'
  end
  
  test "login with remembering" do
    log_in_as(@user,remember_me: '1')
    assert_not_nil cookies['remember_token']
  end
  
  test "login without remembering" do
    log_in_as(@user,remember_me: '0')
    assert_nil cookies['remember_token']
  end
end
