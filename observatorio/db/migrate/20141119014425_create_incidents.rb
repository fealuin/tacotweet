class CreateIncidents < ActiveRecord::Migration
  def change
    create_table :incidents do |t|

      t.timestamps
    end
  end
end
