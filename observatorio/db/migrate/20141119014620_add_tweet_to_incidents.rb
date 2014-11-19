class AddTweetToIncidents < ActiveRecord::Migration
  def change
    add_reference :incidents, :tweet, index: true
  end
end
