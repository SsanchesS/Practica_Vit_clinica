CREATE TABLE application(
  application_id INTEGER PRIMARY KEY,
  applicationStatus TEXT,
  dataAt DATE,
  animal TEXT,
  treatmentType TEXT,
  descriptionDisease TEXT,
  customerData TEXT,
  treatmentStatus TEXT,
  veterinarian_id INTEGER,
  treatmentStage TEXT,
  descriptionTreatment TEXT,
  comments TEXT,
  applicationExecutor_id INTEGER,
  FOREIGN KEY (veterinarian_id) REFERENCES veterinarian (veterinarian_id),
  FOREIGN KEY (applicationExecutor_id) REFERENCES departmentPerformanceStatisticsM (applicationExecutor_id)
);
CREATE TABLE veterinarian(
  veterinarian_id INTEGER PRIMARY KEY,
  name TEXT
);
CREATE TABLE departmentPerformanceStatistics(
  applicationExecutor_id INTEGER PRIMARY KEY,
  NumberCompletedApplications INTEGER,
  AvgApplicationTime INTEGER,
  statisticsTypesDiseases TEXT
);
CREATE TABLE role(
  role_id INTEGER PRIMARY KEY,
  role TEXT
);
CREATE TABLE user(
  user_id INTEGER PRIMARY KEY,
  name TEXT,
  login TEXT,
  password TEXT,
  role_id INTEGER,
  FOREIGN KEY (role_id) REFERENCES role (role_id)
);
INSERT INTO role (role) VALUES ('user');
INSERT INTO role (role) VALUES ('admin');
INSERT INTO user (name, login, password, role_id) VALUES ('admin', 'admin', 'admin', 1);
INSERT INTO user (name, login, password, role_id) VALUES ('user', 'user', 'user', 0);