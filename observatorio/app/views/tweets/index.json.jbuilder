json.array!(@tweets) do |tweet|
  json.extract! tweet, :id, :text, :retweets, :id_user, :source, :coordinates, :procesado, :geoenable, :id_twitter
  json.url tweet_url(tweet, format: :json)
end
