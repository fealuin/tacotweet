class AddLongitudeToIncident < ActiveRecord::Migration
  def change
    add_column :incidents, :longitude, :decimal, precision: 9, scale: 6
  end
end
