CREATE TABLE Status (
    StatusId INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL UNIQUE
);
CREATE TABLE RoomTypes (
    RoomTypeId INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL UNIQUE,
    StatusId INT NOT NULL,
    FOREIGN KEY (StatusId) REFERENCES Status(StatusId)
);
CREATE TABLE Rooms (
    RoomId INT AUTO_INCREMENT PRIMARY KEY,
    Number VARCHAR(10) UNIQUE NOT NULL,
    RoomTypeId INT NOT NULL,
    Capacity INT NOT NULL,
    DailyRate DECIMAL(10,2) NOT NULL,
    StatusId INT NOT NULL,
    FOREIGN KEY (RoomTypeId) REFERENCES RoomTypes(RoomTypeId),
    FOREIGN KEY (StatusId) REFERENCES Status(StatusId)
);
CREATE TABLE Customers (
    CustomerId INT AUTO_INCREMENT PRIMARY KEY,
    FullName VARCHAR(100) NOT NULL,
    CPF VARCHAR(14) UNIQUE NOT NULL,
    Phone VARCHAR(15),
    Email VARCHAR(100),
    RegistrationDate DATE DEFAULT CURRENT_DATE,
    StatusId INT NOT NULL,
    FOREIGN KEY (StatusId) REFERENCES Status(StatusId)
);
CREATE TABLE Bookings (
    BookingId INT AUTO_INCREMENT PRIMARY KEY,
    CustomerId INT NOT NULL,
    RoomId INT NOT NULL,
    CheckInDate DATE NOT NULL,
    CheckOutDate DATE NOT NULL,
    StatusId INT NOT NULL,
    FOREIGN KEY (CustomerId) REFERENCES Customers(CustomerId),
    FOREIGN KEY (RoomId) REFERENCES Rooms(RoomId),
    FOREIGN KEY (StatusId) REFERENCES Status(StatusId)
);
CREATE TABLE Sales (
    SaleId INT AUTO_INCREMENT PRIMARY KEY,
    BookingId INT NOT NULL,
    TotalAmount DECIMAL(10,2) NOT NULL,
    PaymentMethod ENUM('Cash', 'Card', 'Pix', 'BankTransfer') NOT NULL,
    SaleDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    StatusId INT NOT NULL,
    FOREIGN KEY (BookingId) REFERENCES Bookings(BookingId),
    FOREIGN KEY (StatusId) REFERENCES Status(StatusId)
);
CREATE TABLE ExtraServices (
    ExtraServiceId INT AUTO_INCREMENT PRIMARY KEY,
    ServiceName VARCHAR(100) NOT NULL,
    ServicePrice DECIMAL(10,2) NOT NULL,
    StatusId INT NOT NULL,
    FOREIGN KEY (StatusId) REFERENCES Status(StatusId)
);
CREATE TABLE SalesExtraServices (
    SalesExtraServiceId INT NOT NULL AUTO_INCREMENT,
    SaleId INT NOT NULL,
    ExtraServiceId INT NOT NULL,
    Quantity INT DEFAULT 1,
    PRIMARY KEY (SalesExtraServiceId),
    FOREIGN KEY (SaleId) REFERENCES Sales(SaleId),
    FOREIGN KEY (ExtraServiceId) REFERENCES ExtraServices(ExtraServiceId)
);