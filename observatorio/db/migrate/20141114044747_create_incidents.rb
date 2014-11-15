class CreateIncidents < ActiveRecord::Migration
  def change
    create_table :incidents do |t|
      t.integer :id_tweet
      t.integer :id_itype

      t.timestamps
    end
  end
end
