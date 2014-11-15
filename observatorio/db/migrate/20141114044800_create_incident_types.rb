class CreateIncidentTypes < ActiveRecord::Migration
  def change
    create_table :incident_types do |t|
      t.string :itype_desc, limit: 40

      t.timestamps
    end
  end
end
