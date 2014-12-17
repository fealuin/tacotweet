class AddColumnToIncidents < ActiveRecord::Migration
  def change
    add_column :incidents, :text, :string
  end
end
