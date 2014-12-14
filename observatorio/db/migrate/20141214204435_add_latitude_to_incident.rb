class AddLatitudeToIncident < ActiveRecord::Migration
  def change
    add_column :incidents, :latitude, :decimal, precision: 9, scale: 6
  end
end
