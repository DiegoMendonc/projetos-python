from fastapi import FastAPI

app = FastAPI(title="WorkoutAPI")

# para rodar virtualmente >
# workoutapi\Scripts\Activate  >    uvicorn workout_api.main:app --reload

if __name__ == "main":
    import uvicorn
    
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)