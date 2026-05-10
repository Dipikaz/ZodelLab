@app.post("/api/simulate")
async def run_simulation(request: SimulationRequest, db: Session = Depends(get_db)):
    # 1. Brain: Generate the logic
    raw_code = gemini_service.generate_simulation_code(request.prompt)
    
    # 2. Engine: Run the simulation
    execution_output = executor.safe_execute(raw_code)
    
    # 3. Storage: Persist the success or failure
    new_sim = Simulation(
        prompt=request.prompt,
        code=raw_code,
        result_data=execution_output.json_data # The Plotly JSON
    )
    db.add(new_sim)
    db.commit()
    
    return {"id": new_sim.id, "viz": execution_output.json_data}