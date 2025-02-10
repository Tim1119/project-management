# This is the answer for task 4

import frappe
from frappe import _
# from frappe.cache_manager import cache
from frappe.utils.response import json_handler
import json


@frappe.whitelist()
def get_all_projects():

    """Fetch all projects with caching. The caching will be implemented for only 5 minutes or 300 seconds as mentioned below"""
    cache_key = "eglobalsphere_interview"

    cached_data = frappe.cache().get_value(cache_key)
    if cached_data:
        return json.loads(cached_data)

    
    projects = frappe.db.get_all(
        "Project",
        fields=["name", "title", "description", "start_date", "end_date", "status"]
    )
    frappe.cache().set_value(cache_key, json.dumps(projects), expires_in_sec=600)

    return projects

@frappe.whitelist()
def get_project(project_name):
    """This Fetch a single project by name"""
    project = frappe.get_doc("Project", project_name)
    return frappe.response.json(project)


@frappe.whitelist()
def create_project():
    """Create a new project """
    data = json.loads(frappe.request.data)
    project = frappe.get_doc({
        "doctype": "Project",
        "title": data.get("title"),
        "description": data.get("description"),
        "start_date": data.get("start_date"),
        "end_date": data.get("end_date"),
        "status": data.get("status")
    })
    project.insert()
    frappe.db.commit()
    return project.as_dict()