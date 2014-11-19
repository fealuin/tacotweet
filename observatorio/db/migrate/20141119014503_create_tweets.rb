class CreateTweets < ActiveRecord::Migration
  def change
    create_table :tweets do |t|
      t.string :text
      t.integer :retweets
      t.string :source, limit: 100
      t.string :coordinates
      t.integer :procesado
      t.integer :geoenable
      t.string :id_twitter, limit: 100

      t.timestamps
    end
  end
end
