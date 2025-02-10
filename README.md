# Backend Developer Test (Frappe) - eglobalsphere

## Task 1: Frappe Application Setup

### Prerequisites

Before you begin, kindly ensure that  your system meets the following requirements:

#### **Required Dependencies**
- **MariaDB** 10.6.6+ (Database Engine)
- **Python** 3.10/3.11/3.12 (Primary language for Frappe)
- **Node.js** 18 or 20 & npm (Required for frontend assets and WebSockets)
- **Redis** 6 (Used for caching and real-time updates)
- **Yarn** 1.12+ (JavaScript dependency manager)
- **pip** 20+ (Python package manager)
- **wkhtmltopdf** (version 0.12.5 with patched Qt) (For PDF generation)
- **cron** (Required for scheduled jobs like backups and certificate renewal)

> 💡 If you need help installing these dependencies, refer to the [official Frappe installation guide](https://docs.frappe.io/framework/user/en/installation).

### **Installation Steps**

#### **Step 1: Install Frappe Bench**
Run the following command in your terminal:
```sh (run this commands in you shell)
pip install frappe-bench
```

#### **Step 2: Initialize a New Bench Instance**
```sh
bench init eglobalsphere-bench
cd eglobalsphere-bench
```
- This creates a new **Frappe Bench environment** where all applications will be managed.

#### **Step 3: Create a New Frappe App**
```sh
bench new-app eglobalsphere_app
```
- This initializes a new **Frappe app** named `eglobalsphere_app`.

### Task 2
a. The Custom doc "Task" can be migrated into the db. it is the fixtures folder  (project_management/project_management/fixtures)
b. The api is implemented here (in project_management/project_management/api/task_api) api keys  would have to be generated  
To access send a request from postman etc use  Authorization: token <api_key>:<api_secret>
the key should be genrated in user

### Task 3
- The schema image is attached and name schema.png
- All required doctypes can be found in project managemet folder

### Task 4
- Required api with endpoints with caching is implemented in  project_management/project_management/api/project_api