class AddIncidentTypeToIncidents < ActiveRecord::Migration
  def change
    add_reference :incidents, :itype, index: true
  end
end
