# Insecure Web Application Project

## **Project Description**
This project is an insecure web application built using Django. The purpose of this project is to demonstrate and explore five security flaws from the [OWASP to ten list](https://owasp.org/www-project-top-ten/).

## **Implemented Security Flaws**

### **1. SQL Injection **
- **Description**: The login functionality uses raw SQL queries that are vulnerable to injection attacks.

### **2. Security Logging and Monitoring Failures **
- **Description**: Failed login attempts are not logged, making it impossible to detect brute force or injection attacks.

### **3. Broken Access Control **
- **Description**: The admin page is accessible to any user without authentication or proper authorization checks.

### **4. Identification and Authentication Failures **
- **Description**: The application allows users to sign up with weak passwords without enforcing complexity requirements.

### **5. Cryptographic Failures **
- **Description**: Passwords are stored in plain text in the database without hashing or encryption.
