class CreateUsers < ActiveRecord::Migration
  def change
    create_table :users do |t|
      t.string :name, limit: 100
      t.string :timezone, limit: 100
      t.string :language, limit: 100
      t.integer :followers
      t.string :description

      t.timestamps
    end
  end
end
