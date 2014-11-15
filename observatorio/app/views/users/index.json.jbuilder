json.array!(@users) do |user|
  json.extract! user, :id, :name, :timezone, :language, :followers, :description
  json.url user_url(user, format: :json)
end
