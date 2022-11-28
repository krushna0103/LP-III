//SPDX-License-Identifier: MIT 
pragma solidity ^0.8.6;

contract MarksManagmtSys {
    
    // Structure for student details 
    struct Student { 
        int ID; string fName; string lName; int marks;
    } 

    address owner; 
    int public stdCount = 0; 

    // Map student data into Record Block
    mapping(int => Student) public stdRecords;
    
    modifier onlyOwner { 
        require(owner == msg.sender);_; 
    } 
    
    constructor(){ 
        owner = msg.sender;
    }

    function addNewRecords(int _ID, string memory _fName, string memory _lName, int _marks) public onlyOwner {
        
        // Increase the student count
        stdCount = stdCount + 1;

        // Fetch the student details with the help of stdCount 
        stdRecords[stdCount] = Student(_ID, _fName,_lName, _marks);
    }

    // Function to add bonus marks
    function bonusMarks(int _bonus) public onlyOwner { 

        stdRecords[stdCount].marks = stdRecords[stdCount].marks + _bonus;

    }
}
