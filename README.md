# Klimbb_test_challenge
Develop an Incident Management API using Django Rest Framework, focusing on basic functionality and specific business logic for incident handling under ideal scenarios.

Asks
Setup:
Initialize a Django project with Django Rest Framework.
API Development:
Develop endpoints for reporting, updating, and querying incidents.
Business Logic Implementation:
Incorporate logic for handling incidents, focusing on scenarios where everything functions as expected.
Deets
Incident Schema:
Fields: incident_id (UUID), type (String), severity (Integer 1-5), timestamp (DateTime), description (Text), status (String), assigned_to (String, nullable).
API Endpoints:
POST /incidents/: Report new incidents.
PUT /incidents/{incident_id}/: Update the status or assigned handler of an incident.
Business Logic Scenarios:
High Severity Incident Handling: Immediate prioritization and assignment to available handler.
Multiple Incidents with Equal Severity: Prioritization based on timestamp; even distribution among handlers.
Updating Incident Status: Automatic re-assignment of pending incidents upon resolution of current ones.
Handler Unavailability: New incidents marked as 'Pending' and assigned when a handler becomes available.
Incident Escalation: Re-prioritization of escalated incidents according to their new severity.
Seed data
Handlers

Assume we have three handlers: Alice, Bob, and Charlie. These handlers will be referenced in the incident reports for assignment purposes.

Incident Reports

High Severity Incident Handling
Incident: {"type": "System Outage", "severity": 1, "description": "Complete system failure", "timestamp": "2023-12-17T10:00:00Z"}
Expected Behavior: Immediate assignment to the first available handler.
Multiple Incidents with Equal Severity
Incident 1: {"type": "Performance Issue", "severity": 3, "description": "Service response delay", "timestamp": "2023-12-17T10:05:00Z"}
Incident 2: {"type": "Data Inconsistency", "severity": 3, "description": "Mismatch in database records", "timestamp": "2023-12-17T10:06:00Z"}
Expected Behavior: Both incidents are assigned based on their timestamp, evenly distributing the load among handlers.
Updating Incident Status
Incident: {"type": "Network Issue", "severity": 2, "description": "Intermittent network downtime", "timestamp": "2023-12-17T10:10:00Z", "status": "Resolved"}
Expected Behavior: Once resolved, the next highest-priority 'Pending' incident should be assigned to the freed-up handler.
Handler Unavailability
Incident: {"type": "Application Crash", "severity": 2, "description": "Critical application crashed", "timestamp": "2023-12-17T10:15:00Z"}
Expected Behavior: If all handlers are busy, the incident is marked as 'Pending' until a handler becomes available.
Incident Escalation
Incident: {"type": "Security Breach", "severity": 4, "description": "Suspected data breach", "timestamp": "2023-12-17T10:20:00Z", "severity": 1}
Expected Behavior: The incident, initially low severity, is escalated to high severity and should be re-prioritized accordingly.
