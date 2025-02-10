import frappe
from frappe import _



@frappe.whitelist()
def create_task(title, description, status="Open"):
    """Create a new Task with title as its name"""
    if not title or not description:
        frappe.throw(_("Title and Description are required."))

    if frappe.db.exists("Task", title):
        frappe.throw(_("A Task with this title already exists."))

    try:
        task = frappe.get_doc({
            "doctype": "Task",
            "title": title,
            "description": description,
            "status": status
        })
        task.insert()
        frappe.db.commit()
        return task.as_dict()
    
    except Exception as e:
        frappe.logger().error(f"Task creation failed: {str(e)}")
        return {"error": "Task creation failed", "details": str(e)}

@frappe.whitelist()
def get_task(task_id):
    """Get Task details by ID"""
    try:
        task = frappe.get_doc("Task", task_id)
        return task.as_dict()
    except frappe.DoesNotExistError:
        frappe.logger().error(f"Task {task_id} not found!")
        return {"error": f"Task {task_id} not found"}


@frappe.whitelist()
def update_task(task_id, **kwargs):
    """Update an existing Task"""
    task = frappe.get_doc("Task", task_id)
    for key, value in kwargs.items():
        if hasattr(task, key):
            setattr(task, key, value)
    task.save()
    return task.as_dict()

@frappe.whitelist()
def delete_task(task_id):
    """Delete a Task"""
    frappe.delete_doc("Task", task_id)
    return {"message": "Task deleted successfully"}



import frappe
from frappe import _


@frappe.whitelist()
def get_all_tasks(status=None, limit_page_length=10, limit_start=0):
    """
    Get all tasks with optional filters.
    Supports:
    - Filtering by status
    - Pagination (limit_page_length, limit_start)
    """
    try:
        filters = {}
        if status:
            filters["status"] = status

        tasks = frappe.get_all(
            "Task",
            filters=filters,
            fields=["name", "title", "description", "status", "priority", "start_date", "due_date"],
            order_by="modified desc",
            limit_page_length=int(limit_page_length),
            limit_start=int(limit_start)
        )

        return {"tasks": tasks}

    except Exception as e:
        frappe.logger().error(f"Failed to fetch tasks: {str(e)}")
        return {"error": "Failed to fetch tasks", "details": str(e)}
