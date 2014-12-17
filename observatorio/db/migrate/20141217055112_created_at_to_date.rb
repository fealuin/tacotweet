class CreatedAtToDate < ActiveRecord::Migration
  def change
    change_column :incidents, :created_at, :date
  end
end
