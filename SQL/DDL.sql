-- Create the Member table 
CREATE TABLE Member (
  memberID SERIAL PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  fitnessGoals VARCHAR(100) NOT NULL,
  healthMetrics TEXT
);

-- Explicitly create the sequence
CREATE SEQUENCE member_id_seq
    START WITH 1 
    INCREMENT BY 1
    MINVALUE 1 
    MAXVALUE 9223372036854775807 
    CACHE 1;


-- Create the Trainer table
CREATE TABLE Trainer (
  trainerID INT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  availability VARCHAR(20) CHECK (availability IN ('morning', 'noon', 'afternoon'))
);

-- Create the Class table
CREATE TABLE Class (
  classID INT PRIMARY KEY,
  className VARCHAR(50) NOT NULL,
  instructorID INT REFERENCES Trainer(trainerID) NOT NULL,
  time VARCHAR(20) CHECK (time IN ('morning', 'noon', 'afternoon'))
);

-- Create the Room table
CREATE TABLE Room (
  roomID INT PRIMARY KEY,
  roomName VARCHAR(50) NOT NULL
);

-- Create the Session table
CREATE TABLE Session (
  sessionID INT PRIMARY KEY,
  memberID INT REFERENCES Member(memberID) NOT NULL,
  trainerID INT REFERENCES Trainer(trainerID),
  time VARCHAR(20) CHECK (time IN ('morning', 'noon', 'afternoon')),
  roomID INT REFERENCES Room(roomID) NOT NULL
);

-- Create the Equipment table
CREATE TABLE Equipment (
  equipmentID INT PRIMARY KEY,
  equipmentName VARCHAR(50) NOT NULL,
  status VARCHAR(20) CHECK (status IN ('available', 'under maintenance', 'out of service'))
);

-- Create the Payment table
CREATE TABLE Payment (
  paymentID INT PRIMARY KEY,
  memberID INT REFERENCES Member(memberID) NOT NULL,
  amount DECIMAL(10,2) NOT NULL,
  description VARCHAR(100) NOT NULL
);

-- Create the AdministrativeStaff table
CREATE TABLE AdministrativeStaff (
  staffID INT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  role VARCHAR(20) NOT NULL
);

-- Create the junction table for the many-to-many relationship between Member and Class
CREATE TABLE MemberClass (
  memberID INT REFERENCES Member(memberID) NOT NULL,
  classID INT REFERENCES Class(classID) NOT NULL,
  PRIMARY KEY (memberID, classID)
);

-- Create the junction table for the many-to-many relationship between Member and Session
CREATE TABLE MemberSession (
  memberID INT REFERENCES Member(memberID) NOT NULL,
  sessionID INT REFERENCES Session(sessionID) NOT NULL,
  PRIMARY KEY (memberID, sessionID)
);

-- Create the junction table for the many-to-many relationship between Member and Equipment 
CREATE TABLE MemberEquipment (
  memberID INT REFERENCES Member(memberID) NOT NULL,
  equipmentID INT REFERENCES Equipment(equipmentID) NOT NULL,
  PRIMARY KEY (memberID, equipmentID)
);

