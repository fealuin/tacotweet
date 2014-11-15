json.array!(@incidents) do |incident|
  json.extract! incident, :id, :id_tweet, :id_itype
  json.url incident_url(incident, format: :json)
end
