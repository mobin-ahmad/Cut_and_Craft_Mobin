# Cut & Craft Tailor Management System (TMS) - User Manual

This manual provides a detailed, menu-wise explanation of every process within the Cut & Craft Tailor Management System.

---

## 1. Dashboard (Home)
The Dashboard serves as the command center, providing a high-level overview of branch operations and quick access to key actions.

### 1.1 Key Performance Indicators (KPIs)
*   **Today's Orders**: Total number of orders placed in the current business day.
*   **In Stitching**: Count of garments currently in the production phase at the hub.
*   **Ready for Pickup**: Orders that have passed quality checks and are awaiting customer collection.
*   **Active Customers**: Total number of unique customers registered in the system.

### 1.2 Recent Activity & Quick Actions
*   **Activity Feed**: A real-time log of the latest orders, status changes, and customer registrations.
*   **View All Orders**: A shortcut button that redirects directly to the full Orders management menu.
*   **Create New Order**: A primary action button to initiate the order creation wizard immediately.

---

## 2. Orders Menu
The central hub for managing the lifecycle of every garment.

### 2.1 Order Tracking
*   **Search Bar**: Quickly locate orders by Order ID (e.g., ORD-7721) or Customer Name.
*   **Status Badges**: Visual indicators for order stages:
    *   `MEASUREMENT TAKEN`: Initial order entry complete.
    *   `FABRIC DISPATCHED`: Materials sent to the stitching hub.
    *   `IN STITCHING`: Tailors are actively working on the garment.
    *   `READY FOR PICKUP`: Garment is back at the branch.
    *   `COMPLETED`: Handed over to the customer.
    *   `REWORK`: Returned for adjustments.

### 2.2 Rework Management
*   **Eligibility**: Only orders marked as `COMPLETED` within the configured "Rework Window" (e.g., 10 days) are eligible.
*   **Flagging for Rework**: 
    1.  Locate a completed order.
    2.  Click the **REWORK** button or select "Flag for Rework" from the 3-dot menu.
    3.  Enter detailed **Rework Remarks** (e.g., "Shorten sleeves by 0.5 inches").
    4.  Click **SEND TO STITCHING** to move the order back into the production queue.

---

## 3. New Order Flow (Wizard)
A guided 5-step process to ensure precision in bespoke tailoring.

### 3.1 Step 1: Customer Identification
*   **Mobile Search**: Enter the customer's 11-digit mobile number.
*   **Profile Selection**: Choose the specific individual (Self, Spouse, Child) for whom the garment is being made.
*   **New Customer**: If the number isn't found, you can register a new customer on the spot.

### 3.2 Step 2: Garment Selection
*   Choose the base garment type: **Shalwar Kameez**, **Shirt**, **Pant**, or **Suit**. This selection determines the available measurement fields and design options in subsequent steps.

### 3.3 Step 3: Measurements & Sizing
*   **Sizing Base**:
    *   `Standard`: Use pre-defined S/M/L/XL templates.
    *   `Last Order`: Automatically pull measurements from the customer's previous successful order.
    *   `Bespoke`: Enter every dimension manually for a perfect fit.
*   **Adjustments**: Apply +/- deviations in inches to any specific measurement (e.g., "Standard Large but +1 inch on Length").

### 3.4 Step 4: Design & Catalog
*   **Style Selection**: Configure specific elements like Collar Type (Ban, Shirt, V-Neck), Cuffs, Pockets, and Plackets.
*   **Visual Catalog**: Browse high-quality images of finished designs to help the customer visualize the final product.

### 3.5 Step 5: Review & Lock
*   A comprehensive summary of all selections. Once "Locked," the order is assigned a unique ID and the status is set to `MEASUREMENT TAKEN`.

---

## 4. Customers Menu
Manage the master database of your clientele.

### 4.1 Customer Directory
*   **Search**: Filter by name or mobile number.
*   **Profile View**: Click a customer to see their full history, linked family profiles, and saved measurements.

### 4.2 Registration Process
*   **Validation**: Mobile numbers must be at least 11 digits to ensure WhatsApp/SMS compatibility.
*   **Mandatory Fields**: Full Name, Mobile, and City are required for a valid registration.
*   **Cancel Option**: Use the **CANCEL** button to exit the form without saving if a customer changes their mind.

---

## 5. Stitching Hub
The production management interface for workshop administrators.

### 5.1 Kanban Board
*   **Status Columns**: Move orders between `Incoming`, `Queue`, `Active`, and `Done`. Use the **Back** button to return an order to a previous stage if needed.
*   **Progress Tracking**: Use the manual slider (0-100%) on each order card to report real-time stitching progress.

### 5.2 Assignments
*   **Tailor Assignment**: Assign specific masters or stitchers to an order.
*   **Deadline Management**: Set target completion dates to ensure timely delivery.

---

## 6. User Management (Admin Only)
Control system access and assign roles to staff members.

### 6.1 Role Definitions
*   **Administrator**: Full system access, including settings and user control.
*   **Branch Manager**: Oversees branch orders and customer data.
*   **Tailor/Shop Staff**: Focuses on order entry and customer service.
*   **Stitching Hub Admin**: Manages the production floor.

---

## 7. Settings (Admin Only)
Configure global system parameters and integrations.

### 7.1 Rework Policy
*   **Rework Window**: Set the maximum number of days (e.g., 10, 15, 30) a customer has to request a rework after handover.

### 7.2 GitHub Integration
*   **Sync Documentation**: Connect to a GitHub repository to backup activity logs and system manuals.
*   **OAuth Security**: Uses secure GitHub authentication for data transfer.

