# encoding: UTF-8
# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 20141114044824) do

  create_table "incident_types", force: true do |t|
    t.string   "itype_desc", limit: 40
    t.datetime "created_at"
    t.datetime "updated_at"
  end

  create_table "incidents", force: true do |t|
    t.integer  "id_tweet"
    t.integer  "id_itype"
    t.datetime "created_at"
    t.datetime "updated_at"
  end

  create_table "tweets", force: true do |t|
    t.string   "text"
    t.integer  "retweets"
    t.string   "id_user",     limit: 100
    t.string   "source",      limit: 100
    t.string   "coordinates"
    t.integer  "procesado"
    t.integer  "geoenable"
    t.string   "id_twitter",  limit: 100
    t.datetime "created_at"
    t.datetime "updated_at"
  end

  create_table "users", force: true do |t|
    t.string   "name",        limit: 100
    t.string   "timezone",    limit: 100
    t.string   "language",    limit: 100
    t.integer  "followers"
    t.string   "description"
    t.datetime "created_at"
    t.datetime "updated_at"
  end

end
