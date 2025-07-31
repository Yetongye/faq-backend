# Test Case Document & API Testing Results

## Test Case Summary

| Test Case ID | Endpoint              | Method | Description                         | Expected Result                  | 
|--------------|-----------------------|--------|-------------------------------------|----------------------------------|
| TC001        | `/api/faqs`           | GET    | Retrieve all FAQs                   | 200 + list of FAQ items          | 
| TC002        | `/api/faqs`           | POST   | Add a new FAQ                       | 201 + new FAQ JSON               | 
| TC003        | `/api/faqs/1`         | GET    | Retrieve FAQ with ID = 1           | 200 + corresponding FAQ JSON     | 
| TC004        | `/api/faqs/999`       | GET    | Retrieve non-existent FAQ          | 404 + error message              | 
| TC005        | `/api/faqs/1`         | PUT    | Update FAQ with ID = 1             | 200 + updated FAQ JSON           | 
| TC006        | `/api/faqs/999`       | PUT    | Update non-existent FAQ            | 404 + error message              | 
| TC007        | `/api/faqs/1`         | DELETE | Delete FAQ with ID = 1             | 200 + success message            | 
| TC008        | `/api/faqs/999`       | DELETE | Delete non-existent FAQ            | 404 + error message              | 

---

## Add FAQ
**Request Body:**
```json
[
  {
    "question": "What is the company dress code?",
    "answer": "Smart casual from Monday to Thursday, casual on Friday."
  },
  {
    "question": "How do I access the company intranet?",
    "answer": "Use the link provided in your onboarding email."
  },
  {
    "question": "How do I change my direct deposit information?",
    "answer": "Go to the HR portal under 'Payroll Settings'."
  }
]
```
**Response:**
```json
[
  {
    "answer": "Smart casual from Monday to Thursday, casual on Friday.",
    "id": null,
    "question": "What is the company dress code?"
  },
  {
    "answer": "Use the link provided in your onboarding email.",
    "id": null,
    "question": "How do I access the company intranet?"
  },
  {
    "answer": "Go to the HR portal under 'Payroll Settings'.",
    "id": null,
    "question": "How do I change my direct deposit information?"
  }
]
```

## Update FAQ (PUT `/api/faqs/1`)
**Request Body:**
```json
{
  "question": "How do I access the VPN?",
  "answer": "Use Cisco AnyConnect with your employee login."
}

```
**Response:**
```json
{
  "answer": "Use Cisco AnyConnect with your employee login.",
  "id": 1,
  "question": "How do I access the VPN?"
}
```

## Delete FAQ (DELETE `/api/faqs/1`)
**Response:**
```json
{
  "message": "FAQ deleted successfully"
}
```

## FAQ not found (GET `/api/faqs/999`)
**Response:**
```json
127.0.0.1 - - [27/Jul/2025 18:55:12] "GET /api/faqs/9999 HTTP/1.1" 404 -
```

## Get FAQ (GET `/api/faqs`)
**Response:**
```json
[
  {
    "answer": "You can apply for vacation leave through the HR portal under 'Leave Management'.",
    "id": 1,
    "question": "How do I apply for vacation leave?"
  },
  {
    "answer": "Smart casual from Monday to Thursday, casual on Friday.",
    "id": 2,
    "question": "What is the company dress code?"
  },
  {
    "answer": "Use the link provided in your onboarding email.",
    "id": 3,
    "question": "How do I access the company intranet?"
  },
  {
    "answer": "Go to the HR portal under 'Payroll Settings'.",
    "id": 4,
    "question": "How do I change my direct deposit information?"
  },
  {
    "answer": "Smart casual from Monday to Thursday, casual on Friday.",
    "id": 5,
    "question": "What is the company dress code?"
  },
  {
    "answer": "Use the link provided in your onboarding email.",
    "id": 6,
    "question": "How do I access the company intranet?"
  },
  {
    "answer": "Go to the HR portal under 'Payroll Settings'.",
    "id": 7,
    "question": "How do I change my direct deposit information?"
  }
]
```