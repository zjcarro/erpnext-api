import datetime
from fastapi import FastAPI, HTTPException, Request
import uvicorn

app = FastAPI()

@app.post("/erpnext-po-webhook")
async def handle_po_creation(request: Request):
    data = await request.json()
    print("New PO Created:", data)  # Log to console
    # Add your custom logic (e.g., send Lark message here)
    return {"status": "success"}

@app.post("/po-assignment")
async def handle_assignment(request: Request):
    try:
        data = await request.json()
        print("Incoming Webhook Data:", data)  # For debugging
        
        # Required fields check
        if "allocated_to" not in data:
            return {
                "status": "error",
                "error": "Missing allocated_to field",
                "received_data": data
            }
        
        # Skip cancelled assignments
        if data.get("status") == "Cancelled":
            return {
                "status": "ignored",
                "reason": "Assignment was cancelled",
                "data": data
            }
            
        # Successful assignment
        return {
            "status": "success",
            "assignment_status": data.get("status", "Unknown"),
            "assigned_to": data["allocated_to"],
            "assigned_by": data.get("assigned_by"),
            "assignment_id": data["name"],
            "server_time": datetime.utcnow().isoformat()
        }
    
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "received_data": data
        }
    
@app.post("/erpnext-po-submitted")
async def handle_po_submission(request: Request):
    try:
        data = await request.json()
        print("PO Submitted:", data)

        # Example: Extract key info
        po_name = data.get("name")
        submitted_by = data.get("owner")
        modified_on = data.get("modified")

        # Your custom logic goes here (e.g., notify a team on Lark)

        return {
            "status": "success",
            "po": po_name,
            "submitted_by": submitted_by,
            "timestamp": modified_on,
            "server_time": datetime.utcnow().isoformat()
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e)
        }

@app.get("/")
def read_root():
    return {"message": "Hello, world!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)