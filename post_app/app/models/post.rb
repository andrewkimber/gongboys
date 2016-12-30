class Post < ActiveRecord::Base
  default_scope{order("created_at DESC")}
  
  has_many :comments, dependent: :destroy
  belongs_to :user
  
  self.per_page = 5
end
