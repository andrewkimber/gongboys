class SessionsController < ApplicationController
  before_action :remember_location, :back

  def new
  end

  def create
    user = User.find_by(email: params[:session][:email].downcase)
    if user && user.authenticate(params[:session][:password])
      log_in user
      params[:session][:remember_me]=='1'? remember(user) : forget(user)
      redirect_back_or user
    else
      redirect_to login_path, notice: "Invalid Email/password combination."
    end
  end

  def destroy
    ## logging out is only done when you're only logged in.
    ##So, a second logout click from a second window wouldn't cause a problem!
    log_out if logged_in?
    redirect_to root_path, notice: "Good bye!"
  end
end
