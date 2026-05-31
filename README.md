Smart Expense Tracker Web App

A modern full-stack Expense Tracker Web Application that helps users manage personal finances efficiently. The application allows users to track income and expenses, set budgets, analyze spending habits, upload transaction records, and visualize financial data through interactive dashboards.

🚀 Features
🔐 User Authentication
User Registration
Secure Login & Logout
Password Encryption using JWT/Bcrypt
Protected Routes
💰 Expense Management
Add Income Transactions
Add Expense Transactions
Edit Transactions
Delete Transactions
Transaction History
📂 Smart Categorization
Automatic Expense Categorization
Custom Categories
Category-wise Spending Analysis
📊 Dashboard & Analytics
Monthly Expense Overview
Income vs Expense Charts
Budget Tracking
Financial Summary Cards
Interactive Graphs
📈 Budget Management
Create Monthly Budgets
Track Budget Utilization
Budget Alerts
Overspending Notifications
🔄 Recurring Transactions
Daily Expenses
Weekly Expenses
Monthly Bills
Automatic Future Entries
🌍 Multi-Currency Support
INR (₹)
USD ($)
EUR (€)
GBP (£)
Currency Conversion Support
📁 File Import
CSV Upload
Bank Statement Import
Bulk Transaction Import
📷 Receipt OCR (Optional)
Upload Receipt Images
Extract Transaction Details
Auto-fill Expense Entries
📱 Progressive Web App (PWA)
Mobile Friendly
Installable App
Offline Support
Responsive Design
🛠️ Tech Stack
Frontend
React.js
React Router DOM
Redux Toolkit
Axios
Chart.js
Bootstrap / Tailwind CSS
Backend
Node.js
Express.js
JWT Authentication
Multer
Database
MongoDB Atlas
Mongoose ODM
Additional Tools
OCR API (Tesseract.js)
CSV Parser
Currency Exchange API
project structure
smart-expense-tracker/
│
├── client/
│   ├── public/
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── redux/
│   │   ├── services/
│   │   ├── App.js
│   │   └── index.js
│
├── server/
│   ├── controllers/
│   ├── middleware/
│   ├── models/
│   ├── routes/
│   ├── uploads/
│   ├── config/📊 Main Modules
Dashboard

Displays:

Total Income
Total Expenses
Remaining Balance
Monthly Trends
Recent Transactions
Transactions

Users can:

Add New Transactions
Update Existing Transactions
Delete Transactions
Filter Transactions
Budgets

Users can:

Set Spending Limits
Monitor Progress
Receive Alerts
Reports

Generate:

Monthly Reports
Category Reports
Expense Summaries
📸 Screenshots
Home Page
<img width="1360" height="682" alt="Screenshot 2026-05-31 212106" src="https://github.com/user-attachments/assets/8b5b470e-0152-434d-9081-00fdc95bebe5" />

Financial Summary
Recent Transactions
<img width="1353" height="674" alt="Screenshot 2026-05-31 212556" src="https://github.com/user-attachments/assets/d104c648-c156-4ce9-bac2-413638379092" />

Expense Charts
Budget Page
Budget Progress Bars
<img width="1366" height="627" alt="Screenshot 2026-05-31 212451" src="https://github.com/user-attachments/assets/525e6b74-dedb-4f85-b2a4-7fba3111f6dd" />

Spending Alerts
Analytics Page
<img width="1354" height="665" alt="Screenshot 2026-05-31 212426" src="https://github.com/user-attachments/assets/b87b3152-680b-46fe-b58a-6b7151f936f7" />

Pie Charts
Bar Charts
Trend Analysis
<img width="1365" height="658" alt="Screenshot 2026-05-31 212520" src="https://github.com/user-attachments/assets/ef24e47e-fa03-4787-acda-8fa32d5e5633" />

🔒 Security Features
JWT Authentication
Password Hashing
Protected API Routes
Input Validation
MongoDB Injection Prevention
CORS Protection
🧪 Future Enhancements
AI-Based Expense Prediction
Voice Expense Entry
Email Notifications
SMS Alerts
Investment Tracking
Savings Goals
Dark Mode
Family Shared Accounts
Banking API Integration
📈 Performance Optimizations
Lazy Loading
Pagination
API Caching
Optimized Database Queries
Responsive UI
🤝 Contributing
Fork the Repository
Create a New Branch
git checkout -b feature-name
Commit Changes
git commit -m "Added new feature"
Push Changes
git push origin feature-name
Create Pull Request
📝 License

This project is licensed under the MIT License.

👩‍💻 Author

Tanisha Mittal

Full Stack Developer Project
│   └── server.js
│
├── README.md
└── package.json
