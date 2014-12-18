class IncidentsController < ApplicationController
  before_action :set_incident, only: [:show, :edit, :update, :destroy]

  # GET /incidents
  # GET /incidents.json
  def index
    @incidents = Incident.all
    @incident_map =Incident.select(:id,:latitude,:longitude,:text,:itype_id,:timestamp).where(timestamp: 1.days.ago..(Time.now)) 
    @incident_graf=Incident.find_by_sql("select count(*) as Cuenta, date_format(created_at,'%d/%m/%y') as Fecha, if(itype_id=1,'A','T') AS Tipo  From incidents group by Fecha,Tipo")
    @incident_fechas=Incident.select(:created_at).group(:created_at)
    @incident_accidentes=Incident.select(:created_at).group(:created_at,:itype_id).having(:itype_id=>2).count
    @incident_graf=Incident.find_by_sql("select count(*) as Cuenta, date_format(created_at,'%d/%m/%y') as Fecha, if(itype_id=1,'A','T') AS Tipo  From incidents group by Fecha,Tipo")
    @incident_taco=Incident.select(:created_at).group(:created_at,:itype_id).having(:itype_id=>1).count
    @incident_ultimo=Tweet.last()
    @tweet_total=Tweet.count


  end

  # GET /incidents/1
  # GET /incidents/1.json
  def show
  end

  # Get
  def mapa
    @incident_map = Incident.select(:id,:latitude,:longitude,:text)
    respond_to do |format|
    format.html
    format.json {
      render:json=>@incident_map.to_json
    }
    end
  end

  def grafico
    @incident_graf=Incident.find_by_sql("select count(*) as Cuenta, date_format(created_at,'%d/%m/%y') as Fecha, if(itype_id=1,'A','T') AS Tipo  From incidents group by Fecha,Tipo")
  end

  def fechas
    @incident_fechas=Incident.select(:created_at).group(:created_at)
  end

  def accidentes
    @incident_accidentes=Incident.select(:created_at).group(:created_at,:itype_id).having(:itype_id=>1).count
  end

  def taco
    @incident_taco=Incident.select(:created_at).group(:created_at,:itype_id).having(:itype_id=>2).count
  end
 

  # GET /incidents/new
  def new
    @incident = Incident.new
  end

  # GET /incidents/1/edit
  def edit
  end

  # POST /incidents
  # POST /incidents.json
  def create
    @incident = Incident.new(incident_params)

    respond_to do |format|
      if @incident.save
        format.html { redirect_to @incident, notice: 'Incident was successfully created.' }
        format.json { render :show, status: :created, location: @incident }
      else
        format.html { render :new }
        format.json { render json: @incident.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /incidents/1
  # PATCH/PUT /incidents/1.json
  def update
    respond_to do |format|
      if @incident.update(incident_params)
        format.html { redirect_to @incident, notice: 'Incident was successfully updated.' }
        format.json { render :show, status: :ok, location: @incident }
      else
        format.html { render :edit }
        format.json { render json: @incident.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /incidents/1
  # DELETE /incidents/1.json
  def destroy
    @incident.destroy
    respond_to do |format|
      format.html { redirect_to incidents_url, notice: 'Incident was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_incident
      @incident = Incident.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def incident_params
      params[:incident]
      params.require(:incident).permit(:created_at,:latitude,:longitude)
    end
end
