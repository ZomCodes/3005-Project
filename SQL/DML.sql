-- Insert Member Data
INSERT INTO Member (memberID, name, fitnessGoals, healthMetrics) VALUES
(1, 'Sarah Johnson', 'Weight loss and muscle toning', 'Height: 5ft 7in, Weight: 160lbs'),
(2, 'David Miller', 'Improve endurance and flexibility', 'Height: 6ft, Weight: 185lbs'),
(3, 'Emily Williams', 'Build strength', 'Height: 5ft 5in, Weight: 130lbs');

-- Insert Trainer Data
INSERT INTO Trainer (trainerID, name, availability) VALUES
(1, 'John Peterson', 'morning'),
(2, 'Alice Garcia', 'afternoon'),
(3, 'Mark Lee', 'noon');

-- Insert Class Data
INSERT INTO Class (classID, className, instructorID, time) VALUES
(1, 'Yoga Flow', 1, 'morning'),
(2, 'Cardio Blast', 2, 'afternoon'), 
(3, 'Strength Training 101', 3, 'noon'),
(4, 'HIIT Workout', 2, 'noon');

-- Insert Room Data
INSERT INTO Room (roomID, roomName) VALUES
(1, 'Studio 1'),
(2, 'Gym Floor'),
(3, 'Weight Room');

-- Insert Session Data (Ensure roomIDs are valid based on the Room table)
INSERT INTO Session (sessionID, memberID, trainerID, time, roomID) VALUES
(1, 1, 1, 'morning', 1),
(2, 2, 2, 'afternoon', 2),
(3, 1, 3, 'noon', 1), 
(4, 3, 2, 'afternoon', 3); 

-- Insert Equipment Data
INSERT INTO Equipment (equipmentID, equipmentName, status) VALUES
(1, 'Treadmill', 'available'),
(2, 'Elliptical', 'available'),
(3, 'Bench Press', 'available'),
(4, 'Dumbbell Set', 'available'),
(5, 'Squat Rack', 'under maintenance');

-- Insert Payment Data
INSERT INTO Payment (paymentID, memberID, amount, description) VALUES
(1, 1, 80.00, 'Monthly Membership'),
(2, 2, 100.00, 'Monthly Membership + Personal Training'),
(3, 3, 60.00, 'Monthly Membership');

-- Insert AdministrativeStaff Data
INSERT INTO AdministrativeStaff (staffID, name, role) VALUES
(1, 'Jane Thompson', 'manager'),
(2, 'Bob Richards', 'reception');

-- Insert data into junction tables
INSERT INTO MemberClass (memberID, classID) VALUES
(1, 1), -- Sarah is enrolled in Yoga Flow
(1, 3), -- Sarah is enrolled in Strength Training
(2, 2), -- David is enrolled in Cardio Blast
(3, 4); -- Emily is enrolled in HIIT Workout

INSERT INTO MemberSession (memberID, sessionID) VALUES
(1, 1), -- Sarah has a session scheduled 
(2, 2), -- David has a session scheduled 
(3, 4); -- Emily has a session scheduled 

INSERT INTO MemberEquipment (memberID, equipmentID) VALUES 
(1, 1), -- Sarah uses a treadmill
(1, 3), -- Sarah uses a bench press
(2, 2), -- David uses an elliptical
(3, 4);  -- Emily uses dumbbells


