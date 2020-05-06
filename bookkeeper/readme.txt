Creating/Recording SalesBook
Invoice form will be populated with lists of sold items
each item have a price property
all price property will be added, sum(pricei, i...n) => total

This also happen: delete, update, put, get
Invoice is first created (at the path: /invoices) and it object return to the frontend, then
Each item will be created one by one: use loop, by sending request to the path: '/sales' and writes to SalesBook
Total prices of items would be write to Sales

