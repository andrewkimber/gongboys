class CommentsController < ApplicationController
  before_action :set_comment, only: [:edit, :update, :destroy]
  before_action :logged_in_user, only: [:edit, :create, :update, :destroy]
  before_action :comment_authorized, only: [:edit, :update, :destroy]


  # POST /comments
  # POST /comments.json
  def create
    @comment = current_user.comments.new(comment_params)
    @comment.save
  end

  def edit
  end
  
  def update
    @comment.update(comment_params)
    respond_to do |format|
      format.html { render @comment.post }
      format.js
    end
  end

  # DELETE /comments/1
  # DELETE /comments/1.json
  def destroy
    @comment.destroy
    respond_to do |format|
      format.html { render @comment.post }
      format.js
    end
  end


  private
    # Use callbacks to share common setup or constraints between actions.
  def set_comment
    @comment = Comment.find(params[:id])
  end

  # Never trust parameters from the scary internet, only allow the white list through.
  def comment_params
    params.require(:comment).permit(:body, :post_id, :user_id)
  end
   
  #callback
  def comment_authorized
    #This code is necessary in general.
    #But since it is already set by set_comment callback for :destroy method
                    #(the method post_authorized is supposed to callback upon),
                    #this code is unnecessary in this case! Nevertheless, beware.
    #@comment=Comment.find(params[:id])
    redirect_to(@comment.post, notice: 'Invalid user') unless (current_user == @comment.user || current_user.admin?)
  end
end
