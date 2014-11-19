json.array!(@incidents) do |incident|
  json.extract! incident, :id
  json.url incident_url(incident, format: :json)
end
