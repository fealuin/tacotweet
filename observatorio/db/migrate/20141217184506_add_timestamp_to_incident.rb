class AddTimestampToIncident < ActiveRecord::Migration
  def change
    add_column :incidents, :timestamp, :datetime
  end
end
