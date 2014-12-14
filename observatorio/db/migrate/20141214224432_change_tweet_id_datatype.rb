class ChangeTweetIdDatatype < ActiveRecord::Migration
  def change
    change_column :incidents, :tweet_id, :string
  end
end
