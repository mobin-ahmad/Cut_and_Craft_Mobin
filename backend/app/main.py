from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, List
from enum import Enum
import uvicorn

app = FastAPI(title="Cut & Craft API - Zoi Solution")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class OrderStatus(str, Enum):
    draft = "draft"
    fed_in_system = "fed_in_system"
    displayed_inventory = "displayed_inventory"
    pending_approval = "pending_approval"
    approved = "approved"
    material_issued = "material_issued"
    synced_candila = "synced_candila"
    material_received = "material_received"
    stitching_in_process = "stitching_in_process"
    finished_packaging = "finished_packaging"
    dispatched = "dispatched"
    received_outlet = "received_outlet"
    handed_over = "handed_over"

class OrderCreate(BaseModel):
    customer_name: str
    measurements: Dict[str, float]  # 22 fields e.g., {"chest": 38.0, "waist": 32.0, ...}
    fabric_code: str
    quantity_meters: float
    outlet: str  # "Lahore Defence"

class OrderResponse(BaseModel):
    id: str
    status: OrderStatus
    # ... other fields

# In-memory store for demo (use PostgreSQL later)
orders: List[Dict] = []
next_id = 1

@app.get("/")
def home():
    return {"message": "Cut & Craft by Zoi Solution - Mobin Bhai Edition | Full Flow Live!"}

@app.post("/orders/", response_model=OrderResponse)
def create_order(order: OrderCreate):
    global next_id
    new_order = {
        "id": str(next_id),
        "status": OrderStatus.fed_in_system,
        "customer_name": order.customer_name,
        "measurements": order.measurements,
        "fabric_code": order.fabric_code,
        "quantity_meters": order.quantity_meters,
        "outlet": order.outlet
    }
    orders.append(new_order)
    next_id += 1
    return new_order

@app.get("/orders/{order_id}")
def get_order(order_id: str):
    for o in orders:
        if o["id"] == order_id:
            return o
    raise HTTPException(404, "Order not found")

@app.post("/orders/{order_id}/approve")
def approve_order(order_id: str, approved: bool = True):
    for o in orders:
        if o["id"] == order_id:
            if approved:
                o["status"] = OrderStatus.material_issued
            else:
                o["status"] = OrderStatus.pending_approval
            return {"status": o["status"]}
    raise HTTPException(404, "Order not found")

@app.post("/orders/{order_id}/sync-material")
def sync_material(order_id: str):
    for o in orders:
        if o["id"] == order_id:
            o["status"] = OrderStatus.material_received
            return {"status": "synced"}
    raise HTTPException(404, "Order not found")

@app.post("/orders/{order_id}/start-stitching")
def start_stitching(order_id: str):
    for o in orders:
        if o["id"] == order_id:
            o["status"] = OrderStatus.stitching_in_process
            return {"status": "in process"}
    raise HTTPException(404, "Order not found")

@app.post("/orders/{order_id}/dispatch")
def dispatch_order(order_id: str):
    for o in orders:
        if o["id"] == order_id:
            o["status"] = OrderStatus.dispatched
            return {"status": "dispatched"}
    raise HTTPException(404, "Order not found")

@app.post("/orders/{order_id}/handover")
def handover_order(order_id: str):
    for o in orders:
        if o["id"] == order_id:
            o["status"] = OrderStatus.handed_over
            return {"status": "handed over"}
    raise HTTPException(404, "Order not found")

@app.get("/flow-diagram")
def get_flow_diagram():
    # Returns the exact flow as JSON (for frontend viz)
    nodes = [
        {"id": "user_login", "label": "User Login", "color": "#003087"},
        {"id": "customer_creation", "label": "Customer Creation", "color": "#003087"},
        # ... (full 22 nodes from your diagram)
        {"id": "process_start_blue", "label": "Process Start", "color": "#003087"}
    ]
    edges = [
        {"from": "user_login", "to": "customer_creation"},
        # ... (full 25 edges)
        {"from": "hand_over", "to": "process_start_blue", "label": "Loop"}
    ]
    return {"nodes": nodes, "edges": edges}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)