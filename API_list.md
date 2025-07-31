# API\_list

This document lists the backend APIs required for the FAQ management component. Each API includes the endpoint path, HTTP method, purpose, and sample JSON input/output.&#x20;

### 1. Get all FAQs

- **Endpoint:** `/api/faqs` &#x20;
- **Method:** `GET` &#x20;
- **Description:** Retrieve all FAQ entries from the database. &#x20;
- **Request Body:** *None* &#x20;
- **Sample Response (200 OK):**

```json 
[
  {
    "id": 1,
    "question": "How do I apply for leave?",
    "answer": "Use the HR portal under 'Leave Management'."
  },
  {
    "id": 2,
    "question": "How do I reset my password?",
    "answer": "Go to the IT self-service portal and click 'Reset Password'."
  }
 ]
```


### 2. Get FAQ by ID

- **Endpoint:**`/api/faqs/<id>`
- **Method:**`GET`
- **Description:** Retrieve a single FAQ by its ID.
- **Request Body:** None
- **Sample Response (200 OK):**

```json 
  {
    "id": 1,
    "question": "How do I apply for leave?",
    "answer": "Use the HR portal under 'Leave Management'."
  },

```


- **Sample Error (404 Not Found):**

```json 
{
  "error": "FAQ not found"
}

```


### 3. Add new FAQ

- **Endpoint:**`/api/faqs`
- **Method:**`POST`
- **Description:** Add a new FAQ entry to the database.
- **Sample Request Body:**

```json 
{
  "question": "Where can I find the employee handbook?",
  "answer": "Download it from the internal HR SharePoint."
}

```


- **Sample Response (201 Created):**

```json 
{
  "id": 3,
  "question": "Where can I find the employee handbook?",
  "answer": "Download it from the internal HR SharePoint."
}

```


- **Sample Error (400 Bad Request):**

```json 
{
  "error": "Missing fields"
}

```


### 4. Update existing FAQ

- **Endpoint:**`/api/faqs/<id>`
- **Method:**`PUT`
- **Description:** Update an existing FAQ based on ID.
- **Sample Request Body:**

```json 
{
  "question": "How do I request time off?",
  "answer": "Submit a request via the HR system."
}

```


- **Sample Response (200 OK):**

```json 
{
  "id": 1,
  "question": "How do I request time off?",
  "answer": "Submit a request via the HR system."
}


```


- **Sample Error  (404 Not Found):**

```json 
{
  "error": "FAQ not found"
}

```


### 5. Delete FAQ

- **Endpoint:**`/api/faqs/<id>`
- **Method:**`DELETE`
- **Description:** Remove a specific FAQ from the database.
- **Request Body:** None
- **Sample Response (200 OK):**

```json 
{
  "success": true
}

```


- **Sample Error  (404 Not Found):**

```json 
{
  "error": "FAQ not found"
}

```
