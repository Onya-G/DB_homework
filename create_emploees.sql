CREATE TABLE IF NOT EXISTS employees (
	id SERIAL PRIMARY KEY, 
	name VARCHAR(40) NOT NULL, 
	department VARCHAR(100),
	manager_id INTEGER REFERENCES employees(id)
);
