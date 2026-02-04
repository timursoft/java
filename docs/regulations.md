# Regulations

## Regulation Identification Process

To identify applicable data protection regulations for a project, follow these steps:

1. Use the `/get_applicable_regulations` API endpoint to determine applicable regulations.
2. Provide the `region` parameter to specify the geographic area.
3. The system will return a list of applicable regulations based on the defined criteria for that region.

### Example Request
```
GET /get_applicable_regulations?region=EU
```

### Example Response
```
[
  {
    "name": "GDPR",
    "country": "EU"
  }
]
```

Ensure that stakeholders review and approve the identified regulations for compliance purposes.